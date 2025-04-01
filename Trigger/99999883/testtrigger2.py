""" trigger/99999883/testtrigger2.xml """
import trigger_api


class State1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='현재 State1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='test') == 1:
            return State2(self.ctx)


class State2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='test', value=0)
        self.debug_string(value='현재 State2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return State1(self.ctx)


initial_state = State1
