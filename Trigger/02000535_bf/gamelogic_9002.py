""" trigger/02000535_bf/gamelogic_9002.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='TypingGame') # 키입력 게임 선언
        self.create_widget(type='Round') # 라운드 관리 트리거위젯 선언
        self.widget_action(type='Round', func='SettingFinalRound', widget_arg='1')
        self.widget_action(type='Round', func='SettingAllowedFailCount', widget_arg='3')
        self.widget_action(type='Round', func='SettingRoundInitIfFail', widget_arg='0')
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameLogicStart') == 1:
            return 게임진입(self.ctx)


class 게임진입(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 새라운드시작가능체크(self.ctx)


class 새라운드시작가능체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Round', name='GameClear') == 1:
            return 게임성공종료(self.ctx)
        if self.widget_value(type='Round', name='GameFail') == 1:
            return 게임실패종료(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 라운드체크(self.ctx)


class 라운드체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Round', name='CurrentRound') == 1:
            return 라운드1시작전UI(self.ctx)
        if self.widget_value(type='Round', name='CurrentRound') == 2:
            return 라운드2시작전UI(self.ctx)
        if self.widget_value(type='Round', name='CurrentRound') == 3:
            return 라운드3시작전UI(self.ctx)


class 라운드1시작전UI(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.lock_my_pc(is_lock=True)
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__1$', duration=6000)
            self.widget_action(type='TypingGame', func='Start', widget_arg_num=7, widget_arg='6000')
            return 라운드1진행(self.ctx)


class 라운드1진행(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='TypingGame', name='Result') == 1:
            self.widget_action(type='Round', func='RoundResult', widget_arg='1')
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__2$', duration=3000)
            return 라운드종료(self.ctx)
        if self.widget_value(type='TypingGame', name='Result') == 0:
            self.widget_action(type='Round', func='RoundResult', widget_arg='0')
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__3$', duration=3000)
            return 라운드종료(self.ctx)


class 라운드2시작전UI(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.lock_my_pc(is_lock=True)
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__5$', duration=4000)
            self.widget_action(type='TypingGame', func='Start', widget_arg_num=6, widget_arg='4000')
            return 라운드2진행(self.ctx)


class 라운드2진행(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='TypingGame', name='Result') == 1:
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__6$', duration=3000)
            self.widget_action(type='Round', func='RoundResult', widget_arg='1')
            return 라운드종료(self.ctx)
        if self.widget_value(type='TypingGame', name='Result') == 0:
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__7$', duration=3000)
            self.widget_action(type='Round', func='RoundResult', widget_arg='0')
            return 라운드종료(self.ctx)


class 라운드3시작전UI(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__8$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.lock_my_pc(is_lock=True)
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__9$', duration=3000)
            self.widget_action(type='TypingGame', func='Start', widget_arg_num=7, widget_arg='3000')
            return 라운드3진행(self.ctx)


class 라운드3진행(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='TypingGame', name='Result') == 1:
            self.lock_my_pc(is_lock=True)
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__10$', duration=3000)
            self.widget_action(type='Round', func='RoundResult', widget_arg='1')
            return 라운드종료(self.ctx)
        if self.widget_value(type='TypingGame', name='Result') == 0:
            self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__GAMELOGIC_9002__11$', duration=3000)
            self.widget_action(type='Round', func='RoundResult', widget_arg='0')
            return 라운드종료(self.ctx)


class 라운드종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.lock_my_pc()
        return 새라운드시작가능체크(self.ctx)


class 게임성공종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1001, key='GameLogicEnd', value=1)
        self.set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 게임실패종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1001, key='GameLogicEnd', value=2)
        self.set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
