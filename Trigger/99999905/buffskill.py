""" trigger/99999905/buffskill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_event_ui(type=1, arg2='$99999905__BUFFSKILL__0$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[103]):
            return 초기화(self.ctx)
        if self.random_condition(weight=33.0):
            return A스킬작동(self.ctx)
        if self.random_condition(weight=33.0):
            return B스킬작동(self.ctx)
        if self.random_condition(weight=34.0):
            return C스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True)
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            self.set_skill(trigger_ids=[7001])
            return 스킬랜덤(self.ctx)


class B스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7002], enable=True)
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            self.set_skill(trigger_ids=[7002])
            return 스킬랜덤(self.ctx)


class C스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7003], enable=True)
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            self.set_skill(trigger_ids=[7003])
            return 스킬랜덤(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[7001])
        self.set_skill(trigger_ids=[7002])
        self.set_skill(trigger_ids=[7003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
