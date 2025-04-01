""" trigger/52000120_qd/04_npcdown.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001170], state=2)
        self.destroy_monster(spawn_ids=[230]) # NPC
        self.set_user_value(key='NpcDown', value=0)
        self.set_user_value(key='BattleEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcDown') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='NpcDown', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            # NPC 마다 다름
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[220])
        self.set_interact_object(trigger_ids=[10001170], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return Quit(self.ctx)
        if self.object_interacted(interact_ids=[10001170], state=0):
            return NpcWakeUp(self.ctx)


class NpcWakeUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001170], state=2)
        self.spawn_monster(spawn_ids=[230], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return Quit(self.ctx)
        if self.npc_detected(box_id=9900, spawn_ids=[220]):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001170], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=20000):
            # NPC 마다 다름
            return NpcDown02(self.ctx)


class NpcDown02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[220])
        self.set_interact_object(trigger_ids=[10001170], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return Quit(self.ctx)
        if self.object_interacted(interact_ids=[10001170], state=0):
            return NpcWakeUp(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[220,230])
        self.set_interact_object(trigger_ids=[10001170], state=0)


initial_state = Wait
