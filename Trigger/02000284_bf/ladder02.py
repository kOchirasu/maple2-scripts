""" trigger/02000284_bf/ladder02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000436], state=1)
        self.set_mesh(trigger_ids=[321,322,323,324])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000436], state=0):
            return 사다리생성(self.ctx)


class 사다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000436], state=0)
        self.set_mesh(trigger_ids=[321,322,323,324], visible=True, interval=500)
        self.set_timer(timer_id='1500', seconds=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1500'):
            return 대기(self.ctx)


initial_state = 대기
