""" trigger/02000088_bf/fruit01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000138], state=1)
        self.set_effect(trigger_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000138], state=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[201])
        self.spawn_monster(spawn_ids=[101])
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대화(self.ctx)


class 대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 트리거초기화(self.ctx)
        if self.time_expired(timer_id='1'):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
