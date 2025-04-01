""" trigger/84000007_wd/sensor_9230.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box23Check', value=10)
        self.set_mesh(trigger_ids=[523], visible=True) # 23 / Ground outter
        self.set_mesh(trigger_ids=[5230], visible=True) # 23 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box23Check') == 0:
            return Sensor0(self.ctx)
        if self.user_value(key='Box23Check') == 1:
            return Sensor1(self.ctx)
        if self.user_value(key='Box23Check') == 2:
            return Sensor2(self.ctx)
        if self.user_value(key='Box23Check') == 3:
            return Sensor3(self.ctx)
        if self.user_value(key='Box23Check') == 4:
            return Sensor4(self.ctx)
        if self.user_value(key='Box23Check') == 5:
            return Sensor5(self.ctx)
        if self.user_value(key='Box23Check') == 7:
            return Sensor7(self.ctx)
        if self.user_value(key='Box23Check') == 8:
            return Sensor8(self.ctx)
        if self.user_value(key='Box23Check') == 9:
            return Sensor9(self.ctx)
        if self.user_value(key='Box23Check') == 6:
            return Sensor10(self.ctx)
        if self.user_value(key='Box23Check') == 15:
            return Sensor15(self.ctx)
        if self.user_value(key='Box23Check') == 20:
            return Sensor20(self.ctx)
        if self.user_value(key='Box23Check') == 25:
            return Sensor25(self.ctx)
        if self.user_value(key='Box23Check') == 30:
            return Sensor30(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 1:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9230) != 1:
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 2:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9230) != 2:
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 3:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9230) != 3:
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 4:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9230) != 4:
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 5:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9230) != 5:
            return Fail(self.ctx)


class Sensor7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 7:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9230) != 7:
            return Fail(self.ctx)


class Sensor8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 8:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9230) != 8:
            return Fail(self.ctx)


class Sensor9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 9:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9230) != 9:
            return Fail(self.ctx)


class Sensor10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 10:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9230) != 10:
            return Fail(self.ctx)


class Sensor15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 15:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9230) != 15:
            return Fail(self.ctx)


class Sensor20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 20:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9230) != 20:
            return Fail(self.ctx)


class Sensor25(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 25:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9230) != 25:
            return Fail(self.ctx)


class Sensor30(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 30:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9230) != 30:
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7230, key='Color23', value=0) # color reset
        self.set_mesh(trigger_ids=[523], fade=2.0) # 23 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GamblePass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7230, key='Color23', value=0) # color reset
        # Gamble Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='GamblePass', value=23)
        self.set_mesh(trigger_ids=[523], fade=2.0) # 23 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9230, event='char_event', level=4, sub_event='gamble')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return GambleReset(self.ctx)


class JackpotPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7230, key='Color23', value=0) # color reset
        # Jackpot Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='JackpotPass', value=23)
        self.set_mesh(trigger_ids=[523], fade=2.0) # 23 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9230, event='char_event', level=4, sub_event='jackpot')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return JackpotReset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[523], fade=2.0) # 23 / Ground outter
        self.set_mesh(trigger_ids=[5230]) # 23 / Ground inner
        self.set_user_value(trigger_id=7230, key='Color23', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GambleReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9230, type='trigger', achieve='ddstop_gamble')
        # Gamble Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9230, exp_rate=0.1)
        # self.create_item(spawn_ids=[7200,7201,7202,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212], trigger_id=9230)
        self.set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class JackpotReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9230, type='trigger', achieve='ddstop_gamble')
        # Jackpot Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9230, exp_rate=0.3)
        # self.create_item(spawn_ids=[7600,7601,7602,7602,7603,7604,7605,7606,7607,7608,7609,7610,7611,7612], trigger_id=9230)
        self.set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
