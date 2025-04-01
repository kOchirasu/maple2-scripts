""" trigger/82000001_survival/10_ridingbattle.xml """
import trigger_api


# 변신 탈것 riding battle
class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341])
        self.set_user_value(key='BattleRidingOnCount', value=0)
        self.set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOnCount') == 1:
            return OnOffRandom(self.ctx)


class OnOffRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=40.0):
            return BattleRidingOn(self.ctx)
        if self.random_condition(weight=60.0):
            return BattleRidingOff(self.ctx)


class BattleRidingOff(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class BattleRidingOn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DelayRandom(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class DelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Delay_5min00sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_5min20sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_5min40sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_6min00sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_6min20sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_6min40sec(self.ctx)
        if self.random_condition(weight=10.0):
            return Delay_7min00sec(self.ctx)


class Delay_5min00sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300000):
            # 5분 300초 300000 ms
            # test용 10배 빠름 100000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_5min20sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=320000):
            # 320초 320000 ms
            # test용 10배 빠름 106000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_5min40sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=340000):
            # 340초 340000 ms
            # test용 10배 빠름 113000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_6min00sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=360000):
            # 6분 360초 360000 ms
            # test용 10배 빠름 120000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_6min20sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=380000):
            # 380초 380000 ms
            # test용 10배 빠름 126000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_6min40sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400000):
            # 400초 400000 ms
            # test용 10배 빠름 133000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Delay_7min00sec(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=420000):
            # 7분 420초 420000 ms
            # test용 10배 빠름 140000
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337], is_start=True) # riding battle test
        self.side_npc_talk(npc_id=23000110, illust='Mushking_normal', duration=5000, script='$82000000_survival__10_RIDINGBATTLE__0$')

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
        self.start_combine_spawn(group_id=[10000338], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_south(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000340], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_east(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000339], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_west(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000341], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northsouth(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000338,10000340], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northeast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000338,10000339], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_northwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000338,10000341], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_eastwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000339,10000341], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_southeast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000339,10000340], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class RidingSpawn_Extra_southwest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000341,10000340], is_start=True) # riding battle test

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleRidingOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341]) # riding battle test


initial_state = Setting
