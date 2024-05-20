""" trigger/02000253_bf/wall_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_mesh(trigger_ids=[501,502], visible=True)
        self.set_mesh(trigger_ids=[601,602,603], visible=True)
        self.set_interact_object(trigger_ids=[10000437], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000437], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_mesh(trigger_ids=[501,502])
        self.set_mesh(trigger_ids=[601,602,603])


initial_state = 대기
