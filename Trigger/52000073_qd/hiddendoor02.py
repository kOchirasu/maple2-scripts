""" trigger/52000073_qd/hiddendoor02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Closed') # HiddenDoor
        self.set_mesh(trigger_ids=[2000], visible=True) # Wall
        self.set_breakable(trigger_ids=[4000]) # Move
        self.set_visible_breakable_object(trigger_ids=[4000]) # Move
        self.set_interact_object(trigger_ids=[10001082], state=1) # BookCase
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001082], state=0):
            return BookCaseMove01(self.ctx)


class BookCaseMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000], enable=True) # Move
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True) # Move
        self.set_mesh(trigger_ids=[2000], fade=3.0) # Wall

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DoorOpen01(self.ctx)


class DoorOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Opened') # HiddenDoor
        self.set_portal(portal_id=2, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DoorOpen02(self.ctx)


class DoorOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=57000):
            return DoorClose01(self.ctx)


class DoorClose01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Closed') # HiddenDoor
        self.set_portal(portal_id=2, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DoorClose02(self.ctx)


class DoorClose02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000]) # Move
        self.set_visible_breakable_object(trigger_ids=[4000]) # Move
        self.set_mesh(trigger_ids=[2000], visible=True, fade=3.0) # Wall
        self.set_interact_object(trigger_ids=[10001082], state=1) # BookCase
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001082], state=0):
            return BookCaseMove01(self.ctx)


initial_state = Wait
