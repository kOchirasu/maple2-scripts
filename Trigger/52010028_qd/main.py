""" trigger/52010028_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 흘러내린 시간의 틈 : 52010028
class 던전에들어왔으면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return black(self.ctx)


class black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(is_visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 떨어져서아파(self.ctx)


class 떨어져서아파(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequence_names=['Damg_C'])
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 웰컴문구1(self.ctx)


class 웰컴문구1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequence_name='Emotion_Bloompicnic_A', duration=7000.0)
        self.spawn_monster(spawn_ids=[9999], auto_target=False) # 구르는 천둥:11003390
        self.face_emotion(emotion_name='Trigger_disappoint')
        self.show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__0$', desc='$52010028_QD__MAIN__1$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__2$', duration=3000)
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 웰컴문구2(self.ctx)


class 웰컴문구2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__3$', duration=2000)
        self.set_onetime_effect(id=302, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시선이동(self.ctx)


class 시선이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=303, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=403, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 웰컴문구3(self.ctx)


class 웰컴문구3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 웰컴문구4(self.ctx)


class 웰컴문구4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__7$', duration=3000)
        self.destroy_monster(spawn_ids=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 웰컴문구4_1(self.ctx)


class 웰컴문구4_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이제가자(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=500.0)
        self.destroy_monster(spawn_ids=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이제가자(self.ctx)


class 이제가자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__35$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 구르는 천둥:11003390
        self.spawn_monster(spawn_ids=[201]) # 붉은 늑대의 심장:11003387
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010028, portal_id=7001)
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__9$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Down_Idle_A', duration=1500000.0)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Attack_Idle_A', duration=1500000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC진입(self.ctx)


class PC진입(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='3002')
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__10$', duration=2000)
        self.add_balloon_talk(msg='$52010028_QD__MAIN__11$', duration=2000, delay_tick=1000)
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Crazy')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_01(self.ctx)


class 연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__12$', duration=3000)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Danger')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_02(self.ctx)


class 연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연출_02_1(self.ctx)


class 연출_02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Attack_02_D')
        self.set_effect(trigger_ids=[5001], visible=True)
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__13$', duration=3000)
        self.show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__14$', desc='$52010028_QD__MAIN__15$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003390, msg='$52010028_QD__MAIN__16$', duration=3000, illust_id='0', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__17$', duration=2000)
        self.add_cinematic_talk(npc_id=11003390, msg='$52010028_QD__MAIN__18$', duration=3000)
        self.set_onetime_effect(id=304, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Crazy')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 연출_03(self.ctx)


class 연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.add_cinematic_talk(npc_id=11003390, msg='$52010028_QD__MAIN__19$', duration=3000, illust_id='0', align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Idle_A', duration=10000.0)
        self.select_camera_path(path_ids=[4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_04(self.ctx)


class 연출_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_3001')
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__20$', duration=3000, illust_id='0', align=Align.Left)
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출_04_01(self.ctx)


class 연출_04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Attack_02_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 연출_04_02(self.ctx)


class 연출_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Fury')
        self.set_effect(trigger_ids=[5002], visible=True)
        self.add_cinematic_talk(npc_id=11003387, msg='$52010028_QD__MAIN__22$', duration=3000, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 연출_05(self.ctx)


class 연출_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Crazy')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출_06(self.ctx)


class 연출_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출_07(self.ctx)


class 연출_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.move_user_path(patrol_name='3002')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비(self.ctx)


class 전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Down_Idle_A', duration=3000.0)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_3003')
        self.destroy_monster(spawn_ids=[201]) # 붉은 늑대의 심장:11003387
        self.spawn_monster(spawn_ids=[501]) # 붉은 늑대의 심장:22000324

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투메시지(self.ctx)


class 전투메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__23$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투(self.ctx)


class 전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501]):
            return 전투종료(self.ctx)


class 전투종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투종료대사(self.ctx)


class 전투종료대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Maze')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=이동, action='exit')
        self.move_user(map_id=52010028, portal_id=7002)
        self.spawn_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투종료이후연출(self.ctx)


class 전투종료이후연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=1500000.0)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Dead')
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Dead_Idle_A', duration=150000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 찾으러왔어01(self.ctx)


class 찾으러왔어01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__24$', duration=3000)
        self.spawn_monster(spawn_ids=[301])
        self.face_emotion(spawn_id=301, emotion_name='Trigger_Dead')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 찾으러왔어02(self.ctx)


class 찾으러왔어02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3004')
        self.add_balloon_talk(spawn_id=301, msg='$52010028_QD__MAIN__25$', duration=2000, delay_tick=1000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=150000.0)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Dead')
        self.face_emotion(spawn_id=301, emotion_name='down_Idle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 찾으러왔어03(self.ctx)


class 찾으러왔어03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[302])
        self.spawn_monster(spawn_ids=[303])
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3005')
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_3006')
        self.add_balloon_talk(spawn_id=302, msg='$52010028_QD__MAIN__26$', duration=2000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=303, msg='$52010028_QD__MAIN__27$', duration=2000, delay_tick=1200)
        self.move_user(map_id=52010028, portal_id=7003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 찾으러왔어04(self.ctx)


class 찾으러왔어04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[304])
        self.spawn_monster(spawn_ids=[305])
        self.move_npc(spawn_id=304, patrol_name='MS2PatrolData_3007')
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_3008')
        self.add_balloon_talk(spawn_id=304, msg='$52010028_QD__MAIN__28$', duration=2000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=305, msg='$52010028_QD__MAIN__29$', duration=2000, delay_tick=1200)
        self.move_user(map_id=52010028, portal_id=7003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 어서와(self.ctx)


class 어서와(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_Idle_A', duration=1500000.0)
        self.face_emotion(spawn_id=101, emotion_name='Trigger_Dead')
        self.add_cinematic_talk(npc_id=0, msg='$52010028_QD__MAIN__30$', duration=3000)
        self.add_cinematic_talk(npc_id=11003456, msg='$52010028_QD__MAIN__31$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8191):
            return 어서와02(self.ctx)


class 어서와02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=305, sequence_name='Bore_A')
        self.set_npc_emotion_sequence(spawn_id=304, sequence_name='Talk_A')
        self.add_balloon_talk(spawn_id=305, msg='$52010028_QD__MAIN__32$', duration=2000)
        self.add_balloon_talk(spawn_id=304, msg='$52010028_QD__MAIN__33$', duration=2000, delay_tick=500)
        self.add_balloon_talk(spawn_id=302, msg='$52010028_QD__MAIN__34$', duration=2000, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 어서와03(self.ctx)


class 어서와03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010032, portal_id=1)


initial_state = 던전에들어왔으면
