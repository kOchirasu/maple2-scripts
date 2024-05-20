""" trigger/52000050_qd/common.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[121]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[122]):
            return npc_exit_02(self.ctx)


class npc_exit_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[122])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


initial_state = idle
