""" trigger/02000378_bf/1305_route_05roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_mesh(trigger_ids=[4011], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[18051], visible=True)
        self.set_agent(trigger_ids=[18052], visible=True)
        self.set_effect(trigger_ids=[5005]) # 05Round_BridgeApp
        self.set_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519]) # Fake
        self.set_mesh(trigger_ids=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) >= 1:
            return StartDazzling01(self.ctx)


class StartDazzling01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True) # 05Round_BridgeApp
        self.set_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519], visible=True, start_delay=20, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18051])
        self.set_agent(trigger_ids=[18052])
        self.set_portal(portal_id=11, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4011]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
