""" trigger/02000303_bf/object_01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000586], state=0)
        self.set_interact_object(trigger_ids=[10000587], state=0)
        self.set_interact_object(trigger_ids=[10000588], state=0)
        self.set_interact_object(trigger_ids=[10000589], state=0)
        self.set_interact_object(trigger_ids=[10000590], state=0)
        self.set_effect(trigger_ids=[60586])
        self.set_effect(trigger_ids=[60587])
        self.set_effect(trigger_ids=[60588])
        self.set_effect(trigger_ids=[60589])
        self.set_effect(trigger_ids=[60590])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 생성랜덤(self.ctx)


class 생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 생성01(self.ctx)
        if self.random_condition(weight=20.0):
            return 생성02(self.ctx)
        if self.random_condition(weight=20.0):
            return 생성03(self.ctx)
        if self.random_condition(weight=20.0):
            return 생성04(self.ctx)
        if self.random_condition(weight=20.0):
            return 생성05(self.ctx)


class 생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60586], visible=True)
        self.set_interact_object(trigger_ids=[10000586], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000586], state=0):
            self.set_effect(trigger_ids=[60586])
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000587], state=1)
        self.set_effect(trigger_ids=[60587], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000587], state=0):
            self.set_effect(trigger_ids=[60587])
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60588], visible=True)
        self.set_interact_object(trigger_ids=[10000588], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000588], state=0):
            self.set_effect(trigger_ids=[60588])
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60589], visible=True)
        self.set_interact_object(trigger_ids=[10000589], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000589], state=0):
            self.set_effect(trigger_ids=[60589])
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60590], visible=True)
        self.set_interact_object(trigger_ids=[10000590], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000590], state=0):
            self.set_effect(trigger_ids=[60590])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
