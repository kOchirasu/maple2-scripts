""" trigger/52000014_qd/collapse_2700.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2700,2701,2702,2703,2704,2705,2706], visible=True)
        self.set_effect(trigger_ids=[12700]) # Vibrate Short
        self.set_effect(trigger_ids=[22700]) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92700]):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=10)
        self.set_effect(trigger_ids=[12700], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22700], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2700,2701,2702,2703,2704,2705,2706], start_delay=7, interval=300, fade=300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12700]) # Vibrate Short
        self.set_effect(trigger_ids=[22700]) # Vibrate Sound


initial_state = 대기
