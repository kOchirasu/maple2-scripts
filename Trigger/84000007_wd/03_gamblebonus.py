""" trigger/84000007_wd/03_gamblebonus.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001]) # Firework

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GamblePass') == 22:
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass') == 23:
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass') == 32:
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass') == 33:
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass') == 22:
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass') == 23:
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass') == 32:
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass') == 33:
            return JackpotBonusDelay01(self.ctx)


# 한 팀이라도 큰 숫자 발판에서 통과하면 스테이지 위에 보너스 지급
class GambleBonusDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='GambleSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GambleBonusDelay02(self.ctx)


class GambleBonusDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001], visible=True) # Firework

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GambleBonus(self.ctx)


class GambleBonus(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Gamble Pass Bonus For Everyone
        self.mini_game_give_exp(box_id=9001, exp_rate=0.1)
        # # Gamble Pass Bonus For Everyone
        self.create_item(spawn_ids=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123,6124,6125,6126,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,6137,6138,6139,6140,6141,6142,6143,6144,6145,6146,6147,6148,6149,6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166,6167,6168,6169,6161,6171,6172,6173,6174,6175,6176,6177,6178,6179,6180,6181,6182,6183,6184])

    def on_tick(self) -> trigger_api.Trigger:
        return Quit(self.ctx)


class JackpotBonusDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='GambleSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return JackpotBonusDelay02(self.ctx)


class JackpotBonusDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001], visible=True) # Firework

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JackpotBonus(self.ctx)


class JackpotBonus(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Jackpot Pass Bonus For Everyone
        self.mini_game_give_exp(box_id=9001, exp_rate=0.1)
        # # Jackpot Pass Bonus For Everyone
        self.create_item(spawn_ids=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211,6212,6213,6214,6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228,6229,6230,6231,6232,6233,6234,6235,6236,6237,6238,6239,6240,6241,6242,6243,6244,6245,6246,6247,6248,6249,6250,6251,6252,6253,6254,6255,6256,6257,6258,6259,6260,6262,6262,6263,6264,6265,6266,6267,6268,6269,6262,6271,6272,6273,6274,6275,6276,6277,6278,6279,6280,6281,6282,6283,6284])

    def on_tick(self) -> trigger_api.Trigger:
        return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001]) # Firework
        self.set_user_value(key='GamblePass', value=0)


initial_state = Wait
