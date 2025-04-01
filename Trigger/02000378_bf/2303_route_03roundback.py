""" trigger/02000378_bf/2303_route_03roundback.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[28031], visible=True)
        self.set_agent(trigger_ids=[28032], visible=True)
        self.set_agent(trigger_ids=[28033], visible=True)
        self.set_agent(trigger_ids=[28034], visible=True)
        self.set_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319]) # Fake
        self.set_mesh(trigger_ids=[430300,430301,430302,430303,430304,430305,430306,430307,430308,430309,430310,430311,430312,430313,430314,430315,430316,430317,430318,430319]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # 03Round_BridgeApp
        self.set_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430300,430301,430302,430303,430304,430305,430306,430307,430308,430309,430310,430311,430312,430313,430314,430315,430316,430317,430318,430319], visible=True, start_delay=20, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[28031])
        self.set_agent(trigger_ids=[28032])
        self.set_agent(trigger_ids=[28033])
        self.set_agent(trigger_ids=[28034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
