""" trigger/52000148_qd/52000148_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 잠시대기_01(self.ctx)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_user(map_id=52000148, portal_id=99)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 잠시대기_03(self.ctx)


class 잠시대기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=130000.0)
        self.face_emotion(emotion_name='Think_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시작_02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작_03(self.ctx)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스카와대화_01(self.ctx)


class 오스카와대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__1$', duration=2500, align=Align.Right)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
        self.set_scene_skip(state=오스카퇴장_02, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카와대화_02(self.ctx)


class 오스카와대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__2$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카와대화_03(self.ctx)


class 오스카와대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__3$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카와대화_04(self.ctx)


class 오스카와대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__4$', duration=3000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스카와대화_05(self.ctx)


class 오스카와대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__5$', duration=4000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 오스카와대화_06(self.ctx)


class 오스카와대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__6$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카와대화_07(self.ctx)


class 오스카와대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__7$', duration=3000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__8$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 오스카와대화_08(self.ctx)


class 오스카와대화_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스카와대화_09(self.ctx)


class 오스카와대화_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__9$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__10$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 오스카와대화_10(self.ctx)


class 오스카와대화_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스카와대화_11(self.ctx)


class 오스카와대화_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__11$', duration=2500, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스카와대화_12(self.ctx)


class 오스카와대화_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__12$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__13$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 오스카와대화_13(self.ctx)


class 오스카와대화_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__14$', duration=3500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__15$', duration=3500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__16$', duration=2500, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16613):
            return 오스카와대화_14(self.ctx)


class 오스카와대화_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__17$', duration=2500, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__18$', duration=4000, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__19$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 오스카와대화_15(self.ctx)


class 오스카와대화_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__20$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카와대화_16(self.ctx)


class 오스카와대화_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__21$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스카와대화_17(self.ctx)


class 오스카와대화_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__22$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__23$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 오스카와대화_18(self.ctx)


class 오스카와대화_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__24$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스카와대화_19(self.ctx)


class 오스카와대화_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000148_QD__52000148_MAIN__25$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스카퇴장_01(self.ctx)


class 오스카퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 오스카퇴장_02(self.ctx)


class 오스카퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 독백_01(self.ctx)


class 독백_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 독백_02(self.ctx)


class 독백_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__26$', duration=2500, align=Align.Right)
        self.set_scene_skip(state=마무리_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 독백_03(self.ctx)


class 독백_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 독백_04(self.ctx)


class 독백_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__27$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 독백_05(self.ctx)


class 독백_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 독백_06(self.ctx)


class 독백_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000148_QD__52000148_MAIN__28$', duration=3500, align=Align.Right)
        self.face_emotion()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마무리_01(self.ctx)


class 마무리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마무리_02(self.ctx)


class 마무리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__29$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000062, portal_id=13)


initial_state = 준비
