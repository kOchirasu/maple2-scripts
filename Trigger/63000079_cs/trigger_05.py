""" trigger/63000079_cs/trigger_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[305], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 발판05(self.ctx)


class 발판05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[305], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[105]):
            return 발판05끝(self.ctx)


class 발판05끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='405', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='405'):
            return 대기(self.ctx)


initial_state = 대기
