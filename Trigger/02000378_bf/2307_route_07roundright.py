""" trigger/02000378_bf/2307_route_07roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[28071], visible=True)
        self.set_agent(trigger_ids=[28072], visible=True)
        self.set_agent(trigger_ids=[28073], visible=True)
        self.set_agent(trigger_ids=[28074], visible=True)
        self.set_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719]) # Fake
        self.set_mesh(trigger_ids=[430700,430701,430702,430703,430704,430705,430706,430707,430708,430709,430710,430711,430712,430713,430714,430715,430716,430717,430718,430719]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007], visible=True) # 07Round_BridgeApp
        self.set_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430700,430701,430702,430703,430704,430705,430706,430707,430708,430709,430710,430711,430712,430713,430714,430715,430716,430717,430718,430719], visible=True, start_delay=20, fade=50) # Real
        self.set_agent(trigger_ids=[28071])
        self.set_agent(trigger_ids=[28072])
        self.set_agent(trigger_ids=[28073])
        self.set_agent(trigger_ids=[28074])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
