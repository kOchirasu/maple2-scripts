""" trigger/66200001_gd/barrier_8340.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=2) # On
        self.set_interact_object(trigger_ids=[10001212], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier34') == 1:
            return Sensor7341(self.ctx)
        if self.user_value(key='Barrier34') == 2:
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 3:
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 4:
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 5:
            return Sensor7345(self.ctx)


# 1명 방어 불가
class Sensor7341(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 1:
            return Activate7341(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Activate7341(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 1:
            return Sensor7341(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=1) # yellow
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=0) # On
        self.set_interact_object(trigger_ids=[10001212], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 2:
            return SafeGreen7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class SafeGreen7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 2:
            return CheckSameUserTag7342(self.ctx)
        if self.count_users(box_id=9340) != 2:
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7342(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9340) and self.count_users(box_id=9340) == 2:
            return Enable7342(self.ctx)
        if self.count_users(box_id=9340) != 2:
            return Sensor7342(self.ctx)
        if not self.check_same_user_tag(box_id=9340):
            return SafeGreen7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Enable7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001196], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001196], state=0):
            # On
            return Activate7342(self.ctx)
        if self.count_users(box_id=9340) != 2:
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Activate7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340], visible=True)
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346], visible=True)
        self.set_interact_object(trigger_ids=[10001196], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 2:
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7342(self.ctx)


class Delay7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001212], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 2:
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001212], state=0):
            # Off
            return DeActivate7342(self.ctx)


class DeActivate7342(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340])
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=1) # yellow
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=0) # On
        self.set_interact_object(trigger_ids=[10001212], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 3:
            return SafeGreen7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class SafeGreen7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 3:
            return CheckSameUserTag7343(self.ctx)
        if self.count_users(box_id=9340) != 3:
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7343(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9340) and self.count_users(box_id=9340) == 3:
            return Enable7343(self.ctx)
        if self.count_users(box_id=9340) != 3:
            return Sensor7343(self.ctx)
        if not self.check_same_user_tag(box_id=9340):
            return SafeGreen7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Enable7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001196], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001196], state=0):
            # On
            return Activate7343(self.ctx)
        if self.count_users(box_id=9340) != 3:
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Activate7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340], visible=True)
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346], visible=True)
        self.set_interact_object(trigger_ids=[10001196], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 3:
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7343(self.ctx)


class Delay7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001212], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 3:
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001212], state=0):
            # Off
            return DeActivate7343(self.ctx)


class DeActivate7343(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340])
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=1) # yellow
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=0) # On
        self.set_interact_object(trigger_ids=[10001212], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 4:
            return SafeGreen7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class SafeGreen7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 4:
            return CheckSameUserTag7344(self.ctx)
        if self.count_users(box_id=9340) != 4:
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7344(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9340) and self.count_users(box_id=9340) == 4:
            return Enable7344(self.ctx)
        if self.count_users(box_id=9340) != 4:
            return Sensor7344(self.ctx)
        if not self.check_same_user_tag(box_id=9340):
            return SafeGreen7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Enable7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001196], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001196], state=0):
            # On
            return Activate7344(self.ctx)
        if self.count_users(box_id=9340) != 4:
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Activate7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340], visible=True)
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346], visible=True)
        self.set_interact_object(trigger_ids=[10001196], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 4:
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7344(self.ctx)


class Delay7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001212], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 4:
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001212], state=0):
            # Off
            return DeActivate7344(self.ctx)


class DeActivate7344(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340])
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=1) # yellow
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=0) # On
        self.set_interact_object(trigger_ids=[10001212], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 5:
            return SafeGreen7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class SafeGreen7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) == 5:
            return CheckSameUserTag7345(self.ctx)
        if self.count_users(box_id=9340) != 5:
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7345(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9340) and self.count_users(box_id=9340) == 5:
            return Enable7345(self.ctx)
        if self.count_users(box_id=9340) != 5:
            return Sensor7345(self.ctx)
        if not self.check_same_user_tag(box_id=9340):
            return SafeGreen7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Enable7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001196], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001196], state=0):
            # On
            return Activate7345(self.ctx)
        if self.count_users(box_id=9340) != 5:
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Activate7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340], visible=True)
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346], visible=True)
        self.set_interact_object(trigger_ids=[10001196], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 5:
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7345(self.ctx)


class Delay7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001212], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340) != 5:
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001212], state=0):
            # Off
            return DeActivate7345(self.ctx)


class DeActivate7345(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8340])
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8341,8342,8343,8344,8345,8346])
        self.set_effect(trigger_ids=[8340])
        self.set_interact_object(trigger_ids=[10001196], state=0) # On
        self.set_interact_object(trigger_ids=[10001212], state=0) # Off
        self.set_user_value(key='Barrier34', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
