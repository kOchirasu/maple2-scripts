""" trigger/52000117_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 트라이아 청사 : 60100015
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100015], quest_states=[1]):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadein(self.ctx)

    def on_exit(self) -> None:
        self.move_user(map_id=52000117, portal_id=6001)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return jordyidle(self.ctx)


class jordyidle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__0$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__1$', duration=3000)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return wow(self.ctx)


class wow(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Angry_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52000117_QD__MAIN__15$', duration=2000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_Down_A', duration=3000.0)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_Down_A', duration=3000.0)
        self.add_balloon_talk(spawn_id=101, msg='$52000117_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$52000117_QD__MAIN__6$', duration=3000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False) # 대화 모습
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__7$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_pc_emotion_loop(sequence_name='Emotion_Dance_S', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return pctalk(self.ctx)


class pctalk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Talk_A','Talk_B'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__10$', duration=3000)
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__12$', duration=3000)
        self.add_cinematic_talk(npc_id=11003166, msg='$52000117_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_fadeout(self.ctx)


class scene_fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return jordydel(self.ctx)


class jordydel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_fadein(self.ctx)


class scene_fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='jordyhello')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return endmessage(self.ctx)


class endmessage(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000117_QD__MAIN__14$', arg3='3000', arg4='0')
        self.move_user(map_id=52000118)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return endmessage(self.ctx)


initial_state = ready
