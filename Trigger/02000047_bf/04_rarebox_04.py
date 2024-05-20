""" trigger/02000047_bf/04_rarebox_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[404])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[204]):
            return 발판04(self.ctx)


class 발판04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[404], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[204]):
            return 발판04끝(self.ctx)


class 발판04끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='504', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='504'):
            return 대기(self.ctx)


initial_state = 대기
