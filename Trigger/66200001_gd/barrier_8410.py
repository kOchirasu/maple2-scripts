""" trigger/66200001_gd/barrier_8410.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=2) # On
        self.set_interact_object(trigger_ids=[10001213], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier41') == 1:
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41') == 2:
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 3:
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 4:
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 5:
            return Sensor7415(self.ctx)


# 1명 방어 불가
class Sensor7411(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 1:
            return Activate7411(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Activate7411(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 1:
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=0) # On
        self.set_interact_object(trigger_ids=[10001213], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 2:
            return SafeGreen7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class SafeGreen7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 2:
            return CheckSameUserTag7412(self.ctx)
        if self.count_users(box_id=9410) != 2:
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7412(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9410) and self.count_users(box_id=9410) == 2:
            return Enable7412(self.ctx)
        if self.count_users(box_id=9410) != 2:
            return Sensor7412(self.ctx)
        if not self.check_same_user_tag(box_id=9410):
            return SafeGreen7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Enable7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001197], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001197], state=0):
            # On
            return Activate7412(self.ctx)
        if self.count_users(box_id=9410) != 2:
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Activate7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True)
        self.set_interact_object(trigger_ids=[10001197], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 2:
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7412(self.ctx)


class Delay7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001213], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 2:
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001213], state=0):
            # Off
            return DeActivate7412(self.ctx)


class DeActivate7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410])
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=0) # On
        self.set_interact_object(trigger_ids=[10001213], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 3:
            return SafeGreen7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class SafeGreen7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 3:
            return CheckSameUserTag7413(self.ctx)
        if self.count_users(box_id=9410) != 3:
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7413(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9410) and self.count_users(box_id=9410) == 3:
            return Enable7413(self.ctx)
        if self.count_users(box_id=9410) != 3:
            return Sensor7413(self.ctx)
        if not self.check_same_user_tag(box_id=9410):
            return SafeGreen7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Enable7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001197], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001197], state=0):
            # On
            return Activate7413(self.ctx)
        if self.count_users(box_id=9410) != 3:
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Activate7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True)
        self.set_interact_object(trigger_ids=[10001197], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 3:
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7413(self.ctx)


class Delay7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001213], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 3:
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001213], state=0):
            # Off
            return DeActivate7413(self.ctx)


class DeActivate7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410])
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=0) # On
        self.set_interact_object(trigger_ids=[10001213], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 4:
            return SafeGreen7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class SafeGreen7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 4:
            return CheckSameUserTag7414(self.ctx)
        if self.count_users(box_id=9410) != 4:
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7414(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9410) and self.count_users(box_id=9410) == 4:
            return Enable7414(self.ctx)
        if self.count_users(box_id=9410) != 4:
            return Sensor7414(self.ctx)
        if not self.check_same_user_tag(box_id=9410):
            return SafeGreen7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Enable7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001197], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001197], state=0):
            # On
            return Activate7414(self.ctx)
        if self.count_users(box_id=9410) != 4:
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Activate7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True)
        self.set_interact_object(trigger_ids=[10001197], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 4:
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7414(self.ctx)


class Delay7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001213], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 4:
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001213], state=0):
            # Off
            return DeActivate7414(self.ctx)


class DeActivate7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410])
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=0) # On
        self.set_interact_object(trigger_ids=[10001213], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 5:
            return SafeGreen7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class SafeGreen7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) == 5:
            return CheckSameUserTag7415(self.ctx)
        if self.count_users(box_id=9410) != 5:
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7415(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9410) and self.count_users(box_id=9410) == 5:
            return Enable7415(self.ctx)
        if self.count_users(box_id=9410) != 5:
            return Sensor7415(self.ctx)
        if not self.check_same_user_tag(box_id=9410):
            return SafeGreen7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Enable7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001197], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001197], state=0):
            # On
            return Activate7415(self.ctx)
        if self.count_users(box_id=9410) != 5:
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Activate7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True)
        self.set_interact_object(trigger_ids=[10001197], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 5:
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7415(self.ctx)


class Delay7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001213], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410) != 5:
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001213], state=0):
            # Off
            return DeActivate7415(self.ctx)


class DeActivate7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410])
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8411,8412,8413,8414])
        self.set_effect(trigger_ids=[8410])
        self.set_interact_object(trigger_ids=[10001197], state=0) # On
        self.set_interact_object(trigger_ids=[10001213], state=0) # Off
        self.set_user_value(key='Barrier41', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
