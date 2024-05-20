""" trigger/52000070_qd/npcdown_904.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9900, spawn_ids=[904]):
            return NpcFight(self.ctx)


class NpcFight(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[904]):
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[304], auto_target=False)


initial_state = Wait
