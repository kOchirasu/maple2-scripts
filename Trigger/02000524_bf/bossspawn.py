""" trigger/02000524_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 난이도별보스등장(self.ctx)


class 난이도별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id() == 23046003:
            # 현재 입장한 던전ID가 23046003  이라면 , <transition state="일반난이도_보스등장" /> 실행
            return 일반난이도_보스등장(self.ctx)
        if self.dungeon_id() == 23047003:
            # 현재 입장한 던전ID가 23047003  이라면 ,<transition state="어려움난이도_보스등장" /> 실행
            return 어려움난이도_보스등장(self.ctx)
        if self.wait_tick(wait_tick=1100):
            # 던전 로직을 통해 입장하지 않고, 걍 디버그 모드 맵툴로 들어오면 이 부분 실행됨
            return 일반난이도_보스등장(self.ctx)


class 일반난이도_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[98], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[98]):
            return 클리어처리(self.ctx)


class 어려움난이도_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[99], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 클리어처리(self.ctx)


class 클리어처리(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.dungeon_clear()
            return 종료처리(self.ctx)


class 종료처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
