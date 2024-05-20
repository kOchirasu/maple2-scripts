""" trigger/02000298_bf/door_08.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=208, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3081], visible=True)
        self.set_mesh(trigger_ids=[3082], visible=True)
        self.set_agent(trigger_ids=[9081], visible=True)
        self.set_agent(trigger_ids=[9082], visible=True)
        self.set_agent(trigger_ids=[9083], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[108]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=208, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3081], fade=5.0)
        self.set_mesh(trigger_ids=[3082], fade=5.0)
        self.set_agent(trigger_ids=[9081])
        self.set_agent(trigger_ids=[9082])
        self.set_agent(trigger_ids=[9083])


initial_state = 시작
