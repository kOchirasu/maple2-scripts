""" trigger/02000471_bf/timer.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='TimerEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 1:
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='Timer', seconds=420, auto_remove=True, display=True)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__TIMER__0$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='Timer'):
            return end_fail(self.ctx)
        if self.user_value(key='InteractClear') == 1:
            return end_clear(self.ctx)


class end_fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='TimerEnd', value=1)
        self.reset_timer(timer_id='Timer')


class end_clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040301, key='InteractClear', value=1)
        self.reset_timer(timer_id='Timer')


initial_state = idle
