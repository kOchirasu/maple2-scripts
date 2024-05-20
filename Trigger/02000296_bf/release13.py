""" trigger/02000296_bf/release13.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5011,50111,50112])
        self.set_interact_object(trigger_ids=[10000503], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000503], state=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5011,50111,50112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5011, script='$02000296_BF__NPC4__0$', time=2)
        self.set_dialogue(type=1, spawn_id=50111, script='$02000296_BF__NPC11__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=50112, script='$02000296_BF__NPC12__0$', time=2, arg5=2)
        self.move_npc(spawn_id=5011, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50111, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=50112, patrol_name='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5011,50111,50112])


initial_state = Wait
