""" trigger/02000139_bf/01_trigger01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[401,402,403,404])
        self.set_interact_object(trigger_ids=[10000131], state=1)
        self.set_mesh(trigger_ids=[201,202,203])
        self.set_ladder(trigger_ids=[301])
        self.set_ladder(trigger_ids=[302])
        self.set_ladder(trigger_ids=[303])
        self.set_ladder(trigger_ids=[304])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000131], state=0):
            return 발판등장1(self.ctx)


class 발판등장1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201], visible=True)
        self.set_timer(timer_id='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 발판등장2(self.ctx)


class 발판등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[202], visible=True)
        self.set_timer(timer_id='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 발판등장3(self.ctx)


class 발판등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[203], visible=True)
        self.set_timer(timer_id='4', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 사다리등장(self.ctx)


class 사다리등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[301], visible=True, enable=True)
        self.set_effect(trigger_ids=[401], visible=True)
        self.set_ladder(trigger_ids=[302], visible=True, enable=True)
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_ladder(trigger_ids=[303], visible=True, enable=True)
        self.set_effect(trigger_ids=[403], visible=True)
        self.set_ladder(trigger_ids=[304], visible=True, enable=True)
        self.set_effect(trigger_ids=[404], visible=True)
        self.set_timer(timer_id='4', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 대기(self.ctx)


initial_state = 대기
