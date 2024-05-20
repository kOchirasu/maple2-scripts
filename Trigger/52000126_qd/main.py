""" trigger/52000126_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 이름 없는 부랑자 (11000213) 퀘스트 / 이름 없는 부랑자(11003209) 연출
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이름 없는 부랑자 퀘스트 (11000213)
        self.spawn_monster(spawn_ids=[101])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100210], quest_states=[1]):
            return ready(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_portal(portal_id=1)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.destroy_monster(spawn_ids=[101]) # 이름 없는 부랑자 퀘스트
        self.spawn_monster(spawn_ids=[102]) # 이름 없는 부랑자 연출
        self.move_user(map_id=52000126, portal_id=6002)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return talk_01(self.ctx)


# 이름 없는 부랑자 대사
class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003209, msg='$52000126_QD__MAIN__0$', duration=2000, align=Align.Left)
        self.spawn_monster(spawn_ids=[301]) # 11003214
        self.spawn_monster(spawn_ids=[302]) # 11003213
        self.spawn_monster(spawn_ids=[303]) # 11003212

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003209, msg='$52000126_QD__MAIN__1$', duration=2000, align=Align.Left)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_01(self.ctx)


# 마스크단 등장씬
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003214, msg='$52000126_QD__MAIN__2$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003214, msg='$52000126_QD__MAIN__3$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003214, msg='$52000126_QD__MAIN__4$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005,4006,4007], return_view=False)
        self.add_cinematic_talk(npc_id=11003214, msg='$52000126_QD__MAIN__5$', duration=3000, align=Align.Left)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3005')
        self.set_npc_emotion_loop(spawn_id=302, sequence_name='Attack_Idle_A', duration=7000.0)
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Attack_Idle_A', duration=7000.0)
        self.add_cinematic_talk(npc_id=11003213, msg='$52000126_QD__MAIN__6$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Attack_01_A')
        self.add_cinematic_talk(npc_id=11003214, msg='$52000126_QD__MAIN__7$', duration=3000, align=Align.Left)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[301,302,303]) # 디쓰리 엔피씨
        self.spawn_monster(spawn_ids=[601,602,603]) # 디쓰리 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000126_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='maskbattle')
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = idle
