""" trigger/02020112_bf/reconnect.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reconnect') == 1:
            return 버프쏴주기(self.ctx)


class 버프쏴주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[916], skill_id=70002105, level=1, is_skill_set=False)
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reconnect') == 2:
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[931], skill_id=70002112, level=1, is_skill_set=False)


initial_state = 대기
