""" trigger/02020301_bf/3000039_phase_2_interect_09.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return None # Missing State: 시작


initial_state = 대기
