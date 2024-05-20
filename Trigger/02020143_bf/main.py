""" trigger/02020143_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003330], quest_states=[2]):
            return 이동(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003330], quest_states=[3]):
            return 이동(self.ctx)
        if self.user_detected(box_ids=[102]):
            # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        102는 공중에 떠있는 스타팅 포인트 지점 , 이전 첫번째 두번째 페이즈 맵을 통해서 정상 트리거를 타고 이 맵으로 오면 이 공중 떠있는 스타팅 포인트로 오게 될 것임
            return 보스등장준비(self.ctx)


class 보스등장준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 공중에 떠있는 스타팅 지점의 바닥 트리거 메쉬 제거하여 플레이어가 공중에서 추락하면서 시작 하도록 하기
        self.set_mesh(trigger_ids=[301])
        # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안의 플레이어에게 애디셔널 50000554(레벨1) 회복 버프 부여하기, 이 맵은 추락하면서 시작하는데 추락 대미지에 의해 죽을 수있기 때문에 시작하자마자 무조건 HP회복 버프 부여함
        self.add_buff(box_ids=[102], skill_id=50000554, level=1, is_player=False, is_skill_set=False)
        # arg4 =1 이면 타겟이 npc로 변경 / arg1이 스폰 포인트 ID가 된다.       arg5 =1 이면 박스 외에 모든 맵/ 0은 박스 안

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
        # 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


class 연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3="TurkaQuestDungeonClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        self.set_achievement(achieve='TurkaQuestDungeonClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            # 보스 죽으면 보스 죽음 동작 충분히 본 다음에(7초 딜레이) 클리어 UI 나오도록 함
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # 보스 죽으면 보스 죽음 동작 충분히 본 다음에(7초 딜레이) 클리어 UI 나오도록 함
            return 영상재생준비(self.ctx)


class 영상재생준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\Kritias_03.usm', movie_id=1)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=129000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003330], quest_states=[2]):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52100304, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중(self.ctx)


initial_state = 시작대기중
