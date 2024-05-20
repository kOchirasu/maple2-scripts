""" trigger/02000298_bf/door_01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3011], visible=True)
        self.set_mesh(trigger_ids=[3012], visible=True)
        self.set_agent(trigger_ids=[9011], visible=True)
        self.set_agent(trigger_ids=[9012], visible=True)
        self.set_agent(trigger_ids=[9013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.set_mesh(trigger_ids=[3011], fade=5.0)
        self.set_mesh(trigger_ids=[3012], fade=5.0)
        self.set_agent(trigger_ids=[9011])
        self.set_agent(trigger_ids=[9012])
        self.set_agent(trigger_ids=[9013])


initial_state = 시작
