""" trigger/02000378_bf/2302_route_02roundback.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[28021], visible=True)
        self.set_agent(trigger_ids=[28022], visible=True)
        self.set_agent(trigger_ids=[28023], visible=True)
        self.set_agent(trigger_ids=[28024], visible=True)
        self.set_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219]) # Fake
        self.set_mesh(trigger_ids=[430200,430201,430202,430203,430204,430205,430206,430207,430208,430209,430210,430211,430212,430213,430214,430215,430216,430217,430218,430219]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 02Round_BridgeApp
        self.set_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430200,430201,430202,430203,430204,430205,430206,430207,430208,430209,430210,430211,430212,430213,430214,430215,430216,430217,430218,430219], visible=True, start_delay=20, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[28021])
        self.set_agent(trigger_ids=[28022])
        self.set_agent(trigger_ids=[28023])
        self.set_agent(trigger_ids=[28024])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
