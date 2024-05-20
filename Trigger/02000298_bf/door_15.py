""" trigger/02000298_bf/door_15.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=215, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3151], visible=True)
        self.set_mesh(trigger_ids=[3152], visible=True)
        self.set_agent(trigger_ids=[9151], visible=True)
        self.set_agent(trigger_ids=[9152], visible=True)
        self.set_agent(trigger_ids=[9153], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[115]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=215, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3151], fade=5.0)
        self.set_mesh(trigger_ids=[3152], fade=5.0)
        self.set_agent(trigger_ids=[9151])
        self.set_agent(trigger_ids=[9152])
        self.set_agent(trigger_ids=[9153])
        self.spawn_monster(spawn_ids=[1016])


initial_state = 시작
