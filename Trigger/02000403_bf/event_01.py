""" trigger/02000403_bf/event_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000403_BF__EVENT_01__0$', duration=3000)


initial_state = idle
