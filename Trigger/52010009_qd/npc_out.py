""" trigger/52010009_qd/npc_out.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[111]):
            return npc_out(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[112]):
            return npc_out(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[113]):
            return npc_out(self.ctx)


class npc_out(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112,113])

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


initial_state = idle
