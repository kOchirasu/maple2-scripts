""" trigger/02000376_bf/11_innerlightguide.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='DungeonStart', value=0)
        self.set_effect(trigger_ids=[5100]) # 화살표
        self.set_effect(trigger_ids=[5101]) # 화살표
        self.set_effect(trigger_ids=[5102]) # 화살표
        self.set_effect(trigger_ids=[5103]) # 화살표
        self.set_effect(trigger_ids=[5104]) # 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonStart') >= 1:
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideOn(self.ctx)


class GuideOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000376_BF__11_INNERLIGHTGUIDE__0$', arg3='4000', arg4='0')
        self.set_effect(trigger_ids=[5100], visible=True) # 화살표
        self.set_effect(trigger_ids=[5101], visible=True) # 화살표
        self.set_effect(trigger_ids=[5102], visible=True) # 화살표
        self.set_effect(trigger_ids=[5103], visible=True) # 화살표
        self.set_effect(trigger_ids=[5104], visible=True) # 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5100]) # 화살표
        self.set_effect(trigger_ids=[5101]) # 화살표
        self.set_effect(trigger_ids=[5102]) # 화살표
        self.set_effect(trigger_ids=[5103]) # 화살표
        self.set_effect(trigger_ids=[5104]) # 화살표


initial_state = Wait
