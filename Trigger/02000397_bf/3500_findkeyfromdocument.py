""" trigger/02000397_bf/3500_findkeyfromdocument.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3500]) # FindKeyFromDocument
        self.set_mesh(trigger_ids=[3501], visible=True) # Document
        self.set_interact_object(trigger_ids=[10001144], state=0) # Document
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindKey') == 1:
            return StateTrue(self.ctx)
        if self.user_value(key='FindKey') == 2:
            return StateFalse(self.ctx)


class StateTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3501], start_delay=100, fade=2.0) # Document
        self.set_interact_object(trigger_ids=[10001144], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001144], state=0):
            return KeyFound(self.ctx)


class KeyFound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3500], visible=True, fade=2.0) # FindKeyFromDocument
        self.set_user_value(trigger_id=1, key='PortalOn', value=1)


class StateFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001144], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001144], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3501], visible=True) # Document


initial_state = Wait
