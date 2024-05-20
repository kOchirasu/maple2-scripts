""" trigger/52020030_qd/main30000332.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 천공의 탑 입장
class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[30000332], quest_states=[1]):
            return 천공의탑전경보여주기(self.ctx)


class 천공의탑전경보여주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 천공의탑전경보여주기02(self.ctx)


class 천공의탑전경보여주기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4008,4010], return_view=False)
        self.show_caption(type='VerticalCaption', title='천공의 탑', desc='크리티아스 마법 연구소', align=Align.Center | Align.Left, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 천공의탑전경보여주기03(self.ctx)


class 천공의탑전경보여주기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52020030, portal_id=6006)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 천공의탑전경보여주기04(self.ctx)


class 천공의탑전경보여주기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 입장
