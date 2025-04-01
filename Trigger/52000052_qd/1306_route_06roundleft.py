""" trigger/52000052_qd/1306_route_06roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=13)
        self.set_mesh(trigger_ids=[4013], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[18061], visible=True)
        self.set_agent(trigger_ids=[18062], visible=True)
        self.set_effect(trigger_ids=[5006]) # 06Round_BridgeApp
        self.set_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625]) # Fake
        self.set_mesh(trigger_ids=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625]) # Real
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
        self.set_random_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], start_delay=26) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], start_delay=26) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5006], visible=True) # 06Round_BridgeApp
        self.set_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625], visible=True, start_delay=26, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18061])
        self.set_agent(trigger_ids=[18062])
        self.set_portal(portal_id=13, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4013]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
