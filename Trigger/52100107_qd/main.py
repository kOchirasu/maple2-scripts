""" trigger/52100107_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000890], quest_states=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000900], quest_states=[1]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000900], quest_states=[2]):
            return NPC소환(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)


initial_state = Ready
