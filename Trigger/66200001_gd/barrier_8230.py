""" trigger/66200001_gd/barrier_8230.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=2) # On
        self.set_interact_object(trigger_ids=[10001207], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier23') == 1:
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23') == 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 5:
            return Sensor7235(self.ctx)


# 1명 방어 불가
class Sensor7231(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 1:
            return Activate7231(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7231(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 1:
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=1) # yellow
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=0) # On
        self.set_interact_object(trigger_ids=[10001207], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 2:
            return SafeGreen7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 2:
            return CheckSameUserTag7232(self.ctx)
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7232(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9230) and self.count_users(box_id=9230) == 2:
            return Enable7232(self.ctx)
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if not self.check_same_user_tag(box_id=9230):
            return SafeGreen7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001191], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001191], state=0):
            # On
            return Activate7232(self.ctx)
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10001191], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7232(self.ctx)


class Delay7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001207], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001207], state=0):
            # Off
            return DeActivate7232(self.ctx)


class DeActivate7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=1) # yellow
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=0) # On
        self.set_interact_object(trigger_ids=[10001207], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 3:
            return SafeGreen7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 3:
            return CheckSameUserTag7233(self.ctx)
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7233(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9230) and self.count_users(box_id=9230) == 3:
            return Enable7233(self.ctx)
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if not self.check_same_user_tag(box_id=9230):
            return SafeGreen7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001191], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001191], state=0):
            # On
            return Activate7233(self.ctx)
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10001191], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7233(self.ctx)


class Delay7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001207], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001207], state=0):
            # Off
            return DeActivate7233(self.ctx)


class DeActivate7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=1) # yellow
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=0) # On
        self.set_interact_object(trigger_ids=[10001207], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 4:
            return SafeGreen7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 4:
            return CheckSameUserTag7234(self.ctx)
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7234(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9230) and self.count_users(box_id=9230) == 4:
            return Enable7234(self.ctx)
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if not self.check_same_user_tag(box_id=9230):
            return SafeGreen7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001191], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001191], state=0):
            # On
            return Activate7234(self.ctx)
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10001191], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7234(self.ctx)


class Delay7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001207], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001207], state=0):
            # Off
            return DeActivate7234(self.ctx)


class DeActivate7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=1) # yellow
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=0) # On
        self.set_interact_object(trigger_ids=[10001207], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 5:
            return SafeGreen7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 5:
            return CheckSameUserTag7235(self.ctx)
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7235(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9230) and self.count_users(box_id=9230) == 5:
            return Enable7235(self.ctx)
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if not self.check_same_user_tag(box_id=9230):
            return SafeGreen7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001191], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001191], state=0):
            # On
            return Activate7235(self.ctx)
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10001191], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7235(self.ctx)


class Delay7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001207], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001207], state=0):
            # Off
            return DeActivate7235(self.ctx)


class DeActivate7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10001191], state=0) # On
        self.set_interact_object(trigger_ids=[10001207], state=0) # Off
        self.set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
