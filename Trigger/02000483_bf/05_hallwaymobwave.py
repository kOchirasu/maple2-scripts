""" trigger/02000483_bf/05_hallwaymobwave.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[930,931,932,933]) # Mob
        self.set_user_value(key='MobWave', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWave') == 1:
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[930], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MobSpawn02(self.ctx)


class MobSpawn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[931], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return MobSpawn03(self.ctx)


class MobSpawn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[932], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return MobSpawn04(self.ctx)


class MobSpawn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[933], auto_target=False) # Mob


initial_state = Setting
