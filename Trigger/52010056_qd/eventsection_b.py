""" trigger/52010056_qd/eventsection_b.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2004]):
            return 연출준비_A(self.ctx)


class 연출준비_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.add_buff(box_ids=[2001], skill_id=70000085, level=1, is_player=False) # 연출용 무적 버프
        self.add_buff(box_ids=[2001], skill_id=70000085, level=1, is_player=False, is_skill_set=False) # 연출용 무적 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출준비_B(self.ctx)


class 연출준비_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[999], auto_target=False) # 크림슨 스피어: 29000386
        self.select_camera_path(path_ids=[4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 경비병_스폰(self.ctx)


class 경비병_스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=121, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003816, msg='$52010056_QD__EventSection_B__0$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 경비병_이동시작(self.ctx)


class 경비병_이동시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=999, patrol_name='MS2PatrolData_3008')
        self.select_camera_path(path_ids=[4005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조작_시작(self.ctx)


class 조작_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.remove_buff(box_id=2001, skill_id=70000107)
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection_B__1$', arg3='3000', arg4='0')

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(trigger_id=7001)


initial_state = Idle
