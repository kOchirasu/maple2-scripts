""" trigger/52000020_qd/main_02.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60100095], quest_states=[1]):
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
        self.spawn_monster(spawn_ids=[302]) # 연출용 흑성회 행동대장
        self.spawn_monster(spawn_ids=[404,405,406,407,408,409,410,411]) # 연출용 흑성회
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
        self.set_sound(trigger_id=7001)
        self.set_sound(trigger_id=7002, enable=True)
        self.add_cinematic_talk(npc_id=11003193, msg='$52000020_QD__MAIN_02__0$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003,4004], return_view=False)
        self.move_user(map_id=52000020, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=302, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_02__1$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=302, sequence_name='Emotion_Angry_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_02__2$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=302, sequence_name='ChatUp_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_02__3$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=404, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=405, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=406, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=407, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=408, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=409, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=410, sequence_name='ChatUp_A')
        self.set_npc_emotion_sequence(spawn_id=411, sequence_name='ChatUp_A')
        self.add_balloon_talk(spawn_id=404, msg='$52000020_QD__MAIN_02__4$', duration=2000)
        self.add_balloon_talk(spawn_id=405, msg='$52000020_QD__MAIN_02__5$', duration=2000)
        self.add_balloon_talk(spawn_id=406, msg='$52000020_QD__MAIN_02__6$', duration=2000)
        self.add_balloon_talk(spawn_id=407, msg='$52000020_QD__MAIN_02__7$', duration=2000)
        self.add_balloon_talk(spawn_id=408, msg='$52000020_QD__MAIN_02__8$', duration=2000)
        self.add_balloon_talk(spawn_id=409, msg='$52000020_QD__MAIN_02__9$', duration=2000)
        self.add_balloon_talk(spawn_id=410, msg='$52000020_QD__MAIN_02__10$', duration=2000)
        self.add_balloon_talk(spawn_id=411, msg='$52000020_QD__MAIN_02__11$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=502, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=29000266, msg='$52000020_QD__MAIN_02__12$', duration=2000, align=Align.Center)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return battle_ready(self.ctx)


# Round_1 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[404,405]) # 연출용 흑성회
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[604,605]) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000020_QD__MAIN_02__13$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[604,605]):
            return delay(self.ctx)


class delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return round_2(self.ctx)


class round_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[406,407,408,409]) # 연출용 흑성회
        self.spawn_monster(spawn_ids=[606,607,608,609]) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[604,605]):
            return delay_a(self.ctx)


class delay_a(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return round_3(self.ctx)


class round_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[410,411,302]) # 연출용 흑성회
        self.spawn_monster(spawn_ids=[610,611,502]) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[610,611,502]):
            return delay_b(self.ctx)


class delay_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2002, type='trigger', achieve='mafiabattle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return winready(self.ctx)


class winready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202]) # 연출용 리퍼트
        self.spawn_monster(spawn_ids=[201]) # 퀘스트용 리퍼트(11001262)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_sound(trigger_id=7002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
