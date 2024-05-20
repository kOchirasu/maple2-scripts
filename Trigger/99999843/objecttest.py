""" trigger/99999843/objecttest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000401], state=1)
        self.set_interact_object(trigger_ids=[12000400], state=2)
        self.set_interact_object(trigger_ids=[12000402], state=2)
        self.set_interact_object(trigger_ids=[12000403], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000401], state=0):
            return PC_MOVE_01(self.ctx)


"""
class PC_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC_02(self.ctx)
"""

class PC_MOVE_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.patrol_condition_user(patrol_name='MS2PatrolData0', patrol_index=1, additional_effect_id=73000006)
            # self.patrol_condition_user(patrol_name='MS2PatrolData2', patrol_index=2, additional_effect_id=73000007)
            return PC_MOVE_02_Delay(self.ctx)


class PC_MOVE_02_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PC_MOVE_02(self.ctx)


class PC_MOVE_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[901], skill_id=73000009, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC_MOVE_02_Delay(self.ctx)


class RESET_DELAY(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


initial_state = 대기
