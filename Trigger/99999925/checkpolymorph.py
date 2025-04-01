""" trigger/99999925/checkpolymorph.xml """
import trigger_api


class CheckIdle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BuffGo') == 1:
            return Checkpoly(self.ctx)


class Checkpoly(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='BuffStart', value=1, is_modify=True)
        self.set_user_value(key='BuffGo', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CheckIdle(self.ctx)


initial_state = CheckIdle
