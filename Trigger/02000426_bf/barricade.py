""" trigger/02000426_bf/barricade.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 알림시작중(self.ctx)


class 알림시작중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000207_BF__BARRICADE__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=23000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True)


initial_state = 대기
