""" trigger/02020027_bf/specialtimer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpecialTimer') == 1:
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='SpecialTimer', seconds=180, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크(self.ctx)


class 타이머체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='SpecialTimer'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=0)
        self.reset_timer(timer_id='SpecialTimer')


initial_state = 대기
