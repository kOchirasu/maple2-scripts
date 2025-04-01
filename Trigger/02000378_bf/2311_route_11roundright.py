""" trigger/02000378_bf/2311_route_11roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_mesh(trigger_ids=[4010], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[28111], visible=True)
        self.set_agent(trigger_ids=[28112], visible=True)
        self.set_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111]) # Fake
        self.set_mesh(trigger_ids=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], start_delay=12) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], start_delay=12) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011], visible=True) # 11Round_BridgeApp
        self.set_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111], visible=True, start_delay=12, fade=50) # Real
        self.set_agent(trigger_ids=[28111])
        self.set_agent(trigger_ids=[28112])
        self.set_portal(portal_id=10, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4010]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
