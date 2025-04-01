""" trigger/61000022_me/color_7320.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Color32', value=10)
        self.set_mesh(trigger_ids=[832], visible=True) # yellow
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[1032]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorStart') == 1:
            return YellowBefore(self.ctx)
        if self.user_value(key='ColorStart') == 6:
            return RedBefore(self.ctx)


# Yellow Before
class YellowBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[832], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[1032]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32') == 3:
            return None # Missing State: YellowtoRed
        if self.user_value(key='Color32') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color32') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# Red Before
class RedBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1032], visible=True) # red
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[832]) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color32') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# Green After
class GreenAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[932], visible=True) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32') == 3:
            return RedAfter(self.ctx)
        if self.user_value(key='Color32') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color32') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# Yellow After
class YellowAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[832], visible=True, fade=2.0) # yellow
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[1032], start_delay=100) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32') == 3:
            return RedAfter(self.ctx)
        if self.user_value(key='Color32') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color32') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# Red After
class RedAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1032], visible=True) # red
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[832], start_delay=100) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 1:
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32') == 2:
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32') == 4:
            return Clear(self.ctx)
        if self.user_value(key='Color32') == 0:
            return Reset(self.ctx)
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# All Clear
class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[932], fade=2.0) # green
        self.set_mesh(trigger_ids=[832], fade=2.0) # yellow
        self.set_mesh(trigger_ids=[1032], fade=2.0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 5:
            return Regen(self.ctx)


# Regen
class Regen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_mesh(trigger_ids=[832], visible=True, start_delay=400) # yellow
        self.set_mesh(trigger_ids=[932]) # green
        self.set_mesh(trigger_ids=[1032]) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Color32') == 5:
            return Wait(self.ctx)


initial_state = Wait
