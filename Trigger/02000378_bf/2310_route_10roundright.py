""" trigger/02000378_bf/2310_route_10roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=18)
        self.set_mesh(trigger_ids=[4018], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[28101], visible=True)
        self.set_agent(trigger_ids=[28102], visible=True)
        self.set_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011]) # Fake
        self.set_mesh(trigger_ids=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], start_delay=12) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], start_delay=12) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5010], visible=True) # 10Round_BridgeApp
        self.set_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011], visible=True, start_delay=12, fade=50) # Real
        self.set_agent(trigger_ids=[28101])
        self.set_agent(trigger_ids=[28102])
        self.set_portal(portal_id=18, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4018]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
