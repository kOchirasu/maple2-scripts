""" trigger/52000066_qd/rockdrop_14.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8008])
        self.set_skill(trigger_ids=[8009])
        self.set_skill(trigger_ids=[8010])
        self.set_effect(trigger_ids=[7008]) # RockDrop
        self.set_effect(trigger_ids=[7009]) # RockDrop
        self.set_effect(trigger_ids=[7010]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RockDrop01(self.ctx)


class RockDrop01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7010], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop02(self.ctx)


class RockDrop02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8010], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return RockDrop11(self.ctx)


class RockDrop11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7009], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop12(self.ctx)


class RockDrop12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8009], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RockDrop21(self.ctx)


class RockDrop21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7008], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop22(self.ctx)


class RockDrop22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8008], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8008])
        self.set_skill(trigger_ids=[8009])
        self.set_skill(trigger_ids=[8010])
        self.set_effect(trigger_ids=[7008]) # RockDrop
        self.set_effect(trigger_ids=[7009]) # RockDrop
        self.set_effect(trigger_ids=[7010]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return RockDrop01(self.ctx)


initial_state = Wait
