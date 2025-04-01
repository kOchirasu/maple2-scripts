""" trigger/51000003_dg/wave_projectile_02.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_00') == 1:
            return Round_00_Ready(self.ctx)
        if self.user_value(key='Round_01') == 1:
            return Round_01_Ready(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return Round_03_Ready(self.ctx)
        if self.user_value(key='Round_04') == 1:
            return Round_04_Ready(self.ctx)
        if self.user_value(key='Round_05') == 1:
            return Round_05_Ready(self.ctx)


class Round_00_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Round_00(self.ctx)


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Round_01(self.ctx)


class Round_03_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return None # Missing State: Round_03


class Round_04_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Round_04(self.ctx)


class Round_05_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Round_05(self.ctx)


class Round_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_00_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_00_Random_02(self.ctx)


class Round_00_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[403])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_00(self.ctx)
        if self.user_value(key='Round_01') == 1:
            return Round_01(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_00_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[404])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_00(self.ctx)
        if self.user_value(key='Round_01') == 1:
            return Round_01(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_01_Random_04(self.ctx)


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[402])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[403])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[404])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_02_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_02_Random_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_02_Random_03(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_02_Random_04(self.ctx)


class Round_02_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[405,406])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[407,408])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[410,411])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[412,413])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_04_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_04_Random_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_04_Random_03(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_04_Random_04(self.ctx)


class Round_04_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[408])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[406])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[403])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[405])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_05_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_05_Random_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_05_Random_03(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_05_Random_04(self.ctx)


class Round_05_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[408])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_05_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[406])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_05_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[403])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_05_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[405])
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Round_06_Random_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_06_Random_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_06_Random_03(self.ctx)
        if self.random_condition(weight=1.0):
            return Round_06_Random_04(self.ctx)


class Round_06_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[421])
        self.spawn_monster(spawn_ids=[422], delay=2000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_06_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[423])
        self.spawn_monster(spawn_ids=[424], delay=2000)
        self.spawn_monster(spawn_ids=[425])
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_06_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[426])
        self.spawn_monster(spawn_ids=[427], delay=2000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_06_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[428])
        self.spawn_monster(spawn_ids=[429], delay=2000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06') == 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='wave_projectile_02 종료', duration=1000)
        pass


initial_state = Round_check
