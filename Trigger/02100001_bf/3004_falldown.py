""" trigger/02100001_bf/3004_falldown.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3004], visible=True) # 투명 발판

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9004]):
            return RemoveMesh(self.ctx)


class RemoveMesh(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3004]) # 투명 발판

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9004]):
            return Wait(self.ctx)


initial_state = Wait
