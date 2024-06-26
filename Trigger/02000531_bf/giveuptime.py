""" trigger/02000531_bf/giveuptime.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            self.set_event_ui_script(type=BannerType.GameOver, script='$DUNGEON__GIVEUP__TIME__0$', duration=3000)
            self.dungeon_enable_give_up(is_enable=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
