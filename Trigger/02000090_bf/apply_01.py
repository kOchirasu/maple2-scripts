""" trigger/02000090_bf/apply_01.xml """
import trigger_api


class 대기0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1000])
        self.set_effect(trigger_ids=[1001])
        self.set_interact_object(trigger_ids=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 대기1(self.ctx)
        if self.random_condition(weight=33.0):
            return 대기2(self.ctx)
        if self.random_condition(weight=34.0):
            return 대기3(self.ctx)
        if self.object_interacted(interact_ids=[10000360], state=0):
            return 이펙트1(self.ctx)


class 대기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_effect(trigger_ids=[1000], visible=True)
        self.set_interact_object(trigger_ids=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기0(self.ctx)
        if self.object_interacted(interact_ids=[10000360], state=0):
            return 이펙트1(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=7)
        self.set_effect(trigger_ids=[1000], visible=True)
        self.set_effect(trigger_ids=[1001], visible=True)
        self.set_interact_object(trigger_ids=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 대기0(self.ctx)
        if self.object_interacted(interact_ids=[10000360], state=0):
            return 이펙트1(self.ctx)


class 대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)
        self.set_effect(trigger_ids=[1000], visible=True)
        self.set_effect(trigger_ids=[1001], visible=True)
        self.set_interact_object(trigger_ids=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대기0(self.ctx)
        if self.object_interacted(interact_ids=[10000360], state=0):
            return 이펙트1(self.ctx)


class 이펙트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=1)
        self.set_effect(trigger_ids=[1000], visible=True)
        self.set_effect(trigger_ids=[1001], visible=True)
        self.set_effect(trigger_ids=[2000], visible=True)
        self.set_effect(trigger_ids=[2001], visible=True)
        self.set_effect(trigger_ids=[2002], visible=True)
        self.set_effect(trigger_ids=[2003], visible=True)
        self.set_effect(trigger_ids=[2004], visible=True)
        self.set_effect(trigger_ids=[2005], visible=True)
        self.set_effect(trigger_ids=[2006], visible=True)
        self.set_effect(trigger_ids=[2007], visible=True)
        self.set_effect(trigger_ids=[1000])
        self.set_effect(trigger_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[1000])
        self.set_effect(trigger_ids=[1001])
        self.set_effect(trigger_ids=[2000])
        self.set_effect(trigger_ids=[2001])
        self.set_effect(trigger_ids=[2002])
        self.set_effect(trigger_ids=[2003])
        self.set_effect(trigger_ids=[2004])
        self.set_timer(timer_id='20', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 대기0(self.ctx)


initial_state = 대기0
