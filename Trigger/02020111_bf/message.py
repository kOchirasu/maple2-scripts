""" trigger/02020111_bf/message.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') >= 0:
            return 메세지출력(self.ctx)


class 메세지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020111_BF__MESSAGE__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') >= 1:
            return 시작(self.ctx)


initial_state = 시작
