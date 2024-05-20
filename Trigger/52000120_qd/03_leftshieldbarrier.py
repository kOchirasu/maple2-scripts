""" trigger/52000120_qd/03_leftshieldbarrier.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3201], visible=True) # Invisible_Barrier
        self.destroy_monster(spawn_ids=[990,991,992,993,994,995])
        self.set_skill(trigger_ids=[7001]) # Push
        # self.set_user_value(key='PushStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return ActivateShiled01(self.ctx)


class ActivateShiled01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[990,991,992,993,994,995], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9201]):
            return Push01(self.ctx)


class Push01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=990, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=991, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=992, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=993, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=994, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=995, sequence_name='Attack_01_A')
        self.set_skill(trigger_ids=[7001], enable=True) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1333):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9201]):
            return Push01(self.ctx)


initial_state = Wait
