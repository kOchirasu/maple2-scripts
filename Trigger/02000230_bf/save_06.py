""" trigger/02000230_bf/save_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[600], auto_target=False)
        self.set_actor(trigger_id=601, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=60601, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=60602, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=60603, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=60604, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=60605, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000358], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000358], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=600, script='$02000230_BF__SAVE_06__0$', time=2)
        self.set_actor(trigger_id=60601, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[60611])
        self.set_actor(trigger_id=60602, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[60612])
        self.set_actor(trigger_id=60603, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[60613])
        self.set_actor(trigger_id=60604, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[60614])
        self.set_actor(trigger_id=60605, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[60615])
        self.set_dialogue(type=1, spawn_id=60611, script='$02000230_BF__SAVE_06__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=60613, script='$02000230_BF__SAVE_06__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[600])
        self.set_actor(trigger_id=601, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[611], auto_target=False)
        self.set_dialogue(type=1, spawn_id=611, script='$02000230_BF__SAVE_06__3$', time=2)
        self.move_npc(spawn_id=611, patrol_name='MS2PatrolData_611_11000688')
        self.set_dialogue(type=1, spawn_id=611, script='$02000230_BF__SAVE_06__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90611, spawn_ids=[611]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[611])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[60611,60612,60613,60614,60615]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[60611,60612,60613,60614,60615]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[60611,60612,60613,60614,60615])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
