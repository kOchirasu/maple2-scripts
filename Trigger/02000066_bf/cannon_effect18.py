""" trigger/02000066_bf/cannon_effect18.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[818])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[128]):
            return 이펙트대기(self.ctx)


class 이펙트대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=128, spawn_ids=[8018]):
            return 이펙트on(self.ctx)


class 이펙트on(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[818], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[8018]):
            return 대기시간(self.ctx)
        if not self.user_detected(box_ids=[128]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[818])
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작(self.ctx)


initial_state = 시작
