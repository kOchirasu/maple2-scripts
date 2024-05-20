""" trigger/52000119_qd/main2.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
골든타워 8층 : 60100030
랄프:11003187 / 조디:11003169 / 코쿤:11003171
오프닝 연출
"""
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60100060], quest_states=[1]):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[105,106])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawn_ids=[921,922,923,924,925,926,927,928,929])
        # 105:조디 / 106: 브로커 랄프의 수하
        self.spawn_monster(spawn_ids=[105,106])
        self.move_user(map_id=52000119, portal_id=6002)
        self.set_scene_skip(state=fadeout_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006,4007], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.face_emotion(emotion_name='Object_React_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Sit_Down_A', duration=6000.0)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN2__0$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008,4013,4014,4015], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN2__1$', duration=3000, align=Align.Left)
        self.set_dialogue(type=1, spawn_id=105, script='$52000119_QD__MAIN2__2$', time=3) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN2__3$', duration=3000, align=Align.Left)
        self.set_dialogue(type=1, spawn_id=105, script='$52000119_QD__MAIN2__4$', time=3) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN2__5$', duration=4989, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN2__6$', duration=8254, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Damg_B')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__7$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Attack_02_A')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__8$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_npc_emotion_loop(spawn_id=106, sequence_name='Attack_Idle_A', duration=8000.0)
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__9$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016,4017,4018], return_view=False)
        self.face_emotion(emotion_name='Object_React_A')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__10$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__11$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Attack_02_C')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN2__12$', duration=3000, align=Align.Left)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return fadeout_01(self.ctx)


class fadeout_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(trigger_id=7001)
        self.set_sound(trigger_id=7002, enable=True)
        self.set_effect(trigger_ids=[5002])
        self.destroy_monster(spawn_ids=[106]) # 106: 코쿤
        self.spawn_monster(spawn_ids=[998]) # 998: 강해진 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadein_01(self.ctx)


class fadein_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return msg(self.ctx)


class msg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN2__13$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawn_id=997, msg='$52000119_QD__MAIN2__14$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[998]):
            return fadeout_02(self.ctx)


class fadeout_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7002)
        self.destroy_monster(spawn_ids=[998]) # 106: 코쿤
        self.set_achievement(type='trigger', achieve='jordysave2')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
