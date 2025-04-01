""" trigger/66200001_gd/sensor_9140.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box14Check', value=10)
        self.set_mesh(trigger_ids=[514], visible=True) # 14 / Ground outter
        self.set_mesh(trigger_ids=[5140], visible=True) # 14 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box14Check') == 0:
            return Sensor0(self.ctx)
        if self.user_value(key='Box14Check') == 1:
            return Sensor1(self.ctx)
        if self.user_value(key='Box14Check') == 2:
            return Sensor2(self.ctx)
        if self.user_value(key='Box14Check') == 3:
            return Sensor3(self.ctx)
        if self.user_value(key='Box14Check') == 4:
            return Sensor4(self.ctx)
        if self.user_value(key='Box14Check') == 5:
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 1:
            return Pass(self.ctx)
        if self.count_users(box_id=9140) != 1:
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 2:
            return Pass(self.ctx)
        if self.count_users(box_id=9140) != 2:
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 3:
            return Pass(self.ctx)
        if self.count_users(box_id=9140) != 3:
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 4:
            return Pass(self.ctx)
        if self.count_users(box_id=9140) != 4:
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 5:
            return Pass(self.ctx)
        if self.count_users(box_id=9140) != 5:
            return Fail(self.ctx)


class Pass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Pass_01')
        self.set_mesh(trigger_ids=[514], fade=2.0) # 14 / Ground outter
        self.set_user_value(trigger_id=7140, key='ColorReset', value=1) # color reset

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[514], fade=2.0) # 14 / Ground outter
        self.set_mesh(trigger_ids=[5140]) # 14 / Ground inner
        self.set_user_value(trigger_id=7140, key='ColorClear', value=1) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box14Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
