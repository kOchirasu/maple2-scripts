""" trigger/52000014_qd/rockdrop_1000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1000])
        self.set_skill(trigger_ids=[1002])
        self.set_skill(trigger_ids=[1004])
        self.set_effect(trigger_ids=[1001]) # RockDrop
        self.set_effect(trigger_ids=[1003]) # RockDrop
        self.set_effect(trigger_ids=[1005]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 낙하01시작(self.ctx)


class 낙하01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1001], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하01완료(self.ctx)


class 낙하01완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 낙하02시작(self.ctx)


class 낙하02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1003], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하02완료(self.ctx)


class 낙하02완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)
        self.set_skill(trigger_ids=[1002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 낙하03시작(self.ctx)


class 낙하03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1005], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하03완료(self.ctx)


class 낙하03완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=1)
        self.set_skill(trigger_ids=[1004], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=2)
        self.set_skill(trigger_ids=[1000])
        self.set_skill(trigger_ids=[1002])
        self.set_skill(trigger_ids=[1004])
        self.set_effect(trigger_ids=[1001]) # RockDrop
        self.set_effect(trigger_ids=[1003]) # RockDrop
        self.set_effect(trigger_ids=[1005]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 낙하01시작(self.ctx)


initial_state = 대기
