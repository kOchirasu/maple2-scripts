""" trigger/02000064_tw_triatown02/massive_door_4.xml """
import trigger_api


class 클로즈대기중(trigger_api.Trigger):
    pass


class 클로즈5초전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.announce(content='5초 후 게이트가 닫힙니다. 서둘러 입장해 주세요.', arg3=True)
        self.set_timer(timer_id='115', seconds=115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='115'):
            return 클로즈중1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='115')


class 클로즈중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 클로즈중2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='5')


class 클로즈중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.announce(content='빛나는 문이 닫혔습니다.', arg3=True)
        self.set_timer(timer_id='6', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 클로즈대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='6')


initial_state = 클로즈대기중
