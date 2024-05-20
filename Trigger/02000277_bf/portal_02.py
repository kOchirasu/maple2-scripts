""" trigger/02000277_bf/portal_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000631], state=1)
        self.set_portal(portal_id=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000631], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_portal(portal_id=50, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
