""" trigger/84000007_wd/barrier_8110.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=2) # On
        self.set_interact_object(trigger_ids=[10000954], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier11') == 1:
            return Sensor7111(self.ctx)
        if self.user_value(key='Barrier11') == 2:
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 3:
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 4:
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 5:
            return Sensor7115(self.ctx)


# 1명 방어 불가
class Sensor7111(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 1:
            return Activate7111(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Activate7111(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 1:
            return Sensor7111(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=1) # yellow
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=0) # On
        self.set_interact_object(trigger_ids=[10000954], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 2:
            return SafeGreen7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class SafeGreen7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 2:
            return Enable7112(self.ctx)
        if self.count_users(box_id=9110) != 2:
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Enable7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000938], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000938], state=0):
            # On
            return Activate7112(self.ctx)
        if self.count_users(box_id=9110) != 2:
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Activate7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110], visible=True)
        self.set_mesh(trigger_ids=[8111,8112,8113,8114], visible=True)
        self.set_interact_object(trigger_ids=[10000938], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 2:
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7112(self.ctx)


class Delay7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000954], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 2:
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000954], state=0):
            # Off
            return DeActivate7112(self.ctx)


class DeActivate7112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110])
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=1) # yellow
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=0) # On
        self.set_interact_object(trigger_ids=[10000954], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 3:
            return SafeGreen7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class SafeGreen7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 3:
            return Enable7113(self.ctx)
        if self.count_users(box_id=9110) != 3:
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Enable7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000938], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000938], state=0):
            # On
            return Activate7113(self.ctx)
        if self.count_users(box_id=9110) != 3:
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Activate7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110], visible=True)
        self.set_mesh(trigger_ids=[8111,8112,8113,8114], visible=True)
        self.set_interact_object(trigger_ids=[10000938], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 3:
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7113(self.ctx)


class Delay7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000954], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 3:
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000954], state=0):
            # Off
            return DeActivate7113(self.ctx)


class DeActivate7113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110])
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=1) # yellow
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=0) # On
        self.set_interact_object(trigger_ids=[10000954], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 4:
            return SafeGreen7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class SafeGreen7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 4:
            return Enable7114(self.ctx)
        if self.count_users(box_id=9110) != 4:
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Enable7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000938], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000938], state=0):
            # On
            return Activate7114(self.ctx)
        if self.count_users(box_id=9110) != 4:
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Activate7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110], visible=True)
        self.set_mesh(trigger_ids=[8111,8112,8113,8114], visible=True)
        self.set_interact_object(trigger_ids=[10000938], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 4:
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7114(self.ctx)


class Delay7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000954], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 4:
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000954], state=0):
            # Off
            return DeActivate7114(self.ctx)


class DeActivate7114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110])
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=1) # yellow
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=0) # On
        self.set_interact_object(trigger_ids=[10000954], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 5:
            return SafeGreen7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class SafeGreen7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) == 5:
            return Enable7115(self.ctx)
        if self.count_users(box_id=9110) != 5:
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Enable7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000938], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000938], state=0):
            # On
            return Activate7115(self.ctx)
        if self.count_users(box_id=9110) != 5:
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Activate7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110], visible=True)
        self.set_mesh(trigger_ids=[8111,8112,8113,8114], visible=True)
        self.set_interact_object(trigger_ids=[10000938], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 5:
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7115(self.ctx)


class Delay7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000954], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9110) != 5:
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000954], state=0):
            # Off
            return DeActivate7115(self.ctx)


class DeActivate7115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8110])
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8111,8112,8113,8114])
        self.set_effect(trigger_ids=[8110])
        self.set_interact_object(trigger_ids=[10000938], state=0) # On
        self.set_interact_object(trigger_ids=[10000954], state=0) # Off
        self.set_user_value(key='Barrier11', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
