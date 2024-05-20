""" trigger/52000193_qd/52000193.xml """
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
        self.spawn_monster(spawn_ids=[202])
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02_01(self.ctx)


class CameraEffect02_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003406], quest_states=[2]):
            return CameraEffect02_02(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[3]):
            return 이동(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[2]):
            return 변신_02(self.ctx)
        if not self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[2]):
            return 변신_02(self.ctx)


class CameraEffect02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000193_QD__52000193__0$')

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
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52000193_QD__52000193__1$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraEffect03_4(self.ctx)


class CameraEffect03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 변신_01(self.ctx)


class 변신_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[201])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 품
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False) # 에레브 변신
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False, is_skill_set=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraEffect03_6(self.ctx)


class 변신_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000193, portal_id=5002)
        self.reset_camera()
        self.destroy_monster(spawn_ids=[201])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 품
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False) # 에레브 변신
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False, is_skill_set=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraEffect03_6(self.ctx)


class CameraEffect03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_8(self.ctx)


class CameraEffect03_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[3]):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000065)


initial_state = start
