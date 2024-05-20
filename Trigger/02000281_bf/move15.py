""" trigger/02000281_bf/move15.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[815])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[195]):
            return 발판발동(self.ctx)


class 발판발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)
        self.set_breakable(trigger_ids=[815], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 대기(self.ctx)


initial_state = 대기
