""" trigger/52010032_qd/main_quest10003087.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003086,10003087], quest_states=[2]):
            return NpcSpawn(self.ctx)


class NpcSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601])
        self.spawn_monster(spawn_ids=[602])
        self.set_npc_emotion_sequence(spawn_id=601, sequence_name='Idle_A')
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Idle_A')


initial_state = Ready
