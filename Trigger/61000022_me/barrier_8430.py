""" trigger/61000022_me/barrier_8430.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=2) # On
        self.set_interact_object(trigger_ids=[10000968], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier43') == 1:
            return Sensor7431(self.ctx)
        if self.user_value(key='Barrier43') == 2:
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 3:
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 4:
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 5:
            return Sensor7435(self.ctx)


# 1명 방어 불가
class Sensor7431(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 1:
            return Activate7431(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Activate7431(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 1:
            return Sensor7431(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=1) # yellow
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=0) # On
        self.set_interact_object(trigger_ids=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 2:
            return SafeGreen7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class SafeGreen7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 2:
            return Enable7432(self.ctx)
        if self.count_users(box_id=9430) != 2:
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Enable7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000952], state=0):
            # On
            return Activate7432(self.ctx)
        if self.count_users(box_id=9430) != 2:
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Activate7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430], visible=True)
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436], visible=True)
        self.set_interact_object(trigger_ids=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 2:
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7432(self.ctx)


class Delay7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 2:
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000968], state=0):
            # Off
            return DeActivate7432(self.ctx)


class DeActivate7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430])
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=1) # yellow
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=0) # On
        self.set_interact_object(trigger_ids=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 3:
            return SafeGreen7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class SafeGreen7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 3:
            return Enable7433(self.ctx)
        if self.count_users(box_id=9430) != 3:
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Enable7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000952], state=0):
            # On
            return Activate7433(self.ctx)
        if self.count_users(box_id=9430) != 3:
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Activate7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430], visible=True)
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436], visible=True)
        self.set_interact_object(trigger_ids=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 3:
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7433(self.ctx)


class Delay7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 3:
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000968], state=0):
            # Off
            return DeActivate7433(self.ctx)


class DeActivate7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430])
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=1) # yellow
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=0) # On
        self.set_interact_object(trigger_ids=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 4:
            return SafeGreen7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class SafeGreen7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 4:
            return Enable7434(self.ctx)
        if self.count_users(box_id=9430) != 4:
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Enable7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000952], state=0):
            # On
            return Activate7434(self.ctx)
        if self.count_users(box_id=9430) != 4:
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Activate7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430], visible=True)
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436], visible=True)
        self.set_interact_object(trigger_ids=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 4:
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7434(self.ctx)


class Delay7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 4:
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000968], state=0):
            # Off
            return DeActivate7434(self.ctx)


class DeActivate7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430])
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=1) # yellow
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=0) # On
        self.set_interact_object(trigger_ids=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 5:
            return SafeGreen7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class SafeGreen7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) == 5:
            return Enable7435(self.ctx)
        if self.count_users(box_id=9430) != 5:
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Enable7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000952], state=0):
            # On
            return Activate7435(self.ctx)
        if self.count_users(box_id=9430) != 5:
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Activate7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430], visible=True)
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436], visible=True)
        self.set_interact_object(trigger_ids=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 5:
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7435(self.ctx)


class Delay7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9430) != 5:
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000968], state=0):
            # Off
            return DeActivate7435(self.ctx)


class DeActivate7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8430])
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8431,8432,8433,8434,8435,8436])
        self.set_effect(trigger_ids=[8430])
        self.set_interact_object(trigger_ids=[10000952], state=0) # On
        self.set_interact_object(trigger_ids=[10000968], state=0) # Off
        self.set_user_value(key='Barrier43', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
