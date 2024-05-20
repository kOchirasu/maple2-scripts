""" trigger/02000251_bf/timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3001])
        self.set_effect(trigger_ids=[3002])
        self.set_effect(trigger_ids=[3003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            return 초재기1(self.ctx)


class 초재기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 초재기2(self.ctx)
        if self.count_users(box_id=202) >= 4:
            return 초재기2(self.ctx)


class 초재기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)
        self.set_event_ui(type=1, arg2='$02000251_BF__TIMER__0$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)
        self.set_event_ui(type=1, arg2='$02000251_BF__TIMER__1$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[3002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 초재기3(self.ctx)


class 초재기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000251_BF__TIMER__2$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 유저이동음성(self.ctx)


class 유저이동음성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_effect(trigger_ids=[3003], visible=True)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    pass


initial_state = 대기
