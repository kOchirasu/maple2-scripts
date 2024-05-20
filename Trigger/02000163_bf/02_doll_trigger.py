""" trigger/02000163_bf/02_doll_trigger.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000102], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[401], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000102], state=0):
            return 로봇사라짐(self.ctx)


class 로봇사라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000102], state=1):
            return 대기(self.ctx)


initial_state = 시작
