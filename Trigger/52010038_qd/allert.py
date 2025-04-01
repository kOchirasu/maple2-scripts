""" trigger/52010038_qd/allert.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(131,160,209))
        self.set_directional_light(diffuse_color=Vector3(134,160,143), specular_color=Vector3(130,130,130))
        self.set_effect(trigger_ids=[6000,6299])
        self.set_effect(trigger_ids=[6101,6102,6103,6104,6105,6106,6107,6108,6109])
        self.set_effect(trigger_ids=[6201,6202,6203,6204])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=209, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=210, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=213, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=214, visible=True, initial_sequence='sf_quest_light_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AllertStart') == 1:
            return 이펙트시퀀스01(self.ctx)


class 이펙트시퀀스01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701], enable=True)
        self.set_skill(trigger_ids=[704], enable=True)
        self.set_effect(trigger_ids=[6101,6104], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이펙트시퀀스02(self.ctx)


class 이펙트시퀀스02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[707], enable=True)
        self.set_skill(trigger_ids=[708], enable=True)
        self.set_effect(trigger_ids=[6107,6108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이펙트시퀀스03(self.ctx)


class 이펙트시퀀스03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.set_skill(trigger_ids=[702], enable=True)
        self.set_skill(trigger_ids=[706], enable=True)
        self.set_effect(trigger_ids=[6102,6106], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 경보(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[709], enable=True)
        self.set_effect(trigger_ids=[6109], visible=True)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=8000, script='$52010038_QD__allert__0$', voice='ko/Npc/00002104')
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=209, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=210, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=213, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=214, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4202):
            return 이펙트시퀀스04(self.ctx)


class 이펙트시퀀스04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[703], enable=True)
        self.set_skill(trigger_ids=[705], enable=True)
        self.set_effect(trigger_ids=[6103,6105], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AllertEnd') == 1:
            self.set_user_value(trigger_id=999004, key='AllertStart', value=0)
            return 대기(self.ctx)


initial_state = 대기
