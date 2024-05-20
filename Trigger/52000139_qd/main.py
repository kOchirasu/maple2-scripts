""" trigger/52000139_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0) # 유저 이동 하게
        self.set_cinematic_ui(type=2) # UI 복구
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[107])
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014]) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002700], quest_states=[3]):
            return 다시검은화면_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002700], quest_states=[2]):
            return 퀘스트진행_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002700], quest_states=[1]):
            return 퀘스트수락_02(self.ctx)
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
        self.play_scene_movie(file_name='common\\JobIntro_Priest.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상마무리_01(self.ctx)
        if self.wait_tick(wait_tick=53000):
            return 영상마무리_01(self.ctx)


class 영상마무리_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라연출_01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 카메라연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_cinematic_ui(type=1) # 유저 이동 못하게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라연출_02(self.ctx)


class 카메라연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=14000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 카메라연출_03(self.ctx)


class 카메라연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000139_QD__MAIN__22$', desc='$52000139_QD__MAIN__23$', align=Align.Bottom | Align.Left, duration=4000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 검은화면전환_01(self.ctx)


class 검은화면전환_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검은화면전환_02(self.ctx)


class 검은화면전환_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=3) # 상하 레터박스
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 밝은화면전환_01(self.ctx)


class 밝은화면전환_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=2000.0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_00(self.ctx)


class 기사와대화_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=퀘스트수락_01, action='nextState')
        self.add_cinematic_talk(npc_id=11003320, msg='$52000139_QD__MAIN__0$', duration=2500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_01(self.ctx)


class 기사와대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__1$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_02(self.ctx)


class 기사와대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003320, msg='$52000139_QD__MAIN__2$', duration=2500, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003320, msg='$52000139_QD__MAIN__3$', duration=2500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 기사와대화_03(self.ctx)


class 기사와대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__4$', duration=2500)
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__5$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 기사와대화_04(self.ctx)


class 기사와대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003320, msg='$52000139_QD__MAIN__6$', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_05(self.ctx)


class 기사와대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_06(self.ctx)


class 기사와대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.move_user_path(patrol_name='MS2PatrolData_2004')
        self.add_cinematic_talk(npc_id=11003321, msg='$52000139_QD__MAIN__8$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 기사와대화_07(self.ctx)


class 기사와대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003320, msg='$52000139_QD__MAIN__9$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 퀘스트수락_01(self.ctx)


"""
class 기사와대화_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003321, msg='$52000139_QD__MAIN__10$', duration=2500, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003321, msg='$52000139_QD__MAIN__11$', duration=2500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5772):
            return 기사와대화_09(self.ctx)
"""

"""
class 기사와대화_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__12$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트수락_01(self.ctx)
"""

class 퀘스트수락_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게
        self.set_cinematic_ui(type=2) # UI 원상복구
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트수락_02(self.ctx)


class 퀘스트수락_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201394, text_id=25201394)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002700], quest_states=[1]):
            return 기지로이동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201394)


class 기지로이동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014], visible=True) # 경로 안내
        self.show_guide_summary(entity_id=25201391, text_id=25201391)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002700], quest_states=[1]):
            return 퀘스트진행_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201391)


class 퀘스트진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014])
        self.show_guide_summary(entity_id=25201392, text_id=25201392)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002700], quest_states=[2]):
            return 퀘스트완료가능_01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108], auto_target=False)


class 퀘스트완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201392)
        self.show_guide_summary(entity_id=25201393, text_id=25201393)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002700], quest_states=[3]):
            return 다시검은화면_01(self.ctx)


class 다시검은화면_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000139, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 다시검은화면_02(self.ctx)


class 다시검은화면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 부상병과대화_01(self.ctx)


class 부상병과대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201393)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003327, msg='$52000139_QD__MAIN__13$', duration=3000)
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부상병과대화_02(self.ctx)


class 부상병과대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부상병과대화_03(self.ctx)


class 부상병과대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003327, msg='$52000139_QD__MAIN__15$', duration=2500)
        self.add_cinematic_talk(npc_id=11003327, msg='$52000139_QD__MAIN__16$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 부상병과대화_04(self.ctx)


class 부상병과대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부상병과대화_05(self.ctx)


class 부상병과대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003327, msg='$52000139_QD__MAIN__18$', duration=2500)
        self.add_cinematic_talk(npc_id=11003327, msg='$52000139_QD__MAIN__19$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 부상병과대화_06(self.ctx)


class 부상병과대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__20$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부상병과대화_07(self.ctx)


class 부상병과대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004,8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return 부상병과대화_08(self.ctx)


class 부상병과대화_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000139_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000140, portal_id=1)


initial_state = 준비
