""" trigger/52000198_qd/52000198.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5002)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=4)
        self.set_mesh(trigger_ids=[8002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003422], quest_states=[2]):
            # 바론구한 직후로
            return 도망쳐_12(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003422], quest_states=[1]):
            # 첨부터
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003422], quest_states=[3]):
            # 퀘완료
            return 도망쳐_26(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 에레브
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000198, portal_id=5001)
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect04(self.ctx)


class CameraEffect04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 도망쳐_01(self.ctx)


class 도망쳐_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__1$', align=Align.Left, illust_id='Ereb_serious', duration=4500)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__2$', duration=4000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__3$', align=Align.Left, illust_id='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return 도망쳐_01_02(self.ctx)


class 도망쳐_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__4$', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 도망쳐_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_02(self.ctx)


class 도망쳐_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$52000198_QD__52000198__5$', duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            # 내려가는 포탈1
            return 도망쳐_03(self.ctx)


class 도망쳐_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True)
        self.spawn_monster(spawn_ids=[102]) # 에레브
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            # 내려가는 포탈2
            return 도망쳐_04(self.ctx)


class 도망쳐_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='$52000198_QD__52000198__6$', duration=4000)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2004]):
            # 내려가는 포탈3
            return 도망쳐_05(self.ctx)


class 도망쳐_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=True, enable=True)
        self.spawn_monster(spawn_ids=[103]) # 에레브
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2005]):
            # 내려가는 포탈2
            return 도망쳐_06(self.ctx)


class 도망쳐_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='$52000198_QD__52000198__7$', duration=4000)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2006]):
            # 비밀통로 앞
            return 도망쳐_07(self.ctx)


class 도망쳐_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_08(self.ctx)


class 도망쳐_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000198, portal_id=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 도망쳐_09(self.ctx)


class 도망쳐_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_10(self.ctx)


class 도망쳐_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__8$', align=Align.Right, illust_id='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 도망쳐_10_01(self.ctx)


class 도망쳐_10_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__9$', duration=4000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__10$', align=Align.Right, illust_id='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 도망쳐_10_02(self.ctx)


class 도망쳐_10_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4500.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__11$', duration=4500)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__12$', align=Align.Right, illust_id='Ereb_closeEye', duration=1800)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__13$', align=Align.Right, illust_id='Ereb_serious', duration=4500)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10800):
            return 도망쳐_11(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_11(self.ctx)


class 도망쳐_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='$52000198_QD__52000198__14$', duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2007], quest_ids=[10003422], quest_states=[2]):
            # 바론 감옥 앞
            return 도망쳐_12(self.ctx)


class 도망쳐_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_13(self.ctx)


class 도망쳐_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104]) # 바론
        self.move_user(map_id=52000198, portal_id=5004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 도망쳐_14(self.ctx)


class 도망쳐_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_15(self.ctx)


class 도망쳐_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__15$', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000198_QD__52000198__16$', align=Align.Left, illust_id='Baron_normal', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 도망쳐_15_01(self.ctx)


class 도망쳐_15_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000198_QD__52000198__17$', duration=4500)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000198_QD__52000198__18$', align=Align.Left, illust_id='Baron_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000198_QD__52000198__19$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12500):
            return 도망쳐_16(self.ctx)


class 도망쳐_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_17(self.ctx)


class 도망쳐_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104]) # 아래층바론
        self.spawn_monster(spawn_ids=[105]) # 바론
        self.move_user(map_id=52000198, portal_id=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 도망쳐_19(self.ctx)


class 도망쳐_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_20(self.ctx)


class 도망쳐_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__20$', align=Align.Right, illust_id='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000198_QD__52000198__21$', align=Align.Left, illust_id='Baron_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__22$', align=Align.Right, illust_id='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12500):
            return 도망쳐_21(self.ctx)


class 도망쳐_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 도망쳐_22(self.ctx)


class 도망쳐_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Object_React_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도망쳐_23(self.ctx)


class 도망쳐_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_mesh(trigger_ids=[8001])
        self.set_mesh(trigger_ids=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도망쳐_24(self.ctx)


class 도망쳐_24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.reset_camera()
        self.add_cinematic_talk(npc_id=11001302, msg='$52000198_QD__52000198__23$', align=Align.Right, illust_id='Ereb_serious', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도망쳐_25(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[104]) # 아래층바론
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[105]) # 바론
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(trigger_ids=[8001])
        self.set_mesh(trigger_ids=[8002], visible=True)
        self.move_user(map_id=52000198, portal_id=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 도망쳐_25(self.ctx)


class 도망쳐_25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003422], quest_states=[3]):
            # 퀘완료
            return 도망쳐_26(self.ctx)


class 도망쳐_26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 불길 속으로 퀘스트 바론에게 완료하고 나면 포탈이 활성화 되게 수정
        self.set_portal(portal_id=5002, visible=True, enable=True)
        self.destroy_monster(spawn_ids=[105])


initial_state = start
