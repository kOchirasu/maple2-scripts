""" trigger/52000071_qd/02_falsedoor.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001]) # 미니맵용_Invisible
        self.set_interact_object(trigger_ids=[10001104], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001104], state=0):
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902])


initial_state = Wait
