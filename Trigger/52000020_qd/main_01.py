""" trigger/52000020_qd/main_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201]) # 퀘스트용 리퍼트(11001262)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100090], quest_states=[2]):
            return ready(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202]) # 연출용 리퍼트 (11003193)
        self.spawn_monster(spawn_ids=[301])
        self.spawn_monster(spawn_ids=[401,402,403]) # 연출용 흑성회
        self.set_portal(portal_id=1)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return camera(self.ctx)


class camera(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4001, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Bore_C')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_01__0$', duration=3709, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003193, msg='$52000020_QD__MAIN_01__1$', duration=3369, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003193, msg='$52000020_QD__MAIN_01__2$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Emotion_Troubled_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_01__3$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_01__4$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.add_balloon_talk(spawn_id=401, msg='$52000020_QD__MAIN_01__5$', duration=1000)
        self.add_balloon_talk(spawn_id=402, msg='$52000020_QD__MAIN_01__6$', duration=1000)
        self.add_balloon_talk(spawn_id=403, msg='$52000020_QD__MAIN_01__7$', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Emotion_Angry_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_01__8$', duration=2000, align=Align.Left)
        self.add_balloon_talk(spawn_id=202, msg='$52000020_QD__MAIN_01__9$', duration=2000, delay_tick=1000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001)
        self.set_sound(trigger_id=7002, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[301]) # 연출용 흑성회 대장(11001262)
        self.destroy_monster(spawn_ids=[401,402,403]) # 연출용 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[501]) # 몬스터 흑성회 대장
        self.spawn_monster(spawn_ids=[601,602,603]) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000020_QD__MAIN_01__10$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawn_id=601, msg='$52000020_QD__MAIN_01__11$', duration=3000, delay_tick=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,601,602,603]):
            return delay(self.ctx)


class delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return winready(self.ctx)


class winready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202]) # 연출용 리퍼트
        self.destroy_monster(spawn_ids=[501]) # 흑성회 대장
        self.destroy_monster(spawn_ids=[601,602,603]) # 흑성회
        self.spawn_monster(spawn_ids=[201]) # 퀘스트용 리퍼트(11001262)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
