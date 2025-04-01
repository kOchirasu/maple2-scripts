""" trigger/82000003_survival/10_ridingbattle.xml """
import trigger_api


# 변신 탈것 riding battle
class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518])
        self.set_user_value(key='BattleRidingOnCount', value=0)
        self.set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOnCount') == 1:
            return RidingSpawn(self.ctx)


class RidingSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_none(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_north(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_south(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_east(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_west(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_northsouth(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_northeast(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_northwest(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_eastwest(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_southeast(self.ctx)
        if self.random_condition(weight=10.0):
            return RidingSpawn_Extra_southwest(self.ctx)


class RidingSpawn_Extra_none(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_north(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000515], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_south(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000517], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_east(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000516], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_west(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000518], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northsouth(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000515,10000517], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northeast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000515,10000516], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000515,10000518], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_eastwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000516,10000518], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_southeast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000516,10000517], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_southwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000518,10000517], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518]) # riding battle test


initial_state = Setting
