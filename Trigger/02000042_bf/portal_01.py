""" trigger/02000042_bf/portal_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000583], state=1)
        self.set_portal(portal_id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000583], state=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=5)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            # self.set_portal(portal_id=6)
            return 대기(self.ctx)


initial_state = 대기
