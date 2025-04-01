""" trigger/61000008_me/04_thenumber.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerCheckIn') == 1:
            return BannerCheckIn(self.ctx)


class BannerCheckIn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) == 50:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=50)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 49:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=49)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 48:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=48)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 47:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=47)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 46:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=46)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 45:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=45)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 44:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=44)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 43:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=43)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 42:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=42)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 41:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=41)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 40:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=40)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 39:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=39)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 38:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=38)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 37:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=37)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 36:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=36)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 35:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=35)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 34:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=34)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 33:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=33)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 32:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=32)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 31:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=31)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 30:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=30)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 29:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=29)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 28:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=28)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 27:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=27)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 26:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=26)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 25:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=25)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 24:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=24)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 23:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=23)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 22:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=22)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 21:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=21)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 20:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=20)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 19:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=19)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 18:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=18)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 17:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=17)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 16:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=16)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 15:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=15)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 14:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=14)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 13:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=13)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 12:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=12)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 11:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=11)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 10:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=10)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 9:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=9)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 8:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=8)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 7:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=7)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 6:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=6)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 5:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=5)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 4:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=4)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 3:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=3)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 2:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=2)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001) == 1:
            self.set_user_value(trigger_id=5, key='BannerNumber', value=1)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=0)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='BannerCheckIn', value=0)
        self.set_user_value(key='BannerNumber', value=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
