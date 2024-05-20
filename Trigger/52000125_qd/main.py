""" trigger/52000125_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 노란 머리의 행방: 60100185 / 거짓말의 이유: 60100190 / 유력한 목격자: 60100195
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 연출용 마크(11003205)
        self.set_sound(trigger_id=7001, enable=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100185], quest_states=[1]):
            return fadein(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100185,60100186,60100187,60100188,60100189,60100190,60100191,60100192,60100193,60100194,60100195], quest_states=[2]):
            return end(self.ctx)


# 준비
class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[301]) # 연출용 디나(11003214)
        self.spawn_monster(spawn_ids=[302])
        self.spawn_monster(spawn_ids=[303]) # 연출용 디오(11003212)
        self.move_user(map_id=52000125, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003205, msg='$52000125_QD__MAIN__0$', duration=3000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.add_cinematic_talk(npc_id=11003214, msg='$52000125_QD__MAIN__1$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003214, msg='$52000125_QD__MAIN__2$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.add_cinematic_talk(npc_id=11003213, msg='$52000125_QD__MAIN__3$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003205, msg='$52000125_QD__MAIN__4$', duration=3000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.add_cinematic_talk(npc_id=11003212, msg='$52000125_QD__MAIN__5$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.add_cinematic_talk(npc_id=11003205, msg='$52000125_QD__MAIN__6$', duration=3000, align=Align.Center)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return wait(self.ctx)


class wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301,302,303]) # 연출용 마스크단
        self.spawn_monster(spawn_ids=[601,602,603], auto_target=False) # 몬스터 불량배
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawn_id=601, msg='$52000125_QD__MAIN__7$', duration=3000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=602, msg='$52000125_QD__MAIN__8$', duration=3000, delay_tick=3000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000125_QD__MAIN__9$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603]):
            return delay(self.ctx)


class delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='markguard')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return winready(self.ctx)


class winready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601,602,603]) # 불량배
        self.spawn_monster(spawn_ids=[304,305,306])
        self.move_user(map_id=52000125, portal_id=6001)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return endcamera(self.ctx)


class endcamera(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return bye(self.ctx)


class bye(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003214, msg='$52000125_QD__MAIN__10$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return run(self.ctx)


class run(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=304, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=306, patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=11003214, msg='$52000125_QD__MAIN__11$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return thanks(self.ctx)


class thanks(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Clap_A')
        self.add_cinematic_talk(npc_id=11003205, msg='$52000125_QD__MAIN__12$', duration=2000, align=Align.Center)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(trigger_id=7001)
        self.destroy_monster(spawn_ids=[304,305,306])
        self.destroy_monster(spawn_ids=[101]) # 연출용 마크(11003205)
        self.spawn_monster(spawn_ids=[102]) # 퀘스트용 마크(11003206)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()


initial_state = idle
