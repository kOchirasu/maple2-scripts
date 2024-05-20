""" trigger/52000141_qd/main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 침대로이동(self.ctx)


class 침대로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000141, portal_id=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라연출_01(self.ctx)


class 카메라연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_B', duration=100000.0)
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라연출_02(self.ctx)


class 카메라연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라연출_03(self.ctx)


class 카메라연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 루아나와알론대화_01(self.ctx)


class 루아나와알론대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=정리, action='exit')
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 루아나와알론대화_02(self.ctx)


class 루아나와알론대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__1$', duration=3000)
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 루아나와알론대화_03(self.ctx)


class 루아나와알론대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__3$', duration=2200)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__4$', duration=2200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 루아나줌인_01(self.ctx)


class 루아나줌인_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 버즈아이뷰_01(self.ctx)


class 버즈아이뷰_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루아나워킹_01(self.ctx)


class 루아나워킹_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 알론워킹_01(self.ctx)


class 알론워킹_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다시루아나와알론대화_01(self.ctx)


class 다시루아나와알론대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 다시루아나와알론대화_02(self.ctx)


class 다시루아나와알론대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__6$', duration=3000)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6300):
            return 다시루아나와알론대화_03(self.ctx)


class 다시루아나와알론대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6300):
            return 다시루아나와알론대화_04(self.ctx)


class 다시루아나와알론대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__10$', duration=3000)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__11$', duration=2500)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 다시루아나와알론대화_05(self.ctx)


class 다시루아나와알론대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003330, msg='$52000141_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 다시루아나와알론대화_06(self.ctx)


class 다시루아나와알론대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__14$', duration=3000)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__15$', duration=3000)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000141_QD__MAIN__16$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9300):
            return 알론퇴장_01(self.ctx)


class 알론퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 루아나퇴장_01(self.ctx)


class 루아나퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2004')
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루아나퇴장_02(self.ctx)


class 루아나퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 루아나퇴장_03(self.ctx)


class 루아나퇴장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=100000.0)
        self.face_emotion(emotion_name='Point_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 우울한PC_01(self.ctx)


class 우울한PC_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 프레데릭등장_01(self.ctx)


class 프레데릭등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8009], return_view=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 프레데릭등장_02(self.ctx)


class 프레데릭등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 우울한PC_02(self.ctx)


class 우울한PC_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 프레데릭등장_03(self.ctx)


class 프레데릭등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008], return_view=False)
        self.face_emotion(emotion_name='Think_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 프레데릭과대화_01(self.ctx)


class 프레데릭과대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 프레데릭과대화_02(self.ctx)


class 프레데릭과대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000141_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 프레데릭과대화_03(self.ctx)


class 프레데릭과대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__19$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 프레데릭과대화_04(self.ctx)


class 프레데릭과대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000141_QD__MAIN__20$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 프레데릭과대화_05(self.ctx)


class 프레데릭과대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__21$', duration=2500)
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__22$', duration=3000)
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__23$', duration=2000)
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__24$', duration=3000)
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__25$', duration=3000)
        self.add_cinematic_talk(npc_id=11003331, msg='$52000141_QD__MAIN__26$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return 프리스트의독백_01(self.ctx)


class 프리스트의독백_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008,8006], return_view=False)
        self.face_emotion(emotion_name='Sit_Ground_Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 프리스트의독백_02(self.ctx)


class 프리스트의독백_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000141_QD__MAIN__27$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 프리스트의독백_03(self.ctx)


class 프리스트의독백_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion()
        self.add_cinematic_talk(npc_id=0, msg='$52000141_QD__MAIN__28$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 암전_01(self.ctx)


class 정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=2000062, portal_id=13)


initial_state = 준비
