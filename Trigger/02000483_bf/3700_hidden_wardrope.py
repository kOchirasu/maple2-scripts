""" trigger/02000483_bf/3700_hidden_wardrope.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004]) # PortalOn
        self.set_ladder(trigger_ids=[540]) # Ladder
        self.set_ladder(trigger_ids=[541]) # Ladder
        self.set_ladder(trigger_ids=[542]) # Ladder
        self.set_ladder(trigger_ids=[543]) # Ladder
        self.set_ladder(trigger_ids=[544]) # Ladder
        self.set_ladder(trigger_ids=[545]) # Ladder
        self.set_mesh(trigger_ids=[3700], visible=True) # Wall_BehindWardrope
        self.set_mesh(trigger_ids=[3701,3704], visible=True) # BehindWardropeCover01
        self.set_mesh(trigger_ids=[3702], visible=True) # Wardrope
        self.set_mesh(trigger_ids=[3703], visible=True) # WardropeInvisible
        self.set_interact_object(trigger_ids=[10002044], state=0) # Wardrope
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen') == 1:
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen') == 2:
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3702], start_delay=100, fade=2.0) # Wardrope
        self.set_interact_object(trigger_ids=[10002044], state=1) # Wardrope

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002044], state=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True) # PortalOn
        self.set_mesh(trigger_ids=[3700], fade=3.0) # Wall_BehindWardrope
        self.set_mesh(trigger_ids=[3701,3704], fade=3.0) # BehindWardropeCover
        self.set_mesh(trigger_ids=[3703]) # WardropeInvisible
        self.set_ladder(trigger_ids=[540], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[541], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[542], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[543], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[544], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[545], visible=True, enable=True, fade=2) # Ladder


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3702], start_delay=100, fade=2.0) # Wardrope
        self.set_interact_object(trigger_ids=[10002044], state=1) # Wardrope

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002044], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3702], visible=True) # Wardrope


initial_state = Wait
