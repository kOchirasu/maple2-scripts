""" trigger/61000005_me/wait.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='90', seconds=90, start_delay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[196]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$61000005_ME__WAIT__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=196) >= 20:
            return 시작(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 대기(self.ctx)
        if self.time_expired(timer_id='90'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$61000005_ME__WAIT__1$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 입장
