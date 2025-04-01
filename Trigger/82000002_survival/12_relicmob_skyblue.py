""" trigger/82000002_survival/12_relicmob_skyblue.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])
        self.set_user_value(key='RelicMobSpawn', value=0)
        self.set_user_value(key='RelicMobRemove', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSpawn') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            # 30초 30000
            return MobSpawnRandom(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawnRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return MobSpawn01(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn02(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn03(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn04(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn05(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn06(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn07(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn08(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn09(self.ctx)
        if self.random_condition(weight=10.0):
            return MobSpawn10(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1200], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1200]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1201]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1202]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1203]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1204]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1205]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1206]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1207], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1207]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1208], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1208]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1209], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1209]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class Notice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=16, key='RelicMobSkyblueDie', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])


initial_state = Setting
