""" trigger/52000014_qd/move_6300.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[6300])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9630]):
            return 침몰01(self.ctx)


class 침몰01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=17)
        self.set_breakable(trigger_ids=[6300], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
