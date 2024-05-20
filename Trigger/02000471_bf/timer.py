""" trigger/02000471_bf/timer.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='TimerEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') >= 1:
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='Timer', seconds=420, start_delay=1, interval=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='Timer'):
            return end_fail(self.ctx)
        if self.user_value(key='InteractClear') >= 1:
            return end_clear(self.ctx)


class end_fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='TimerEnd', value=1)
        self.reset_timer(timer_id='Timer')


class end_clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='InteractClear', value=1)
        self.reset_timer(timer_id='Timer')


initial_state = idle
