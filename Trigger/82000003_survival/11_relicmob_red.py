""" trigger/82000003_survival/11_relicmob_red.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])
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
        self.spawn_monster(spawn_ids=[1100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1100]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1102]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1103]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1104]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1105]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1106]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1107], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1107]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1108]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class MobSpawn10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1109], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1109]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class Notice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=16, key='RelicMobRedDie', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRemove') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])


initial_state = Setting
