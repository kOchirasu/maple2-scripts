""" trigger/02000081_in/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000384], state=1)
        self.destroy_monster(spawn_ids=[201])
        self.set_mesh(trigger_ids=[101,102,103,104])
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000384], state=0):
            return 닫히기(self.ctx)


class 닫히기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104], visible=True)
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Closed')
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 토무등장(self.ctx)


class 토무등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=402, spawn_ids=[202]):
            return 토무대사(self.ctx)


class 토무대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$02000081_IN__TRIGGER_01__0$', time=4)
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 토무대사2(self.ctx)


class 토무대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$02000081_IN__TRIGGER_01__1$', time=4)
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 토무대사3(self.ctx)


class 토무대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$02000081_IN__TRIGGER_01__2$', time=2)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 변신(self.ctx)


class 변신(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[201])
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[101,102,103,104])

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return 대기(self.ctx)
        if not self.monster_in_combat(spawn_ids=[201]):
            return 토무소멸(self.ctx)


class 토무소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[201]):
            self.reset_timer(timer_id='1')
        if self.monster_dead(spawn_ids=[201]):
            return 대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(spawn_ids=[201]):
            return 토무소멸(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[201]):
            return 토무소멸(self.ctx)
        if not self.monster_in_combat(spawn_ids=[201]):
            self.destroy_monster(spawn_ids=[201])
            return 대기(self.ctx)


initial_state = 대기
