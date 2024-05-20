""" trigger/02020025_bf/background.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 지하배경(self.ctx)


class 지하배경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_background(dds='BG_Cave_D.dds')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[903]):
            return 지상배경(self.ctx)


class 지상배경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_background(dds='BG_Tria.dds')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 지하배경(self.ctx)


initial_state = 대기
