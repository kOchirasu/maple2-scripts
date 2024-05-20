""" trigger/52010032_qd/main_quest10003079.xml """
import trigger_api


# 나메드가 페리온이야기하고 에바고르는 삐져서 나감
class 무르파고스에들어오면(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003079], quest_states=[1]):
            self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[301])
        self.destroy_monster(spawn_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Ready01(self.ctx)


class Ready01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.face_emotion(spawn_id=401, emotion_name='Trigger_angry')
        self.spawn_monster(spawn_ids=[401]) # 나메드
        self.spawn_monster(spawn_ids=[301]) # 시끄러운 주먹
        self.spawn_monster(spawn_ids=[302]) # 에바고르
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대화시작(self.ctx)


class 대화시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Talk_A')
        self.move_user(map_id=52010032, portal_id=6002)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__0$', duration=3000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__1$', duration=4000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__2$', duration=4000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__3$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 대화시작01(self.ctx)


class 대화시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__4$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52010032_QD__MAIN_QUEST10003079__5$', duration=3500)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__6$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 대화시작02(self.ctx)


class 대화시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Focus_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52010032_QD__MAIN_QUEST10003079__7$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대화시작03(self.ctx)


class 대화시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Bore_A')
        self.face_emotion(spawn_id=203, emotion_name='Trigger_Sad')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__8$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에바고르삐짐(self.ctx)


class 에바고르삐짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010032_QD__MAIN_QUEST10003079__9$', duration=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010032_QD__MAIN_QUEST10003079__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 에바고르삐짐01(self.ctx)


class 에바고르삐짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__11$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010032_QD__MAIN_QUEST10003079__12$', duration=2000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__13$', duration=5000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__14$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 에바고르삐짐02(self.ctx)


class 에바고르삐짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=302, sequence_name='Attack_01_A')
        self.add_cinematic_talk(npc_id=11003391, msg='$52010032_QD__MAIN_QUEST10003079__15$', duration=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010032_QD__MAIN_QUEST10003079__16$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 에바고르퇴장(self.ctx)


class 에바고르퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010032_QD__MAIN_QUEST10003079__17$', duration=3000)
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3006')
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Namid')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에바고르퇴장후(self.ctx)


class 에바고르퇴장후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__18$', duration=3500)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN_QUEST10003079__19$', duration=3500)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010032_QD__MAIN_QUEST10003079__20$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 에바고르퇴장후_1(self.ctx)


class 에바고르퇴장후_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 나메드에게퀘스트마무리(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[302])
        self.destroy_monster(spawn_ids=[401])
        self.reset_camera(interpolation_time=0.5)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Namid')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 나메드에게퀘스트마무리(self.ctx)


class 나메드에게퀘스트마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[302])
        self.destroy_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[202])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return None # Missing State: State


initial_state = 무르파고스에들어오면
