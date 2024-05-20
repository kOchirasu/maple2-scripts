""" trigger/52000142_qd/52000142_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025])
        self.set_effect(trigger_ids=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039])
        self.set_effect(trigger_ids=[5040,5041,5042,5043])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002721], quest_states=[3]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002721], quest_states=[2]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002720], quest_states=[3]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002720], quest_states=[2]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002720], quest_states=[1]):
            return 퀘스트1진행_01(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.add_buff(box_ids=[701], skill_id=70000124, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\JobIntro_Knight.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 시작_01(self.ctx)
        if self.wait_tick(wait_tick=53000):
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작_02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구보훈련_01(self.ctx)


class 구보훈련_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 구보훈련_01_1(self.ctx)


class 구보훈련_01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구보훈련_02(self.ctx)


class 구보훈련_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구보훈련_03(self.ctx)


class 구보훈련_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__0$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 구보훈련_04_1(self.ctx)


class 구보훈련_04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구보훈련_04(self.ctx)


class 구보훈련_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201421, text_id=25201421)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002720], quest_states=[1]):
            return 퀘스트1진행_01(self.ctx)


class 단계별이동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[701], skill_id=70000124, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 단계별이동_02(self.ctx)


class 단계별이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000142, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002721], quest_states=[3]):
            return 퀘2완료(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002721], quest_states=[2]):
            return 퀘2완료가능(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002720], quest_states=[3]):
            return 퀘1완료(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002720], quest_states=[2]):
            return 퀘1완료가능(self.ctx)


class 퀘2완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Emotion_lie_facedown_Idle_A', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2완료_01(self.ctx)


class 퀘2완료가능(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[106])
        self.destroy_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Emotion_lie_facedown_Idle_A', duration=600000.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 수호사제찾기_01(self.ctx)


class 퀘1완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=107, sequence_name='Down_Idle_B', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1완료_02(self.ctx)


class 퀘1완료가능(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[106])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[106])
        self.hide_guide_summary(entity_id=25201421)
        self.show_guide_summary(entity_id=25201422, text_id=25201422)
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025], visible=True)
        self.add_buff(box_ids=[701], skill_id=70000124, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002720], quest_states=[2]):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025])
        self.hide_guide_summary(entity_id=25201422)
        self.show_guide_summary(entity_id=25201423, text_id=25201423)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=107, sequence_name='Down_Idle_B', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002720], quest_states=[3]):
            return 퀘스트1완료_01(self.ctx)


class 퀘스트1완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201423)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1완료_02(self.ctx)


class 퀘스트1완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000142, portal_id=99)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1완료_03(self.ctx)


class 퀘스트1완료_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 로베와대화1_01(self.ctx)


class 로베와대화1_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=벌칙_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__1$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화1_02(self.ctx)


class 로베와대화1_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__2$', duration=3000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화1_03(self.ctx)


class 로베와대화1_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__3$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화1_04(self.ctx)


class 로베와대화1_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__4$', duration=4000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 로베와대화1_05(self.ctx)


class 로베와대화1_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화1_06(self.ctx)


class 로베와대화1_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__6$', duration=3500, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__7$', duration=2500, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__8$', duration=4000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 로베와대화1_07(self.ctx)


class 로베와대화1_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__9$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화1_08(self.ctx)


class 로베와대화1_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__10$', duration=3500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 동료의비웃음_01(self.ctx)


class 동료의비웃음_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52000142_QD__52000142_MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 동료의비웃음_02(self.ctx)


class 동료의비웃음_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=103, script='$52000142_QD__52000142_MAIN__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 동료의비웃음_03(self.ctx)


class 동료의비웃음_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$52000142_QD__52000142_MAIN__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 해명에도불구_01(self.ctx)


class 해명에도불구_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__14$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 해명에도불구_02(self.ctx)


class 해명에도불구_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__15$', duration=3000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 해명에도불구_03(self.ctx)


class 해명에도불구_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__16$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 벌칙_01(self.ctx)


class 벌칙_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=999, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벌칙_02(self.ctx)


class 벌칙_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000142_QD__52000142_MAIN__17$')
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Emotion_lie_facedown_Idle_A', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 벌칙_03(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 벌칙_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=999, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벌칙_04(self.ctx)


class 벌칙_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=수호사제찾기_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__18$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 벌칙_04_1(self.ctx)


class 벌칙_04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벌칙_05(self.ctx)


class 벌칙_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__19$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 벌칙_06(self.ctx)


class 벌칙_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003399, msg='$52000142_QD__52000142_MAIN__20$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 벌칙_06_1(self.ctx)


class 벌칙_06_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벌칙_07(self.ctx)


class 벌칙_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__21$', duration=3500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 벌칙_08(self.ctx)


class 벌칙_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__22$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 벌칙_09(self.ctx)


class 벌칙_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__23$', duration=4000, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__24$', duration=2500, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__25$', duration=3000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 벌칙_10(self.ctx)


class 벌칙_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__26$', duration=3500, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__27$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return 수호사제찾기_01(self.ctx)


class 수호사제찾기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201424, text_id=25201424)
        self.set_effect(trigger_ids=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039], visible=True)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return 수호사제찾기_02(self.ctx)


class 수호사제찾기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039])
        self.hide_guide_summary(entity_id=25201424)
        self.show_guide_summary(entity_id=25201425, text_id=25201425)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[703], quest_ids=[40002721], quest_states=[2]):
            return 퀘스트2완료가능_01(self.ctx)


class 퀘스트2완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201425)
        self.show_guide_summary(entity_id=25201426, text_id=25201426)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[703], quest_ids=[40002721], quest_states=[3]):
            return 퀘스트2완료_01(self.ctx)


class 퀘스트2완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2완료_02(self.ctx)


class 퀘스트2완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.move_user(map_id=52000142, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2완료_03(self.ctx)


class 퀘스트2완료_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 란스구하기_01(self.ctx)


class 란스구하기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=란스구하기스킵_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__28$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_02(self.ctx)


class 란스구하기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__29$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_03(self.ctx)


class 란스구하기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__30$', duration=2500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 란스구하기_04(self.ctx)


class 란스구하기_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=8000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 란스구하기_05(self.ctx)


class 란스구하기_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__31$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__32$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return 란스구하기_06(self.ctx)


class 란스구하기_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003399, msg='$52000142_QD__52000142_MAIN__33$', duration=1000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 란스구하기_06_1(self.ctx)


class 란스구하기_06_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2006')
        self.destroy_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Down_Idle_B', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 란스구하기_07(self.ctx)


class 란스구하기_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 란스구하기_08(self.ctx)


class 란스구하기_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.move_user_path(patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=1, script='$52000142_QD__52000142_MAIN__34$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 란스구하기_09(self.ctx)


class 란스구하기_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=108, script='$52000142_QD__52000142_MAIN__35$', time=3)
        # self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__35$', duration=2500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 란스구하기_10(self.ctx)


class 란스구하기_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__36$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 란스구하기_10_1(self.ctx)


class 란스구하기_10_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 란스구하기_11(self.ctx)


class 란스구하기_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=110, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__37$', duration=5720, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5720):
            return 란스구하기_11_1(self.ctx)


class 란스구하기_11_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 란스구하기_12(self.ctx)


class 란스구하기_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__38$', duration=3000, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__39$', duration=2500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 란스구하기_13(self.ctx)


class 란스구하기_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2004')
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__40$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_14(self.ctx)


class 란스구하기_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__41$', duration=5903, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8698):
            return 란스구하기_15(self.ctx)


class 란스구하기_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2005')
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__42$', duration=5955, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5955):
            return 란스구하기_16(self.ctx)


class 란스구하기_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__43$', duration=3500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_17(self.ctx)


class 란스구하기_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__44$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_18(self.ctx)


class 란스구하기_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000142_QD__52000142_MAIN__45$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_19(self.ctx)


class 란스구하기_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__46$', duration=3000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 란스구하기_20(self.ctx)


class 란스구하기_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__47$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__48$', duration=2500, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003403, msg='$52000142_QD__52000142_MAIN__49$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 란스구하기_21(self.ctx)


class 란스구하기_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000142_QD__52000142_MAIN__50$', duration=3000, illust_id='Robe_normal', align=Align.Right)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 퇴장_01(self.ctx)


class 란스구하기스킵_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Down_Idle_B', duration=600000.0)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 란스구하기스킵_02(self.ctx)


class 란스구하기스킵_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퇴장_01(self.ctx)


class 퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 퇴장_02(self.ctx)


class 퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108])
        self.show_guide_summary(entity_id=25201427, text_id=25201427)
        self.set_effect(trigger_ids=[5040,5041,5042,5043], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704]):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201427)
        self.remove_buff(box_id=704, skill_id=70000124)
        self.set_effect(trigger_ids=[5040,5041,5042,5043])
        self.move_user(map_id=52000143, portal_id=1)


initial_state = 준비
