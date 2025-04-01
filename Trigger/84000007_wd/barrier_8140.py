""" trigger/84000007_wd/barrier_8140.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=2) # On
        self.set_interact_object(trigger_ids=[10000957], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier14') == 1:
            return Sensor7141(self.ctx)
        if self.user_value(key='Barrier14') == 2:
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 3:
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 4:
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 5:
            return Sensor7145(self.ctx)


# 1명 방어 불가
class Sensor7141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 1:
            return Activate7141(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Activate7141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 1:
            return Sensor7141(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=0) # On
        self.set_interact_object(trigger_ids=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 2:
            return SafeGreen7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class SafeGreen7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 2:
            return Enable7142(self.ctx)
        if self.count_users(box_id=9140) != 2:
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Enable7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000941], state=0):
            # On
            return Activate7142(self.ctx)
        if self.count_users(box_id=9140) != 2:
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Activate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True)
        self.set_interact_object(trigger_ids=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 2:
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7142(self.ctx)


class Delay7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 2:
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000957], state=0):
            # Off
            return DeActivate7142(self.ctx)


class DeActivate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140])
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=0) # On
        self.set_interact_object(trigger_ids=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 3:
            return SafeGreen7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class SafeGreen7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 3:
            return Enable7143(self.ctx)
        if self.count_users(box_id=9140) != 3:
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Enable7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000941], state=0):
            # On
            return Activate7143(self.ctx)
        if self.count_users(box_id=9140) != 3:
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Activate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True)
        self.set_interact_object(trigger_ids=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 3:
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7143(self.ctx)


class Delay7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 3:
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000957], state=0):
            # Off
            return DeActivate7143(self.ctx)


class DeActivate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140])
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=0) # On
        self.set_interact_object(trigger_ids=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 4:
            return SafeGreen7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class SafeGreen7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 4:
            return Enable7144(self.ctx)
        if self.count_users(box_id=9140) != 4:
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Enable7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000941], state=0):
            # On
            return Activate7144(self.ctx)
        if self.count_users(box_id=9140) != 4:
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Activate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True)
        self.set_interact_object(trigger_ids=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 4:
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7144(self.ctx)


class Delay7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 4:
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000957], state=0):
            # Off
            return DeActivate7144(self.ctx)


class DeActivate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140])
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=0) # On
        self.set_interact_object(trigger_ids=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 5:
            return SafeGreen7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class SafeGreen7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) == 5:
            return Enable7145(self.ctx)
        if self.count_users(box_id=9140) != 5:
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Enable7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000941], state=0):
            # On
            return Activate7145(self.ctx)
        if self.count_users(box_id=9140) != 5:
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Activate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True)
        self.set_interact_object(trigger_ids=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 5:
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7145(self.ctx)


class Delay7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140) != 5:
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000957], state=0):
            # Off
            return DeActivate7145(self.ctx)


class DeActivate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140])
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8141,8142,8143,8144])
        self.set_effect(trigger_ids=[8140])
        self.set_interact_object(trigger_ids=[10000941], state=0) # On
        self.set_interact_object(trigger_ids=[10000957], state=0) # Off
        self.set_user_value(key='Barrier14', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
