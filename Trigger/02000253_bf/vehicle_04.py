""" trigger/02000253_bf/vehicle_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8054])

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count() == 4:
            # 던전 최대 인원수가 4이면
            return vehicle_01(self.ctx)


class vehicle_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=906) >= 1:
            return monster_spawn_ready(self.ctx)


class monster_spawn_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return monster_spawn(self.ctx)


class monster_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8054], visible=True)
        self.spawn_monster(spawn_ids=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3002]):
            return vehicle_spawn(self.ctx)


class vehicle_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8054])
        self.set_interact_object(trigger_ids=[10001051], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001051], state=0):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001051], state=2)


initial_state = idle
