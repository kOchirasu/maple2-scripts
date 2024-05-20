""" trigger/99999911/fail.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=1, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return fail_random(self.ctx)


class fail_random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return fail_01(self.ctx)
        if self.random_condition(weight=1.0):
            return fail_02(self.ctx)
        if self.random_condition(weight=1.0):
            return fail_03(self.ctx)
        if self.random_condition(weight=1.0):
            return fail_04(self.ctx)
        if self.random_condition(weight=5.0):
            return fail_04(self.ctx)


class fail_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=1, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


class fail_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=2, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


class fail_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=3, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


class fail_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=4, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


class fail_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999911, portal_id=5, box_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


initial_state = idle
