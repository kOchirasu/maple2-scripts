""" trigger/52000014_qd/rockdrop_1500.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1500])
        self.set_skill(trigger_ids=[1502])
        self.set_skill(trigger_ids=[1504])
        self.set_effect(trigger_ids=[1501]) # RockDrop
        self.set_effect(trigger_ids=[1503]) # RockDrop
        self.set_effect(trigger_ids=[1505]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 낙하01시작(self.ctx)


class 낙하01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1501], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하01완료(self.ctx)


class 낙하01완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1500], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 낙하02시작(self.ctx)


class 낙하02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1503], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하02완료(self.ctx)


class 낙하02완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)
        self.set_skill(trigger_ids=[1502], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 낙하03시작(self.ctx)


class 낙하03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1505], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 낙하03완료(self.ctx)


class 낙하03완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=2)
        self.set_skill(trigger_ids=[1504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_skill(trigger_ids=[1500])
        self.set_skill(trigger_ids=[1502])
        self.set_skill(trigger_ids=[1504])
        self.set_effect(trigger_ids=[1501]) # RockDrop
        self.set_effect(trigger_ids=[1503]) # RockDrop
        self.set_effect(trigger_ids=[1505]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 낙하01시작(self.ctx)


initial_state = 대기
