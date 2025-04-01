""" trigger/02000378_bf/1311_route_11roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=19)
        self.set_mesh(trigger_ids=[4019], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[18111], visible=True)
        self.set_agent(trigger_ids=[18112], visible=True)
        self.set_effect(trigger_ids=[5011]) # 11Round_BridgeApp
        self.set_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109]) # Fake
        self.set_mesh(trigger_ids=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109]) # Real
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
        self.set_random_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, start_delay=3, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], start_delay=10) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, start_delay=3, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], start_delay=10) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011], visible=True) # 11Round_BridgeApp
        self.set_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109], visible=True, start_delay=10, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18111])
        self.set_agent(trigger_ids=[18112])
        self.set_portal(portal_id=19, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4019]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
