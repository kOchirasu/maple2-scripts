""" trigger/02000523_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)
        self.spawn_monster(spawn_ids=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
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
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
