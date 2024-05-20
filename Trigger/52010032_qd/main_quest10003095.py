""" trigger/52010032_qd/main_quest10003095.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # 나메드 치유 시전 이펙트
        self.set_effect(trigger_ids=[5002]) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003095], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.move_user(map_id=52010032, portal_id=7001)
        self.spawn_monster(spawn_ids=[101]) # 붉은늑대의심장:
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=100000000.0)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Dead')
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[201]) # 나메드:

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 치유의식_01(self.ctx)


class 치유의식_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__0$', duration=4000)
        self.add_balloon_talk(msg='$52010032_QD__MAIN_QUEST10003095__1$', duration=2000, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 치유의식_02(self.ctx)


class 치유의식_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 치유의식_03(self.ctx)


class 치유의식_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_B')
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_pc_emotion_loop(sequence_name='Emotion_Dance_Event01', duration=7000.0)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__3$', duration=5000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 치유의식_04(self.ctx)


class 치유의식_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 치유의식_04_1(self.ctx)


class 치유의식_04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Down_Idle_A', duration=100000000.0)
        self.add_cinematic_talk(npc_id=11003406, msg='$52010032_QD__MAIN_QUEST10003095__5$', duration=4000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__6$', duration=3000)
        self.add_cinematic_talk(npc_id=11003406, msg='$52010032_QD__MAIN_QUEST10003095__7$', duration=3000)
        self.add_balloon_talk(msg='$52010032_QD__MAIN_QUEST10003095__8$', duration=2000, delay_tick=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 치유의식_05(self.ctx)


class 치유의식_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 치유의식_05_1(self.ctx)


class 치유의식_05_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4003,4001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_B')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=100000000.0)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Dead')
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52010032_QD__MAIN_QUEST10003095__9$', duration=3000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__10$', duration=4000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 의식종료_01(self.ctx)


class 의식종료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A')
        self.move_user_path(patrol_name='MS2PatrolData_3007')
        self.add_cinematic_talk(npc_id=0, msg='$52010032_QD__MAIN_QUEST10003095__12$', duration=3000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003095__13$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 의식종료_02(self.ctx)


class 의식종료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Namid2')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Namid2')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.spawn_monster(spawn_ids=[202]) # 나메드:
        self.destroy_monster(spawn_ids=[201])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return None # Missing State: State


initial_state = idle
