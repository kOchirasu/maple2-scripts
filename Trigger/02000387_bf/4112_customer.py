""" trigger/02000387_bf/4112_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001102], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CustomerEnter') == 1:
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4112], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9140, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9141, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4112, patrol_name='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9142, spawn_ids=[0]):
            # 두 번째 대기 손님이 없으면
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4112, patrol_name='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9143, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4112, patrol_name='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9143, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9143, spawn_ids=[4112]):
            # 카운터 앞에 도착했으면
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001102], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001102], state=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001102], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return PickItem_30000649(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000657(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000697(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000698(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000701(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000716(self.ctx)


# 30000649
class PickItem_30000649(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000649)
        self.add_effect_nif(spawn_id=4112, nif_path='Map/Tria/Indoor/tr_in_prop_mirror_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000649(self.ctx)


class DetectItem_30000649(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000649):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000649):
            # 오답
            return WrongItem(self.ctx)


# 30000657
class PickItem_30000657(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000657)
        self.add_effect_nif(spawn_id=4112, nif_path='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000657(self.ctx)


class DetectItem_30000657(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000657):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000657):
            # 오답
            return WrongItem(self.ctx)


# 30000697
class PickItem_30000697(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000697)
        self.add_effect_nif(spawn_id=4112, nif_path='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000697(self.ctx)


class DetectItem_30000697(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000697):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000697):
            # 오답
            return WrongItem(self.ctx)


# 30000698
class PickItem_30000698(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000698)
        self.add_effect_nif(spawn_id=4112, nif_path='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000698(self.ctx)


class DetectItem_30000698(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000698):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000698):
            # 오답
            return WrongItem(self.ctx)


# 30000701
class PickItem_30000701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000701)
        self.add_effect_nif(spawn_id=4112, nif_path='Map/Common/Indoor/co_in_prop_security_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000701(self.ctx)


class DetectItem_30000701(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000701):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000701):
            # 오답
            return WrongItem(self.ctx)


# 30000716
class PickItem_30000716(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000716)
        self.add_effect_nif(spawn_id=4112, nif_path='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000716(self.ctx)


class DetectItem_30000716(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000716):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000716):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=4112)
        self.set_dialogue(type=1, spawn_id=4112, script='$02000387_BF__4112_CUSTOMER__0$', time=3)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4112, patrol_name='MS2PatrolData_444')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9304, spawn_ids=[4112]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[4112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=4112)
        self.set_dialogue(type=1, spawn_id=4112, script='$02000387_BF__4112_CUSTOMER__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') == 30000649:
            return PickItem_30000649(self.ctx)
        if self.user_value(key='ItemNumber') == 30000657:
            return PickItem_30000657(self.ctx)
        if self.user_value(key='ItemNumber') == 30000697:
            return PickItem_30000697(self.ctx)
        if self.user_value(key='ItemNumber') == 30000698:
            return PickItem_30000698(self.ctx)
        if self.user_value(key='ItemNumber') == 30000701:
            return PickItem_30000701(self.ctx)
        if self.user_value(key='ItemNumber') == 30000716:
            return PickItem_30000716(self.ctx)


initial_state = Wait
