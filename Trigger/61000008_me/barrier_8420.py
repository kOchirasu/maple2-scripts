""" trigger/61000008_me/barrier_8420.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=2) # On
        self.set_interact_object(trigger_ids=[10000967], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier42') == 1:
            return Sensor7421(self.ctx)
        if self.user_value(key='Barrier42') == 2:
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 3:
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 4:
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 5:
            return Sensor7425(self.ctx)


# 1명 방어 불가
class Sensor7421(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 1:
            return Activate7421(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Activate7421(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 1:
            return Sensor7421(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=1) # yellow
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=0) # On
        self.set_interact_object(trigger_ids=[10000967], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 2:
            return SafeGreen7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class SafeGreen7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 2:
            return Enable7422(self.ctx)
        if self.count_users(box_id=9420) != 2:
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Enable7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000951], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000951], state=0):
            # On
            return Activate7422(self.ctx)
        if self.count_users(box_id=9420) != 2:
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Activate7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420], visible=True)
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426], visible=True)
        self.set_interact_object(trigger_ids=[10000951], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 2:
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7422(self.ctx)


class Delay7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000967], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 2:
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000967], state=0):
            # Off
            return DeActivate7422(self.ctx)


class DeActivate7422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420])
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=1) # yellow
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=0) # On
        self.set_interact_object(trigger_ids=[10000967], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 3:
            return SafeGreen7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class SafeGreen7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 3:
            return Enable7423(self.ctx)
        if self.count_users(box_id=9420) != 3:
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Enable7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000951], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000951], state=0):
            # On
            return Activate7423(self.ctx)
        if self.count_users(box_id=9420) != 3:
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Activate7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420], visible=True)
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426], visible=True)
        self.set_interact_object(trigger_ids=[10000951], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 3:
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7423(self.ctx)


class Delay7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000967], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 3:
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000967], state=0):
            # Off
            return DeActivate7423(self.ctx)


class DeActivate7423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420])
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=1) # yellow
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=0) # On
        self.set_interact_object(trigger_ids=[10000967], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 4:
            return SafeGreen7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class SafeGreen7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 4:
            return Enable7424(self.ctx)
        if self.count_users(box_id=9420) != 4:
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Enable7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000951], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000951], state=0):
            # On
            return Activate7424(self.ctx)
        if self.count_users(box_id=9420) != 4:
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Activate7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420], visible=True)
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426], visible=True)
        self.set_interact_object(trigger_ids=[10000951], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 4:
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7424(self.ctx)


class Delay7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000967], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 4:
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000967], state=0):
            # Off
            return DeActivate7424(self.ctx)


class DeActivate7424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420])
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=1) # yellow
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=0) # On
        self.set_interact_object(trigger_ids=[10000967], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 5:
            return SafeGreen7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class SafeGreen7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7420, key='Color42', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) == 5:
            return Enable7425(self.ctx)
        if self.count_users(box_id=9420) != 5:
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Enable7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000951], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000951], state=0):
            # On
            return Activate7425(self.ctx)
        if self.count_users(box_id=9420) != 5:
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Activate7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420], visible=True)
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426], visible=True)
        self.set_interact_object(trigger_ids=[10000951], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 5:
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7425(self.ctx)


class Delay7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000967], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9420) != 5:
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000967], state=0):
            # Off
            return DeActivate7425(self.ctx)


class DeActivate7425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8420])
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8420])
        self.set_interact_object(trigger_ids=[10000951], state=0) # On
        self.set_interact_object(trigger_ids=[10000967], state=0) # Off
        self.set_user_value(key='Barrier42', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
