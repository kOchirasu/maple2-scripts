""" trigger/52020010_qd/main_c.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200055], quest_states=[2]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200055], quest_states=[3]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[1]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[3]):
            return Actor_Off(self.ctx)


class Actor_On(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Event_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[3]):
            return Actor_Off(self.ctx)


class Actor_Off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Event_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(box_ids=[2007], quest_ids=[60200060], quest_states=[2]):
            return Actor_Off(self.ctx)


initial_state = Idle
