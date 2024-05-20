""" trigger/02000230_bf/save_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400], auto_target=False)
        self.set_actor(trigger_id=401, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=40401, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=40402, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=40403, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=40404, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=40405, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000356], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000356], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=400, script='$02000230_BF__SAVE_04__0$', time=2)
        self.set_actor(trigger_id=40401, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[40411])
        self.set_actor(trigger_id=40402, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[40412])
        self.set_actor(trigger_id=40403, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[40413])
        self.set_actor(trigger_id=40404, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[40414])
        self.set_actor(trigger_id=40405, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[40415])
        self.set_dialogue(type=1, spawn_id=40411, script='$02000230_BF__SAVE_04__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=40413, script='$02000230_BF__SAVE_04__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[400])
        self.set_actor(trigger_id=401, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[411], auto_target=False)
        self.set_dialogue(type=1, spawn_id=411, script='$02000230_BF__SAVE_04__3$', time=2)
        self.move_npc(spawn_id=411, patrol_name='MS2PatrolData_411_11000687')
        self.set_dialogue(type=1, spawn_id=411, script='$02000230_BF__SAVE_04__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90411, spawn_ids=[411]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[411])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[40411,40412,40413,40414,40415]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[40411,40412,40413,40414,40415]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[40411,40412,40413,40414,40415])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
