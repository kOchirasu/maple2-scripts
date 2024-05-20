""" trigger/02000382_bf/03_boss03portal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=40) # Boss01Spawn

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9900, spawn_ids=[903]):
            # 유저가 왼쪽에서 입장
            return ActionPortal01(self.ctx)


class ActionPortal01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=40, enable=True) # Boss01Spawn


initial_state = Wait
