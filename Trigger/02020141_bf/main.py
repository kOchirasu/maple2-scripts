""" trigger/02020141_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        102는 공중에 떠있는 스타팅 포인트 지점 , 이전 첫번째 두번째 페이즈 맵을 통해서 정상 트리거를 타고 이 맵으로 오면 이 공중 떠있는 스타팅 포인트로 오게 될 것임
            return 보스등장준비(self.ctx)
        if self.wait_tick(wait_tick=2000):
            # 테스트를 위해 바로 이 맵으로 들어왔을 경우,  WaitTick = 2초 지난 후 다음 단계로 넘어가도록 함
            return 보스등장준비(self.ctx)


class 보스등장준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 공중에 떠있는 스타팅 지점의 바닥 트리거 메쉬 제거하여 플레이어가 공중에서 추락하면서 시작 하도록 하기
        self.set_mesh(trigger_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 플레이어 추락해서 바닥에 떨어진 이후 보스 등장하도록 타이밍 조절
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   arg1="99"
        self.spawn_monster(spawn_ids=[99], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return 클리어성공유무체크시작(self.ctx)
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 클리어성공유무체크시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 연출딜레이(self.ctx)
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 메인 전투판에 나가기 포탈 생성하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


class 연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 음모의 전당 두번째 마지막 전투판에서 일부 파티원은 투르카 보스를 때리지 않고 로봇 탈것해서 졸몹만 처리하는 경우가 있는데 이때 보스 처치 조건을 보스 코드로 입력할 경우 조건을 만족하지 못하는 버그 스러운 경우가 있어서 , 보스Kill이 목적인 던전미션과 트로피 달성을 트리거를 통해서 이루어 지도록 설정  하였음
        # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임
        self.dungeon_mission_complete(mission_id=23090000)
        # achieve.xlsx 트로피 투르카던전클리어 조건 체크, arg1을 넣지 않으면 이 맵 전체에 있는 플레이어를 체크함 , 참고로 arg1을 넣으면 트리거 박스 안에 있는 플레이어만 체크하는 것임
        self.set_achievement(type='trigger', achieve='TurkaDungeonClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            # 보스 죽으면 보스 죽음 동작 충분히 본 다음에(9초 딜레이) 클리어 UI 나오도록 함
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽음과 동시에 자체 60초 늘어나기 때문에,  <state name="연출딜레이"> 단계 끝나고 WaitTick=9초 후에 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.dungeon_clear()
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 메인 전투판에 나가기 포탈 생성하기


initial_state = 시작대기중
