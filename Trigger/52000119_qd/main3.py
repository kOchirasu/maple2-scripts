""" trigger/52000119_qd/main3.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
골든타워 8층 : 60100030
랄프:11003187 / 조디:11003169 / 코쿤:11003171
오프닝 연출
"""
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100070], quest_states=[2]):
            return monsterdel(self.ctx)
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60100075], quest_states=[1]):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawn_ids=[921,922,923,924,925,926,927,928,929])
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[201,202])
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306])
        self.move_user(map_id=52000119, portal_id=6001)
        self.set_scene_skip(state=fadeout_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=6000.0)
        self.face_emotion(emotion_name='Object_React_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003169, illust_id='Jordy_normal', msg='$52000119_QD__MAIN3__0$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN3__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013,4014,4015], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN3__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003187, msg='$52000119_QD__MAIN3__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return cheer_01(self.ctx)


# 응원 씬
class cheer_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.select_camera_path(path_ids=[4023,4024], return_view=False)
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__4$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return cheer_02(self.ctx)


class cheer_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=306, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__5$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return cheer_03(self.ctx)


class cheer_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4024,4025], return_view=False)
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__6$', duration=2000)
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__7$', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return cheer_04(self.ctx)


class cheer_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__8$', duration=2000)
        self.add_balloon_talk(spawn_id=303, msg='$52000119_QD__MAIN3__9$', duration=2000, delay_tick=1)
        self.add_cinematic_talk(npc_id=11003354, msg='$52000119_QD__MAIN3__10$', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_05(self.ctx)


# 응원 씬 종료
class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Stun_A')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN3__11$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003171, msg='$52000119_QD__MAIN3__12$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019,4022], return_view=False)
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_3001')
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN3__13$', time=3) # 코쿤
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return fadeout_01(self.ctx)


class fadeout_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001)
        self.set_sound(trigger_id=7002, enable=True)
        self.destroy_monster(spawn_ids=[106]) # 106: 코쿤
        self.spawn_monster(spawn_ids=[999]) # 998: 강해진 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=100.0)

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
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN3__14$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawn_id=999, msg='$52000119_QD__MAIN3__15$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return fadeout_02(self.ctx)


class fadeout_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7002)
        self.add_balloon_talk(spawn_id=999, msg='$52000119_QD__MAIN3__19$', duration=2000)
        self.add_balloon_talk(spawn_id=306, msg='$52000119_QD__MAIN3__20$', duration=2000, delay_tick=1)
        self.destroy_monster(spawn_ids=[201,202])
        self.destroy_monster(spawn_ids=[401,402,403,404,405,406,407])
        self.set_achievement(type='trigger', achieve='jordysave3')
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


# 진입 시
class monsterdel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawn_ids=[921,922,923,924,925,926,927,928,929])
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406,407])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60100075], quest_states=[1]):
            return ready(self.ctx)


initial_state = idle
