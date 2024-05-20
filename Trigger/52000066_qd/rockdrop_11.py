""" trigger/52000066_qd/rockdrop_11.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8002])
        self.set_skill(trigger_ids=[8003])
        self.set_effect(trigger_ids=[7002]) # RockDrop
        self.set_effect(trigger_ids=[7003]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return RockDrop01(self.ctx)


class RockDrop01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop02(self.ctx)


class RockDrop02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return RockDrop11(self.ctx)


class RockDrop11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop12(self.ctx)


class RockDrop12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8003], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RockDrop21(self.ctx)


class RockDrop21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return RockDrop22(self.ctx)


class RockDrop22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8002])
        self.set_skill(trigger_ids=[8003])
        self.set_effect(trigger_ids=[7002]) # RockDrop
        self.set_effect(trigger_ids=[7003]) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RockDrop01(self.ctx)


initial_state = Wait
