""" trigger/99999907/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000019], state=1)
        self.set_interact_object(trigger_ids=[12000020], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000019], state=0):
            return 리셋(self.ctx)
        if self.object_interacted(interact_ids=[12000020], state=0):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 대기(self.ctx)


initial_state = 대기
