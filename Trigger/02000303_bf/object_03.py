""" trigger/02000303_bf/object_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000596], state=0)
        self.set_interact_object(trigger_ids=[10000597], state=0)
        self.set_interact_object(trigger_ids=[10000598], state=0)
        self.set_interact_object(trigger_ids=[10000599], state=0)
        self.set_interact_object(trigger_ids=[10000600], state=0)
        self.set_effect(trigger_ids=[60596])
        self.set_effect(trigger_ids=[60597])
        self.set_effect(trigger_ids=[60598])
        self.set_effect(trigger_ids=[60599])
        self.set_effect(trigger_ids=[60600])

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
        self.set_effect(trigger_ids=[60596], visible=True)
        self.set_interact_object(trigger_ids=[10000596], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000596], state=0):
            self.set_effect(trigger_ids=[60596])
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60597], visible=True)
        self.set_interact_object(trigger_ids=[10000597], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000597], state=0):
            self.set_effect(trigger_ids=[60597])
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60598], visible=True)
        self.set_interact_object(trigger_ids=[10000598], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000598], state=0):
            self.set_effect(trigger_ids=[60598])
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60599], visible=True)
        self.set_interact_object(trigger_ids=[10000599], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000599], state=0):
            self.set_effect(trigger_ids=[60599])
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60600], visible=True)
        self.set_interact_object(trigger_ids=[10000600], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000600], state=0):
            self.set_effect(trigger_ids=[60600])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
