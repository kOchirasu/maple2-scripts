""" trigger/02000136_ad/01_trigger03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[804])
        self.set_interact_object(trigger_ids=[10000068], state=1)
        self.set_mesh(trigger_ids=[15])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000068], state=0):
            return 발판등장(self.ctx)


class 발판등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[15], visible=True)
        self.set_effect(trigger_ids=[804], visible=True)
        self.set_timer(timer_id='2', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 대기(self.ctx)


initial_state = 대기
