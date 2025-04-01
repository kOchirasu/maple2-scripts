""" trigger/02000378_bf/2304_route_04roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[28041], visible=True)
        self.set_agent(trigger_ids=[28042], visible=True)
        self.set_agent(trigger_ids=[28043], visible=True)
        self.set_agent(trigger_ids=[28044], visible=True)
        self.set_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419]) # Fake
        self.set_mesh(trigger_ids=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True) # 04Round_BridgeApp
        self.set_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419], visible=True, start_delay=20, fade=50) # Real
        self.set_agent(trigger_ids=[28041])
        self.set_agent(trigger_ids=[28042])
        self.set_agent(trigger_ids=[28043])
        self.set_agent(trigger_ids=[28044])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
