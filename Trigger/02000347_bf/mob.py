""" trigger/02000347_bf/mob.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[60002]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 랜덤몬스터소환(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 랜덤몬스터소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return 번소환1(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환2(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환3(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환4(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환5(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환6(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환7(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환8(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환9(self.ctx)
        if self.random_condition(weight=10.0):
            return 번소환10(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1007])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1008])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1009])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번소환10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1010])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤몬스터소환(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=1):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])


initial_state = 대기
