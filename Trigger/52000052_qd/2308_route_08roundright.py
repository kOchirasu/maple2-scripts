""" trigger/52000052_qd/2308_route_08roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[28081], visible=True)
        self.set_agent(trigger_ids=[28082], visible=True)
        self.set_agent(trigger_ids=[28083], visible=True)
        self.set_agent(trigger_ids=[28084], visible=True)
        self.set_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821]) # Fake
        self.set_mesh(trigger_ids=[430800,430801,430802,430803,430804,430805,430806,430807,430808,430809,430810,430811,430812,430813,430814,430815,430816,430817,430818,430819,430820,430821]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], start_delay=22) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], start_delay=22) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5008], visible=True) # 08Round_BridgeApp
        self.set_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430800,430801,430802,430803,430804,430805,430806,430807,430808,430809,430810,430811,430812,430813,430814,430815,430816,430817,430818,430819,430820,430821], visible=True, start_delay=22, fade=50) # Real
        self.set_agent(trigger_ids=[28081])
        self.set_agent(trigger_ids=[28082])
        self.set_agent(trigger_ids=[28083])
        self.set_agent(trigger_ids=[28084])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
