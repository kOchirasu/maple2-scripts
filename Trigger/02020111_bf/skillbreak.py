""" trigger/02020111_bf/skillbreak.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900001, key='SkillBreakFail', value=0)
        self.set_user_value(trigger_id=900008, key='SkillBreakFail', value=3)
        self.set_user_value(trigger_id=900009, key='SkillBreakFail', value=3)
        self.set_user_value(trigger_id=900010, key='SkillBreakFail', value=3)
        self.set_user_value(trigger_id=900011, key='SkillBreakFail', value=3)
        self.set_user_value(trigger_id=900002, key='Summon', value=2)
        self.set_user_value(trigger_id=900007, key='Summon', value=2)
        self.set_user_value(trigger_id=900003, key='Summon_Enemy_1', value=2)
        self.set_user_value(trigger_id=900005, key='Lapenta_Attack', value=2)
        self.set_user_value(trigger_id=900006, key='Lapenta_Attack_2', value=2)
        self.set_user_value(trigger_id=900102, key='Phase', value=3)
        self.set_user_value(trigger_id=900004, key='Movement', value=2)
        self.set_user_value(trigger_id=900201, key='Movement', value=2)
        self.set_user_value(trigger_id=900202, key='Movement', value=2)
        self.set_user_value(trigger_id=900203, key='Movement', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002181, level=1):
            return 스킬브레이크_실패(self.ctx)


class 스킬브레이크_실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=62100026, level=1)
        self.add_buff(box_ids=[101], skill_id=70002185, level=1) # 스킬브레이크 체크를 제거한다.
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))
        self.add_buff(box_ids=[1006], skill_id=70002151, level=1, is_skill_set=False)
        self.set_user_value(trigger_id=900001, key='SkillBreakFail', value=1)
        # self.set_user_value(trigger_id=900002, key='SkillBreakFail', value=1)
        # self.set_user_value(trigger_id=900003, key='SkillBreakFail', value=1)
        self.set_user_value(trigger_id=900008, key='SkillBreakFail', value=1)
        self.set_user_value(trigger_id=900009, key='SkillBreakFail', value=1)
        self.set_user_value(trigger_id=900010, key='SkillBreakFail', value=1)
        self.set_user_value(trigger_id=900011, key='SkillBreakFail', value=1)
        self.set_user_value(trigger_id=900002, key='Summon', value=0)
        self.set_user_value(trigger_id=900007, key='Summon', value=0)
        self.set_user_value(trigger_id=900003, key='Summon_Enemy_1', value=0)
        self.set_user_value(trigger_id=900004, key='Movement', value=0)
        self.set_user_value(trigger_id=900201, key='Movement', value=0)
        self.set_user_value(trigger_id=900202, key='Movement', value=0)
        self.set_user_value(trigger_id=900203, key='Movement', value=0)
        self.set_user_value(trigger_id=900103, key='Lapenta_Attack_Guide', value=2)
        self.set_user_value(trigger_id=900104, key='SkillBreakSuccess_Reset', value=0)
        self.set_user_value(trigger_id=900104, key='SkillBreakSuccess_1', value=0)
        self.set_user_value(trigger_id=900104, key='SkillBreakSuccess_2', value=0)
        self.set_user_value(trigger_id=900104, key='SkillBreakSuccess_3', value=0)
        self.set_user_value(trigger_id=900104, key='SkillBreakSuccess_4', value=0)
        self.set_user_value(trigger_id=900105, key='SkillBreakSuccess_Reset', value=0)
        self.set_user_value(trigger_id=900105, key='SkillBreakSuccess_5', value=0)
        self.set_user_value(trigger_id=900105, key='SkillBreakSuccess_6', value=0)
        self.set_user_value(trigger_id=900105, key='SkillBreakSuccess_7', value=0)
        self.set_user_value(trigger_id=900105, key='SkillBreakSuccess_8', value=0)
        self.set_user_value(trigger_id=900102, key='Phase', value=1)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=7)
        self.set_portal(portal_id=8)
        self.set_user_value(trigger_id=900301, key='Light_On_1', value=1)
        self.set_user_value(trigger_id=900301, key='Light_On_2', value=1)
        self.set_user_value(trigger_id=900301, key='Light_On_3', value=1)
        self.set_user_value(trigger_id=900301, key='Light_On_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 스킬브레이크_실패_2(self.ctx)


class 스킬브레이크_실패_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900005, key='Lapenta_Attack', value=0)
        self.set_user_value(trigger_id=900006, key='Lapenta_Attack_2', value=0)
        self.set_user_value(trigger_id=900102, key='Phase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
