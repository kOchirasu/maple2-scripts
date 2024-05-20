""" trigger/52000071_qd/03_truedoor.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3002]) # 미니맵용_Invisible
        self.set_portal(portal_id=10)
        self.set_interact_object(trigger_ids=[10001105], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001105], state=0):
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)


initial_state = Wait
