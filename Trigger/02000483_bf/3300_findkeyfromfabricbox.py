""" trigger/02000483_bf/3300_findkeyfromfabricbox.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300]) # FindKeyFromFabricbox
        self.set_mesh(trigger_ids=[3301], visible=True) # Fabricbox
        self.set_interact_object(trigger_ids=[10002040], state=0) # Fabricbox
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindKey') == 1:
            return StateTrue(self.ctx)
        if self.user_value(key='FindKey') == 2:
            return StateFalse(self.ctx)


class StateTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301], start_delay=100, fade=2.0) # Fabricbox
        self.set_interact_object(trigger_ids=[10002040], state=1) # Fabricbox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002040], state=0):
            return KeyFound(self.ctx)


class KeyFound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300], visible=True, fade=2.0) # FindKeyFromFabricbox
        self.set_user_value(trigger_id=1, key='PortalOn', value=1)


class StateFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002040], state=1) # Fabricbox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002040], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301], visible=True) # Fabricbox


initial_state = Wait
