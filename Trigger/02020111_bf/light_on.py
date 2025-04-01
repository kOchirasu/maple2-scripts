""" trigger/02020111_bf/light_on.xml """
import trigger_api
from System.Numerics import Vector3


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Light_On_1') == 2 and self.user_value(key='Light_On_2') == 2 and self.user_value(key='Light_On_3') == 2 and self.user_value(key='Light_On_4') == 2:
            return 대기(self.ctx)
        if self.user_value(key='Light_On_1') == 1 and self.user_value(key='Light_On_2') == 1 and self.user_value(key='Light_On_3') == 1 and self.user_value(key='Light_On_4') == 1:
            return 시작(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라이트_변경(self.ctx)


class 라이트_변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Light_On_1') == 1 and self.user_value(key='Light_On_2') == 1 and self.user_value(key='Light_On_3') == 1 and self.user_value(key='Light_On_4') == 1:
            return 시작(self.ctx)


initial_state = 시작
