""" trigger/02020112_bf/gravityroomtimer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990020, key='TimerReset', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer') == 1:
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10, auto_remove=True, display=True, v_offset=-40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer') == 2:
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.set_user_value(trigger_id=99990020, key='TimerReset', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer') == 2:
            return 종료(self.ctx)
        return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.set_user_value(trigger_id=99990020, key='TimerReset', value=0)


initial_state = 대기
