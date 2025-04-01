""" trigger/02020097_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 첫번째 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=4)
        # 두번째 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=2)
        # 마지막 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=3)
        # 스타팅 부활 지점에서 바로 3페이지 전투판 입구로 가는 순간이동 포탈 최초에는 감추기
        self.set_portal(portal_id=28)
        # 몬스터는 밟고 플레이어는 밟지 못하는 트리거메쉬 설정하기
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121])
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207]) # 계단 트리거메쉬 초기화 감추기
        self.set_mesh(trigger_ids=[211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239]) # 계단 트리거메쉬 초기화 감추기
        # self.set_user_value(key='DungeonReset', value=0) # 변수

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            # MS2TriggerBox   TriggerObjectID = 10, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        10은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[99], auto_target=False) # 발록 보스 스폰시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기상태(self.ctx)


class 대기상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 2페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk2nd = 1 신호를 받으면 이 부분 실행
        if self.user_value(key='StairsOk') == 1:
            return 계단생성시작중(self.ctx)
        # 3페이지로 들어서면 보스는 하늘높이 날아가는데, 플레이어가 3페이지 전투판으로 들어서면 즉 이 트기러 영역 안으로 들어오면 보스에게 신호를 보내서 3페이지 전투판으로
        if self.user_value(key='StairsOk2nd') == 1:
            return 계단생성시작중2nd(self.ctx)
        if self.user_detected(box_ids=[11]): # 보스가 죽을 경우
            # MS2TriggerBox   TriggerObjectID = 11, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        11은 마지막 3페이지 전투판을 커버하는 비교적 좁은 범위
            return 플레이어3페이지전투판으로오기(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 연출딜레이(self.ctx)


class 계단생성시작중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 발록이 2페이즈 점프 이동 전에 계단 생성되면 이상해 보여서 약간 2초 정도 딜레이 부여함
            return 계단생성(self.ctx)


class 계단생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1페이지 끝내고 2페이지 진입하는 투명벽 제거하기
        self.set_mesh(trigger_ids=[301])
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207], visible=True, start_delay=1, interval=120, fade=0.5) # 계단 트리거메쉬 생성
        # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음
        self.set_user_value(key='StairsOk', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기상태(self.ctx)


class 계단생성시작중2nd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 발록이 3페이즈 점프 이동 전에 계단 생성되면 이상해 보여서 약간 2초 정도 딜레이 부여함
            return 계단생성2nd(self.ctx)


class 계단생성2nd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239], visible=True, start_delay=1, interval=50, fade=0.5) # 계단 트리거메쉬 생성
        # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음
        self.set_user_value(key='StairsOk2nd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 칸막이제거2nd(self.ctx)


class 칸막이제거2nd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2페이지 끝내고 3페이지 진입하는 투명벽 제거하기
        self.set_mesh(trigger_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기상태(self.ctx)


class 플레이어3페이지전투판으로오기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 플레이어가 3페이지 전투판에 들어서면 발록AI에게 3PhaseSetOk=1 신호를 보내서 , 3페이지 전투판으로 점프 내려오도록 함
        self.set_ai_extra_data(key='3PhaseSetOk', value=1)
        # 스타팅 부활 지점에서 바로 3페이지 전투판 입구로 가는 순간이동 포탈 생성하도록 하기
        self.set_portal(portal_id=28, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        # 혹시 몰라서 이부분 다시 설정,          1페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk = 1 신호를 받으면 이 부분 실행
        if self.monster_dead(spawn_ids=[99]):
            return 연출딜레이(self.ctx)
        if self.user_value(key='StairsOk') == 1:
            return None # Missing State: 사다리생성


class 연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3="BalrogKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        self.set_achievement(achieve='BalrogKritiasClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            # 보스 죽으면 보스 죽음 동작 충분히 본 다음에(7초 딜레이) 클리어 UI 나오도록 함
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 첫번째 전투판에서 생성
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 두번째 전투판에서 생성
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 생성
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear()


initial_state = 시작대기중
