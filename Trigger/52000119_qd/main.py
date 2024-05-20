""" trigger/52000119_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
골든타워 8층 : 60100030
랄프:11003187 / 조디:11003169 / 코쿤:11003171
오프닝 연출
"""
class intro(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920]) # 기본 배치 몬스터
        self.spawn_monster(spawn_ids=[921,922,923,924,925,926,927,928,929]) # 기본 배치 몬스터
        self.spawn_monster(spawn_ids=[104,105]) # 104:랄프
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100030], quest_states=[1]):
            return fadeout_01(self.ctx)


class fadeout_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[104,105]) # 104: 랄프
        # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        self.spawn_monster(spawn_ids=[101,102,103])
        self.select_camera_path(path_ids=[4010,4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return fadein_01(self.ctx)


class fadein_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Sit_Down_A', duration=900000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return eventscene_01(self.ctx)


class eventscene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003169, illust_id='Jordy_normal', msg='$52000119_QD__MAIN__0$', duration=3000, align=Align.Left)
        self.set_scene_skip(state=fadeout_02, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return eventscene_02(self.ctx)


class eventscene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.set_dialogue(type=2, spawn_id=11000173, script='$52000119_QD__MAIN__1$', time=3) # 브로커 랄프
        self.set_dialogue(type=2, spawn_id=11000173, script='$52000119_QD__MAIN__2$', time=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return eventscene_03(self.ctx)


class eventscene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4003], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk')
        self.set_dialogue(type=2, spawn_id=11000173, script='$52000119_QD__MAIN__3$', time=3) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return eventscene_04(self.ctx)


class eventscene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Damg_B')
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN__4$', time=3) # 코쿤

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return eventscene_05(self.ctx)


class eventscene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.set_dialogue(type=2, spawn_id=11000173, script='$52000119_QD__MAIN__5$', time=3) # 브로커 랄프
        self.set_dialogue(type=2, spawn_id=11000173, script='$52000119_QD__MAIN__6$', time=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return eventscene_06(self.ctx)


class eventscene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_A')
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN__7$', time=3) # 코쿤
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN__8$', time=3, arg5=3) # 코쿤
        self.set_dialogue(type=1, spawn_id=102, script='$52000119_QD__MAIN__9$', time=2, arg5=4) # 코쿤
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return fadeout_02(self.ctx)


class fadeout_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return reset(self.ctx)


class reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return eventscene_end(self.ctx)


class eventscene_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN__10$', arg3='1000', arg4='0')
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return hintmsg(self.ctx)


class hintmsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_dialogue(type=2, script='$52000119_QD__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return play(self.ctx)


class play(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return fadeout_03(self.ctx)


class fadeout_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawn_ids=[921,922,923,924,925,926,927,928,929])
        # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        self.destroy_monster(spawn_ids=[101,102,103])
        # 104:랄프 / 105:조디 / 106: 브로커 랄프의 수하
        self.spawn_monster(spawn_ids=[104,105,106])
        self.move_user(map_id=52000119, portal_id=6002)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return fadein_03(self.ctx)


class fadein_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_3003')
        self.add_balloon_talk(msg='$52000119_QD__MAIN__12$', duration=2000)
        self.set_scene_skip(state=fadeout_04, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return bossscene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class bossscene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Sit_Down_A', duration=150000.0)
        self.set_dialogue(type=2, spawn_id=11003187, script='$52000119_QD__MAIN__13$', time=3) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return bossscene_02(self.ctx)


class bossscene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.set_dialogue(type=2, spawn_id=11003187, script='$52000119_QD__MAIN__14$', time=3) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return bossscene_03(self.ctx)


class bossscene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11003187, script='$52000119_QD__MAIN__15$', time=3) # 랄프
        self.set_dialogue(type=1, spawn_id=105, script='$52000119_QD__MAIN__16$', time=3, arg5=1) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return bossscene_04(self.ctx)


class bossscene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013,4014,4015], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.set_dialogue(type=2, spawn_id=11003187, script='$52000119_QD__MAIN__17$', time=3) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return bossscene_05(self.ctx)


class bossscene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Talk_A')
        self.face_emotion(emotion_name='Object_React_A')
        self.set_dialogue(type=2, spawn_id=11003187, script='$52000119_QD__MAIN__18$', time=3) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return bossscene_06(self.ctx)


class bossscene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3004')
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Attack_01_C')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_3001')
        self.face_emotion(emotion_name='Object_React_A')
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN__19$', time=3) # 코쿤

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return bossscene_07(self.ctx)


class bossscene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Bore_A')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=4000.0)
        self.face_emotion(emotion_name='Object_React_A')
        self.set_dialogue(type=2, spawn_id=11003171, script='$52000119_QD__MAIN__20$', time=3) # 코쿤
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return fadeout_04(self.ctx)


class fadeout_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001)
        self.set_sound(trigger_id=7002, enable=True)
        self.destroy_monster(spawn_ids=[106]) # 106: 코쿤
        self.spawn_monster(spawn_ids=[997]) # 999: 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadein_04(self.ctx)


class fadein_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_balloon_talk(spawn_id=997, msg='$52000119_QD__MAIN__21$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return bossmsg(self.ctx)


class bossmsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[997]):
            return wait(self.ctx)


class wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7002)
        self.add_balloon_talk(spawn_id=104, msg='$52000119_QD__MAIN__23$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return fadeout_05(self.ctx)


class fadeout_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[997]) # 106: 코쿤
        self.set_achievement(type='trigger', achieve='jordysave')
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


initial_state = intro
