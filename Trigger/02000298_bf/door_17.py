""" trigger/02000298_bf/door_17.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=217, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3171], visible=True)
        self.set_mesh(trigger_ids=[3172], visible=True)
        self.set_agent(trigger_ids=[9171], visible=True)
        self.set_agent(trigger_ids=[9172], visible=True)
        self.set_agent(trigger_ids=[9173], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[117]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=217, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3171], fade=5.0)
        self.set_mesh(trigger_ids=[3172], fade=5.0)
        self.set_agent(trigger_ids=[9171])
        self.set_agent(trigger_ids=[9172])
        self.set_agent(trigger_ids=[9173])
        self.spawn_monster(spawn_ids=[1018])


initial_state = 시작
