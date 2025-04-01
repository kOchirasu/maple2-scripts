""" trigger/02020301_bf/3000055_phase_4_camera_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=690000, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_4_Camera_01') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=690000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_4_Camera_01') == 0:
            return 대기(self.ctx)


initial_state = 대기
