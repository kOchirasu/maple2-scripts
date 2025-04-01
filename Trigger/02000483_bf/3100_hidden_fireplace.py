""" trigger/02000483_bf/3100_hidden_fireplace.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # PortalOn
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_ladder(trigger_ids=[510]) # Ladder
        self.set_ladder(trigger_ids=[511]) # Ladder
        self.set_ladder(trigger_ids=[512]) # Ladder
        self.set_ladder(trigger_ids=[513]) # Ladder
        self.set_ladder(trigger_ids=[514]) # Ladder
        self.set_ladder(trigger_ids=[515]) # Ladder
        self.set_mesh(trigger_ids=[3100], visible=True) # Wall_BehindFirePlace
        self.set_mesh(trigger_ids=[3101], visible=True) # BehindFirePlaceCover
        self.set_mesh(trigger_ids=[3102], visible=True) # FireplaceInvisible
        self.set_interact_object(trigger_ids=[10002038], state=0) # Fireplace
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen') == 1:
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen') == 2:
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_interact_object(trigger_ids=[10002038], state=1) # Fireplace

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002038], state=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # PortalOn
        self.set_mesh(trigger_ids=[3102]) # FireplaceInvisible
        self.set_ladder(trigger_ids=[510], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[511], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[512], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[513], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[514], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[515], visible=True, enable=True, fade=2) # Ladder
        self.set_mesh(trigger_ids=[3100], fade=3.0) # Wall_BehindFirePlace
        self.set_mesh(trigger_ids=[3101], fade=3.0) # BehindFirePlaceCover


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_interact_object(trigger_ids=[10002038], state=1) # Fireplace

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002038], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='he_in_prop_fireplace_A01_Opened') # FireplaceActor


initial_state = Wait
