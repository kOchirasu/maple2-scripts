""" trigger/61000008_me/barrier_8330.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=2) # On
        self.set_interact_object(trigger_ids=[10000964], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier33') == 1:
            return Sensor7331(self.ctx)
        if self.user_value(key='Barrier33') == 2:
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 3:
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 4:
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 5:
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 7:
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 8:
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 9:
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 6:
            # 10
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 15:
            # 15
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 20:
            # 20
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 25:
            # 25
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 30:
            # 30
            return Sensor73330(self.ctx)


# 1명 방어 불가
class Sensor7331(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 1:
            return Activate7331(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7331(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 1:
            return Sensor7331(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 2:
            return SafeGreen7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 2:
            return Enable7332(self.ctx)
        if self.count_users(box_id=9330) != 2:
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7332(self.ctx)
        if self.count_users(box_id=9330) != 2:
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 2:
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7332(self.ctx)


class Delay7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 2:
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7332(self.ctx)


class DeActivate7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 3:
            return SafeGreen7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 3:
            return Enable7333(self.ctx)
        if self.count_users(box_id=9330) != 3:
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7333(self.ctx)
        if self.count_users(box_id=9330) != 3:
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 3:
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7333(self.ctx)


class Delay7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 3:
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7333(self.ctx)


class DeActivate7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 4:
            return SafeGreen7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 4:
            return Enable7334(self.ctx)
        if self.count_users(box_id=9330) != 4:
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7334(self.ctx)
        if self.count_users(box_id=9330) != 4:
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 4:
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7334(self.ctx)


class Delay7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 4:
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7334(self.ctx)


class DeActivate7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 5:
            return SafeGreen7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 5:
            return Enable7335(self.ctx)
        if self.count_users(box_id=9330) != 5:
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7335(self.ctx)
        if self.count_users(box_id=9330) != 5:
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 5:
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7335(self.ctx)


class Delay7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 5:
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7335(self.ctx)


class DeActivate7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 7명
class Sensor7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 7:
            return SafeGreen7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 7:
            return Enable7337(self.ctx)
        if self.count_users(box_id=9330) != 7:
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7337(self.ctx)
        if self.count_users(box_id=9330) != 7:
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 7:
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7337(self.ctx)


class Delay7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 7:
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7337(self.ctx)


class DeActivate7337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 8명
class Sensor7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 8:
            return SafeGreen7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 8:
            return Enable7338(self.ctx)
        if self.count_users(box_id=9330) != 8:
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7338(self.ctx)
        if self.count_users(box_id=9330) != 8:
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 8:
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7338(self.ctx)


class Delay7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 8:
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7338(self.ctx)


class DeActivate7338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 9명
class Sensor7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 9:
            return SafeGreen7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 9:
            return Enable7339(self.ctx)
        if self.count_users(box_id=9330) != 9:
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7339(self.ctx)
        if self.count_users(box_id=9330) != 9:
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 9:
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7339(self.ctx)


class Delay7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 9:
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7339(self.ctx)


class DeActivate7339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 10명
class Sensor7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 10:
            return SafeGreen7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 10:
            return Enable7336(self.ctx)
        if self.count_users(box_id=9330) != 10:
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate7336(self.ctx)
        if self.count_users(box_id=9330) != 10:
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 10:
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7336(self.ctx)


class Delay7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 10:
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate7336(self.ctx)


class DeActivate7336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 15명
class Sensor73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 15:
            return SafeGreen73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 15:
            return Enable73315(self.ctx)
        if self.count_users(box_id=9330) != 15:
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate73315(self.ctx)
        if self.count_users(box_id=9330) != 15:
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 15:
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay73315(self.ctx)


class Delay73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 15:
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate73315(self.ctx)


class DeActivate73315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 20명
class Sensor73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 20:
            return SafeGreen73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 20:
            return Enable73320(self.ctx)
        if self.count_users(box_id=9330) != 20:
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate73320(self.ctx)
        if self.count_users(box_id=9330) != 20:
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 20:
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay73320(self.ctx)


class Delay73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 20:
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate73320(self.ctx)


class DeActivate73320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 25명
class Sensor73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 25:
            return SafeGreen73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 25:
            return Enable73325(self.ctx)
        if self.count_users(box_id=9330) != 25:
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate73325(self.ctx)
        if self.count_users(box_id=9330) != 25:
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 25:
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay73325(self.ctx)


class Delay73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 25:
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate73325(self.ctx)


class DeActivate73325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


# 30명
class Sensor73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=3) # red
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 30:
            return SafeGreen73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class SafeGreen73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) == 30:
            return Enable73330(self.ctx)
        if self.count_users(box_id=9330) != 30:
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Enable73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000948], state=0):
            # On
            return Activate73330(self.ctx)
        if self.count_users(box_id=9330) != 30:
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Activate73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True)
        self.set_interact_object(trigger_ids=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 30:
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay73330(self.ctx)


class Delay73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330) != 30:
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000964], state=0):
            # Off
            return DeActivate73330(self.ctx)


class DeActivate73330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330])
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338])
        self.set_effect(trigger_ids=[8330])
        self.set_interact_object(trigger_ids=[10000948], state=0) # On
        self.set_interact_object(trigger_ids=[10000964], state=0) # Off
        self.set_user_value(key='Barrier33', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
