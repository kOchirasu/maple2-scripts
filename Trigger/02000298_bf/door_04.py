""" trigger/02000298_bf/door_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3041], visible=True)
        self.set_mesh(trigger_ids=[3042], visible=True)
        self.set_agent(trigger_ids=[9041], visible=True)
        self.set_agent(trigger_ids=[9042], visible=True)
        self.set_agent(trigger_ids=[9043], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3041], fade=5.0)
        self.set_mesh(trigger_ids=[3042], fade=5.0)
        self.set_agent(trigger_ids=[9041])
        self.set_agent(trigger_ids=[9042])
        self.set_agent(trigger_ids=[9043])


initial_state = 시작
