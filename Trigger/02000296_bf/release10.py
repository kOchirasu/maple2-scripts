""" trigger/02000296_bf/release10.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000500], state=1)
        self.destroy_monster(spawn_ids=[5008,50081,50082])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000500], state=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5008,50081,50082])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5008, script='$02000296_BF__NPC1__0$', time=2)
        self.set_dialogue(type=1, spawn_id=50081, script='$02000296_BF__NPC5__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=50082, script='$02000296_BF__NPC6__0$', time=2, arg5=2)
        self.move_npc(spawn_id=5008, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50081, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50082, patrol_name='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5008,50081,50082])


initial_state = Wait
