""" trigger/02000047_bf/01_trigger.xml """
import trigger_api


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000084], state=1)
        self.set_interact_object(trigger_ids=[10000085], state=1)
        self.set_mesh(trigger_ids=[10,11,12,13,14,15,16,17]) # 다리안보임

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000084,10000085], state=0):
            return 다리생성1011(self.ctx)


class 다리생성1011(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10,11], visible=True) # 다리보임
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리생성1213(self.ctx)


class 다리생성1213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[12,13], visible=True) # 다리보임
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리생성1415(self.ctx)


class 다리생성1415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[14,15], visible=True) # 다리보임
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리생성1617(self.ctx)


class 다리생성1617(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16,17], visible=True) # 다리보임
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리제거(self.ctx)


class 다리제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            self.set_mesh(trigger_ids=[10,11,12,13,14,15,16,17]) # 다리사라짐
            return 트리거초기화2(self.ctx)


class 트리거초기화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 반응대기(self.ctx)


initial_state = 반응대기
