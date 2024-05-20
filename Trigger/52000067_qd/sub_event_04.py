""" trigger/52000067_qd/sub_event_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[759]) # 시장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=759, sequence_name='Talk_A')
        self.set_dialogue(type=1, spawn_id=759, script='$52000067_QD__SUB_EVENT_04__0$', time=3)
        # self.set_dialogue(type=1, spawn_id=759, script='…', time=3, arg5=3)


initial_state = idle
