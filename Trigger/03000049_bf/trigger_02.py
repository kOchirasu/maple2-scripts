""" trigger/03000049_bf/trigger_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.set_interact_object(trigger_ids=[10000286], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000286], state=0):
            return 반항(self.ctx)


class 반항(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.set_dialogue(type=1, spawn_id=201, script='$03000049_BF__TRIGGER_02__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 반항2(self.ctx)


class 반항2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10000286], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
