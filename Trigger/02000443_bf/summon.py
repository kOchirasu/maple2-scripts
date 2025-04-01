""" trigger/02000443_bf/summon.xml """
import trigger_api


class special_1_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='special_1') == 1:
            return special_1_2(self.ctx)


class special_1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return special_2_1(self.ctx)


class special_2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='special_2') == 1:
            return special_2_2(self.ctx)


class special_2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return special_3_1(self.ctx)


class special_3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='special_3') == 1:
            return special_3_2(self.ctx)


class special_3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return special_4_1(self.ctx)


class special_4_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='special_4') == 1:
            return special_4_2(self.ctx)


class special_4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return special_5_1(self.ctx)


class special_5_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='special_5') == 1:
            return special_5_2(self.ctx)


class special_5_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            pass


initial_state = special_1_1
