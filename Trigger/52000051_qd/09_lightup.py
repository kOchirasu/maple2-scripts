""" trigger/52000051_qd/09_lightup.xml """
import trigger_api
from System.Numerics import Vector3


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindLotus') == 1:
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LightOff01(self.ctx)


class LightOff01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9200, spawn_ids=[900]):
            return LightOff02(self.ctx)
        if not self.npc_detected(box_id=9200, spawn_ids=[900]):
            return RemoveTotem01(self.ctx)


class LightOff02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='InnerLight', value=1)
        self.set_user_value(trigger_id=3, key='ResetInnerLight', value=1)
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_directional_light(diffuse_color=Vector3(0,0,0))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LoadingDelay(self.ctx)


class RemoveTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3, key='RemoveInnerLight', value=1)
        self.set_user_value(trigger_id=2, key='InactivateLotus', value=1)
        self.set_ambient_light(primary=Vector3(96,160,157))
        self.set_directional_light(diffuse_color=Vector3(193,180,137), specular_color=Vector3(100,100,100))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LoadingDelay(self.ctx)


initial_state = Wait
