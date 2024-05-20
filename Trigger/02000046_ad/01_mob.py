""" trigger/02000046_ad/01_mob.xml """
import trigger_api


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000084], state=1)
        self.set_interact_object(trigger_ids=[10000085], state=1)
        self.set_interact_object(trigger_ids=[10000086], state=1)
        self.set_interact_object(trigger_ids=[10000087], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000084,10000085,10000086,10000087], state=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 카단대사(self.ctx)


class 카단대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000046_AD__01_MOB__0$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000046_AD__01_MOB__1$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000046_AD__01_MOB__2$', time=2)
        self.set_timer(timer_id='1', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[101])
            return 휴지(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[102])


class 휴지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return 소멸대기(self.ctx)
        if not self.monster_in_combat(spawn_ids=[102]):
            return 카단소멸(self.ctx)


class 카단소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[102]):
            self.reset_timer(timer_id='1')
        if self.monster_dead(spawn_ids=[102]):
            return 소멸대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(spawn_ids=[102]):
            return 카단소멸(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[102]):
            return 카단소멸(self.ctx)
        if not self.monster_in_combat(spawn_ids=[102]):
            self.destroy_monster(spawn_ids=[102])
            return 반응대기(self.ctx)


initial_state = 반응대기
