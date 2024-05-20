""" trigger/80000013_bonus/mob_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return wait(self.ctx)


class wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[701]):
            return start(self.ctx)
        if self.wait_tick(wait_tick=1500):
            return idle(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
