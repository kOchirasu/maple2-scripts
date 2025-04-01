""" trigger/02000397_bf/3600_hidden_woodbox.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003]) # PortalOn
        self.set_ladder(trigger_ids=[530]) # Ladder
        self.set_ladder(trigger_ids=[531]) # Ladder
        self.set_ladder(trigger_ids=[532]) # Ladder
        self.set_ladder(trigger_ids=[533]) # Ladder
        self.set_ladder(trigger_ids=[534]) # Ladder
        self.set_ladder(trigger_ids=[535]) # Ladder
        self.set_mesh(trigger_ids=[3600], visible=True) # Wall_BehindWoodBox
        self.set_mesh(trigger_ids=[3601], visible=True) # BehindWoodBoxCover
        self.set_mesh(trigger_ids=[3602], visible=True) # WoodBox
        self.set_mesh(trigger_ids=[3603], visible=True) # WoodBoxInvisible
        self.set_interact_object(trigger_ids=[10001145], state=0) # WoodBox
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen') == 1:
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen') == 2:
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], start_delay=100, fade=2.0) # WoodBox
        self.set_interact_object(trigger_ids=[10001145], state=1) # WoodBox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001145], state=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # PortalOn
        self.set_mesh(trigger_ids=[3600], fade=3.0) # Wall_BehindWoodBox
        self.set_mesh(trigger_ids=[3601], fade=3.0) # BehindWoodBoxCover
        self.set_mesh(trigger_ids=[3603]) # WoodBoxInvisible
        self.set_ladder(trigger_ids=[530], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[531], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[532], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[533], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[534], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[535], visible=True, enable=True, fade=2) # Ladder


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], start_delay=100, fade=2.0) # WoodBox
        self.set_interact_object(trigger_ids=[10001145], state=1) # WoodBox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001145], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], visible=True) # WoodBox


initial_state = Wait
