""" trigger/02000499_bf/event_a.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3008')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3009')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3010')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104]):
            return CompleteEffect(self.ctx)


class CompleteEffect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return idle(self.ctx)


initial_state = idle
