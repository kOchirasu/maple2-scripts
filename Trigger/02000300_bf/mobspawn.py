""" trigger/02000300_bf/mobspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1099]):
            return 랜덤생성조건(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 랜덤생성조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 초40(self.ctx)
        if self.random_condition(weight=25.0):
            return 초35(self.ctx)
        if self.random_condition(weight=25.0):
            return 초30(self.ctx)
        if self.random_condition(weight=25.0):
            return 초45(self.ctx)


class 초40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='45', seconds=45)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='45'):
            return 생성(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 초35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='50', seconds=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='50'):
            return 생성(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 초30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='55', seconds=55)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='55'):
            return 생성(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 초45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            return 생성(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1099, script='$02000300_BF__MOBSPAWN__0$', time=2)
        self.set_dialogue(type=1, spawn_id=1001, script='$02000300_BF__MOBSPAWN__1$', time=3)
        self.spawn_monster(spawn_ids=[1097,1098])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1097,1098]):
            return 랜덤생성조건(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1098])
        self.destroy_monster(spawn_ids=[1097])


initial_state = 대기
