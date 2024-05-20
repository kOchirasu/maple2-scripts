""" trigger/02010055_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        # 포탈ID 1: 던전 입구에 있는 나가기 포탈 셋팅 초기화
        self.set_portal(portal_id=1)
        # 포탈ID 2: 3페이즈 전투 장소에 나가기 포탈 셋팅 초기화
        self.set_portal(portal_id=2)
        # 포탈ID 8: 1페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 1페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
        self.set_portal(portal_id=8)
        # 포탈ID 9: 2페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 2페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
        self.set_portal(portal_id=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 난이도체크(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 포탈ID 1: 던전 입구에 있는 나가기 포탈 작동 활성화
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level() == 2:
            return 레이드(self.ctx)
        if self.dungeon_level() == 3:
            return 카오스레이드(self.ctx)


class 퀘스트던전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_timer(timer_id='1', seconds=300, interval=1)
        self.add_buff(box_ids=[101], skill_id=70000118, level=1, is_player=False, is_skill_set=False)
        self.spawn_monster(spawn_ids=[2299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2299]):
            return 종료딜레이(self.ctx)


class 레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 종료딜레이(self.ctx)


class 카오스레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2199], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2199]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 포탈ID 2: 3페이즈 전투 장소에 나가기 포탈 작동 활성화
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            # 포탈ID 8: 1페이즈 전투 장소에 나가기 포탈 작동 활성화, 보스가 1페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
            self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)
            # 포탈ID 9:  2페이즈 전투 장소에 나가기 포탈 작동 활성화, 보스가 2페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
            self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
