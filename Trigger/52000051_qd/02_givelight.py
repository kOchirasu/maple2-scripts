""" trigger/52000051_qd/02_givelight.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001022], state=0) # Lotus
        self.set_user_value(key='InnerLight', value=0)
        self.set_user_value(key='InactivateLotus', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='InnerLight') == 1:
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001022], state=1) # Lotus

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001022], state=0):
            return GiveLight01(self.ctx)
        if self.user_value(key='InactivateLotus') == 1:
            return Wait(self.ctx)


class GiveLight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9100], skill_id=70000102, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Delay01(self.ctx)
        if self.user_value(key='InactivateLotus') == 1:
            return Wait(self.ctx)


initial_state = Wait
