""" trigger/02000298_bf/door_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3021], visible=True)
        self.set_mesh(trigger_ids=[3022], visible=True)
        self.set_agent(trigger_ids=[9021], visible=True)
        self.set_agent(trigger_ids=[9022], visible=True)
        self.set_agent(trigger_ids=[9023], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3021], fade=5.0)
        self.set_mesh(trigger_ids=[3022], fade=5.0)
        self.set_agent(trigger_ids=[9021])
        self.set_agent(trigger_ids=[9022])
        self.set_agent(trigger_ids=[9023])


initial_state = 시작
