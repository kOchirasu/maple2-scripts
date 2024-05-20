""" trigger/99999949/05_whitein.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=2, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=3, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=4, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9041]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='5번 영역에 들어가면 SetOnetimeEffect 트리거가 발동됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9040]):
            return SetOnetimeEffectReady01(self.ctx)


class SetOnetimeEffectReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='SetOnetimeEffect 2초 후에 시작됩니다.')
        self.set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SetOnetimeEffectReady02(self.ctx)


class SetOnetimeEffectReady02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SetOnetimeEffect01(self.ctx)


class SetOnetimeEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.debug_string(value='SetOnetimeEffect 재생')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=4, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.debug_string(value='5초 후에 트리거가 리셋됩니다. 5번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait(self.ctx)


initial_state = Wait
