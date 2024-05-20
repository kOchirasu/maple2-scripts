""" trigger/02000281_bf/move13.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[813])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[193]):
            return 발판발동(self.ctx)


class 발판발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)
        self.set_breakable(trigger_ids=[813], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 대기(self.ctx)


initial_state = 대기
