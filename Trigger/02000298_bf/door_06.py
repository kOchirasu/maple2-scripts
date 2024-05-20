""" trigger/02000298_bf/door_06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3061], visible=True)
        self.set_mesh(trigger_ids=[3062], visible=True)
        self.set_agent(trigger_ids=[9061], visible=True)
        self.set_agent(trigger_ids=[9062], visible=True)
        self.set_agent(trigger_ids=[9063], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3061], fade=5.0)
        self.set_mesh(trigger_ids=[3062], fade=5.0)
        self.set_agent(trigger_ids=[9061])
        self.set_agent(trigger_ids=[9062])
        self.set_agent(trigger_ids=[9063])


initial_state = 시작
