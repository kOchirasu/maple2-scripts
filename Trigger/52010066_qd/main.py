""" trigger/52010066_qd/main.xml """
import trigger_api


class 연출01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            self.visible_my_pc(is_visible=False) # 유저 투명 처리
            self.set_mesh_animation(trigger_ids=[9002])
            self.set_cinematic_ui(type=1)
            return 연출02(self.ctx)


class 연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출03(self.ctx)


class 연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.8, end_scale=0.8, duration=8.0, interpolator=1) # 2초간 느려지기 시작
        self.select_camera_path(path_ids=[2000,2001,2002,2003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출04_b(self.ctx)


class 연출04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh_animation(trigger_ids=[9002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6800):
            return 연출04(self.ctx)


class 연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return quit(self.ctx)


class quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422, portal_id=3)


initial_state = 연출01
