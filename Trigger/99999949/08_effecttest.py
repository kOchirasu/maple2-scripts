""" trigger/99999949/08_effecttest.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='8번 영역에 들어가면 EffectTest 트리거가 발동됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return CameraReady(self.ctx)


class CameraReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='EffectTest 2초 후에 시작됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이펙트출력01(self.ctx)


class 이펙트출력01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='EffectTest 발동')
        self.set_effect(trigger_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='5초 후에 트리거가 리셋됩니다. 8번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait(self.ctx)


initial_state = Wait
