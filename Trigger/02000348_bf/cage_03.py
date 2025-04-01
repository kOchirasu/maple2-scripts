""" trigger/02000348_bf/cage_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2103], interval=10)
        self.set_effect(trigger_ids=[8003])
        self.set_actor(trigger_id=2203, initial_sequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cage_03') == 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2103], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_actor(trigger_id=2203, visible=True, initial_sequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[213]):
            return npc(self.ctx)


class npc(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8003])
        self.set_mesh(trigger_ids=[2103], interval=10)
        self.set_actor(trigger_id=2203, initial_sequence='Dead_A')
        self.spawn_monster(spawn_ids=[223])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[223])


initial_state = idle
