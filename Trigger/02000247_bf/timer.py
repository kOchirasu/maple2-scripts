""" trigger/02000247_bf/timer.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001])
        self.set_effect(trigger_ids=[2002])
        self.set_effect(trigger_ids=[2003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            return 초재기1(self.ctx)


class 초재기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 초재기2(self.ctx)


class 초재기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000247_BF__TIMER__0$', duration=3000, box_ids='0')
        self.set_effect(trigger_ids=[2001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000247_BF__TIMER__1$', duration=3000, box_ids='0')
        self.set_effect(trigger_ids=[2002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 초재기3(self.ctx)


class 초재기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000247_BF__TIMER__2$', duration=5000, box_ids='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 유저이동음성(self.ctx)


class 유저이동음성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_effect(trigger_ids=[2003], visible=True)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    pass


initial_state = 대기
