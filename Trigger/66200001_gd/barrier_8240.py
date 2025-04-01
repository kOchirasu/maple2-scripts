""" trigger/66200001_gd/barrier_8240.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=2) # On
        self.set_interact_object(trigger_ids=[10001208], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier24') == 1:
            return Sensor7241(self.ctx)
        if self.user_value(key='Barrier24') == 2:
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 3:
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 4:
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 5:
            return Sensor7245(self.ctx)


# 1명 방어 불가
class Sensor7241(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 1:
            return Activate7241(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Activate7241(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 1:
            return Sensor7241(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=1) # yellow
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=0) # On
        self.set_interact_object(trigger_ids=[10001208], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 2:
            return SafeGreen7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class SafeGreen7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 2:
            return CheckSameUserTag7242(self.ctx)
        if self.count_users(box_id=9240) != 2:
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7242(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9240) and self.count_users(box_id=9240) == 2:
            return Enable7242(self.ctx)
        if self.count_users(box_id=9240) != 2:
            return Sensor7242(self.ctx)
        if not self.check_same_user_tag(box_id=9240):
            return SafeGreen7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Enable7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9240], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001192], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001192], state=0):
            # On
            return Activate7242(self.ctx)
        if self.count_users(box_id=9240) != 2:
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Activate7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240], visible=True)
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246], visible=True)
        self.set_interact_object(trigger_ids=[10001192], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 2:
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7242(self.ctx)


class Delay7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001208], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 2:
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001208], state=0):
            # Off
            return DeActivate7242(self.ctx)


class DeActivate7242(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240])
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7242(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=1) # yellow
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=0) # On
        self.set_interact_object(trigger_ids=[10001208], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 3:
            return SafeGreen7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class SafeGreen7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 3:
            return CheckSameUserTag7243(self.ctx)
        if self.count_users(box_id=9240) != 3:
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7243(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9240) and self.count_users(box_id=9240) == 3:
            return Enable7243(self.ctx)
        if self.count_users(box_id=9240) != 3:
            return Sensor7243(self.ctx)
        if not self.check_same_user_tag(box_id=9240):
            return SafeGreen7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Enable7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9240], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001192], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001192], state=0):
            # On
            return Activate7243(self.ctx)
        if self.count_users(box_id=9240) != 3:
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Activate7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240], visible=True)
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246], visible=True)
        self.set_interact_object(trigger_ids=[10001192], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 3:
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7243(self.ctx)


class Delay7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001208], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 3:
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001208], state=0):
            # Off
            return DeActivate7243(self.ctx)


class DeActivate7243(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240])
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7243(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=1) # yellow
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=0) # On
        self.set_interact_object(trigger_ids=[10001208], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 4:
            return SafeGreen7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class SafeGreen7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 4:
            return CheckSameUserTag7244(self.ctx)
        if self.count_users(box_id=9240) != 4:
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7244(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9240) and self.count_users(box_id=9240) == 4:
            return Enable7244(self.ctx)
        if self.count_users(box_id=9240) != 4:
            return Sensor7244(self.ctx)
        if not self.check_same_user_tag(box_id=9240):
            return SafeGreen7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Enable7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9240], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001192], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001192], state=0):
            # On
            return Activate7244(self.ctx)
        if self.count_users(box_id=9240) != 4:
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Activate7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240], visible=True)
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246], visible=True)
        self.set_interact_object(trigger_ids=[10001192], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 4:
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7244(self.ctx)


class Delay7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001208], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 4:
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001208], state=0):
            # Off
            return DeActivate7244(self.ctx)


class DeActivate7244(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240])
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7244(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=1) # yellow
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=0) # On
        self.set_interact_object(trigger_ids=[10001208], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 5:
            return SafeGreen7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class SafeGreen7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7240, key='Color24', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) == 5:
            return CheckSameUserTag7245(self.ctx)
        if self.count_users(box_id=9240) != 5:
            return Sensor7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7245(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9240) and self.count_users(box_id=9240) == 5:
            return Enable7245(self.ctx)
        if self.count_users(box_id=9240) != 5:
            return Sensor7245(self.ctx)
        if not self.check_same_user_tag(box_id=9240):
            return SafeGreen7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Enable7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9240], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001192], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001192], state=0):
            # On
            return Activate7245(self.ctx)
        if self.count_users(box_id=9240) != 5:
            return Sensor7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Activate7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240], visible=True)
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246], visible=True)
        self.set_interact_object(trigger_ids=[10001192], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 5:
            return Sensor7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7245(self.ctx)


class Delay7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001208], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9240) != 5:
            return Sensor7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001208], state=0):
            # Off
            return DeActivate7245(self.ctx)


class DeActivate7245(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8240])
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7245(self.ctx)
        if self.user_value(key='Barrier24') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8241,8242,8243,8244,8245,8246])
        self.set_effect(trigger_ids=[8240])
        self.set_interact_object(trigger_ids=[10001192], state=0) # On
        self.set_interact_object(trigger_ids=[10001208], state=0) # Off
        self.set_user_value(key='Barrier24', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
