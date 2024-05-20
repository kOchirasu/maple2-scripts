""" trigger/02000230_bf/save_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300], auto_target=False)
        self.set_actor(trigger_id=301, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=30301, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=30302, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=30303, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=30304, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=30305, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000355], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000355], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=300, script='$02000230_BF__SAVE_03__0$', time=2)
        self.set_actor(trigger_id=30301, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[30311])
        self.set_actor(trigger_id=30302, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[30312])
        self.set_actor(trigger_id=30303, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[30313])
        self.set_actor(trigger_id=30304, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[30314])
        self.set_actor(trigger_id=30305, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[30315])
        self.set_dialogue(type=1, spawn_id=30311, script='$02000230_BF__SAVE_03__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=30313, script='$02000230_BF__SAVE_03__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[300])
        self.set_actor(trigger_id=301, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[311], auto_target=False)
        self.set_dialogue(type=1, spawn_id=311, script='$02000230_BF__SAVE_03__3$', time=2)
        self.move_npc(spawn_id=311, patrol_name='MS2PatrolData_311_11000689')
        self.set_dialogue(type=1, spawn_id=311, script='$02000230_BF__SAVE_03__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90311, spawn_ids=[311]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[311])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[30311,30312,30313,30314,30315]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[30311,30312,30313,30314,30315]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[30311,30312,30313,30314,30315])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
