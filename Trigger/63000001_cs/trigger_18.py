""" trigger/63000001_cs/trigger_18.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[318], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[118]):
            return 발판18(self.ctx)


class 발판18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[318], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[118]):
            return 발판18끝(self.ctx)


class 발판18끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='418', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='418'):
            return 대기(self.ctx)


initial_state = 대기
