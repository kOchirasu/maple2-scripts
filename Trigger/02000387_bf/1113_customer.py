""" trigger/02000387_bf/1113_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001099], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CustomerEnter') >= 1:
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9110, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9111, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1113, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9112, spawn_ids=[0]):
            # 두 번째 대기 손님이 없으면
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1113, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9113, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1113, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9113, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9113, spawn_ids=[1113]):
            # 카운터 앞에 도착했으면
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001099], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001099], state=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001099], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return PickItem_30000617(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000618(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000622(self.ctx)
        if self.random_condition(weight=1.0):
            return None # Missing State: PickItem_30000661
        if self.random_condition(weight=1.0):
            return PickItem_30000662(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000664(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000665(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000666(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000667(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000670(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000681(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000684(self.ctx)


# 30000617
class PickItem_30000617(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000617)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Common/Field/co_fi_prop_game_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000617(self.ctx)


class DetectItem_30000617(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000617):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000617):
            # 오답
            return WrongItem(self.ctx)


# 30000618
class PickItem_30000618(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000618)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Common/Field/co_fi_prop_game_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000618(self.ctx)


class DetectItem_30000618(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000618):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000618):
            # 오답
            return WrongItem(self.ctx)


# 30000622
class PickItem_30000622(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000622)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Iceland/Indoor/ic_in_prop_snowball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000622(self.ctx)


class DetectItem_30000622(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000622):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000622):
            # 오답
            return WrongItem(self.ctx)


# 30000662
class PickItem_30000662(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000662)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_basketball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000662(self.ctx)


class DetectItem_30000662(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000662):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000662):
            # 오답
            return WrongItem(self.ctx)


# 30000664
class PickItem_30000664(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000664)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_trampoline_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000664(self.ctx)


class DetectItem_30000664(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000664):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000664):
            # 오답
            return WrongItem(self.ctx)


# 30000665
class PickItem_30000665(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000665)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_baseballcart_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000665(self.ctx)


class DetectItem_30000665(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000665):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000665):
            # 오답
            return WrongItem(self.ctx)


# 30000666
class PickItem_30000666(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000666)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_basketball_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000666(self.ctx)


class DetectItem_30000666(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000666):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000666):
            # 오답
            return WrongItem(self.ctx)


# 30000667
class PickItem_30000667(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000667)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_handball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000667(self.ctx)


class DetectItem_30000667(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000667):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000667):
            # 오답
            return WrongItem(self.ctx)


# 30000670
class PickItem_30000670(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000670)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Royalcity/Indoor/ry_in_prop_goalpost_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000670(self.ctx)


class DetectItem_30000670(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000670):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000670):
            # 오답
            return WrongItem(self.ctx)


# 30000681
class PickItem_30000681(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000681)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Orient/Field/or_fi_prop_seesaw_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000681(self.ctx)


class DetectItem_30000681(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000681):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000681):
            # 오답
            return WrongItem(self.ctx)


# 30000684
class PickItem_30000684(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000684)
        self.add_effect_nif(spawn_id=1113, nif_path='Map/Ludibrium/Field/lu_fi_prop_rocket_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000684(self.ctx)


class DetectItem_30000684(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000684):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000684):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=1113)
        self.set_dialogue(type=1, spawn_id=1113, script='$02000387_BF__1113_CUSTOMER__0$', time=3)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1113, patrol_name='MS2PatrolData_111')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9301, spawn_ids=[1113]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=1113)
        self.set_dialogue(type=1, spawn_id=1113, script='$02000387_BF__1113_CUSTOMER__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') >= 30000617:
            return PickItem_30000617(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000618:
            return PickItem_30000618(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000622:
            return PickItem_30000622(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000661:
            return None # Missing State: PickItem_30000661
        if self.user_value(key='ItemNumber') >= 30000662:
            return PickItem_30000662(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000664:
            return PickItem_30000664(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000665:
            return PickItem_30000665(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000666:
            return PickItem_30000666(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000667:
            return PickItem_30000667(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000670:
            return PickItem_30000670(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000681:
            return PickItem_30000681(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000684:
            return PickItem_30000684(self.ctx)


initial_state = Wait
