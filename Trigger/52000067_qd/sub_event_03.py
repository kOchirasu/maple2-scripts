""" trigger/52000067_qd/sub_event_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[591,592]) # 시민

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[537,538,539]) # 몬스터
        self.set_npc_emotion_loop(spawn_id=591, sequence_name='Emotion_Failure_Idle_A', duration=600000.0)
        self.set_npc_emotion_loop(spawn_id=592, sequence_name='Emotion_Failure_Idle_A', duration=600000.0)
        self.set_dialogue(type=1, spawn_id=591, script='$52000067_QD__SUB_EVENT_03__0$', time=3)
        self.set_dialogue(type=1, spawn_id=592, script='$52000067_QD__SUB_EVENT_03__1$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[537,538,539]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=591, sequence_name='Talk_A')
        self.set_npc_emotion_sequence(spawn_id=592, sequence_name='Idle_A')
        self.set_dialogue(type=1, spawn_id=591, script='$52000067_QD__SUB_EVENT_03__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=591, patrol_name='MS2PatrolData_5010')
        self.move_npc(spawn_id=592, patrol_name='MS2PatrolData_5010')


initial_state = idle
