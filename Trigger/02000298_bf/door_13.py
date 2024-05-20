""" trigger/02000298_bf/door_13.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=213, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3131], visible=True)
        self.set_mesh(trigger_ids=[3132], visible=True)
        self.set_agent(trigger_ids=[9131], visible=True)
        self.set_agent(trigger_ids=[9132], visible=True)
        self.set_agent(trigger_ids=[9133], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[113]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=213, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3131], fade=5.0)
        self.set_mesh(trigger_ids=[3132], fade=5.0)
        self.set_agent(trigger_ids=[9131])
        self.set_agent(trigger_ids=[9132])
        self.set_agent(trigger_ids=[9133])
        self.spawn_monster(spawn_ids=[1014])


initial_state = 시작
