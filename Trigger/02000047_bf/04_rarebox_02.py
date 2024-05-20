""" trigger/02000047_bf/04_rarebox_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            return 발판02(self.ctx)


class 발판02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[402], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[202]):
            return 발판02끝(self.ctx)


class 발판02끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='502', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='502'):
            return 대기(self.ctx)


initial_state = 대기
