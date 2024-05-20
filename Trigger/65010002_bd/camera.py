""" trigger/65010002_bd/camera.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(box_id=101):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            self.move_user()
            return 종료(self.ctx)


"""
class 카메라300(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.select_camera_path(path_ids=[300,304], return_view=False)
        self.set_event_ui(type=1, arg2='1vs1 대결을 시작합니다.', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 연출시작(self.ctx)
"""

"""
class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='Username1')
        self.select_camera(trigger_id=301)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 카메라302(self.ctx)
"""

"""
class 카메라302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='Username2')
        self.select_camera(trigger_id=302)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 카메라303(self.ctx)
"""

"""
class 카메라303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[303], return_view=False)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.select_camera(trigger_id=303, enable=False)
            return PvP시작(self.ctx)
"""

"""
class PvP시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='1,3')
        self.set_event_ui(type=2, arg2='1라운드시작', arg3='1,3')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)
"""

class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
