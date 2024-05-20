""" trigger/02010026_bf/01_lever01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1000,1001,1002,1003,1004], fade=5.0)
        self.set_interact_object(trigger_ids=[10000908], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000908], state=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[1000,1001,1002,1003,1004], visible=True, start_delay=5, interval=100, fade=100)
        self.set_timer(timer_id='2', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


initial_state = 대기
