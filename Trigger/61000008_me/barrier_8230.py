""" trigger/61000008_me/barrier_8230.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=2) # On
        self.set_interact_object(trigger_ids=[10000960], state=2) # Off

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
        if self.user_value(key='Barrier23') == 7:
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 8:
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 9:
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 6:
            # 10
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 15:
            # 15
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 20:
            # 20
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 25:
            # 25
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 30:
            # 30
            return Sensor72330(self.ctx)


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
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

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
            return Enable7232(self.ctx)
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7232(self.ctx)


class Delay7232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 2:
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

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
            return Enable7233(self.ctx)
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7233(self.ctx)


class Delay7233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 3:
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

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
            return Enable7234(self.ctx)
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7234(self.ctx)


class Delay7234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 4:
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

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
            return Enable7235(self.ctx)
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
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
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7235(self.ctx)


class Delay7235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 5:
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
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


# 7명
class Sensor7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 7:
            return SafeGreen7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 7:
            return Enable7237(self.ctx)
        if self.count_users(box_id=9230) != 7:
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate7237(self.ctx)
        if self.count_users(box_id=9230) != 7:
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 7:
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7237(self.ctx)


class Delay7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 7:
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate7237(self.ctx)


class DeActivate7237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 8명
class Sensor7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 8:
            return SafeGreen7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 8:
            return Enable7238(self.ctx)
        if self.count_users(box_id=9230) != 8:
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate7238(self.ctx)
        if self.count_users(box_id=9230) != 8:
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 8:
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7238(self.ctx)


class Delay7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 8:
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate7238(self.ctx)


class DeActivate7238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 9명
class Sensor7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 9:
            return SafeGreen7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 9:
            return Enable7239(self.ctx)
        if self.count_users(box_id=9230) != 9:
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate7239(self.ctx)
        if self.count_users(box_id=9230) != 9:
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 9:
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7239(self.ctx)


class Delay7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 9:
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate7239(self.ctx)


class DeActivate7239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 10명
class Sensor7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 10:
            return SafeGreen7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 10:
            return Enable7236(self.ctx)
        if self.count_users(box_id=9230) != 10:
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate7236(self.ctx)
        if self.count_users(box_id=9230) != 10:
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 10:
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7236(self.ctx)


class Delay7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 10:
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate7236(self.ctx)


class DeActivate7236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 15명
class Sensor72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 15:
            return SafeGreen72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 15:
            return Enable72315(self.ctx)
        if self.count_users(box_id=9230) != 15:
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate72315(self.ctx)
        if self.count_users(box_id=9230) != 15:
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 15:
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72315(self.ctx)


class Delay72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 15:
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate72315(self.ctx)


class DeActivate72315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 20명
class Sensor72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 20:
            return SafeGreen72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 20:
            return Enable72320(self.ctx)
        if self.count_users(box_id=9230) != 20:
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate72320(self.ctx)
        if self.count_users(box_id=9230) != 20:
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 20:
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72320(self.ctx)


class Delay72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 20:
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate72320(self.ctx)


class DeActivate72320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 25명
class Sensor72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 25:
            return SafeGreen72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 25:
            return Enable72325(self.ctx)
        if self.count_users(box_id=9230) != 25:
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate72325(self.ctx)
        if self.count_users(box_id=9230) != 25:
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 25:
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72325(self.ctx)


class Delay72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 25:
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate72325(self.ctx)


class DeActivate72325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


# 30명
class Sensor72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=3) # red
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 30:
            return SafeGreen72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class SafeGreen72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) == 30:
            return Enable72330(self.ctx)
        if self.count_users(box_id=9230) != 30:
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Enable72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000944], state=0):
            # On
            return Activate72330(self.ctx)
        if self.count_users(box_id=9230) != 30:
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Activate72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230], visible=True)
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True)
        self.set_interact_object(trigger_ids=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 30:
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72330(self.ctx)


class Delay72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230) != 30:
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000960], state=0):
            # Off
            return DeActivate72330(self.ctx)


class DeActivate72330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8230])
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8231,8232,8233,8234,8235,8236,8237,8238])
        self.set_effect(trigger_ids=[8230])
        self.set_interact_object(trigger_ids=[10000944], state=0) # On
        self.set_interact_object(trigger_ids=[10000960], state=0) # Off
        self.set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
