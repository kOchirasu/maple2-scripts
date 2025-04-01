""" trigger/02000382_bf/04_breakwall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000]) # CubeBreak
        self.set_user_value(key='BossKill', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return BreakWall(self.ctx)
        if self.user_value(key='BossKill') == 1:
            return BreakWall(self.ctx)


class BreakWall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000], enable=True) # CubeBreak


initial_state = Wait
