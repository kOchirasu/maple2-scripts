""" trigger/02000230_bf/save_07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[700], auto_target=False)
        self.set_actor(trigger_id=701, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=70701, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=70702, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=70703, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=70704, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=70705, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000359], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000359], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=700, script='$02000230_BF__SAVE_07__0$', time=2)
        self.set_actor(trigger_id=70701, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[70711])
        self.set_actor(trigger_id=70702, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[70712])
        self.set_actor(trigger_id=70703, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[70713])
        self.set_actor(trigger_id=70704, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[70714])
        self.set_actor(trigger_id=70705, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[70715])
        self.set_dialogue(type=1, spawn_id=70711, script='$02000230_BF__SAVE_07__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=70713, script='$02000230_BF__SAVE_07__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[700])
        self.set_actor(trigger_id=701, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[711], auto_target=False)
        self.set_dialogue(type=1, spawn_id=711, script='$02000230_BF__SAVE_07__3$', time=2)
        self.move_npc(spawn_id=711, patrol_name='MS2PatrolData_711_11000687')
        self.set_dialogue(type=1, spawn_id=711, script='$02000230_BF__SAVE_07__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90711, spawn_ids=[711]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[711])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[70711,70712,70713,70714,70715]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[70711,70712,70713,70714,70715]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[70711,70712,70713,70714,70715])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
