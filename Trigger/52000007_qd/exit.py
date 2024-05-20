""" trigger/52000007_qd/exit.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 초5(self.ctx)


class 초5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.create_item(spawn_ids=[9001,9002,9003,9004,9005], trigger_id=101)
            self.add_buff(box_ids=[101], skill_id=70000019, level=1)
            return 초30(self.ctx)


class 초30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='300', seconds=300)
        self.set_event_ui(type=1, arg2='$52000007_QD__EXIT__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='300'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.move_user(map_id=2000064, portal_id=800)
        return 유저감지(self.ctx)


initial_state = 유저감지
