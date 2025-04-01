""" trigger/02020023_bf/timer.xml """
import trigger_api


# <라운드 시작하면서 5분 시간 제한 타이머>
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer') == 1:
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='BattleTimer', seconds=300, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크(self.ctx)


class 타이머체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='BattleTimer'):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='BattleTimer')
        self.set_user_value(trigger_id=99990002, key='Timer', value=2)


initial_state = 대기
