""" trigger/02100001_bf/210_mobspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawn_ids=[210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[210], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[210]):
            return Delay01(self.ctx)
        if self.user_value(key='RemoveAll') == 1:
            return Quit(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=40000):
            # 리스폰 딜레이200
            return MobSpawn(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[210])


initial_state = Wait
