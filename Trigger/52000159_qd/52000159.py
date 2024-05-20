""" trigger/52000159_qd/52000159.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002735], quest_states=[2]):
            return 정리_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002736], quest_states=[2]):
            return 정리_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002737], quest_states=[2]):
            return 정리_01(self.ctx)
        if self.user_detected(box_ids=[2001], job_code=0):
            return wait_01_1(self.ctx)


class wait_01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000159, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 어쌔신과거_01(self.ctx)


class 어쌔신과거_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 어쌔신과거_02(self.ctx)


class 어쌔신과거_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.select_camera_path(path_ids=[4003,4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 어쌔신과거_03(self.ctx)


class 어쌔신과거_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.show_caption(type='VerticalCaption', title='$52000159_QD__52000159__0$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어쌔신과거_04(self.ctx)


class 어쌔신과거_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__1$', duration=4000)
        self.move_user_path(patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어쌔신과거_05(self.ctx)


class 어쌔신과거_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__2$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__3$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__4$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 어쌔신과거_06(self.ctx)


class 어쌔신과거_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__6$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 어쌔신과거_07(self.ctx)


class 어쌔신과거_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__8$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52000159_QD__52000159__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도클로_01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도클로_01(self.ctx)


class 쉐도클로_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_effect(trigger_ids=[5006], visible=True)
        self.move_user(map_id=52000159, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 쉐도클로_02(self.ctx)


class 쉐도클로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리_01(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.destroy_monster(spawn_ids=[101], arg2=False)
        self.destroy_monster(spawn_ids=[103], arg2=False)
        self.destroy_monster(spawn_ids=[105], arg2=False)
        self.destroy_monster(spawn_ids=[106], arg2=False)
        self.destroy_monster(spawn_ids=[107], arg2=False)
        self.destroy_monster(spawn_ids=[108], arg2=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002735], quest_states=[2]):
            return 남자의죽음_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002736], quest_states=[2]):
            return 남자의죽음_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002737], quest_states=[2]):
            return 남자의죽음_01(self.ctx)


class 남자의죽음_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 남자의죽음_01_02(self.ctx)


class 남자의죽음_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera_path(path_ids=[4007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 남자의죽음_02(self.ctx)


class 남자의죽음_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 남자의죽음_03(self.ctx)


class 남자의죽음_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Attack_01_B')
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Dead_B', duration=9000000000000.0)
        self.set_effect(trigger_ids=[5007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 남자의죽음_03_01(self.ctx)


class 남자의죽음_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 남자의죽음_04(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 남자의죽음_04(self.ctx)


class 남자의죽음_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102], arg2=False)
        self.spawn_monster(spawn_ids=[114], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=114, sequence_name='Dead_B', duration=9000000000000.0)
        self.spawn_monster(spawn_ids=[115], auto_target=False)
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 남자의죽음_05(self.ctx)


class 남자의죽음_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002737], quest_states=[2]):
            return 쉐도클로표창_01(self.ctx)


class 쉐도클로표창_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도클로표창_01_01(self.ctx)


class 쉐도클로표창_01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.visible_my_pc(is_visible=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도클로표창_02(self.ctx)


class 쉐도클로표창_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Attack_Idle_A', duration=4000.0)
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도클로표창_03(self.ctx)


class 쉐도클로표창_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Attack_01_B', duration=80000.0)
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.1, duration=10.0, interpolator=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 쉐도클로표창_03_01(self.ctx)


class 쉐도클로표창_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=115, sequence_name='Dead_A', duration=80000.0)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도클로표창_04(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도클로표창_04(self.ctx)


class 쉐도클로표창_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 쉐도클로표창_05(self.ctx)


class 쉐도클로표창_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=52000158, portal_id=6001)


initial_state = wait_01
