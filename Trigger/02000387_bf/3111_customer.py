""" trigger/02000387_bf/3111_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001101], state=0) # Greeting
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
        self.spawn_monster(spawn_ids=[3111], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9130, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9131, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3111, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9132, spawn_ids=[0]):
            # 두 번째 대기 손님이 없으면
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3111, patrol_name='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9133, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3111, patrol_name='MS2PatrolData_303')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9133, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9133, spawn_ids=[3111]):
            # 카운터 앞에 도착했으면
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001101], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001101], state=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001101], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return PickItem_30000644(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000679(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000683(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000685(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000686(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000716(self.ctx)


# 30000644
class PickItem_30000644(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000644)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Iceland/Indoor/ic_in_cubric_box_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000644(self.ctx)


class DetectItem_30000644(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000644):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000644):
            # 오답
            return WrongItem(self.ctx)


# 30000679
class PickItem_30000679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000679)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Royalcity/Field/ry_fi_prop_yacht_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000679(self.ctx)


class DetectItem_30000679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000679):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000679):
            # 오답
            return WrongItem(self.ctx)


# 30000683
class PickItem_30000683(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000683)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Orient/Field/or_fi_prop_ship_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000683(self.ctx)


class DetectItem_30000683(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000683):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000683):
            # 오답
            return WrongItem(self.ctx)


# 30000685
class PickItem_30000685(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000685)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Lith/Field/li_fi_prop_anchor_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000685(self.ctx)


class DetectItem_30000685(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000685):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000685):
            # 오답
            return WrongItem(self.ctx)


# 30000686
class PickItem_30000686(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000686)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Lith/Field/li_fi_prop_tube_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000686(self.ctx)


class DetectItem_30000686(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000686):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000686):
            # 오답
            return WrongItem(self.ctx)


# 30000716
class PickItem_30000716(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000716)
        self.add_effect_nif(spawn_id=3111, nif_path='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=0):
            return DetectItem_30000716(self.ctx)


class DetectItem_30000716(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9203], item_id=30000716):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9203], item_id=30000716):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=3111)
        self.set_dialogue(type=1, spawn_id=3111, script='$02000387_BF__3111_CUSTOMER__0$', time=3)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3111, patrol_name='MS2PatrolData_333')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9303, spawn_ids=[3111]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[3111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=3111)
        self.set_dialogue(type=1, spawn_id=3111, script='$02000387_BF__3111_CUSTOMER__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') >= 30000644:
            return PickItem_30000644(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000679:
            return PickItem_30000679(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000683:
            return PickItem_30000683(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000685:
            return PickItem_30000685(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000686:
            return PickItem_30000686(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000716:
            return PickItem_30000716(self.ctx)


initial_state = Wait
