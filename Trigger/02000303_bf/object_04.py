""" trigger/02000303_bf/object_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000601], state=0)
        self.set_interact_object(trigger_ids=[10000602], state=0)
        self.set_interact_object(trigger_ids=[10000603], state=0)
        self.set_interact_object(trigger_ids=[10000604], state=0)
        self.set_interact_object(trigger_ids=[10000605], state=0)
        self.set_effect(trigger_ids=[60601])
        self.set_effect(trigger_ids=[60602])
        self.set_effect(trigger_ids=[60603])
        self.set_effect(trigger_ids=[60604])
        self.set_effect(trigger_ids=[60605])

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
        self.set_effect(trigger_ids=[60601], visible=True)
        self.set_interact_object(trigger_ids=[10000601], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000601], state=0):
            self.set_effect(trigger_ids=[60601])
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60602], visible=True)
        self.set_interact_object(trigger_ids=[10000602], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000602], state=0):
            self.set_effect(trigger_ids=[60602])
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60603], visible=True)
        self.set_interact_object(trigger_ids=[10000603], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000603], state=0):
            self.set_effect(trigger_ids=[60603])
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60604], visible=True)
        self.set_interact_object(trigger_ids=[10000604], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000604], state=0):
            self.set_effect(trigger_ids=[60604])
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[60605], visible=True)
        self.set_interact_object(trigger_ids=[10000605], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000605], state=0):
            self.set_effect(trigger_ids=[60605])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
