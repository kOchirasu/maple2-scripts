""" trigger/61000022_me/barrier_8440.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=2) # On
        self.set_interact_object(trigger_ids=[10000969], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier44') == 1:
            return Sensor7441(self.ctx)
        if self.user_value(key='Barrier44') == 2:
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 3:
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 4:
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 5:
            return Sensor7445(self.ctx)


# 1명 방어 불가
class Sensor7441(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 1:
            return Activate7441(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Activate7441(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 1:
            return Sensor7441(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=1) # yellow
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=0) # On
        self.set_interact_object(trigger_ids=[10000969], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 2:
            return SafeGreen7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class SafeGreen7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 2:
            return Enable7442(self.ctx)
        if self.count_users(box_id=9440) != 2:
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Enable7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000953], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000953], state=0):
            # On
            return Activate7442(self.ctx)
        if self.count_users(box_id=9440) != 2:
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Activate7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440], visible=True)
        self.set_mesh(trigger_ids=[8441,8442,8443,8444], visible=True)
        self.set_interact_object(trigger_ids=[10000953], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 2:
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7442(self.ctx)


class Delay7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000969], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 2:
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000969], state=0):
            # Off
            return DeActivate7442(self.ctx)


class DeActivate7442(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440])
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=1) # yellow
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=0) # On
        self.set_interact_object(trigger_ids=[10000969], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 3:
            return SafeGreen7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class SafeGreen7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 3:
            return Enable7443(self.ctx)
        if self.count_users(box_id=9440) != 3:
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Enable7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000953], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000953], state=0):
            # On
            return Activate7443(self.ctx)
        if self.count_users(box_id=9440) != 3:
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Activate7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440], visible=True)
        self.set_mesh(trigger_ids=[8441,8442,8443,8444], visible=True)
        self.set_interact_object(trigger_ids=[10000953], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 3:
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7443(self.ctx)


class Delay7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000969], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 3:
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000969], state=0):
            # Off
            return DeActivate7443(self.ctx)


class DeActivate7443(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440])
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=1) # yellow
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=0) # On
        self.set_interact_object(trigger_ids=[10000969], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 4:
            return SafeGreen7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class SafeGreen7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 4:
            return Enable7444(self.ctx)
        if self.count_users(box_id=9440) != 4:
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Enable7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000953], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000953], state=0):
            # On
            return Activate7444(self.ctx)
        if self.count_users(box_id=9440) != 4:
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Activate7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440], visible=True)
        self.set_mesh(trigger_ids=[8441,8442,8443,8444], visible=True)
        self.set_interact_object(trigger_ids=[10000953], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 4:
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7444(self.ctx)


class Delay7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000969], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 4:
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000969], state=0):
            # Off
            return DeActivate7444(self.ctx)


class DeActivate7444(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440])
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=1) # yellow
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=0) # On
        self.set_interact_object(trigger_ids=[10000969], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 5:
            return SafeGreen7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class SafeGreen7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7440, key='Color44', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) == 5:
            return Enable7445(self.ctx)
        if self.count_users(box_id=9440) != 5:
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Enable7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000953], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000953], state=0):
            # On
            return Activate7445(self.ctx)
        if self.count_users(box_id=9440) != 5:
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Activate7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440], visible=True)
        self.set_mesh(trigger_ids=[8441,8442,8443,8444], visible=True)
        self.set_interact_object(trigger_ids=[10000953], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 5:
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7445(self.ctx)


class Delay7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000969], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9440) != 5:
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000969], state=0):
            # Off
            return DeActivate7445(self.ctx)


class DeActivate7445(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8440])
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8441,8442,8443,8444])
        self.set_effect(trigger_ids=[8440])
        self.set_interact_object(trigger_ids=[10000953], state=0) # On
        self.set_interact_object(trigger_ids=[10000969], state=0) # Off
        self.set_user_value(key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
