""" trigger/52000052_qd/1309_route_09roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=15)
        self.set_mesh(trigger_ids=[4015], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[18091], visible=True)
        self.set_agent(trigger_ids=[18092], visible=True)
        self.set_effect(trigger_ids=[5009]) # 09Round_BridgeApp
        self.set_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911]) # Fake
        self.set_mesh(trigger_ids=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911]) # Real
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
        self.set_random_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], start_delay=12) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, start_delay=4, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], start_delay=12) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5009], visible=True) # 09Round_BridgeApp
        self.set_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911], visible=True, start_delay=12, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18091])
        self.set_agent(trigger_ids=[18092])
        self.set_portal(portal_id=15, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4015]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
