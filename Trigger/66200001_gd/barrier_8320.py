""" trigger/66200001_gd/barrier_8320.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=2) # On
        self.set_interact_object(trigger_ids=[10001210], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier32') == 1:
            return Sensor7321(self.ctx)
        if self.user_value(key='Barrier32') == 2:
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 3:
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 4:
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 5:
            return Sensor7325(self.ctx)


# 1명 방어 불가
class Sensor7321(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 1:
            return Activate7321(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Activate7321(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 1:
            return Sensor7321(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=1) # yellow
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=0) # On
        self.set_interact_object(trigger_ids=[10001210], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 2:
            return SafeGreen7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class SafeGreen7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 2:
            return CheckSameUserTag7322(self.ctx)
        if self.count_users(box_id=9320) != 2:
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7322(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9320) and self.count_users(box_id=9320) == 2:
            return Enable7322(self.ctx)
        if self.count_users(box_id=9320) != 2:
            return Sensor7322(self.ctx)
        if not self.check_same_user_tag(box_id=9320):
            return SafeGreen7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Enable7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001194], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001194], state=0):
            # On
            return Activate7322(self.ctx)
        if self.count_users(box_id=9320) != 2:
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Activate7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320], visible=True)
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True)
        self.set_interact_object(trigger_ids=[10001194], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 2:
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7322(self.ctx)


class Delay7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001210], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 2:
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001210], state=0):
            # Off
            return DeActivate7322(self.ctx)


class DeActivate7322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320])
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=1) # yellow
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=0) # On
        self.set_interact_object(trigger_ids=[10001210], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 3:
            return SafeGreen7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class SafeGreen7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 3:
            return CheckSameUserTag7323(self.ctx)
        if self.count_users(box_id=9320) != 3:
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7323(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9320) and self.count_users(box_id=9320) == 3:
            return Enable7323(self.ctx)
        if self.count_users(box_id=9320) != 3:
            return Sensor7323(self.ctx)
        if not self.check_same_user_tag(box_id=9320):
            return SafeGreen7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Enable7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001194], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001194], state=0):
            # On
            return Activate7323(self.ctx)
        if self.count_users(box_id=9320) != 3:
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Activate7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320], visible=True)
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True)
        self.set_interact_object(trigger_ids=[10001194], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 3:
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7323(self.ctx)


class Delay7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001210], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 3:
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001210], state=0):
            # Off
            return DeActivate7323(self.ctx)


class DeActivate7323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320])
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=1) # yellow
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=0) # On
        self.set_interact_object(trigger_ids=[10001210], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 4:
            return SafeGreen7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class SafeGreen7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 4:
            return CheckSameUserTag7324(self.ctx)
        if self.count_users(box_id=9320) != 4:
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7324(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9320) and self.count_users(box_id=9320) == 4:
            return Enable7324(self.ctx)
        if self.count_users(box_id=9320) != 4:
            return Sensor7324(self.ctx)
        if not self.check_same_user_tag(box_id=9320):
            return SafeGreen7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Enable7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001194], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001194], state=0):
            # On
            return Activate7324(self.ctx)
        if self.count_users(box_id=9320) != 4:
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Activate7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320], visible=True)
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True)
        self.set_interact_object(trigger_ids=[10001194], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 4:
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7324(self.ctx)


class Delay7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001210], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 4:
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001210], state=0):
            # Off
            return DeActivate7324(self.ctx)


class DeActivate7324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320])
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=1) # yellow
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=0) # On
        self.set_interact_object(trigger_ids=[10001210], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 5:
            return SafeGreen7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class SafeGreen7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7320, key='Color32', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) == 5:
            return CheckSameUserTag7325(self.ctx)
        if self.count_users(box_id=9320) != 5:
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7325(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9320) and self.count_users(box_id=9320) == 5:
            return Enable7325(self.ctx)
        if self.count_users(box_id=9320) != 5:
            return Sensor7325(self.ctx)
        if not self.check_same_user_tag(box_id=9320):
            return SafeGreen7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Enable7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001194], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001194], state=0):
            # On
            return Activate7325(self.ctx)
        if self.count_users(box_id=9320) != 5:
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Activate7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320], visible=True)
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True)
        self.set_interact_object(trigger_ids=[10001194], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 5:
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7325(self.ctx)


class Delay7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001210], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9320) != 5:
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001210], state=0):
            # Off
            return DeActivate7325(self.ctx)


class DeActivate7325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8320])
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8321,8322,8323,8324,8325,8326,8327,8328])
        self.set_effect(trigger_ids=[8320])
        self.set_interact_object(trigger_ids=[10001194], state=0) # On
        self.set_interact_object(trigger_ids=[10001210], state=0) # Off
        self.set_user_value(key='Barrier32', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
