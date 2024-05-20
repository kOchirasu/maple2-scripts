""" trigger/82000012_survival/06_deathfromfall.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return WaitSomeoneFall(self.ctx)


class WaitSomeoneFall(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return KillSomeoneFall(self.ctx)


class KillSomeoneFall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9100], skill_id=70001061, level=1, is_player=False, is_skill_set=False) # 추락사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return KillSomeoneFall(self.ctx)
        if not self.user_detected(box_ids=[9100]):
            return WaitSomeoneFall(self.ctx)


initial_state = Setting
