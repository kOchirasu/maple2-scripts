""" trigger/52000037_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='Dead_A') # NelfActor
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        self.set_onetime_effect(id=3, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=4, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=5, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=6, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100125], quest_states=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100125,60100126,60100127,60100128,60100129,60100130,60100131,60100132,60100133,60100134,60100135], quest_states=[2]):
            return npcspawn_02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100135], quest_states=[3]):
            return npcspawn_03(self.ctx)


# 첫 진입 시 연출
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_sound(trigger_id=7001, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return waitng(self.ctx)


class waitng(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.move_user(map_id=52000037, portal_id=1)
        self.spawn_monster(spawn_ids=[604]) # 604:연출용 고호: 11003204
        self.spawn_monster(spawn_ids=[602]) # 602:연출용 조디: 11003202

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return startscene(self.ctx)


class startscene(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4001,4002,4003,4004,4005,4006,4007], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_01(self.ctx)


# 조디 연출 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=602, patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=11003202, illust_id='Jordy_normal', msg='$52000037_QD__MAIN__0$', duration=3000, align=Align.Right)
        self.set_scene_skip(state=fadeout, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=604, patrol_name='MS2PatrolData_3004')
        self.add_cinematic_talk(npc_id=11003204, msg='$52000037_QD__MAIN__1$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003202, illust_id='Jordy_normal', msg='$52000037_QD__MAIN__2$', duration=4000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003204, msg='$52000037_QD__MAIN__3$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003202, illust_id='Jordy_normal', msg='$52000037_QD__MAIN__4$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=604, sequence_name='Bore_C')
        self.add_cinematic_talk(npc_id=11003204, msg='$52000037_QD__MAIN__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3735):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=602, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_12(self.ctx)


class scene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return scene_13(self.ctx)


class scene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return scene_14(self.ctx)


class scene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_15(self.ctx)


class scene_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003202, illust_id='Jordy_normal', msg='$52000037_QD__MAIN__6$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_16(self.ctx)


class scene_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=604, sequence_name='Bore_C')
        self.add_cinematic_talk(npc_id=11003204, msg='$52000037_QD__MAIN__7$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return endready(self.ctx)


class endready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[602,604])
        self.spawn_monster(spawn_ids=[601]) # 601:퀘스트 고호: 11003204
        self.spawn_monster(spawn_ids=[603]) # 603:퀘스트 조디: 11003203
        self.reset_camera()
        self.set_sound(trigger_id=7001)
        self.set_achievement(trigger_id=9900, type='trigger', achieve='nelfmissing')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 퀘스트 진행 및 완료 상태
class npcspawn_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601,602,603,604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return npcspawn_02_A(self.ctx)


class npcspawn_02_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[603]) # 603:퀘스트 조디
        self.spawn_monster(spawn_ids=[601]) # 601:고호


class npcspawn_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601,602,603,604])


initial_state = idle
