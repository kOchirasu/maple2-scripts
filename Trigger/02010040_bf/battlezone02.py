""" trigger/02010040_bf/battlezone02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4)
        self.set_effect(trigger_ids=[4201])
        self.set_effect(trigger_ids=[4202])
        self.set_mesh(trigger_ids=[1200], visible=True) # barrier
        self.set_mesh(trigger_ids=[1201], visible=True) # barrier
        self.set_actor(trigger_id=2200, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2201, visible=True, initial_sequence='Closed') # door
        self.set_agent(trigger_ids=[3201], visible=True)
        self.set_agent(trigger_ids=[3202], visible=True)
        self.set_agent(trigger_ids=[3203], visible=True)
        self.set_agent(trigger_ids=[3204], visible=True)
        self.set_agent(trigger_ids=[3205], visible=True)
        self.set_agent(trigger_ids=[3206], visible=True)
        self.set_agent(trigger_ids=[3207], visible=True)
        self.set_agent(trigger_ids=[3208], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306,401,402,403,404,405,406,407,408], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303,304,305,306,401,402,403,404,405,406,407,408]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1200]) # barrier
        self.set_mesh(trigger_ids=[1201]) # barrier
        self.set_effect(trigger_ids=[4201], visible=True)
        self.set_effect(trigger_ids=[4202], visible=True)
        self.set_actor(trigger_id=2200, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2201, visible=True, initial_sequence='Opened') # door
        self.set_agent(trigger_ids=[3201])
        self.set_agent(trigger_ids=[3202])
        self.set_agent(trigger_ids=[3203])
        self.set_agent(trigger_ids=[3204])
        self.set_agent(trigger_ids=[3205])
        self.set_agent(trigger_ids=[3206])
        self.set_agent(trigger_ids=[3207])
        self.set_agent(trigger_ids=[3208])
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
