""" trigger/02100001_bf/1212_flyaway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='FlyAway', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FlyAway') == 1:
            return FlyAway(self.ctx)


class FlyAway(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=212, to_spawn_id=1212)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1212])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
