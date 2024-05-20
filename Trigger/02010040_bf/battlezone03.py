""" trigger/02010040_bf/battlezone03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6)
        self.set_effect(trigger_ids=[4301])
        self.set_effect(trigger_ids=[4302])
        self.set_effect(trigger_ids=[4303])
        self.set_mesh(trigger_ids=[1300], visible=True) # barrier
        self.set_mesh(trigger_ids=[1301], visible=True) # barrier
        self.set_mesh(trigger_ids=[1302], visible=True) # barrier
        self.set_actor(trigger_id=2300, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2301, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2302, visible=True, initial_sequence='Closed') # door
        self.set_agent(trigger_ids=[3301], visible=True)
        self.set_agent(trigger_ids=[3302], visible=True)
        self.set_agent(trigger_ids=[3303], visible=True)
        self.set_agent(trigger_ids=[3304], visible=True)
        self.set_agent(trigger_ids=[3305], visible=True)
        self.set_agent(trigger_ids=[3306], visible=True)
        self.set_agent(trigger_ids=[3307], visible=True)
        self.set_agent(trigger_ids=[3308], visible=True)
        self.set_agent(trigger_ids=[3309], visible=True)
        self.set_agent(trigger_ids=[3310], visible=True)
        self.set_agent(trigger_ids=[3311], visible=True)
        self.set_agent(trigger_ids=[3312], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[501,502,601,602,701,702], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,502,601,602,701,702]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1300]) # barrier
        self.set_mesh(trigger_ids=[1301]) # barrier
        self.set_mesh(trigger_ids=[1302]) # barrier
        self.set_effect(trigger_ids=[4301], visible=True)
        self.set_effect(trigger_ids=[4302], visible=True)
        self.set_effect(trigger_ids=[4303], visible=True)
        self.set_actor(trigger_id=2300, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2301, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2302, visible=True, initial_sequence='Opened') # door
        self.set_agent(trigger_ids=[3301])
        self.set_agent(trigger_ids=[3302])
        self.set_agent(trigger_ids=[3303])
        self.set_agent(trigger_ids=[3304])
        self.set_agent(trigger_ids=[3305])
        self.set_agent(trigger_ids=[3306])
        self.set_agent(trigger_ids=[3307])
        self.set_agent(trigger_ids=[3308])
        self.set_agent(trigger_ids=[3309])
        self.set_agent(trigger_ids=[3310])
        self.set_agent(trigger_ids=[3311])
        self.set_agent(trigger_ids=[3312])
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
