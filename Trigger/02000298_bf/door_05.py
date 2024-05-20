""" trigger/02000298_bf/door_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3051], visible=True)
        self.set_mesh(trigger_ids=[3052], visible=True)
        self.set_agent(trigger_ids=[9051], visible=True)
        self.set_agent(trigger_ids=[9052], visible=True)
        self.set_agent(trigger_ids=[9053], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3051], fade=5.0)
        self.set_mesh(trigger_ids=[3052], fade=5.0)
        self.set_agent(trigger_ids=[9051])
        self.set_agent(trigger_ids=[9052])
        self.set_agent(trigger_ids=[9053])


initial_state = 시작
