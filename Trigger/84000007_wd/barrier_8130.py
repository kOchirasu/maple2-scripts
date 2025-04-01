""" trigger/84000007_wd/barrier_8130.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=2) # On
        self.set_interact_object(trigger_ids=[10000956], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier13') == 1:
            return Sensor7131(self.ctx)
        if self.user_value(key='Barrier13') == 2:
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 3:
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 4:
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 5:
            return Sensor7135(self.ctx)


# 1명 방어 불가
class Sensor7131(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 1:
            return Activate7131(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Activate7131(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 1:
            return Sensor7131(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=1) # yellow
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=0) # On
        self.set_interact_object(trigger_ids=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 2:
            return SafeGreen7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class SafeGreen7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 2:
            return Enable7132(self.ctx)
        if self.count_users(box_id=9130) != 2:
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Enable7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000940], state=0):
            # On
            return Activate7132(self.ctx)
        if self.count_users(box_id=9130) != 2:
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Activate7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130], visible=True)
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136], visible=True)
        self.set_interact_object(trigger_ids=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 2:
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7132(self.ctx)


class Delay7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 2:
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000956], state=0):
            # Off
            return DeActivate7132(self.ctx)


class DeActivate7132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130])
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=1) # yellow
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=0) # On
        self.set_interact_object(trigger_ids=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 3:
            return SafeGreen7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class SafeGreen7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 3:
            return Enable7133(self.ctx)
        if self.count_users(box_id=9130) != 3:
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Enable7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000940], state=0):
            # On
            return Activate7133(self.ctx)
        if self.count_users(box_id=9130) != 3:
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Activate7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130], visible=True)
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136], visible=True)
        self.set_interact_object(trigger_ids=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 3:
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7133(self.ctx)


class Delay7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 3:
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000956], state=0):
            # Off
            return DeActivate7133(self.ctx)


class DeActivate7133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130])
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=1) # yellow
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=0) # On
        self.set_interact_object(trigger_ids=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 4:
            return SafeGreen7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class SafeGreen7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 4:
            return Enable7134(self.ctx)
        if self.count_users(box_id=9130) != 4:
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Enable7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000940], state=0):
            # On
            return Activate7134(self.ctx)
        if self.count_users(box_id=9130) != 4:
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Activate7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130], visible=True)
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136], visible=True)
        self.set_interact_object(trigger_ids=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 4:
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7134(self.ctx)


class Delay7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 4:
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000956], state=0):
            # Off
            return DeActivate7134(self.ctx)


class DeActivate7134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130])
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=1) # yellow
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=0) # On
        self.set_interact_object(trigger_ids=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 5:
            return SafeGreen7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class SafeGreen7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) == 5:
            return Enable7135(self.ctx)
        if self.count_users(box_id=9130) != 5:
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Enable7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000940], state=0):
            # On
            return Activate7135(self.ctx)
        if self.count_users(box_id=9130) != 5:
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Activate7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130], visible=True)
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136], visible=True)
        self.set_interact_object(trigger_ids=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 5:
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7135(self.ctx)


class Delay7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9130) != 5:
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000956], state=0):
            # Off
            return DeActivate7135(self.ctx)


class DeActivate7135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8130])
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8131,8132,8133,8134,8135,8136])
        self.set_effect(trigger_ids=[8130])
        self.set_interact_object(trigger_ids=[10000940], state=0) # On
        self.set_interact_object(trigger_ids=[10000956], state=0) # Off
        self.set_user_value(key='Barrier13', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
