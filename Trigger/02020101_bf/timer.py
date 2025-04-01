""" trigger/02020101_bf/timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='TimerReset', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 1:
            return 타이머1_시작(self.ctx)


class 타이머1_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=20, auto_remove=True, display=True, v_offset=-40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)
        if self.user_value(key='TimerStart') == 0:
            return 리셋_1(self.ctx)
        if self.time_expired(timer_id='1'):
            return 리셋_1(self.ctx)


class 리셋_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='TimerReset', value=1)
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)
        if self.user_value(key='TimerStart') == 2:
            return 타이머2_시작(self.ctx)


class 타이머2_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=20, auto_remove=True, display=True, v_offset=-40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)
        if self.user_value(key='TimerStart') == 0:
            return 리셋_2(self.ctx)
        if self.time_expired(timer_id='2'):
            return 리셋_2(self.ctx)


class 리셋_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='TimerReset', value=2)
        self.reset_timer(timer_id='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)
        if self.user_value(key='TimerStart') == 3:
            return 타이머3_시작(self.ctx)


class 타이머3_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=20, auto_remove=True, display=True, v_offset=-40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)
        if self.user_value(key='TimerStart') == 0:
            return 리셋_3(self.ctx)
        if self.time_expired(timer_id='3'):
            return 리셋_3(self.ctx)


class 리셋_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='TimerReset', value=3)
        self.reset_timer(timer_id='3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 9:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')


initial_state = 대기
