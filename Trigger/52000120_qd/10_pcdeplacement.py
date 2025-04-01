""" trigger/52000120_qd/10_pcdeplacement.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='DefencePhase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DefencePhase') == 1:
            return DefencePhase01(self.ctx)


class DefencePhase01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) >= 1:
            return MoveToTheWall(self.ctx)
        if self.user_value(key='DefencePhase') == 2:
            return DefencePhase02(self.ctx)


class MoveToTheWall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000120, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DefencePhase01(self.ctx)
        if self.user_value(key='DefencePhase') == 2:
            return DefencePhase02(self.ctx)


class DefencePhase02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) >= 1:
            return OutsideOfTheWall(self.ctx)
        if self.user_value(key='DefencePhase') == 3:
            return Quit(self.ctx)


class OutsideOfTheWall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000120, portal_id=40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DefencePhase02(self.ctx)
        if self.user_value(key='DefencePhase') == 3:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
