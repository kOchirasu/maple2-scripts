""" trigger/02010026_bf/06_ladder14.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000909], state=1)
        self.set_ladder(trigger_ids=[201])
        self.set_ladder(trigger_ids=[202])
        self.set_ladder(trigger_ids=[203])
        self.set_ladder(trigger_ids=[204])
        self.set_ladder(trigger_ids=[205])
        self.set_ladder(trigger_ids=[206])
        self.set_ladder(trigger_ids=[207])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000909], state=0):
            return 사다리생성01(self.ctx)


class 사다리생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[201], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성02(self.ctx)


class 사다리생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[202], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성03(self.ctx)


class 사다리생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[203], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성04(self.ctx)


class 사다리생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[204], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성05(self.ctx)


class 사다리생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[205], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성06(self.ctx)


class 사다리생성06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[206], visible=True, enable=True, fade=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 사다리생성07(self.ctx)


class 사다리생성07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[207], visible=True, enable=True, fade=5)
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
