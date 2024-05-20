""" trigger/63000006_cs/shake03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5070])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5070], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 간격랜덤(self.ctx)


class 간격랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 초간격4(self.ctx)
        if self.random_condition(weight=25.0):
            return 초간격5(self.ctx)
        if self.random_condition(weight=25.0):
            return 초간격6(self.ctx)
        if self.random_condition(weight=25.0):
            return 초간격7(self.ctx)


class 초간격4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 초기화(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 초간격5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 초기화(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 초간격6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 초기화(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 초간격7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 초기화(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5070])

    def on_tick(self) -> trigger_api.Trigger:
        return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5070])


initial_state = 대기
