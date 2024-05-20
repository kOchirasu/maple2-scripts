""" trigger/02000248_bf/trigger_02.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[2101,2102,2103,2104,2105], is_visible=True)


class objectset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[2101,2102,2103,2104,2105], random_count=1, is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return WaitTick(self.ctx)


class WaitTick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return objectset(self.ctx)


initial_state = ready
