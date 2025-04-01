""" trigger/02100001_bf/800_mobspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawn_ids=[800])
        self.set_mesh(trigger_ids=[3200]) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[800], auto_target=False)
        self.set_mesh(trigger_ids=[3200], visible=True) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[800]):
            return Delay01(self.ctx)
        if self.user_value(key='RemoveAll') == 1:
            return Quit(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200]) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=180000):
            # 리스폰 딜레이
            return MobSpawn(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[800])


initial_state = Wait
