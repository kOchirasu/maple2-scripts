""" trigger/02000298_bf/door_19.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=219, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3191], visible=True)
        self.set_mesh(trigger_ids=[3192], visible=True)
        self.set_agent(trigger_ids=[9191], visible=True)
        self.set_agent(trigger_ids=[9192], visible=True)
        self.set_agent(trigger_ids=[9193], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[119]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=219, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3191], fade=5.0)
        self.set_mesh(trigger_ids=[3192], fade=5.0)
        self.set_agent(trigger_ids=[9191])
        self.set_agent(trigger_ids=[9192])
        self.set_agent(trigger_ids=[9193])
        self.spawn_monster(spawn_ids=[1020])


initial_state = 시작
