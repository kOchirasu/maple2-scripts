""" trigger/02000241_bf/trigger_01_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[303], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[403]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[303])
        self.set_mesh(trigger_ids=[701,702])


initial_state = 대기
