""" trigger/02000296_bf/release11.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5009,50091,50092])
        self.set_interact_object(trigger_ids=[10000501], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000501], state=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5009,50091,50092])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5009, script='$02000296_BF__NPC2__0$', time=2)
        self.set_dialogue(type=1, spawn_id=50091, script='$02000296_BF__NPC7__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=50092, script='$02000296_BF__NPC8__0$', time=2, arg5=2)
        self.move_npc(spawn_id=5009, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50091, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50092, patrol_name='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5009,50091,50092])


initial_state = Wait
