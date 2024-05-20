""" trigger/52100106_qd/52100106.xml """
import trigger_api
from System.Numerics import Vector3


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000880], quest_states=[3]):
            return 들킴(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000890], quest_states=[2]):
            return 들킴(self.ctx)


class 들킴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_On')


initial_state = Ready
