""" trigger/99999896/01_intro.xml """
import trigger_api


class 스타트(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 멘트대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트_1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_event_ui(type=1, arg2='$99999896__01_INTRO__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트_2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_event_ui(type=1, arg2='$99999896__01_INTRO__1$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트_3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_event_ui(type=1, arg2='$99999896__01_INTRO__2$', arg3='2000')
        self.create_item(spawn_ids=[1,2,3])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 완료(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 완료(trigger_api.Trigger):
    pass


initial_state = 스타트
