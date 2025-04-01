""" trigger/02020051_bf/102_timmer.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='990')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timmer') == 1:
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='990', seconds=600, auto_remove=True, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=600000):
            return 종료(self.ctx)
        if self.user_value(key='Timmer') == 3:
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_shy', script='$02020051_BF__102_TIMMER__0$', duration=5684, voice='ko/Npc/00002201')
        self.set_user_value(trigger_id=104, key='End', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timmer') == 2:
            return 시작(self.ctx)


initial_state = 시작
