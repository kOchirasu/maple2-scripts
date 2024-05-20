""" trigger/64000001_gd/ringout.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 링아웃(self.ctx)


class 링아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='링아웃', arg3='2000')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.move_user(map_id=64000001, portal_id=2, box_id=105)
            return 대기(self.ctx)


initial_state = 대기
