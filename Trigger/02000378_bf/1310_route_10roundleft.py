""" trigger/02000378_bf/1310_route_10roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=17)
        self.set_mesh(trigger_ids=[4017], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[18101], visible=True)
        self.set_agent(trigger_ids=[18102], visible=True)
        self.set_effect(trigger_ids=[5010]) # 10Round_BridgeApp
        self.set_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011]) # Fake
        self.set_mesh(trigger_ids=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011]) # Real
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
        self.set_random_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], start_delay=12) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], start_delay=12) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5010], visible=True) # 10Round_BridgeApp
        self.set_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011], visible=True, start_delay=12, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18101])
        self.set_agent(trigger_ids=[18102])
        self.set_portal(portal_id=17, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4017]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
