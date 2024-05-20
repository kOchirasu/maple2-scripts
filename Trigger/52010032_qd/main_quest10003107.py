""" trigger/52010032_qd/main_quest10003107.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003105,10003106], quest_states=[2]):
            return NpcSpawn_01(self.ctx)


class NpcSpawn_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[502])
        self.set_npc_emotion_sequence(spawn_id=502, sequence_name='Idle_A')


initial_state = Ready
