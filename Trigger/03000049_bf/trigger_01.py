""" trigger/03000049_bf/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000289], state=1)
        self.set_effect(trigger_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000289], state=0):
            return 비내림(self.ctx)


class 비내림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[101], visible=True)
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
