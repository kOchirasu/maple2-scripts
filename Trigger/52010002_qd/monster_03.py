""" trigger/52010002_qd/monster_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=701, spawn_ids=[103]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.set_dialogue(type=1, spawn_id=113, script='$52010002_QD__MONSTER_03__0$', time=2, arg5=1)


class End(trigger_api.Trigger):
    pass


initial_state = idle
