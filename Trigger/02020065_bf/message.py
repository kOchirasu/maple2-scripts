""" trigger/02020065_bf/message.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart') >= 1:
            # <게임 시작 결정>
            return 체력공지_1(self.ctx)
        if self.user_value(key='FieldGameStart') >= 2:
            # <방폭 결정>
            return 체력공지_1(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


class 체력공지_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=801, is_relative=True) <= 50:
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__1$', arg3='5000')
            return 체력공지_2(self.ctx)


class 체력공지_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=801, is_relative=True) <= 30:
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__2$', arg3='5000')
            return 체력공지_3(self.ctx)


class 체력공지_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=801, is_relative=True) <= 10:
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__3$', arg3='5000')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
