""" trigger/02000253_bf/wall_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_mesh(trigger_ids=[503,504], visible=True)
        self.set_mesh(trigger_ids=[604,605,606], visible=True)
        self.set_interact_object(trigger_ids=[10000438], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000438], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_mesh(trigger_ids=[503,504])
        self.set_mesh(trigger_ids=[604,605,606])


initial_state = 대기
