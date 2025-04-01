""" trigger/02000378_bf/1308_route_08roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[18081], visible=True)
        self.set_agent(trigger_ids=[18082], visible=True)
        self.set_agent(trigger_ids=[18083], visible=True)
        self.set_agent(trigger_ids=[18084], visible=True)
        self.set_effect(trigger_ids=[5008]) # 08Round_BridgeApp
        self.set_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819]) # Fake
        self.set_mesh(trigger_ids=[330800,330801,330802,330803,330804,330805,330806,330807,330808,330809,330810,330811,330812,330813,330814,330815,330816,330817,330818,330819]) # Real
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
        self.set_random_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], start_delay=20) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') == 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') == 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], start_delay=20) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5008], visible=True) # 08Round_BridgeApp
        self.set_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], fade=5.0) # Fake
        self.set_random_mesh(trigger_ids=[330800,330801,330802,330803,330804,330805,330806,330807,330808,330809,330810,330811,330812,330813,330814,330815,330816,330817,330818,330819], visible=True, start_delay=20, interval=100, fade=50) # Real
        self.set_agent(trigger_ids=[18081])
        self.set_agent(trigger_ids=[18082])
        self.set_agent(trigger_ids=[18083])
        self.set_agent(trigger_ids=[18084])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], fade=5.0) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
