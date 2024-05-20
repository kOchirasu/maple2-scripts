""" trigger/02000441_bf/anchor_01.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1500,1501,1502,1503,1504], visible=True, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001097], state=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1500,1501,1502,1503,1504], fade=10.0)


initial_state = idle
