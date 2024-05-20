""" trigger/02000499_bf/event_b.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_3012')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_3013')
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_3014')
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_3015')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105,106,107,108]):
            return CompleteEffect(self.ctx)


class CompleteEffect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_effect(trigger_ids=[5006], visible=True)
        self.set_effect(trigger_ids=[5007], visible=True)
        self.set_effect(trigger_ids=[5008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return idle(self.ctx)


initial_state = idle
