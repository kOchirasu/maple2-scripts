""" trigger/52100202_qd/52100202.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003250], quest_states=[2]):
            return wait_01_02(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100202, portal_id=6001)
        self.set_mesh(trigger_ids=[4026], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 티마이온(self.ctx)


class 티마이온(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 티마이온_02(self.ctx)


class 티마이온_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=0, msg='$52100202_QD__52100202__0$', duration=3500)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 티마이온_03(self.ctx)


class 티마이온_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 티마이온_03_01(self.ctx)


class 티마이온_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Attack_Idle', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 티마이온_03_02(self.ctx)


class 티마이온_03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_01_J')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 티마이온_04(self.ctx)


class 티마이온_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4006], return_view=False)
        self.face_emotion(emotion_name='Trigger_serious')
        self.add_cinematic_talk(npc_id=0, msg='$52100202_QD__52100202__1$', duration=4500)
        self.add_cinematic_talk(npc_id=0, msg='$52100202_QD__52100202__2$', duration=4500)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
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
        self.move_user(map_id=2020036, portal_id=6001)


initial_state = wait_01
