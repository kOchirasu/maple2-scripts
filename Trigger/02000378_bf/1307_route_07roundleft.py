""" trigger/02000378_bf/1307_route_07roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[18071], visible=True)
        self.set_agent(trigger_ids=[18072], visible=True)
        self.set_agent(trigger_ids=[18073], visible=True)
        self.set_agent(trigger_ids=[18074], visible=True)
        self.set_effect(trigger_ids=[5007]) # 07Round_BridgeApp
        self.set_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721]) # Fake
        self.set_mesh(trigger_ids=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721]) # Real
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
        self.set_random_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], start_delay=22) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], start_delay=22) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007], visible=True) # 07Round_BridgeApp
        self.set_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721], visible=True, start_delay=22, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18071])
        self.set_agent(trigger_ids=[18072])
        self.set_agent(trigger_ids=[18073])
        self.set_agent(trigger_ids=[18074])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
