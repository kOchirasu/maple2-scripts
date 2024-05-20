""" trigger/02000252_bf/bigdoor_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[161,162,163,164], visible=True)
        self.set_interact_object(trigger_ids=[10000403], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000403], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[161,162,163,164])


initial_state = 대기
