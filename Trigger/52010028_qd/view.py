""" trigger/52010028_qd/view.xml """
import trigger_api


class 진동설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=301, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return 흔들흔들(self.ctx)
        if self.user_detected(box_ids=[2006]):
            return 흔들흔들(self.ctx)
        if self.user_detected(box_ids=[2007]):
            return 흔들흔들(self.ctx)


class 흔들흔들(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진동설정(self.ctx)


initial_state = 진동설정
