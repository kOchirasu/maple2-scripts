""" trigger/02000403_bf/magic_06.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000036], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7006])
        self.set_mesh(trigger_ids=[1106], interval=200, fade=15.0)
        self.set_mesh(trigger_ids=[1206], visible=True, interval=200, fade=15.0)
        self.spawn_monster(spawn_ids=[206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[206]):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=716, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_06_b(self.ctx)


class Event_06_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1103, script='$02000403_BF__MAGIC_06__0$', time=3, arg5=1)
        self.set_npc_emotion_sequence(spawn_id=1103, sequence_name='Talk_A')
        self.set_dialogue(type=1, spawn_id=1104, script='$02000403_BF__MAGIC_06__1$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=1103, script='$02000403_BF__MAGIC_06__2$', time=3, arg5=7)
        self.set_dialogue(type=1, spawn_id=1104, script='$02000403_BF__MAGIC_06__8$', time=3, arg5=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_06_c(self.ctx)


class Event_06_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1104, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return Event_06_d(self.ctx)


class Event_06_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1103,1104,1105,1101,1102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Event_06_e(self.ctx)


class Event_06_e(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return Event_06_f(self.ctx)


class Event_06_f(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=702, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[1107,1108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_06_g(self.ctx)


class Event_06_g(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1107, patrol_name='MS2PatrolData_2140')
        self.move_npc(spawn_id=1108, patrol_name='MS2PatrolData_2141')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return Event_06_h(self.ctx)


class Event_06_h(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1107, script='$02000403_BF__MAGIC_06__3$', time=5)
        self.set_dialogue(type=1, spawn_id=1108, script='$02000403_BF__MAGIC_06__4$', time=3, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Event_06_i(self.ctx)


class Event_06_i(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1107, patrol_name='MS2PatrolData_2142')
        self.set_dialogue(type=1, spawn_id=1107, script='$02000403_BF__MAGIC_06__5$', time=5)
        self.set_dialogue(type=1, spawn_id=1108, script='$02000403_BF__MAGIC_06__6$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=1107, script='$02000403_BF__MAGIC_06__7$', time=3, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_06_j(self.ctx)


class Event_06_j(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1108, patrol_name='MS2PatrolData_2143')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Event_06_k(self.ctx)


class Event_06_k(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1107,1108])


initial_state = idle
