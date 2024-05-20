""" trigger/52000185_qd/main.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[2001], skill_id=99910280, level=1, is_player=False) # 벨라 변신
        self.add_buff(box_ids=[2001], skill_id=99910280, level=1, is_player=False, is_skill_set=False) # 벨라 변신

    def on_tick(self) -> trigger_api.Trigger:
        return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[2001], skill_id=99910280, level=1, is_player=False) # 벨라 변신
        self.add_buff(box_ids=[2001], skill_id=99910280, level=1, is_player=False, is_skill_set=False) # 벨라 변신

    def on_tick(self) -> trigger_api.Trigger:
        return Idle(self.ctx)


initial_state = Idle
