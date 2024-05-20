""" trigger/02000298_bf/door_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=209, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3091], visible=True)
        self.set_mesh(trigger_ids=[3092], visible=True)
        self.set_agent(trigger_ids=[9091], visible=True)
        self.set_agent(trigger_ids=[9092], visible=True)
        self.set_agent(trigger_ids=[9093], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[109]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=209, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3091], fade=5.0)
        self.set_mesh(trigger_ids=[3092], fade=5.0)
        self.set_agent(trigger_ids=[9091])
        self.set_agent(trigger_ids=[9092])
        self.set_agent(trigger_ids=[9093])


initial_state = 시작
