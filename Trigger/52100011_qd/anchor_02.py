""" trigger/52100011_qd/anchor_02.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1505,1506,1507,1508,1509], visible=True, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002056], state=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1505,1506,1507,1508,1509], fade=10.0)


initial_state = idle
