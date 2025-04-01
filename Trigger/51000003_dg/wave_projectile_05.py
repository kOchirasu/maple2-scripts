""" trigger/51000003_dg/wave_projectile_05.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') == 1:
            return Round_01_Ready(self.ctx)


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Round_01(self.ctx)


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
        self.spawn_monster(spawn_ids=[296])
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
        self.spawn_monster(spawn_ids=[297])
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
        self.spawn_monster(spawn_ids=[298])
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
        self.spawn_monster(spawn_ids=[299])
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
        self.spawn_monster(spawn_ids=[414])
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return None # Missing State: Round_03
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[415])
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return None # Missing State: Round_03
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[416])
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return None # Missing State: Round_03
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[417])
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return None # Missing State: Round_03
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='wave_projectile_05 종료', duration=1000)
        pass


initial_state = Round_check
