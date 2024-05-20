""" trigger/52010032_qd/main_quest10003106.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003106], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='NewChief')


initial_state = idle
