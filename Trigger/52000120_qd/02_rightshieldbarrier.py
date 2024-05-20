""" trigger/52000120_qd/02_rightshieldbarrier.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200], visible=True) # Invisible_Barrier
        self.destroy_monster(spawn_ids=[980,981,982,983,984,985])
        self.set_skill(trigger_ids=[7000]) # Push
        # self.set_user_value(key='PushStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return ActivateShiled01(self.ctx)


class ActivateShiled01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[980,981,982,983,984,985], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            return Push01(self.ctx)


class Push01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=980, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=981, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=982, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=983, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=984, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=985, sequence_name='Attack_01_A')
        self.set_skill(trigger_ids=[7000], enable=True) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1333):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            return Push01(self.ctx)


initial_state = Wait
