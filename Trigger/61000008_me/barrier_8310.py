""" trigger/61000008_me/barrier_8310.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=2) # On
        self.set_interact_object(trigger_ids=[10000962], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier31') == 1:
            return Sensor7311(self.ctx)
        if self.user_value(key='Barrier31') == 2:
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 3:
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 4:
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 5:
            return Sensor7315(self.ctx)


# 1명 방어 불가
class Sensor7311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 1:
            return Activate7311(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Activate7311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 1:
            return Sensor7311(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=1) # yellow
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=0) # On
        self.set_interact_object(trigger_ids=[10000962], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 2:
            return SafeGreen7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class SafeGreen7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 2:
            return Enable7312(self.ctx)
        if self.count_users(box_id=9310) != 2:
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Enable7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9310], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000946], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000946], state=0):
            # On
            return Activate7312(self.ctx)
        if self.count_users(box_id=9310) != 2:
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Activate7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310], visible=True)
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316], visible=True)
        self.set_interact_object(trigger_ids=[10000946], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 2:
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7312(self.ctx)


class Delay7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000962], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 2:
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000962], state=0):
            # Off
            return DeActivate7312(self.ctx)


class DeActivate7312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310])
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7312(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=1) # yellow
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=0) # On
        self.set_interact_object(trigger_ids=[10000962], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 3:
            return SafeGreen7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class SafeGreen7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 3:
            return Enable7313(self.ctx)
        if self.count_users(box_id=9310) != 3:
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Enable7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9310], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000946], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000946], state=0):
            # On
            return Activate7313(self.ctx)
        if self.count_users(box_id=9310) != 3:
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Activate7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310], visible=True)
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316], visible=True)
        self.set_interact_object(trigger_ids=[10000946], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 3:
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7313(self.ctx)


class Delay7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000962], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 3:
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000962], state=0):
            # Off
            return DeActivate7313(self.ctx)


class DeActivate7313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310])
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7313(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=1) # yellow
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=0) # On
        self.set_interact_object(trigger_ids=[10000962], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 4:
            return SafeGreen7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class SafeGreen7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 4:
            return Enable7314(self.ctx)
        if self.count_users(box_id=9310) != 4:
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Enable7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9310], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000946], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000946], state=0):
            # On
            return Activate7314(self.ctx)
        if self.count_users(box_id=9310) != 4:
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Activate7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310], visible=True)
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316], visible=True)
        self.set_interact_object(trigger_ids=[10000946], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 4:
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7314(self.ctx)


class Delay7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000962], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 4:
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000962], state=0):
            # Off
            return DeActivate7314(self.ctx)


class DeActivate7314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310])
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7314(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=1) # yellow
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=0) # On
        self.set_interact_object(trigger_ids=[10000962], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 5:
            return SafeGreen7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class SafeGreen7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7310, key='Color31', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) == 5:
            return Enable7315(self.ctx)
        if self.count_users(box_id=9310) != 5:
            return Sensor7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Enable7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9310], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000946], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000946], state=0):
            # On
            return Activate7315(self.ctx)
        if self.count_users(box_id=9310) != 5:
            return Sensor7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Activate7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310], visible=True)
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316], visible=True)
        self.set_interact_object(trigger_ids=[10000946], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 5:
            return Sensor7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7315(self.ctx)


class Delay7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000962], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9310) != 5:
            return Sensor7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000962], state=0):
            # Off
            return DeActivate7315(self.ctx)


class DeActivate7315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8310])
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7315(self.ctx)
        if self.user_value(key='Barrier31') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8311,8312,8313,8314,8315,8316])
        self.set_effect(trigger_ids=[8310])
        self.set_interact_object(trigger_ids=[10000946], state=0) # On
        self.set_interact_object(trigger_ids=[10000962], state=0) # Off
        self.set_user_value(key='Barrier31', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
