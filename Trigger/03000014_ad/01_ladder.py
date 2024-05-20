""" trigger/03000014_ad/01_ladder.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000066], state=1)
        self.set_effect(trigger_ids=[201,202,211,212,221,222,231,232,241,242])
        self.set_ladder(trigger_ids=[101])
        self.set_ladder(trigger_ids=[102])
        self.set_ladder(trigger_ids=[111])
        self.set_ladder(trigger_ids=[112])
        self.set_ladder(trigger_ids=[121])
        self.set_ladder(trigger_ids=[122])
        self.set_ladder(trigger_ids=[131])
        self.set_ladder(trigger_ids=[132])
        self.set_ladder(trigger_ids=[141])
        self.set_ladder(trigger_ids=[142])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000066], state=0):
            return 사다리생성101(self.ctx)


class 사다리생성101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[201,202], visible=True)
        self.set_ladder(trigger_ids=[101], visible=True, enable=True)
        self.set_ladder(trigger_ids=[102], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성102(self.ctx)


class 사다리생성102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[211,212], visible=True)
        self.set_ladder(trigger_ids=[111], visible=True, enable=True)
        self.set_ladder(trigger_ids=[112], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성111(self.ctx)


class 사다리생성111(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[221,222], visible=True)
        self.set_ladder(trigger_ids=[121], visible=True, enable=True)
        self.set_ladder(trigger_ids=[122], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성112(self.ctx)


class 사다리생성112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[231,232], visible=True)
        self.set_ladder(trigger_ids=[131], visible=True, enable=True)
        self.set_ladder(trigger_ids=[132], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성121(self.ctx)


class 사다리생성121(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[241,242], visible=True)
        self.set_ladder(trigger_ids=[141], visible=True, enable=True)
        self.set_ladder(trigger_ids=[142], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저감지(self.ctx)


class 사다리생성122(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[122], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성131(self.ctx)


class 사다리생성131(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[131], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성132(self.ctx)


class 사다리생성132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[132], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성141(self.ctx)


class 사다리생성141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[141], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 사다리생성142(self.ctx)


class 사다리생성142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[142], visible=True, enable=True)
        self.set_timer(timer_id='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저감지(self.ctx)


initial_state = 유저감지
