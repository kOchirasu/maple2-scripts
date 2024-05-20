""" trigger/02000230_bf/save_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100], auto_target=False)
        self.set_actor(trigger_id=101, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=10101, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=10102, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=10103, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=10104, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=10105, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000354], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000354], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=100, script='$02000230_BF__SAVE_01__0$', time=2)
        self.set_actor(trigger_id=10101, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[10111])
        self.set_actor(trigger_id=10102, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[10112])
        self.set_actor(trigger_id=10103, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[10113])
        self.set_actor(trigger_id=10104, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[10114])
        self.set_actor(trigger_id=10105, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[10115])
        self.set_dialogue(type=1, spawn_id=10111, script='$02000230_BF__SAVE_01__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=10113, script='$02000230_BF__SAVE_01__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[100])
        self.set_actor(trigger_id=101, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.set_dialogue(type=1, spawn_id=111, script='$02000230_BF__SAVE_01__3$', time=2)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_111_11000687')
        self.set_dialogue(type=1, spawn_id=111, script='$02000230_BF__SAVE_01__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90111, spawn_ids=[111]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10111,10112,10113,10114,10115]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[10111,10112,10113,10114,10115]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[10111,10112,10113,10114,10115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
