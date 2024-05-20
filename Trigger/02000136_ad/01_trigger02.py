""" trigger/02000136_ad/01_trigger02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[801,802,803])
        self.set_interact_object(trigger_ids=[10000067], state=1)
        self.set_mesh(trigger_ids=[14,17,16])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000067], state=0):
            return 발판등장1(self.ctx)


class 발판등장1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[14], visible=True)
        self.set_effect(trigger_ids=[801], visible=True)
        self.set_timer(timer_id='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 발판등장2(self.ctx)


class 발판등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[17], visible=True)
        self.set_effect(trigger_ids=[802], visible=True)
        self.set_timer(timer_id='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 발판등장3(self.ctx)


class 발판등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16], visible=True)
        self.set_effect(trigger_ids=[803], visible=True)
        self.set_timer(timer_id='4', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 대기(self.ctx)


initial_state = 대기
