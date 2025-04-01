""" trigger/51000003_dg/buff.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial') == 1:
            return Tutorial_buff(self.ctx)


class Tutorial_buff(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial') == 0:
            return idle(self.ctx)
        if self.user_detected(box_ids=[701]):
            return buff(self.ctx)


class buff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000085, level=1, is_skill_set=False) # 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial') == 0:
            return idle(self.ctx)
        return Tutorial_buff(self.ctx)


initial_state = idle
