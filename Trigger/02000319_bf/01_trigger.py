""" trigger/02000319_bf/01_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301]):
            return 포털(self.ctx)


class 포털(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
