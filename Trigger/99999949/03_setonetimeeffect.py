""" trigger/99999949/03_setonetimeeffect.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=2, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        # 툴벤치 상 좌표 : 	-600, -600, 1200
        self.set_onetime_effect(id=3, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9021]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='3번 영역에 들어가면 SetOnetime트리거가 발동됩니다.Effect targetBox 이펙트 테스트.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9020]):
            return SetOnetimeEffectReady01(self.ctx)


class SetOnetimeEffectReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='SetOnetimeEffect 1초 후에 시작됩니다.')
        self.set_onetime_effect(id=1, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SetOnetimeEffect01(self.ctx)


class SetOnetimeEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='SetOnetimeEffect 재생')
        self.set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.2, duration=2.0, interpolator=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.2, end_scale=1.0, duration=2.0, interpolator=2)
        self.set_onetime_effect(id=3, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')
        # self.set_time_scale(enable=True, end_scale=1.0, duration=8.0, interpolator=2)
        self.debug_string(value='5초 후에 트리거가 리셋됩니다. 3번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait(self.ctx)


initial_state = Wait
