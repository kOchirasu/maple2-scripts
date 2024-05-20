""" trigger/02000242_bf/trigger_04_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[303], visible=True)
        self.set_mesh(trigger_ids=[703,704], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[402]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[303])
        self.set_mesh(trigger_ids=[703,704])
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
