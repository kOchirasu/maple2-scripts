""" trigger/84000007_wd/barrier_8210.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=2) # On
        self.set_interact_object(trigger_ids=[10000958], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier21') == 1:
            return Sensor7211(self.ctx)
        if self.user_value(key='Barrier21') == 2:
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 3:
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 4:
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 5:
            return Sensor7215(self.ctx)


# 1명 방어 불가
class Sensor7211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 1:
            return Activate7211(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Activate7211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 1:
            return Sensor7211(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=1) # yellow
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=0) # On
        self.set_interact_object(trigger_ids=[10000958], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 2:
            return SafeGreen7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class SafeGreen7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 2:
            return Enable7212(self.ctx)
        if self.count_users(box_id=9210) != 2:
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Enable7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000942], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000942], state=0):
            # On
            return Activate7212(self.ctx)
        if self.count_users(box_id=9210) != 2:
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Activate7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210], visible=True)
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216], visible=True)
        self.set_interact_object(trigger_ids=[10000942], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 2:
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7212(self.ctx)


class Delay7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000958], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 2:
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000958], state=0):
            # Off
            return DeActivate7212(self.ctx)


class DeActivate7212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210])
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=1) # yellow
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=0) # On
        self.set_interact_object(trigger_ids=[10000958], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 3:
            return SafeGreen7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class SafeGreen7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 3:
            return Enable7213(self.ctx)
        if self.count_users(box_id=9210) != 3:
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Enable7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000942], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000942], state=0):
            # On
            return Activate7213(self.ctx)
        if self.count_users(box_id=9210) != 3:
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Activate7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210], visible=True)
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216], visible=True)
        self.set_interact_object(trigger_ids=[10000942], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 3:
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7213(self.ctx)


class Delay7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000958], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 3:
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000958], state=0):
            # Off
            return DeActivate7213(self.ctx)


class DeActivate7213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210])
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=1) # yellow
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=0) # On
        self.set_interact_object(trigger_ids=[10000958], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 4:
            return SafeGreen7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class SafeGreen7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 4:
            return Enable7214(self.ctx)
        if self.count_users(box_id=9210) != 4:
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Enable7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000942], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000942], state=0):
            # On
            return Activate7214(self.ctx)
        if self.count_users(box_id=9210) != 4:
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Activate7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210], visible=True)
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216], visible=True)
        self.set_interact_object(trigger_ids=[10000942], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 4:
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7214(self.ctx)


class Delay7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000958], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 4:
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000958], state=0):
            # Off
            return DeActivate7214(self.ctx)


class DeActivate7214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210])
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=1) # yellow
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=0) # On
        self.set_interact_object(trigger_ids=[10000958], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 5:
            return SafeGreen7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class SafeGreen7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) == 5:
            return Enable7215(self.ctx)
        if self.count_users(box_id=9210) != 5:
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Enable7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000942], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000942], state=0):
            # On
            return Activate7215(self.ctx)
        if self.count_users(box_id=9210) != 5:
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Activate7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210], visible=True)
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216], visible=True)
        self.set_interact_object(trigger_ids=[10000942], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 5:
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7215(self.ctx)


class Delay7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000958], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9210) != 5:
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000958], state=0):
            # Off
            return DeActivate7215(self.ctx)


class DeActivate7215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8210])
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8211,8212,8213,8214,8215,8216])
        self.set_effect(trigger_ids=[8210])
        self.set_interact_object(trigger_ids=[10000942], state=0) # On
        self.set_interact_object(trigger_ids=[10000958], state=0) # Off
        self.set_user_value(key='Barrier21', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
