""" trigger/52000045_qd/common.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[201]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[202]):
            return npc_exit_02(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[203]):
            return npc_exit_03(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[204]):
            return npc_exit_04(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[205]):
            return npc_exit_05(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[206]):
            return npc_exit_06(self.ctx)


class npc_exit_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[206])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


initial_state = idle
