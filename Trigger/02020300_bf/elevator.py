""" trigger/02020300_bf/elevator.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 메시지_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='elevator') == 1:
            return 엘리베이터_정지(self.ctx)


class 엘리베이터_정지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020300_BF__MAIN__12$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            self.set_breakable(trigger_ids=[5001])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='elevator') == 0:
            return 메시지_대기(self.ctx)


initial_state = 메시지_대기
