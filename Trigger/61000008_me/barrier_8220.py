""" trigger/61000008_me/barrier_8220.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=2) # On
        self.set_interact_object(trigger_ids=[10000959], state=2) # Off

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
        if self.user_value(key='Barrier22') == 7:
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 8:
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 9:
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 6:
            # 10
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 15:
            # 15
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 20:
            # 20
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 25:
            # 25
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 30:
            # 30
            return Sensor72230(self.ctx)


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
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

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
            return Enable7222(self.ctx)
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7222(self.ctx)


class Delay7222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 2:
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

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
            return Enable7223(self.ctx)
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7223(self.ctx)


class Delay7223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 3:
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

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
            return Enable7224(self.ctx)
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7224(self.ctx)


class Delay7224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 4:
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

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
            return Enable7225(self.ctx)
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
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
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7225(self.ctx)


class Delay7225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 5:
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
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


# 7명
class Sensor7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 7:
            return SafeGreen7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 7:
            return Enable7227(self.ctx)
        if self.count_users(box_id=9220) != 7:
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate7227(self.ctx)
        if self.count_users(box_id=9220) != 7:
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 7:
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7227(self.ctx)


class Delay7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 7:
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate7227(self.ctx)


class DeActivate7227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 8명
class Sensor7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 8:
            return SafeGreen7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 8:
            return Enable7228(self.ctx)
        if self.count_users(box_id=9220) != 8:
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate7228(self.ctx)
        if self.count_users(box_id=9220) != 8:
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 8:
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7228(self.ctx)


class Delay7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 8:
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate7228(self.ctx)


class DeActivate7228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 9명
class Sensor7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 9:
            return SafeGreen7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 9:
            return Enable7229(self.ctx)
        if self.count_users(box_id=9220) != 9:
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate7229(self.ctx)
        if self.count_users(box_id=9220) != 9:
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 9:
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7229(self.ctx)


class Delay7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 9:
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate7229(self.ctx)


class DeActivate7229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 10명
class Sensor7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 10:
            return SafeGreen7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 10:
            return Enable7226(self.ctx)
        if self.count_users(box_id=9220) != 10:
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate7226(self.ctx)
        if self.count_users(box_id=9220) != 10:
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 10:
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7226(self.ctx)


class Delay7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 10:
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate7226(self.ctx)


class DeActivate7226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 15명
class Sensor72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 15:
            return SafeGreen72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 15:
            return Enable72215(self.ctx)
        if self.count_users(box_id=9220) != 15:
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate72215(self.ctx)
        if self.count_users(box_id=9220) != 15:
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 15:
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72215(self.ctx)


class Delay72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 15:
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate72215(self.ctx)


class DeActivate72215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 20명
class Sensor72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 20:
            return SafeGreen72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 20:
            return Enable72220(self.ctx)
        if self.count_users(box_id=9220) != 20:
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate72220(self.ctx)
        if self.count_users(box_id=9220) != 20:
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 20:
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72220(self.ctx)


class Delay72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 20:
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate72220(self.ctx)


class DeActivate72220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 25명
class Sensor72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 25:
            return SafeGreen72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 25:
            return Enable72225(self.ctx)
        if self.count_users(box_id=9220) != 25:
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate72225(self.ctx)
        if self.count_users(box_id=9220) != 25:
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 25:
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72225(self.ctx)


class Delay72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 25:
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate72225(self.ctx)


class DeActivate72225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


# 30명
class Sensor72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=3) # red
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 30:
            return SafeGreen72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class SafeGreen72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7220, key='Color22', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) == 30:
            return Enable72230(self.ctx)
        if self.count_users(box_id=9220) != 30:
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Enable72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000943], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000943], state=0):
            # On
            return Activate72230(self.ctx)
        if self.count_users(box_id=9220) != 30:
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Activate72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220], visible=True)
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True)
        self.set_interact_object(trigger_ids=[10000943], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 30:
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay72230(self.ctx)


class Delay72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000959], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220) != 30:
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000959], state=0):
            # Off
            return DeActivate72230(self.ctx)


class DeActivate72230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8220])
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22') == 10:
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8221,8222,8223,8224,8225,8226,8227,8228])
        self.set_effect(trigger_ids=[8220])
        self.set_interact_object(trigger_ids=[10000943], state=0) # On
        self.set_interact_object(trigger_ids=[10000959], state=0) # Off
        self.set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
