""" trigger/02020111_bf/message.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') == 0:
            return 메세지출력(self.ctx)


class 메세지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020111_BF__MESSAGE__0$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') == 1:
            return 시작(self.ctx)


initial_state = 시작
