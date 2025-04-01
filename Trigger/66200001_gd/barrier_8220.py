""" trigger/66200001_gd/barrier_8220.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=2) # On
        self.set_interact_object(trigger_ids=[10001206], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier22') == 1:
            return Sensor7221(self.ctx)
        if self.user_value(key='Barrier22') == 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 5:
            return Sensor7225(self.ctx)


# 1명 방어 불가
class Sensor7221(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 1:
            return Activate7221(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7221(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 1:
            return Sensor7221(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 2명
class Sensor7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=1) # yellow
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=0) # On
        self.set_interact_object(trigger_ids=[10001206], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 2:
            return SafeGreen7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 2:
            return CheckSameUserTag7222(self.ctx)
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7222(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9220) and self.count_users(box_id=9220) == 2:
            return Enable7222(self.ctx)
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if not self.check_same_user_tag(box_id=9220):
            return SafeGreen7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001190], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001190], state=0):
            # On
            return Activate7222(self.ctx)
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10001190], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7222(self.ctx)


class Delay7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001206], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001206], state=0):
            # Off
            return DeActivate7222(self.ctx)


class DeActivate7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 3명
class Sensor7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=1) # yellow
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=0) # On
        self.set_interact_object(trigger_ids=[10001206], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 3:
            return SafeGreen7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 3:
            return CheckSameUserTag7223(self.ctx)
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7223(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9220) and self.count_users(box_id=9220) == 3:
            return Enable7223(self.ctx)
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if not self.check_same_user_tag(box_id=9220):
            return SafeGreen7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001190], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001190], state=0):
            # On
            return Activate7223(self.ctx)
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10001190], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7223(self.ctx)


class Delay7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001206], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001206], state=0):
            # Off
            return DeActivate7223(self.ctx)


class DeActivate7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 4명
class Sensor7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=1) # yellow
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=0) # On
        self.set_interact_object(trigger_ids=[10001206], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 4:
            return SafeGreen7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 4:
            return CheckSameUserTag7224(self.ctx)
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7224(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9220) and self.count_users(box_id=9220) == 4:
            return Enable7224(self.ctx)
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if not self.check_same_user_tag(box_id=9220):
            return SafeGreen7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001190], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001190], state=0):
            # On
            return Activate7224(self.ctx)
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10001190], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7224(self.ctx)


class Delay7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001206], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001206], state=0):
            # Off
            return DeActivate7224(self.ctx)


class DeActivate7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 5명
class Sensor7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=1) # yellow
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=0) # On
        self.set_interact_object(trigger_ids=[10001206], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 5:
            return SafeGreen7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 5:
            return CheckSameUserTag7225(self.ctx)
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class CheckSameUserTag7225(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9220) and self.count_users(box_id=9220) == 5:
            return Enable7225(self.ctx)
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if not self.check_same_user_tag(box_id=9220):
            return SafeGreen7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001190], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001190], state=0):
            # On
            return Activate7225(self.ctx)
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10001190], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7225(self.ctx)


class Delay7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001206], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001206], state=0):
            # Off
            return DeActivate7225(self.ctx)


class DeActivate7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10001190], state=0) # On
        self.set_interact_object(trigger_ids=[10001206], state=0) # Off
        self.set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
