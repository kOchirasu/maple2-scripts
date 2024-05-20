""" trigger/52000167_qd/52000167.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1000)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='jobChangeStory.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 묘지전경씬01(self.ctx)
        if self.wait_tick(wait_tick=85000):
            return 묘지전경씬01(self.ctx)


class 묘지전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_effect(trigger_ids=[700])
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 묘지전경씬02_1(self.ctx)


class 묘지전경씬02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrol_name='MS2PatrolData_pc')
        self.select_camera_path(path_ids=[4000,4001,4002,4003], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 묘지전경씬02(self.ctx)


class 묘지전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000167_QD__52000167__0$', desc='$52000167_QD__52000167__1$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 묘지전경씬03(self.ctx)


class 묘지전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_balloon_talk(msg='$52000167_QD__52000167__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=52001671, text_id=52001671, duration=10000)
        self.spawn_monster(spawn_ids=[400], auto_target=False) # 조디의무덤

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002369], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 홀슈타트등장00(self.ctx)


# ########################씬2 케이틀린 등장########################
class 홀슈타트등장00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.spawn_monster(spawn_ids=[402], auto_target=False)
        self.spawn_monster(spawn_ids=[403], auto_target=False)
        self.spawn_monster(spawn_ids=[404], auto_target=False)
        self.spawn_monster(spawn_ids=[405], auto_target=False)
        self.spawn_monster(spawn_ids=[406], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 홀슈타트등장01(self.ctx)


class 홀슈타트등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[5000,5001,5002,5003,5004], return_view=False)
        self.move_npc(spawn_id=402, patrol_name='MS2PatrolData_402_hol')
        self.move_npc(spawn_id=403, patrol_name='MS2PatrolData_403')
        self.move_npc(spawn_id=404, patrol_name='MS2PatrolData_404')
        self.move_npc(spawn_id=405, patrol_name='MS2PatrolData_405')
        self.move_npc(spawn_id=406, patrol_name='MS2PatrolData_406')
        self.move_user_path(patrol_name='MS2PatrolData_pc_move')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 홀슈타트등장02_c(self.ctx)


class 홀슈타트등장02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[700], visible=True)
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.3, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        self.add_balloon_talk(msg='$52000167_QD__52000167__3$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 홀슈타트등장02(self.ctx)


class 홀슈타트등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 홀슈타트등장03(self.ctx)


class 홀슈타트등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=52001672, text_id=52001672, duration=10000)
        self.set_onetime_effect(id=40, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002370], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 홀슈타트등장04(self.ctx)


class 홀슈타트등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=402, sequence_name='Attack_Idle_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=403, sequence_name='Attack_Idle_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=404, sequence_name='Attack_Idle_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=405, sequence_name='Attack_Idle_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=406, sequence_name='Attack_Idle_A', duration=800000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002371], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장이동01(self.ctx)


class 수련장이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=100000.0, arg3=True)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 수련장이동02(self.ctx)


class 수련장이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000168, portal_id=80)


initial_state = Wait
