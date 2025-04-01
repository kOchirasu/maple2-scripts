""" trigger/99999849/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Test') == 2:
            return None # Missing State: 두번


initial_state = 대기
