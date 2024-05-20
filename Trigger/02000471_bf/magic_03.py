""" trigger/02000471_bf/magic_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002021clear', value=0)
        self.set_user_value(trigger_id=2040318, key='10002021clear', value=0)
        self.set_user_value(trigger_id=2040322, key='10002021clear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002021], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003])
        self.set_mesh(trigger_ids=[1103], interval=200, fade=15.0)
        self.set_mesh(trigger_ids=[1203], visible=True, interval=200, fade=15.0)
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.add_buff(box_ids=[203], skill_id=70002021, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[203]):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002021clear', value=1)
        self.set_user_value(trigger_id=2040318, key='10002021clear', value=1)
        self.set_user_value(trigger_id=2040322, key='10002021clear', value=1)
        self.set_achievement(trigger_id=713, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[165,166,167,168,169], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=165, sequence_name='Down_Idle_A', duration=600000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_03_b(self.ctx)


class Event_03_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=168, patrol_name='MS2PatrolData_2138')
        self.set_npc_emotion_loop(spawn_id=165, sequence_name='Down_Idle_A', duration=600000.0)
        self.set_dialogue(type=1, spawn_id=165, script='$02000471_BF__MAGIC_03__0$', time=3)
        self.set_dialogue(type=1, spawn_id=169, script='$02000471_BF__MAGIC_03__1$', time=3, arg5=2)
        self.set_dialogue(type=1, spawn_id=168, script='$02000471_BF__MAGIC_03__2$', time=3, arg5=1)
        self.set_dialogue(type=1, spawn_id=168, script='$02000471_BF__MAGIC_03__3$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return Event_03_c(self.ctx)


class Event_03_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[165,166,167,168,169])


initial_state = idle
