""" trigger/02020068_bf/missiontypemonster_spawn.xml """
import trigger_api


class 루프1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.start_combine_spawn(group_id=[521], is_start=True)
            return 루프2(self.ctx)


class 루프2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150000):
            return 루프3(self.ctx)


class 루프3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150000):
            return 루프2(self.ctx)


initial_state = 루프1
