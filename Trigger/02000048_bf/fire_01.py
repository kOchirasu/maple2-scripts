""" trigger/02000048_bf/fire_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000306], state=1)
        self.set_mesh(trigger_ids=[201])
        self.set_effect(trigger_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000306], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[201], visible=True, fade=1.0)
        self.set_effect(trigger_ids=[301], visible=True)
        self.spawn_monster(spawn_ids=[401], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=401, script='$02000048_BF__FIRE_01__0$', time=2)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[401]):
            return 딜레이(self.ctx)
        if not self.monster_in_combat(spawn_ids=[401]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[401]):
            self.reset_timer(timer_id='1')
        if self.monster_dead(spawn_ids=[401]):
            return 소멸대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 딜레이(self.ctx)
        if self.monster_in_combat(spawn_ids=[401]):
            return 몬스터소멸(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[401])
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
