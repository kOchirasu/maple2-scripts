""" trigger/84000007_wd/sensor_9320.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box32Check', value=10)
        self.set_mesh(trigger_ids=[532], visible=True) # 32 / Ground outter
        self.set_mesh(trigger_ids=[5320], visible=True) # 32 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box32Check') == 0:
            return Sensor0(self.ctx)
        if self.user_value(key='Box32Check') == 1:
            return Sensor1(self.ctx)
        if self.user_value(key='Box32Check') == 2:
            return Sensor2(self.ctx)
        if self.user_value(key='Box32Check') == 3:
            return Sensor3(self.ctx)
        if self.user_value(key='Box32Check') == 4:
            return Sensor4(self.ctx)
        if self.user_value(key='Box32Check') == 5:
            return Sensor5(self.ctx)
        if self.user_value(key='Box32Check') == 7:
            return Sensor7(self.ctx)
        if self.user_value(key='Box32Check') == 8:
            return Sensor8(self.ctx)
        if self.user_value(key='Box32Check') == 9:
            return Sensor9(self.ctx)
        if self.user_value(key='Box32Check') == 6:
            return Sensor10(self.ctx)
        if self.user_value(key='Box32Check') == 15:
            return Sensor15(self.ctx)
        if self.user_value(key='Box32Check') == 20:
            return Sensor20(self.ctx)
        if self.user_value(key='Box32Check') == 25:
            return Sensor25(self.ctx)
        if self.user_value(key='Box32Check') == 30:
            return Sensor30(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 1:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9320) != 1:
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 2:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9320) != 2:
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 3:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9320) != 3:
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 4:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9320) != 4:
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 5:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9320) != 5:
            return Fail(self.ctx)


class Sensor7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 7:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9320) != 7:
            return Fail(self.ctx)


class Sensor8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 8:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9320) != 8:
            return Fail(self.ctx)


class Sensor9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 9:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9320) != 9:
            return Fail(self.ctx)


class Sensor10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 10:
            return GamblePass(self.ctx)
        if self.count_users(box_id=9320) != 10:
            return Fail(self.ctx)


class Sensor15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 15:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9320) != 15:
            return Fail(self.ctx)


class Sensor20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 20:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9320) != 20:
            return Fail(self.ctx)


class Sensor25(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 25:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9320) != 25:
            return Fail(self.ctx)


class Sensor30(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 30:
            return JackpotPass(self.ctx)
        if self.count_users(box_id=9320) != 30:
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7320, key='Color32', value=0) # color reset
        self.set_mesh(trigger_ids=[532], fade=2.0) # 32 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GamblePass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_GamblePass_01')
        self.set_user_value(trigger_id=7320, key='Color32', value=0) # color reset
        # Gamble Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='GamblePass', value=32)
        self.set_mesh(trigger_ids=[532], fade=2.0) # 32 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9320, event='char_event', level=4, sub_event='gamble')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return GambleReset(self.ctx)


class JackpotPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7320, key='Color32', value=0) # color reset
        # Jackpot Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='JackpotPass', value=32)
        self.set_mesh(trigger_ids=[532], fade=2.0) # 32 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9320, event='char_event', level=4, sub_event='jackpot')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return JackpotReset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[532], fade=2.0) # 32 / Ground outter
        self.set_mesh(trigger_ids=[5320]) # 32 / Ground inner
        self.set_user_value(trigger_id=7320, key='Color32', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GambleReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9320, type='trigger', achieve='ddstop_gamble')
        # Gamble Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9320, exp_rate=0.1)
        # self.create_item(spawn_ids=[7300,7301,7302,7302,7303,7304,7305,7306,7307,7308,7309,7310,7311,7312], trigger_id=9320)
        self.set_user_value(key='Box32Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class JackpotReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9320, type='trigger', achieve='ddstop_gamble')
        # Jackpot Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9320, exp_rate=0.3)
        # self.create_item(spawn_ids=[7700,7701,7702,7702,7703,7704,7705,7706,7707,7708,7709,7710,7711,7712], trigger_id=9320)
        self.set_user_value(key='Box32Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box32Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
