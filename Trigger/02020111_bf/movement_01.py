""" trigger/02020111_bf/movement_01.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 환경변화(self.ctx)


# **********************환경 변화 페이즈_1*******************************************************************************************
class 환경변화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Movement') >= 0:
            return 시작(self.ctx)
        if self.user_value(key='dark') >= 1:
            return 페이드아웃(self.ctx)


class 페이드아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=7)
        self.set_portal(portal_id=8)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조명변경(self.ctx)


class 조명변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=62100014, level=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_event_ui_script(type=BannerType.GameOver, script='$02020111_BF__MOVEMENT_01__0$', duration=3000)
        self.set_ambient_light(primary=Vector3(52,48,38))
        self.set_directional_light(diffuse_color=Vector3(0,0,0), specular_color=Vector3(206,174,84))
        self.add_buff(box_ids=[1001], skill_id=75000001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 페이드인(self.ctx)
        if self.user_value(key='Movement') >= 0:
            return 시작(self.ctx)


class 페이드인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_user(map_id=2020111, portal_id=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02020111_BF__MOVEMENT_01__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조명리셋(self.ctx)


class 조명리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02020111_BF__MOVEMENT_01__1$', time=3)
        self.move_npc_to_pos(spawn_id=101, pos=Vector3(-3743,294,1651), rot=Vector3(0,0,45))
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))
        self.add_buff(box_ids=[1001], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1002], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1003], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1004], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1005], skill_id=75000002, level=1)
        self.set_effect(trigger_ids=[200031,200032,200033,200034,200035], visible=True)
        self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Movement') >= 0:
            return 시작(self.ctx)
        if self.user_value(key='dark') >= 2:
            return 중앙지역이동_1(self.ctx)


class 중앙지역이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200031,200032,200033,200034,200035])
        self.move_npc_to_pos(spawn_id=101, pos=Vector3(-13,288,1951), rot=Vector3(0,0,45)) # 페이즈 꼬임을 방지하기 위한 npc이동장치
        self.set_portal(portal_id=9)
        # self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            # self.move_user(map_id=2020111, portal_id=4)
            return 중앙지역이동_1_페이드인(self.ctx)


class 중앙지역이동_1_페이드인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 포탈설정_1(self.ctx)


class 포탈설정_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Movement') >= 0:
            return 시작(self.ctx)


initial_state = 시작
