""" trigger/02000378_bf/1304_route_04roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[18041], visible=True)
        self.set_agent(trigger_ids=[18042], visible=True)
        self.set_agent(trigger_ids=[18043], visible=True)
        self.set_agent(trigger_ids=[18044], visible=True)
        self.set_effect(trigger_ids=[5004]) # 04Round_BridgeApp
        self.set_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419]) # Fake
        self.set_mesh(trigger_ids=[330400,330401,330402,330403,330404,330405,330406,330407,330408,330409,330410,330411,330412,330413,330414,330415,330416,330417,330418,330419]) # Real
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
        self.set_random_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True) # 04Round_BridgeApp
        self.set_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330400,330401,330402,330403,330404,330405,330406,330407,330408,330409,330410,330411,330412,330413,330414,330415,330416,330417,330418,330419], visible=True, start_delay=20, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18041])
        self.set_agent(trigger_ids=[18042])
        self.set_agent(trigger_ids=[18043])
        self.set_agent(trigger_ids=[18044])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
