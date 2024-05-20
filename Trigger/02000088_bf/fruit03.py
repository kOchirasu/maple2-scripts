""" trigger/02000088_bf/fruit03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000140], state=1)
        self.set_effect(trigger_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000140], state=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[203])
        self.spawn_monster(spawn_ids=[103])
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대화(self.ctx)


class 대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return 트리거초기화(self.ctx)
        if self.time_expired(timer_id='1'):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
