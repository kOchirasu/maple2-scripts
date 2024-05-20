""" trigger/52010059_qd/52010059.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 콘대르
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 샤텐
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 네이린
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 메이슨
        self.set_actor(trigger_id=501, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=507, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=508, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=509, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=510, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=511, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=512, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=513, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=514, visible=True, initial_sequence='sf_quest_light_A01_Off')


initial_state = Wait
