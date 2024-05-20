""" trigger/52000116_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100001], quest_states=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100001], quest_states=[2]):
            return fadeout(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100001], quest_states=[3]):
            return fadeout(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003163, illust_id='Nelf_normal', msg='$52000116_QD__MAIN__0$', duration=4000, align=Align.Right) # 11003163: 넬프
        self.set_scene_skip(state=fadeout, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return jordyspawn(self.ctx)


class jordyspawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000116, portal_id=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        self.spawn_monster(spawn_ids=[102]) # 102:조디
        self.select_camera_path(path_ids=[4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return jordyhelp(self.ctx)


class jordyhelp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        self.set_dialogue(type=2, spawn_id=11001838, script='$52000116_QD__MAIN__1$', time=1) # 조디 계단 올라가며 하는 대사
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return wowspawn(self.ctx)


class wowspawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103]) # 103:연출용 강아지
        self.set_dialogue(type=1, spawn_id=102, script='$52000116_QD__MAIN__2$', time=2) # 조디 뒤로 돌아서 하는 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return camera(self.ctx)


class camera(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wow(self.ctx)


class wow(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Attack_01_A')
        self.set_dialogue(type=2, spawn_id=11003179, script='$52000116_QD__MAIN__3$', time=2) # 강아지 짖는 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return save(self.ctx)


class save(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Sit_Down_A', duration=400000.0)
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return battleready(self.ctx)


class battleready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], delay=500) # 멍멍이 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Attack_Idle_A', duration=10000.0)
        self.reset_camera(interpolation_time=0.5)
        self.move_user_path(patrol_name='MS2PatrolData_3003')
        self.set_dialogue(type=1, spawn_id=102, script='$52000116_QD__MAIN__4$', time=2) # 조디 말풍선
        self.set_dialogue(type=1, spawn_id=101, script='$52000116_QD__MAIN__5$', time=2) # 넬프 말풍선
        self.set_dialogue(type=1, spawn_id=102, script='$52000116_QD__MAIN__6$', time=2, arg5=3) # 조디 말풍선

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return camera_A(self.ctx)


class camera_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Motion(self.ctx)


class Motion(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Angry_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return lol(self.ctx)


class lol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Damg_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return run(self.ctx)


class run(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3004')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,103,104])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[105]) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000116, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return thank(self.ctx)


class thank(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')
        self.select_camera_path(path_ids=[4002], return_view=False) # 조디 얼굴로 클로즈업
        self.add_cinematic_talk(npc_id=11003164, msg='$52000116_QD__MAIN__7$', duration=2000)
        self.set_scene_skip(state=end, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return endready(self.ctx)


class endready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(scale=2.3, type='NameCaption', title='$52000116_QD__MAIN__8$', desc='$52000116_QD__MAIN__9$', align=Align.Center | Align.Left, offset_rate_x=-0.15, duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='jordy')
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
