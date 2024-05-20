""" trigger/02000525_bf/bossspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            return 난이도별보스등장(self.ctx)


class 난이도별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id() == 23048003:
            # 현재 입장한 던전ID가 23048003  이라면 , <transition state="일반난이도_보스등장" /> 실행
            return 일반난이도_보스등장(self.ctx)
        if self.dungeon_id() == 23049003:
            # 현재 입장한 던전ID가 23049003  이라면 ,<transition state="어려움난이도_보스등장" /> 실행
            return 어려움난이도_보스등장(self.ctx)
        if self.wait_tick(wait_tick=1100):
            # 던전 로직을 통해 입장하지 않고, 걍 디버그 모드 맵툴로 들어오면 이 부분 실행됨
            return 일반난이도_보스등장(self.ctx)


class 일반난이도_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 클리어처리(self.ctx)


class 어려움난이도_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return 클리어처리(self.ctx)


class 클리어처리(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.dungeon_clear()
            return 종료처리(self.ctx)


class 종료처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
