""" trigger/02000296_bf/release12.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5010,50101,50102])
        self.set_interact_object(trigger_ids=[10000502], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000502], state=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5010,50101,50102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5010, script='$02000296_BF__NPC3__0$', time=2)
        self.set_dialogue(type=1, spawn_id=50101, script='$02000296_BF__NPC9__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=50102, script='$02000296_BF__NPC10__0$', time=2, arg5=2)
        self.move_npc(spawn_id=5010, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50101, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50102, patrol_name='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5010,50101,50102])


initial_state = Wait
