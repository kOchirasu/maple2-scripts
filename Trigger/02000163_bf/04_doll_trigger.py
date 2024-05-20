""" trigger/02000163_bf/04_doll_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[403], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000104], state=0):
            return 로봇사라짐(self.ctx)


class 로봇사라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[403])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000104], state=1):
            return 대기(self.ctx)


initial_state = 대기
