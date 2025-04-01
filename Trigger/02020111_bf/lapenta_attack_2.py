""" trigger/02020111_bf/lapenta_attack_2.xml """
import trigger_api
from System.Numerics import Vector3


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack_2') == 1:
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__LAPENTA_ATTACK_2__0$', duration=3525, voice='ko/Npc/00002200')
        self.set_ambient_light(primary=Vector3(52,48,38))
        self.set_directional_light(diffuse_color=Vector3(0,0,0), specular_color=Vector3(206,174,84))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3525):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035])
        self.set_skill(trigger_ids=[5002], enable=True)
        self.add_buff(box_ids=[101], skill_id=62100026, level=1)
        self.add_buff(box_ids=[1001], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1002], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1003], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1004], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1005], skill_id=75000002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 실패조건버프(self.ctx)


class 실패조건버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900204, key='Message', value=1)
        self.add_buff(box_ids=[101], skill_id=70002181, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack_2') == 0:
            return 시작(self.ctx)


initial_state = 시작
