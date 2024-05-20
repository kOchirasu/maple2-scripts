""" trigger/02000298_bf/door_16.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=216, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3161], visible=True)
        self.set_mesh(trigger_ids=[3162], visible=True)
        self.set_agent(trigger_ids=[9161], visible=True)
        self.set_agent(trigger_ids=[9162], visible=True)
        self.set_agent(trigger_ids=[9163], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[116]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=216, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3161], fade=5.0)
        self.set_mesh(trigger_ids=[3162], fade=5.0)
        self.set_agent(trigger_ids=[9161])
        self.set_agent(trigger_ids=[9162])
        self.set_agent(trigger_ids=[9163])
        self.spawn_monster(spawn_ids=[1017])


initial_state = 시작
