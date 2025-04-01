""" trigger/02000207_bf/arm06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumArmDeath06') == 1:
            return 트로피지급(self.ctx)


class 트로피지급(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='ZakumArmDeath06')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
