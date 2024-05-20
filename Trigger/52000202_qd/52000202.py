""" trigger/52000202_qd/52000202.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003431], quest_states=[1]):
            # 환영의 습격 퀘스트 수락
            return CameraEffect01(self.ctx)
        if not self.quest_user_detected(box_ids=[2001], quest_ids=[10003431], quest_states=[1]):
            # 환영의 습격 퀘스트 수락 유저가 아니면
            return 고마해_04(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000202, portal_id=5001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.show_caption(type='VerticalCaption', title='$52000202_QD__52000202__0$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시공의균열(self.ctx)


class 시공의균열(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003,4004], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__1$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__2$', duration=5000)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__3$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 시공의균열_02_01(self.ctx)


class 시공의균열_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=11000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시공의균열_02_02(self.ctx)


class 시공의균열_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__5$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 시공의균열_03(self.ctx)


class 시공의균열_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.set_portal(portal_id=8001)
        self.set_portal(portal_id=8002)
        self.move_user(map_id=52000202, portal_id=5002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시공의균열_03_02(self.ctx)


class 시공의균열_03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.set_portal(portal_id=8003)
        self.set_portal(portal_id=8004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시공의균열_04(self.ctx)


class 시공의균열_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__7$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__8$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 전투준비(self.ctx)


class 전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=4500.0)
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__9$', duration=4500)
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return UI테스트(self.ctx)


class UI테스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 몰려온다(self.ctx)


class 몰려온다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3006') # 뛰어가기
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_3004')
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_3005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몰려온다_02(self.ctx)


class 몰려온다_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.5, duration=5.0, interpolator=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몰려온다_03(self.ctx)


class 몰려온다_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[205])
        self.destroy_monster(spawn_ids=[206])
        self.destroy_monster(spawn_ids=[207])
        self.destroy_monster(spawn_ids=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 고마해(self.ctx)


class 고마해(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)
        self.select_camera_path(path_ids=[4011], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 고마해_02(self.ctx)


class 고마해_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__10$', duration=2500)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__11$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            return 고마해_03(self.ctx)


class 고마해_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=9000.0)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__13$', duration=4500)
        self.add_cinematic_talk(npc_id=0, msg='$52000202_QD__52000202__14$', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 고마해_04(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 고마해_04(self.ctx)


class 고마해_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=2001, achieve='illusionaryAttack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이동시키기(self.ctx)


class 이동시키기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000201, portal_id=5001)


initial_state = start
