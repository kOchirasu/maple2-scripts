""" trigger/02000230_bf/save_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Emotion_Failure_Idle_A')
        self.set_actor(trigger_id=50501, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=50502, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=50503, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=50504, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=50505, visible=True, initial_sequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000357], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000357], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=500, script='$02000230_BF__SAVE_05__0$', time=2)
        self.set_actor(trigger_id=50501, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[50511])
        self.set_actor(trigger_id=50502, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[50512])
        self.set_actor(trigger_id=50503, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[50513])
        self.set_actor(trigger_id=50504, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[50514])
        self.set_actor(trigger_id=50505, initial_sequence='Attack_02_A')
        self.spawn_monster(spawn_ids=[50515])
        self.set_dialogue(type=1, spawn_id=50511, script='$02000230_BF__SAVE_05__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=50513, script='$02000230_BF__SAVE_05__2$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[500])
        self.set_actor(trigger_id=501, initial_sequence='Emotion_Failure_Idle_A')
        self.spawn_monster(spawn_ids=[511], auto_target=False)
        self.set_dialogue(type=1, spawn_id=511, script='$02000230_BF__SAVE_05__3$', time=2)
        self.move_npc(spawn_id=511, patrol_name='MS2PatrolData_511_11000689')
        self.set_dialogue(type=1, spawn_id=511, script='$02000230_BF__SAVE_05__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90511, spawn_ids=[511]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[511])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[50511,50512,50513,50514,50515]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[50511,50512,50513,50514,50515]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=10)
        self.destroy_monster(spawn_ids=[50511,50512,50513,50514,50515])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 대기(self.ctx)


initial_state = 대기
