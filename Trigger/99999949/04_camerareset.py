""" trigger/99999949/04_camerareset.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9031]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='4번 영역에 들어가면 CameraReset 트리거가 발동됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9030]):
            return CameraReady(self.ctx)


class CameraReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='SetOnetimeEffect 1초 후에 시작됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='600번 카메라 선택')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraWalk03(self.ctx)


"""
class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='601번 카메라 선택')
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraWalk03(self.ctx)
"""

class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='602번 카메라 선택')
        self.select_camera(trigger_id=604)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraReset(self.ctx)


class CameraReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='모든 카메라 리셋')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=604, enable=False)
        # self.reset_camera(interpolation_time=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='5초 후에 트리거가 리셋됩니다. 4번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait(self.ctx)


initial_state = Wait
