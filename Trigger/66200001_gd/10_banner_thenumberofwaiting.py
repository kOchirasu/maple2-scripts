""" trigger/66200001_gd/10_banner_thenumberofwaiting.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerCheckIn') == 1:
            return BannerCheckIn(self.ctx)


class BannerCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_user_count(trigger_box_id=9021, key='BannerNumberOfBlue', user_tag_id=1)
        self.user_value_to_number_mesh(key='BannerNumberOfBlue', start_mesh_id=1500, digit_count=2)
        self.set_user_value_from_user_count(trigger_box_id=9022, key='BannerNumberOfRed', user_tag_id=2)
        self.user_value_to_number_mesh(key='BannerNumberOfRed', start_mesh_id=2500, digit_count=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NextWait(self.ctx)


class NextWait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerCheckIn') == 1:
            return BannerCheckIn(self.ctx)
        if self.user_value(key='BannerCheckIn') == 0:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_user_count(trigger_box_id=9021, key='BannerNumberOfBlue', user_tag_id=1)
        self.user_value_to_number_mesh(key='BannerNumberOfBlue', start_mesh_id=1500, digit_count=2)
        self.set_user_value_from_user_count(trigger_box_id=9022, key='BannerNumberOfRed', user_tag_id=2)
        self.user_value_to_number_mesh(key='BannerNumberOfRed', start_mesh_id=2500, digit_count=2)


initial_state = Wait
