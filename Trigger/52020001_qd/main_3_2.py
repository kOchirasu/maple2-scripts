""" trigger/52020001_qd/main_3_2.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 경고텍스트발생(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 1:
            return 경고텍스트(self.ctx)


class 경고텍스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='더이상 상대할 수 없습니다.\\n포탑을 이용해 다른 곳으로 이동하세요.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 경고텍스트_2(self.ctx)
        if self.user_value(key='respawn_end') == 2:
            return 끝(self.ctx)


class 경고텍스트_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='더이상 상대할 수 없습니다.\\n포탑을 이용해 다른 곳으로 이동하세요.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 경고텍스트(self.ctx)
        if self.user_value(key='respawn_end') == 2:
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            pass


initial_state = 경고텍스트발생
