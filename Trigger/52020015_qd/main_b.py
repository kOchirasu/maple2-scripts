""" trigger/52020015_qd/main_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60200010], quest_states=[1]):
            return Idle(self.ctx)


initial_state = Idle
