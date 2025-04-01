""" trigger/02000443_bf/error.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return buff_1(self.ctx)


class buff_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=49200002, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return buff_2(self.ctx)
        if self.user_value(key='debuff') == 1:
            return None # Missing State: 끝


class buff_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=49200002, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return buff_1(self.ctx)


initial_state = 시작
