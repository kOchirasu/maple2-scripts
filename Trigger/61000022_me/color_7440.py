""" trigger/61000022_me/color_7440.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Color44', value=10)
        self.set_mesh(trigger_ids=[844], visible=True) # yellow
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[1044]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorStart') == 1:
            return YellowBefore(self.ctx)


# Yellow Before
class YellowBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[844], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[1044]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44') == 3:
            return None # Missing State: YellowtoRed
        if self.user_value(key='Color44') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color44') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# Red Before
class RedBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1044], visible=True) # red
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[844]) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color44') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# Green After
class GreenAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[944], visible=True) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44') == 3:
            return RedAfter(self.ctx)
        if self.user_value(key='Color44') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color44') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# Yellow After
class YellowAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[844], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[1044], start_delay=100) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44') == 3:
            return RedAfter(self.ctx)
        if self.user_value(key='Color44') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color44') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# Red After
class RedAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1044], visible=True) # red
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[844], start_delay=100) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color44') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# All Clear
class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[944], fade=2.0) # green
        self.set_mesh(trigger_ids=[844], fade=2.0) # yellow
        self.set_mesh(trigger_ids=[1044], fade=2.0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 5:
            return Regen(self.ctx)


# Regen
class Regen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_mesh(trigger_ids=[844], visible=True, start_delay=400) # yellow
        self.set_mesh(trigger_ids=[944]) # green
        self.set_mesh(trigger_ids=[1044]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color44') == 5:
            return Wait(self.ctx)


initial_state = Wait
