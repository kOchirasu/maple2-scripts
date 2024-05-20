""" trigger/02000230_bf/save_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=20201, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=20202, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=20203, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=20204, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=20205, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000279], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000279], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=200, script='$02000230_BF__SAVE_02__0$', time=2)
        self.set_actor(trigger_id=20201, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[20211])
        self.set_actor(trigger_id=20202, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[20212])
        self.set_actor(trigger_id=20203, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[20213])
        self.set_actor(trigger_id=20204, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[20214])
        self.set_actor(trigger_id=20205, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[20215])
        self.set_dialogue(type=1, spawn_id=20211, script='$02000230_BF__SAVE_02__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=20213, script='$02000230_BF__SAVE_02__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[200])
        self.set_actor(trigger_id=201, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[211], auto_target=False)
        self.set_dialogue(type=1, spawn_id=211, script='$02000230_BF__SAVE_02__3$', time=2)
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_211_11000688')
        self.set_dialogue(type=1, spawn_id=211, script='$02000230_BF__SAVE_02__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90211, spawn_ids=[211]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[20211,20212,20213,20214,20215]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[20211,20212,20213,20214,20215]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[20211,20212,20213,20214,20215])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
