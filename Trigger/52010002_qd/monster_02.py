""" trigger/52010002_qd/monster_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=701, spawn_ids=[102]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.set_dialogue(type=1, spawn_id=112, script='$52010002_QD__MONSTER_02__0$', time=2, arg5=1)


class End(trigger_api.Trigger):
    pass


initial_state = idle
