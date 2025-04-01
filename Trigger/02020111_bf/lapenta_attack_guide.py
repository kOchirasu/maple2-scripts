""" trigger/02020111_bf/lapenta_attack_guide.xml """
import trigger_api
from System.Numerics import Vector3


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035])
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack_Guide') == 1:
            return 어둠효과_페이드아웃(self.ctx)


class 어둠효과_페이드아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_buff(box_ids=[1001], skill_id=75000001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_ambient_light(primary=Vector3(52,48,38))
            self.set_directional_light(diffuse_color=Vector3(0,0,0), specular_color=Vector3(206,174,84))
            return 가이드발동(self.ctx)


class 가이드발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_buff(box_ids=[1001], skill_id=75000001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack_Guide') == 0:
            return 가이드종료(self.ctx)


class 가이드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack_Guide') == 2:
            return 시작(self.ctx)


initial_state = 시작
