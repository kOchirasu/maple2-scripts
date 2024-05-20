""" trigger/52000045_qd/common_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[301]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[302]):
            return npc_exit_02(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[303]):
            return npc_exit_03(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[304]):
            return npc_exit_04(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[305]):
            return npc_exit_05(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[306]):
            return npc_exit_06(self.ctx)


class npc_exit_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[303])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[304])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[305])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


class npc_exit_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[306])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


initial_state = idle
