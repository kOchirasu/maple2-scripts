""" trigger/02000378_bf/2305_route_05roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=12)
        self.set_mesh(trigger_ids=[4012], visible=True) # PortalBarrier
        self.set_agent(trigger_ids=[28051], visible=True)
        self.set_agent(trigger_ids=[28052], visible=True)
        self.set_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525]) # Fake
        self.set_mesh(trigger_ids=[430500,430501,430502,430503,430504,430505,430506,430507,430508,430509,430510,430511,430512,430513,430514,430515,430516,430517,430518,430519,430520,430521,430522,430523,430524,430525]) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') == 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], start_delay=26) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], visible=True, start_delay=7, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], start_delay=26) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True) # 05Round_BridgeApp
        self.set_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[430500,430501,430502,430503,430504,430505,430506,430507,430508,430509,430510,430511,430512,430513,430514,430515,430516,430517,430518,430519,430520,430521,430522,430523,430524,430525], visible=True, start_delay=26, fade=50) # Real
        self.set_agent(trigger_ids=[28051])
        self.set_agent(trigger_ids=[28052])
        self.set_portal(portal_id=12, visible=True, enable=True)
        self.set_mesh(trigger_ids=[4012]) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230500,230501,230502,230503,230504,230505,230506,230507,230508,230509,230510,230511,230512,230513,230514,230515,230516,230517,230518,230519,230520,230521,230522,230523,230524,230525], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
