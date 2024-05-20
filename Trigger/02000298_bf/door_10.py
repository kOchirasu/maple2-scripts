""" trigger/02000298_bf/door_10.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=210, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3101], visible=True)
        self.set_mesh(trigger_ids=[3102], visible=True)
        self.set_agent(trigger_ids=[9101], visible=True)
        self.set_agent(trigger_ids=[9102], visible=True)
        self.set_agent(trigger_ids=[9103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[110]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=210, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3101], fade=5.0)
        self.set_mesh(trigger_ids=[3102], fade=5.0)
        self.set_agent(trigger_ids=[9101])
        self.set_agent(trigger_ids=[9102])
        self.set_agent(trigger_ids=[9103])


initial_state = 시작
