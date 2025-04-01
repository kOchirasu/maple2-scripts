""" trigger/02000312_bf/filter_10.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='1stTreeRemove', value=0)
        self.set_user_value(key='2ndTreeRemove', value=0)
        self.set_user_value(key='3rdTreeRemove', value=0)
        self.set_user_value(key='4thTreeRemove', value=0)
        self.set_user_value(key='5thTreeRemove', value=0)
        self.set_user_value(key='6thTreeRemove', value=0)
        self.set_user_value(key='7thTreeRemove', value=0)
        self.set_user_value(key='8thTreeRemove', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return CheckStart(self.ctx)


# 제거된 씨앗 체크
class CheckStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Check01(self.ctx)


class Check01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='1stTreeRemove') == 1:
            return Check02(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2ndTreeRemove') == 1:
            return Check03(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='3rdTreeRemove') == 1:
            return Check04(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='4thTreeRemove') == 1:
            return Check05(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='5thTreeRemove') == 1:
            return Check06(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='6thTreeRemove') == 1:
            return Check07(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='7thTreeRemove') == 1:
            return Check08(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class Check08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='8thTreeRemove') == 1:
            return BoardApp(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return CheckStart(self.ctx)


class BoardApp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='BoardApp', value=1)
        self.set_user_value(trigger_id=11, key='MobWaveStop', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
