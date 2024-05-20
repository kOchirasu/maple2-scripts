""" trigger/52020010_qd/door_open.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5016]) # 우르르 쾅쾅
        self.set_effect(trigger_ids=[5017]) # 먼지
        self.set_breakable(trigger_ids=[10001])
        self.set_breakable(trigger_ids=[10002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2005], quest_ids=[60200050], quest_states=[2]):
            return Check(self.ctx)
        if self.quest_user_detected(box_ids=[2005], quest_ids=[60200050], quest_states=[3]):
            return Check(self.ctx)


class Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001275], state=0):
            return DoorOpen(self.ctx)


class DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5016], visible=True) # 우르르 쾅쾅
        self.set_effect(trigger_ids=[5017], visible=True) # 먼지
        self.set_breakable(trigger_ids=[10001], enable=True)
        self.set_breakable(trigger_ids=[10002], enable=True)


initial_state = Idle
