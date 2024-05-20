""" trigger/52010056_qd/buff.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[3]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[2]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[1]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000053], quest_states=[3]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000053], quest_states=[2]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000053], quest_states=[1]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000052], quest_states=[3]):
            return Buff_A(self.ctx)


class Buff_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[2001], skill_id=99910300, level=1, is_player=False) # 트리스탄 변신
        self.add_buff(box_ids=[2001], skill_id=99910300, level=1, is_player=False, is_skill_set=False) # 트리스탄 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ready(self.ctx)


class Buff_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[2001], skill_id=99910330, level=1, is_player=False) # 트리스탄 변신
        self.add_buff(box_ids=[2001], skill_id=99910330, level=1, is_player=False, is_skill_set=False) # 트리스탄 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ready(self.ctx)


initial_state = Idle
