""" trigger/84000007_wd/09_fireworks.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Staging(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fireworks') == 1:
            return Volley_Ready(self.ctx)
        if self.user_value(key='Fireworks') == 2:
            return Volley_Ready2(self.ctx)


class Volley_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$84000007_WD__09_FIREWORKS__0$', duration=3000, box_ids=['0'])
        # self.select_camera_path(path_ids=[902,903])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Volley_Fire(self.ctx)


class Volley_Ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$84000007_WD__09_FIREWORKS__1$', duration=3000, box_ids=['0'])
        # self.select_camera_path(path_ids=[902,903])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Volley_Fire(self.ctx)


class Volley_Fire(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            pass


initial_state = Staging
