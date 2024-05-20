""" trigger/65000003_bd/buffskill_04.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10604]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[10604]):
            return 초기화(self.ctx)
        if self.random_condition(weight=33.0):
            return A스킬작동(self.ctx)
        if self.random_condition(weight=33.0):
            return B스킬작동(self.ctx)
        if self.random_condition(weight=34.0):
            return C스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7401], enable=True)
        self.set_timer(timer_id='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            self.set_skill(trigger_ids=[7401])
            return 시작대기중(self.ctx)


class B스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7402], enable=True)
        self.set_timer(timer_id='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            self.set_skill(trigger_ids=[7402])
            return 시작대기중(self.ctx)


class C스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7403], enable=True)
        self.set_timer(timer_id='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            self.set_skill(trigger_ids=[7403])
            return 시작대기중(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[7401])
        self.set_skill(trigger_ids=[7402])
        self.set_skill(trigger_ids=[7403])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
