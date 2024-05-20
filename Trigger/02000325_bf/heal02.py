""" trigger/02000325_bf/heal02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[702])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000740], state=0):
            return 스킬작동(self.ctx)


class 스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[702], enable=True)
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.set_skill(trigger_ids=[702])
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.set_interact_object(trigger_ids=[10000740], state=2)
            return 시작(self.ctx)


initial_state = 시작
