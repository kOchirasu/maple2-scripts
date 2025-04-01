""" trigger/02020051_bf/107_text.xml """
import trigger_api


class 가이드시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Text') == 1:
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 가이드_1(self.ctx)


class 가이드_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', script='$02020051_BF__107_TEXT__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Text') == 2:
            return 가이드시작(self.ctx)


initial_state = 가이드시작
