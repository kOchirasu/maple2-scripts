""" trigger/02000378_bf/1303_route_03roundfront.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[18031], visible=True)
        self.set_agent(trigger_ids=[18032], visible=True)
        self.set_agent(trigger_ids=[18033], visible=True)
        self.set_agent(trigger_ids=[18034], visible=True)
        self.set_effect(trigger_ids=[5003]) # 03Round_BridgeApp
        self.set_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321]) # Fake
        self.set_mesh(trigger_ids=[330300,330301,330302,330303,330304,330305,330306,330307,330308,330309,330310,330311,330312,330313,330314,330315,330316,330317,330318,330319,330320,330321]) # Real
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
        self.set_random_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], start_delay=22) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], start_delay=22) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # 03Round_BridgeApp
        self.set_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330300,330301,330302,330303,330304,330305,330306,330307,330308,330309,330310,330311,330312,330313,330314,330315,330316,330317,330318,330319,330320,330321], visible=True, start_delay=22, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18031])
        self.set_agent(trigger_ids=[18032])
        self.set_agent(trigger_ids=[18033])
        self.set_agent(trigger_ids=[18034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
