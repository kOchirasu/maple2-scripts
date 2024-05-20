""" trigger/52100208_qd/52100208.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003300], quest_states=[2]):
            return wait_01_02(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100208, portal_id=5001)
        self.set_effect(trigger_ids=[6001])
        self.set_effect(trigger_ids=[6002])
        self.set_effect(trigger_ids=[6003])
        self.destroy_monster(spawn_ids=[201,202,203,204,205,206,207,208,209])
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대면(self.ctx)


class 투르카대면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대면_02(self.ctx)


class 투르카대면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004678, illust_id='Neirin_surprise', align=Align.Left, msg='$52100208_QD__52100208__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11004675, illust_id='Bliche_mad', align=Align.Right, msg='$52100208_QD__52100208__1$', duration=4500)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=0, msg='$52100208_QD__52100208__2$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 투르카대면_02_01(self.ctx)


class 투르카대면_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대면_03(self.ctx)


class 투르카대면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52100208_QD__52100208__4$', duration=2500)
        self.add_cinematic_talk(npc_id=0, msg='$52100208_QD__52100208__5$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 투르카대면_04(self.ctx)


class 투르카대면_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4005,4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대면_05(self.ctx)


class 투르카대면_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[209], auto_target=False)
        self.set_effect(trigger_ids=[6001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 투르카대면_06(self.ctx)


class 투르카대면_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52100208_QD__52100208__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 투르카대면_07(self.ctx)


class 투르카대면_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.move_npc(spawn_id=209, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__7$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 투르카대면_07_01(self.ctx)


class 투르카대면_07_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.set_npc_emotion_loop(spawn_id=208, sequence_name='Attack_Idle_A', duration=100000000.0)
        self.add_cinematic_talk(npc_id=11004682, illust_id='ArcaneBlader_unfair', align=Align.Right, msg='$52100208_QD__52100208__8$', duration=3000)
        self.add_cinematic_talk(npc_id=11004680, illust_id='Eone_serious', align=Align.Right, msg='$52100208_QD__52100208__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 투르카대면_08(self.ctx)


class 투르카대면_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008,4009], return_view=False)
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__10$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 투르카대면_09(self.ctx)


class 투르카대면_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=209, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__11$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 투르카대면_10(self.ctx)


class 투르카대면_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11004675, illust_id='Bliche_mad', align=Align.Right, msg='$52100208_QD__52100208__12$', duration=4000)
        self.add_cinematic_talk(npc_id=11004588, illust_id='Conder_normal', align=Align.Left, msg='$52100208_QD__52100208__13$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 투르카대면_11(self.ctx)


class 투르카대면_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011,4012], return_view=False)
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__14$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 투르카대면_12(self.ctx)


class 투르카대면_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=209, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__15$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 투르카대면_13(self.ctx)


class 투르카대면_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014,4015], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Angry_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52100208_QD__52100208__16$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 투르카대면_13_02(self.ctx)


class 투르카대면_13_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_3003')
        self.add_cinematic_talk(npc_id=11004588, illust_id='Conder_normal', align=Align.Right, msg='$52100208_QD__52100208__17$', duration=4000)
        self.add_cinematic_talk(npc_id=11004588, illust_id='Conder_normal', align=Align.Right, msg='$52100208_QD__52100208__18$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 투르카대면_13_03(self.ctx)


class 투르카대면_13_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__19$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 투르카대면_13_04(self.ctx)


class 투르카대면_13_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=209, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대면_13_05(self.ctx)


class 투르카대면_13_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.set_effect(trigger_ids=[6003], visible=True)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Stun_A', duration=100000000.0)
        self.add_cinematic_talk(npc_id=11004588, illust_id='0', msg='$52100208_QD__52100208__20$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 투르카대면_13_06(self.ctx)


class 투르카대면_13_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_3004')
        self.add_cinematic_talk(npc_id=11004678, illust_id='Neirin_surprise', align=Align.Left, msg='$52100208_QD__52100208__21$', duration=4000)
        self.add_cinematic_talk(npc_id=11004677, illust_id='Schatten_surprise', align=Align.Right, msg='$52100208_QD__52100208__22$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 투르카대면_14(self.ctx)


class 투르카대면_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11004683, msg='$52100208_QD__52100208__23$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 투르카대면_15(self.ctx)


class 투르카대면_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True)
        self.destroy_monster(spawn_ids=[209], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카대면_16(self.ctx)


class 투르카대면_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52100208_QD__52100208__24$', duration=3000)
        self.add_cinematic_talk(npc_id=11004679, illust_id='Mason_closeEye', align=Align.Right, msg='$52100208_QD__52100208__25$', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 정리_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리_03(self.ctx)


class 정리_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020071, portal_id=2)


initial_state = wait_01
