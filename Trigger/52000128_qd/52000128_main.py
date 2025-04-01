""" trigger/52000128_qd/52000128_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0) # 유저 이동 하게
        self.set_cinematic_ui(type=2) # UI 복구
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_skill(trigger_ids=[7001])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5008])
        self.set_effect(trigger_ids=[5009])
        self.set_mesh(trigger_ids=[4001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\JobIntro_Thief.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 시작_01(self.ctx)
        if self.wait_tick(wait_tick=33000):
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 금고폭파_01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 금고폭파_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1) # 유저 이동 못 하게
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 금고폭파_02(self.ctx)


class 금고폭파_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 금고폭파_03(self.ctx)


class 금고폭파_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 폭파확인_01(self.ctx)


class 폭파확인_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 빅스소개_01(self.ctx)


class 빅스소개_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 빅스소개_02(self.ctx)


class 빅스소개_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003272, msg='$52000128_QD__52000128_MAIN__0$', duration=2000, align=Align.left)
        self.set_scene_skip(state=제시소개_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 빅스소개_03(self.ctx)


class 빅스소개_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__1$', desc='$52000128_QD__52000128_MAIN__2$', align=Align.bottomLeft, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 제시소개_01(self.ctx)


class 제시소개_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.select_camera_path(path_ids=[8002,8003], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제시소개_02(self.ctx)


class 제시소개_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003273, msg='$52000128_QD__52000128_MAIN__3$', duration=2000, align=Align.left)
        self.set_scene_skip(state=카일소개_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제시소개_03(self.ctx)


class 제시소개_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__4$', desc='$52000128_QD__52000128_MAIN__5$', align=Align.bottomLeft, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 카일소개_01(self.ctx)


class 카일소개_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.select_camera_path(path_ids=[8003,8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카일소개_02(self.ctx)


class 카일소개_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카일소개_03(self.ctx)


class 카일소개_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003280, msg='$52000128_QD__52000128_MAIN__6$', duration=2351, align=Align.left)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_B')
        self.set_scene_skip(state=퀘스트시작_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카일소개_04(self.ctx)


class 카일소개_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__7$', desc='$52000128_QD__52000128_MAIN__8$', align=Align.bottomLeft, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 퀘스트시작_01(self.ctx)


class 퀘스트시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=2.0)
        self.show_guide_summary(entity_id=25201281, text_id=25201281)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002690], quest_states=[1]):
            return 퀘스트진행_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002690], quest_states=[2]):
            return 퀘스트완료가능_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002690], quest_states=[3]):
            return 암전_01(self.ctx)


class 퀘스트진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201281)
        self.show_guide_summary(entity_id=25201282, text_id=25201282)
        self.set_effect(trigger_ids=[5003,5004,5005,5006,5007,5008,5009], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return 퀘스트진행_02(self.ctx)


class 퀘스트진행_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003,5004,5005,5006,5007,5008,5009])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002690], quest_states=[2]):
            return 퀘스트완료가능_01(self.ctx)


class 퀘스트완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201281)
        self.hide_guide_summary(entity_id=25201282)
        self.show_guide_summary(entity_id=25201283, text_id=25201283)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002690], quest_states=[3]):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201281)
        self.hide_guide_summary(entity_id=25201282)
        self.hide_guide_summary(entity_id=25201283)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 암전_02(self.ctx)


class 암전_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.move_user_path(patrol_name='MS2PatrolData_2005')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 밝은화면_01(self.ctx)


class 밝은화면_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 잡담_01(self.ctx)


class 잡담_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000128_QD__52000128_MAIN__9$', time=2)
        self.set_scene_skip(state=교도관등장_06, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 잡담_02(self.ctx)


class 잡담_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[107,109,111,113,115], auto_target=False)
        self.set_dialogue(type=1, spawn_id=104, script='$52000128_QD__52000128_MAIN__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 교도관등장_01(self.ctx)


class 교도관등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2010')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2008')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 교도관등장_02(self.ctx)


class 교도관등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.set_dialogue(type=1, spawn_id=111, script='$52000128_QD__52000128_MAIN__21$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 교도관등장_03(self.ctx)


class 교도관등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 교도관등장_04(self.ctx)


class 교도관등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2012')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 교도관등장_05(self.ctx)


class 교도관등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000128_QD__52000128_MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 교도관등장_06(self.ctx)


class 교도관등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.move_user_path(patrol_name='MS2PatrolData_2013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 교도관등장_07(self.ctx)


class 교도관등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2014')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2014')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 교도관등장_08(self.ctx)


class 교도관등장_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 교도관전투_01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[101,102,104])


class 교도관전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201284, text_id=25201284)
        self.destroy_monster(spawn_ids=[107,109,111,113,115])
        self.spawn_monster(spawn_ids=[108,110,112,114,116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108,110,112,114,116]):
            return 교도관전투끝_01(self.ctx)


class 교도관전투끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25201284)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 교도관전투끝_02(self.ctx)


class 교도관전투끝_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000128, portal_id=99)
        self.spawn_monster(spawn_ids=[117,118,119,120,121])
        self.spawn_monster(spawn_ids=[105])
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2011')
        self.select_camera_path(path_ids=[8009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=117, sequence_name='Dead_Idle_A', duration=3600000.0)
        self.set_npc_emotion_loop(spawn_id=118, sequence_name='Dead_Idle_B', duration=3600000.0)
        self.set_npc_emotion_loop(spawn_id=119, sequence_name='Dead_Idle_B', duration=3600000.0)
        self.set_npc_emotion_loop(spawn_id=120, sequence_name='Dead_Idle_B', duration=3600000.0)
        self.set_npc_emotion_loop(spawn_id=121, sequence_name='Dead_Idle_A', duration=3600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 교도관전투끝_03(self.ctx)


class 교도관전투끝_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투끝_04(self.ctx)


class 전투끝_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=벨마등장_06, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000128_QD__52000128_MAIN__12$', duration=3000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 전투끝_05(self.ctx)


class 전투끝_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52000128_QD__52000128_MAIN__13$', duration=3000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 벨마등장_01(self.ctx)


class 벨마등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 벨마등장_02(self.ctx)


class 벨마등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003274, msg='$52000128_QD__52000128_MAIN__14$', duration=3000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 벨마등장_03(self.ctx)


class 벨마등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000128_QD__52000128_MAIN__15$', duration=4000, align=Align.right)
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 벨마등장_04(self.ctx)


class 벨마등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벨마등장_05(self.ctx)


class 벨마등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003274, msg='$52000128_QD__52000128_MAIN__16$', duration=3000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 벨마등장_06(self.ctx)


class 벨마등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 벨마전투_01(self.ctx)


class 벨마전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201285, text_id=25201285)
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[106])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battleStop') == 1:
            return 벨마전투끝_01(self.ctx)


class 벨마전투끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25201285)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벨마전투끝_02(self.ctx)


class 벨마전투끝_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000128, portal_id=99)
        self.destroy_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[105])
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 벨마전투끝_03(self.ctx)


class 벨마전투끝_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투후대화_01(self.ctx)


class 전투후대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=마무리, action='exit')
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.face_emotion()
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52000128_QD__52000128_MAIN__17$', duration=3000, align=Align.right)
        self.add_cinematic_talk(npc_id=0, msg='$52000128_QD__52000128_MAIN__18$', duration=3000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 전투후대화_02(self.ctx)


class 전투후대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 불길_01(self.ctx)


class 불길_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 탈출_01(self.ctx)


class 탈출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.set_dialogue(type=1, script='$52000128_QD__52000128_MAIN__19$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 탈출_02(self.ctx)


class 탈출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 탈출_03(self.ctx)


class 탈출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003274, msg='$52000128_QD__52000128_MAIN__20$', duration=2000, align=Align.right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000129, portal_id=1)


initial_state = 준비
