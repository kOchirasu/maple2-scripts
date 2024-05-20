""" trigger/02000011_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_breakable(trigger_ids=[7000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000361], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000361], state=0):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.set_breakable(trigger_ids=[7000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 대기(self.ctx)


initial_state = 대기
