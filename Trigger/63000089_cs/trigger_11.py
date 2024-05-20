""" trigger/63000089_cs/trigger_11.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[311], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[111]):
            return 발판11(self.ctx)


class 발판11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[111]):
            return 발판11끝(self.ctx)


class 발판11끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='411', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='411'):
            return 대기(self.ctx)


initial_state = 대기
