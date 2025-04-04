""" trigger/52100205_qd/52100205.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100205, portal_id=5001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02_02(self.ctx)


class CameraEffect02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100205_QD__52100205__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect03_2(self.ctx)


class CameraEffect03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52100205_QD__52100205__1$', align=Align.bottomLeft, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraEffect03_4(self.ctx)


class CameraEffect03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_5(self.ctx)


class CameraEffect03_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[201])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 품
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910400, level=1, ignore_player=False) # 클라디아 변신
        self.add_buff(box_ids=[2001], skill_id=99910400, level=1, ignore_player=False, is_skill_set=False) # 클라디아 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_6(self.ctx)


class CameraEffect03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_7(self.ctx)


class CameraEffect03_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004612, msg='$52100205_QD__52100205__2$', align=Align.left, illust_id='cladia_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CameraEffect03_8(self.ctx)


class CameraEffect03_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return 제시카_01(self.ctx)


class 제시카_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제시카_02(self.ctx)


class 제시카_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.spawn_monster(spawn_ids=[101]) # 제시카

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 제시카_03(self.ctx)


class 제시카_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 제시카_04(self.ctx)


class 제시카_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 제시카_05(self.ctx)


class 제시카_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004575, msg='$52100205_QD__52100205__3$', align=Align.left, illust_id='Jessica_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 제시카_06(self.ctx)


class 제시카_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제시카_07(self.ctx)


class 제시카_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()


initial_state = start
