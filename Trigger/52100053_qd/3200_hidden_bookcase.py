""" trigger/52100053_qd/3200_hidden_bookcase.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002]) # PortalOn
        self.set_ladder(trigger_ids=[520]) # Ladder
        self.set_ladder(trigger_ids=[521]) # Ladder
        self.set_ladder(trigger_ids=[522]) # Ladder
        self.set_ladder(trigger_ids=[523]) # Ladder
        self.set_ladder(trigger_ids=[524]) # Ladder
        self.set_mesh(trigger_ids=[3200], visible=True) # Wall_BehindBookcase
        self.set_mesh(trigger_ids=[3201], visible=True) # BehindBookcaseCover
        self.set_mesh(trigger_ids=[3202], visible=True) # Bookcase
        self.set_mesh(trigger_ids=[3203], visible=True) # BookcaseInvisible
        self.set_interact_object(trigger_ids=[10002092], state=0) # Bookcase
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen') == 1:
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen') == 2:
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3202]) # Bookcase
        self.set_interact_object(trigger_ids=[10002092], state=1) # Bookcase

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002092], state=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # PortalOn
        self.set_mesh(trigger_ids=[3203]) # BookcaseInvisible
        self.set_ladder(trigger_ids=[520], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[521], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[522], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[523], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[524], visible=True, enable=True, fade=2) # Ladder
        self.set_mesh(trigger_ids=[3200], fade=3.0) # Wall_BehindBookcase
        self.set_mesh(trigger_ids=[3201], fade=3.0) # BehindBookcaseCover


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3202]) # Bookcase
        self.set_interact_object(trigger_ids=[10002092], state=1) # Bookcase

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002092], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3202], visible=True) # Bookcase


initial_state = Wait
