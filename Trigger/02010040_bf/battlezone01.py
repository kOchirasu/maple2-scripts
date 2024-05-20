""" trigger/02010040_bf/battlezone01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[4101])
        self.set_effect(trigger_ids=[4102])
        self.set_mesh(trigger_ids=[1100], visible=True) # barrier
        self.set_mesh(trigger_ids=[1101], visible=True) # barrier
        self.set_actor(trigger_id=2100, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2101, visible=True, initial_sequence='Closed') # door
        self.set_agent(trigger_ids=[3101], visible=True)
        self.set_agent(trigger_ids=[3102], visible=True)
        self.set_agent(trigger_ids=[3103], visible=True)
        self.set_agent(trigger_ids=[3104], visible=True)
        self.set_agent(trigger_ids=[3105], visible=True)
        self.set_agent(trigger_ids=[3106], visible=True)
        self.set_agent(trigger_ids=[3107], visible=True)
        self.set_agent(trigger_ids=[3108], visible=True)
        self.set_agent(trigger_ids=[3109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1100]) # barrier
        self.set_mesh(trigger_ids=[1101]) # barrier
        self.set_effect(trigger_ids=[4101], visible=True)
        self.set_effect(trigger_ids=[4102], visible=True)
        self.set_actor(trigger_id=2100, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2101, visible=True, initial_sequence='Opened') # door
        self.set_agent(trigger_ids=[3101])
        self.set_agent(trigger_ids=[3102])
        self.set_agent(trigger_ids=[3103])
        self.set_agent(trigger_ids=[3104])
        self.set_agent(trigger_ids=[3105])
        self.set_agent(trigger_ids=[3106])
        self.set_agent(trigger_ids=[3107])
        self.set_agent(trigger_ids=[3108])
        self.set_agent(trigger_ids=[3109])
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
