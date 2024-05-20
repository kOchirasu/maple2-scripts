""" trigger/52000014_qd/cube_2301.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2301], visible=True)
        self.set_mesh(trigger_ids=[2302], visible=True)
        self.set_effect(trigger_ids=[12301]) # Fire Cast Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92301]):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_effect(trigger_ids=[12301], visible=True) # Fire Cast Sound
        self.set_mesh(trigger_ids=[2301], start_delay=200, fade=1.0)
        self.set_mesh(trigger_ids=[2302], start_delay=700, fade=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12301]) # Fire Cast Sound


initial_state = 대기
