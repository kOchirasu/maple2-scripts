""" trigger/63000001_cs/trigger_16.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[316], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[116]):
            return 발판16(self.ctx)


class 발판16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[316], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[116]):
            return 발판16끝(self.ctx)


class 발판16끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='416', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='416'):
            return 대기(self.ctx)


initial_state = 대기
