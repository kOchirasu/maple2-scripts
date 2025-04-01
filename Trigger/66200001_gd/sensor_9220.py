""" trigger/66200001_gd/sensor_9220.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box22Check', value=10)
        self.set_mesh(trigger_ids=[522], visible=True) # 22 / Ground outter
        self.set_mesh(trigger_ids=[5220], visible=True) # 22 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box22Check') == 0:
            return Sensor0(self.ctx)
        if self.user_value(key='Box22Check') == 1:
            return Sensor1(self.ctx)
        if self.user_value(key='Box22Check') == 2:
            return Sensor2(self.ctx)
        if self.user_value(key='Box22Check') == 3:
            return Sensor3(self.ctx)
        if self.user_value(key='Box22Check') == 4:
            return Sensor4(self.ctx)
        if self.user_value(key='Box22Check') == 5:
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 1:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9220) != 1:
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 2:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9220) != 2:
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 3:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9220) != 3:
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 4:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9220) != 4:
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 5:
            return NormalPass(self.ctx)
        if self.count_users(box_id=9220) != 5:
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Pass_01')
        self.set_mesh(trigger_ids=[522], fade=2.0) # 22 / Ground outter
        self.set_user_value(trigger_id=7220, key='ColorReset', value=1) # color reset

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[522], fade=2.0) # 22 / Ground outter
        self.set_mesh(trigger_ids=[5220]) # 22 / Ground inner
        self.set_user_value(trigger_id=7220, key='ColorClear', value=1) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box22Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
