""" trigger/02020310_bf/move_4.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Archeon4') == 1:
            self.set_user_value(trigger_id=900010, key='Archeon4', value=0)
            return Archeon_Ready(self.ctx)


class Archeon_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=10001, additional_effect_id=73000008, level=1):
            # self.move_user_path(patrol_name='MS2PatrolData_02')
            self.move_user_to_pos(pos=Vector3(8700,-4800,2750))
            return Archeon_On(self.ctx)


class Archeon_On(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


initial_state = 대기
