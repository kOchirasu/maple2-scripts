""" trigger/02000387_bf/2002_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001093], state=0) # Greeting
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
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9120, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9121, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9122, spawn_ids=[0]):
            # 두 번째 대기 손님이 없으면
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9123, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9123, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9123, spawn_ids=[2002]):
            # 카운터 앞에 도착했으면
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001093], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001093], state=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001093], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return PickItem_30000617(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000618(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000619(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000620(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000621(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000622(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000623(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000624(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000625(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000626(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000627(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000628(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000629(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000630(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000631(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000632(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000633(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000634(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000635(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000636(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000637(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000638(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000639(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000640(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000641(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000642(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000643(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000644(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000645(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000646(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000647(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000648(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000649(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000650(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000651(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000652(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000653(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000654(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000655(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000656(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000657(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000658(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000659(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000660(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000661(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000662(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000663(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000664(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000665(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000666(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000667(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000668(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000669(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000670(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000671(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000672(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000673(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000674(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000675(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000676(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000677(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000678(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000679(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000680(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000681(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000682(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000683(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000684(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000685(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000686(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000687(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000688(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000689(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000690(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000691(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000692(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000693(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000694(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000695(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000696(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000697(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000698(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000699(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000700(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000701(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000702(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000703(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000704(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000705(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000706(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000707(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000708(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000709(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000710(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000711(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000712(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000713(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000714(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000715(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000716(self.ctx)


# 30000617
class PickItem_30000617(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000617)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Field/co_fi_prop_game_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000617(self.ctx)


class DetectItem_30000617(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000617):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000617):
            # 오답
            return WrongItem(self.ctx)


# 30000618
class PickItem_30000618(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000618)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Field/co_fi_prop_game_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000618(self.ctx)


class DetectItem_30000618(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000618):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000618):
            # 오답
            return WrongItem(self.ctx)


# 30000619
class PickItem_30000619(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000619)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Field/co_fi_prop_lamp_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000619(self.ctx)


class DetectItem_30000619(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000619):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000619):
            # 오답
            return WrongItem(self.ctx)


class PickItem_30000620(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000620)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Henesys/Indoor/he_in_prop_fireplace_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000620(self.ctx)


class DetectItem_30000620(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000620):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000620):
            # 오답
            return WrongItem(self.ctx)


# 30000621
class PickItem_30000621(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000621)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_sandbag_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000621(self.ctx)


class DetectItem_30000621(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000621):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000621):
            # 오답
            return WrongItem(self.ctx)


# 30000622
class PickItem_30000622(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000622)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Iceland/Indoor/ic_in_prop_snowball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000622(self.ctx)


class DetectItem_30000622(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000622):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000622):
            # 오답
            return WrongItem(self.ctx)


# 30000623
class PickItem_30000623(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000623)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000623(self.ctx)


class DetectItem_30000623(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000623):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000623):
            # 오답
            return WrongItem(self.ctx)


# 30000624
class PickItem_30000624(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000624)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_bath_C01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000624(self.ctx)


class DetectItem_30000624(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000624):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000624):
            # 오답
            return WrongItem(self.ctx)


# 30000625
class PickItem_30000625(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000625)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000625(self.ctx)


class DetectItem_30000625(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000625):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000625):
            # 오답
            return WrongItem(self.ctx)


# 30000626
class PickItem_30000626(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000626)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_fridge_C02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000626(self.ctx)


class DetectItem_30000626(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000626):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000626):
            # 오답
            return WrongItem(self.ctx)


# 30000627
class PickItem_30000627(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000627)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_fridge_D03.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000627(self.ctx)


class DetectItem_30000627(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000627):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000627):
            # 오답
            return WrongItem(self.ctx)


# 30000628
class PickItem_30000628(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000628)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_display_C01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000628(self.ctx)


class DetectItem_30000628(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000628):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000628):
            # 오답
            return WrongItem(self.ctx)


# 30000629
class PickItem_30000629(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000629)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_fridge_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000629(self.ctx)


class DetectItem_30000629(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000629):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000629):
            # 오답
            return WrongItem(self.ctx)


# 30000630
class PickItem_30000630(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000630)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_display_C02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000630(self.ctx)


class DetectItem_30000630(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000630):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000630):
            # 오답
            return WrongItem(self.ctx)


# 30000631
class PickItem_30000631(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000631)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_washstand_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000631(self.ctx)


class DetectItem_30000631(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000631):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000631):
            # 오답
            return WrongItem(self.ctx)


# 30000632
class PickItem_30000632(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000632)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_sink_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000632(self.ctx)


class DetectItem_30000632(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000632):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000632):
            # 오답
            return WrongItem(self.ctx)


# 30000633
class PickItem_30000633(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000633)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_sink_A03.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000633(self.ctx)


class DetectItem_30000633(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000633):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000633):
            # 오답
            return WrongItem(self.ctx)


# 30000634
class PickItem_30000634(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000634)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_tv_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000634(self.ctx)


class DetectItem_30000634(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000634):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000634):
            # 오답
            return WrongItem(self.ctx)


# 30000635
class PickItem_30000635(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000635)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_tv_C01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000635(self.ctx)


class DetectItem_30000635(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000635):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000635):
            # 오답
            return WrongItem(self.ctx)


# 30000636
class PickItem_30000636(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000636)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_toilet_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000636(self.ctx)


class DetectItem_30000636(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000636):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000636):
            # 오답
            return WrongItem(self.ctx)


# 30000637
class PickItem_30000637(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000637)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_washer_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000637(self.ctx)


class DetectItem_30000637(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000637):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000637):
            # 오답
            return WrongItem(self.ctx)


# 30000638
class PickItem_30000638(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000638)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_fan_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000638(self.ctx)


class DetectItem_30000638(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000638):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000638):
            # 오답
            return WrongItem(self.ctx)


# 30000639
class PickItem_30000639(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000639)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000639(self.ctx)


class DetectItem_30000639(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000639):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000639):
            # 오답
            return WrongItem(self.ctx)


# 30000640
class PickItem_30000640(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000640)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000640(self.ctx)


class DetectItem_30000640(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000640):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000640):
            # 오답
            return WrongItem(self.ctx)


# 30000641
class PickItem_30000641(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000641)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Henesys/Indoor/he_in_prop_kettle_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000641(self.ctx)


class DetectItem_30000641(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000641):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000641):
            # 오답
            return WrongItem(self.ctx)


# 30000642
class PickItem_30000642(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000642)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_locker_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000642(self.ctx)


class DetectItem_30000642(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000642):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000642):
            # 오답
            return WrongItem(self.ctx)


# 30000643
class PickItem_30000643(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000643)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_locker_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000643(self.ctx)


class DetectItem_30000643(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000643):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000643):
            # 오답
            return WrongItem(self.ctx)


# 30000644
class PickItem_30000644(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000644)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Iceland/Indoor/ic_in_cubric_box_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000644(self.ctx)


class DetectItem_30000644(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000644):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000644):
            # 오답
            return WrongItem(self.ctx)


# 30000645
class PickItem_30000645(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000645)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Field/tr_fi_prop_swing_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000645(self.ctx)


class DetectItem_30000645(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000645):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000645):
            # 오답
            return WrongItem(self.ctx)


# 30000646
class PickItem_30000646(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000646)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/UGC/Indoor/ugc_in_funct_cook_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000646(self.ctx)


class DetectItem_30000646(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000646):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000646):
            # 오답
            return WrongItem(self.ctx)


# 30000647
class PickItem_30000647(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000647)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/UGC/Indoor/ugc_in_funct_alchemy_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000647(self.ctx)


class DetectItem_30000647(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000647):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000647):
            # 오답
            return WrongItem(self.ctx)


# 30000648
class PickItem_30000648(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000648)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/UGC/Indoor/ugc_in_funct_alchemy_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000648(self.ctx)


class DetectItem_30000648(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000648):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000648):
            # 오답
            return WrongItem(self.ctx)


# 30000649
class PickItem_30000649(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000649)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_mirror_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000649(self.ctx)


class DetectItem_30000649(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000649):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000649):
            # 오답
            return WrongItem(self.ctx)


# 30000650
class PickItem_30000650(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000650)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_easel_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000650(self.ctx)


class DetectItem_30000650(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000650):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000650):
            # 오답
            return WrongItem(self.ctx)


# 30000651
class PickItem_30000651(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000651)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_wardrop_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000651(self.ctx)


class DetectItem_30000651(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000651):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000651):
            # 오답
            return WrongItem(self.ctx)


# 30000652
class PickItem_30000652(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000652)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Indoor/co_in_prop_brazier_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000652(self.ctx)


class DetectItem_30000652(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000652):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000652):
            # 오답
            return WrongItem(self.ctx)


# 30000653
class PickItem_30000653(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000653)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_tray_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000653(self.ctx)


class DetectItem_30000653(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000653):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000653):
            # 오답
            return WrongItem(self.ctx)


# 30000654
class PickItem_30000654(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000654)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_sofa_E01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000654(self.ctx)


class DetectItem_30000654(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000654):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000654):
            # 오답
            return WrongItem(self.ctx)


# 30000655
class PickItem_30000655(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000655)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_amp_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000655(self.ctx)


class DetectItem_30000655(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000655):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000655):
            # 오답
            return WrongItem(self.ctx)


# 30000656
class PickItem_30000656(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000656)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/SF/Indoor/sf_in_prop_bed_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000656(self.ctx)


class DetectItem_30000656(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000656):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000656):
            # 오답
            return WrongItem(self.ctx)


# 30000657
class PickItem_30000657(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000657)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000657(self.ctx)


class DetectItem_30000657(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000657):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000657):
            # 오답
            return WrongItem(self.ctx)


# 30000658
class PickItem_30000658(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000658)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_ringer_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000658(self.ctx)


class DetectItem_30000658(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000658):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000658):
            # 오답
            return WrongItem(self.ctx)


# 30000659
class PickItem_30000659(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000659)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Indoor/co_in_prop_guestbook_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000659(self.ctx)


class DetectItem_30000659(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000659):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000659):
            # 오답
            return WrongItem(self.ctx)


# 30000660
class PickItem_30000660(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000660)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_display_B02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000660(self.ctx)


class DetectItem_30000660(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000660):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000660):
            # 오답
            return WrongItem(self.ctx)


# 30000661
class PickItem_30000661(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000661)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_cubric_fishtank_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000661(self.ctx)


class DetectItem_30000661(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000661):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000661):
            # 오답
            return WrongItem(self.ctx)


# 30000662
class PickItem_30000662(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000662)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_basketball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000662(self.ctx)


class DetectItem_30000662(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000662):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000662):
            # 오답
            return WrongItem(self.ctx)


# 30000663
class PickItem_30000663(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000663)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_running_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000663(self.ctx)


class DetectItem_30000663(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000663):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000663):
            # 오답
            return WrongItem(self.ctx)


# 30000664
class PickItem_30000664(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000664)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_trampoline_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000664(self.ctx)


class DetectItem_30000664(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000664):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000664):
            # 오답
            return WrongItem(self.ctx)


# 30000665
class PickItem_30000665(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000665)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_baseballcart_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000665(self.ctx)


class DetectItem_30000665(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000665):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000665):
            # 오답
            return WrongItem(self.ctx)


# 30000666
class PickItem_30000666(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000666)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_basketball_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000666(self.ctx)


class DetectItem_30000666(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000666):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000666):
            # 오답
            return WrongItem(self.ctx)


# 30000667
class PickItem_30000667(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000667)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_handball_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000667(self.ctx)


class DetectItem_30000667(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000667):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000667):
            # 오답
            return WrongItem(self.ctx)


# 30000668
class PickItem_30000668(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000668)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_cranegame_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000668(self.ctx)


class DetectItem_30000668(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000668):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000668):
            # 오답
            return WrongItem(self.ctx)


# 30000669
class PickItem_30000669(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000669)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_chandelier_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000669(self.ctx)


class DetectItem_30000669(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000669):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000669):
            # 오답
            return WrongItem(self.ctx)


# 30000670
class PickItem_30000670(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000670)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_goalpost_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000670(self.ctx)


class DetectItem_30000670(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000670):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000670):
            # 오답
            return WrongItem(self.ctx)


# 30000671
class PickItem_30000671(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000671)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_photosticker_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000671(self.ctx)


class DetectItem_30000671(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000671):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000671):
            # 오답
            return WrongItem(self.ctx)


# 30000672
class PickItem_30000672(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000672)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_pingpong_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000672(self.ctx)


class DetectItem_30000672(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000672):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000672):
            # 오답
            return WrongItem(self.ctx)


# 30000673
class PickItem_30000673(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000673)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_pooltable_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000673(self.ctx)


class DetectItem_30000673(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000673):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000673):
            # 오답
            return WrongItem(self.ctx)


# 30000674
class PickItem_30000674(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000674)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_pump_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000674(self.ctx)


class DetectItem_30000674(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000674):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000674):
            # 오답
            return WrongItem(self.ctx)


# 30000675
class PickItem_30000675(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000675)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_sewingmachine_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000675(self.ctx)


class DetectItem_30000675(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000675):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000675):
            # 오답
            return WrongItem(self.ctx)


# 30000676
class PickItem_30000676(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000676)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_soccertable_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000676(self.ctx)


class DetectItem_30000676(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000676):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000676):
            # 오답
            return WrongItem(self.ctx)


# 30000677
class PickItem_30000677(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000677)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Field/ry_fi_prop_plane_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000677(self.ctx)


class DetectItem_30000677(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000677):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000677):
            # 오답
            return WrongItem(self.ctx)


# 30000678
class PickItem_30000678(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000678)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Field/ry_fi_prop_hammock_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000678(self.ctx)


class DetectItem_30000678(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000678):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000678):
            # 오답
            return WrongItem(self.ctx)


# 30000679
class PickItem_30000679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000679)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Field/ry_fi_prop_yacht_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000679(self.ctx)


class DetectItem_30000679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000679):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000679):
            # 오답
            return WrongItem(self.ctx)


# 30000680
class PickItem_30000680(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000680)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_grill_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000680(self.ctx)


class DetectItem_30000680(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000680):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000680):
            # 오답
            return WrongItem(self.ctx)


# 30000681
class PickItem_30000681(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000681)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Orient/Field/or_fi_prop_seesaw_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000681(self.ctx)


class DetectItem_30000681(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000681):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000681):
            # 오답
            return WrongItem(self.ctx)


# 30000682
class PickItem_30000682(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000682)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_display_E01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000682(self.ctx)


class DetectItem_30000682(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000682):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000682):
            # 오답
            return WrongItem(self.ctx)


# 30000683
class PickItem_30000683(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000683)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Orient/Field/or_fi_prop_ship_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000683(self.ctx)


class DetectItem_30000683(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000683):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000683):
            # 오답
            return WrongItem(self.ctx)


# 30000684
class PickItem_30000684(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000684)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Ludibrium/Field/lu_fi_prop_rocket_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000684(self.ctx)


class DetectItem_30000684(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000684):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000684):
            # 오답
            return WrongItem(self.ctx)


# 30000685
class PickItem_30000685(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000685)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Lith/Field/li_fi_prop_anchor_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000685(self.ctx)


class DetectItem_30000685(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000685):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000685):
            # 오답
            return WrongItem(self.ctx)


# 30000686
class PickItem_30000686(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000686)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Lith/Field/li_fi_prop_tube_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000686(self.ctx)


class DetectItem_30000686(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000686):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000686):
            # 오답
            return WrongItem(self.ctx)


# 30000687
class PickItem_30000687(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000687)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_beanbag_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000687(self.ctx)


class DetectItem_30000687(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000687):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000687):
            # 오답
            return WrongItem(self.ctx)


# 30000688
class PickItem_30000688(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000688)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_surgerylamp_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000688(self.ctx)


class DetectItem_30000688(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000688):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000688):
            # 오답
            return WrongItem(self.ctx)


# 30000689
class PickItem_30000689(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000689)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_surgery_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000689(self.ctx)


class DetectItem_30000689(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000689):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000689):
            # 오답
            return WrongItem(self.ctx)


# 30000690
class PickItem_30000690(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000690)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_sofa_D01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000690(self.ctx)


class DetectItem_30000690(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000690):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000690):
            # 오답
            return WrongItem(self.ctx)


# 30000691
class PickItem_30000691(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000691)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_paintbag_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000691(self.ctx)


class DetectItem_30000691(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000691):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000691):
            # 오답
            return WrongItem(self.ctx)


# 30000692
class PickItem_30000692(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000692)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_dresser_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000692(self.ctx)


class DetectItem_30000692(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000692):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000692):
            # 오답
            return WrongItem(self.ctx)


# 30000693
class PickItem_30000693(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000693)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_massage_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000693(self.ctx)


class DetectItem_30000693(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000693):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000693):
            # 오답
            return WrongItem(self.ctx)


# 30000694
class PickItem_30000694(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000694)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Indoor/ke_in_prop_catower_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000694(self.ctx)


class DetectItem_30000694(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000694):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000694):
            # 오답
            return WrongItem(self.ctx)


# 30000695
class PickItem_30000695(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000695)
        self.add_effect_nif(spawn_id=2002, nif_path='Npc/Etc/UGC_SportsCar_Npc/UGC_SportsCar_Npc_02.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000695(self.ctx)


class DetectItem_30000695(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000695):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000695):
            # 오답
            return WrongItem(self.ctx)


# 30000696
class PickItem_30000696(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000696)
        self.add_effect_nif(spawn_id=2002, nif_path='Npc/Etc/UGC_F1RacingCar/UGC_F1RacingCar_01.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000696(self.ctx)


class DetectItem_30000696(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000696):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000696):
            # 오답
            return WrongItem(self.ctx)


# 30000697
class PickItem_30000697(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000697)
        self.add_effect_nif(spawn_id=2002, nif_path='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000697(self.ctx)


class DetectItem_30000697(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000697):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000697):
            # 오답
            return WrongItem(self.ctx)


# 30000698
class PickItem_30000698(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000698)
        self.add_effect_nif(spawn_id=2002, nif_path='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', is_outline=True, scale=1.2, rotate_z=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000698(self.ctx)


class DetectItem_30000698(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000698):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000698):
            # 오답
            return WrongItem(self.ctx)


# 30000699
class PickItem_30000699(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000699)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Field/co_fi_prop_tent_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000699(self.ctx)


class DetectItem_30000699(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000699):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000699):
            # 오답
            return WrongItem(self.ctx)


# 30000700
class PickItem_30000700(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000700)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Royalcity/Indoor/ry_in_prop_djtable_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000700(self.ctx)


class DetectItem_30000700(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000700):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000700):
            # 오답
            return WrongItem(self.ctx)


# 30000701
class PickItem_30000701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000701)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Indoor/co_in_prop_security_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000701(self.ctx)


class DetectItem_30000701(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000701):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000701):
            # 오답
            return WrongItem(self.ctx)


# 30000702
class PickItem_30000702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000702)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Tria/Indoor/tr_in_prop_workit_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000702(self.ctx)


class DetectItem_30000702(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000702):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000702):
            # 오답
            return WrongItem(self.ctx)


# 30000703
class PickItem_30000703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000703)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000703(self.ctx)


class DetectItem_30000703(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000703):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000703):
            # 오답
            return WrongItem(self.ctx)


# 30000704
class PickItem_30000704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000704)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000704(self.ctx)


class DetectItem_30000704(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000704):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000704):
            # 오답
            return WrongItem(self.ctx)


# 30000705
class PickItem_30000705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000705)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000705(self.ctx)


class DetectItem_30000705(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000705):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000705):
            # 오답
            return WrongItem(self.ctx)


# 30000706
class PickItem_30000706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000706)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Indoor/co_in_prop_icebox_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000706(self.ctx)


class DetectItem_30000706(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000706):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000706):
            # 오답
            return WrongItem(self.ctx)


# 30000707
class PickItem_30000707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000707)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Henesys/Indoor/he_in_prop_cushiona_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000707(self.ctx)


class DetectItem_30000707(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000707):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000707):
            # 오답
            return WrongItem(self.ctx)


# 30000708
class PickItem_30000708(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000708)
        self.add_effect_nif(spawn_id=2002, nif_path='Effect/BG/Liftup/co_liftup_piano_B01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000708(self.ctx)


class DetectItem_30000708(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000708):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000708):
            # 오답
            return WrongItem(self.ctx)


# 30000709
class PickItem_30000709(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000709)
        self.add_effect_nif(spawn_id=2002, nif_path='Effect/BG/Liftup/co_liftup_vibraphone_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000709(self.ctx)


class DetectItem_30000709(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000709):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000709):
            # 오답
            return WrongItem(self.ctx)


# 30000710
class PickItem_30000710(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000710)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Common/Indoor/co_in_prop_camera_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000710(self.ctx)


class DetectItem_30000710(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000710):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000710):
            # 오답
            return WrongItem(self.ctx)


# 30000711
class PickItem_30000711(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000711)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/UGC/Indoor/ugc_in_funct_workstone_G01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000711(self.ctx)


class DetectItem_30000711(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000711):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000711):
            # 오답
            return WrongItem(self.ctx)


# 30000712
class PickItem_30000712(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000712)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Orient/Indoor/or_in_prop_incense_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000712(self.ctx)


class DetectItem_30000712(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000712):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000712):
            # 오답
            return WrongItem(self.ctx)


# 30000713
class PickItem_30000713(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000713)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Steampunk/Indoor/sp_in_prop_desk_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000713(self.ctx)


class DetectItem_30000713(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000713):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000713):
            # 오답
            return WrongItem(self.ctx)


# 30000714
class PickItem_30000714(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000714)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/SF/Field/sf_fi_prop_incubator_D01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000714(self.ctx)


class DetectItem_30000714(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000714):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000714):
            # 오답
            return WrongItem(self.ctx)


# 30000715
class PickItem_30000715(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000715)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000715(self.ctx)


class DetectItem_30000715(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000715):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000715):
            # 오답
            return WrongItem(self.ctx)


# 30000716
class PickItem_30000716(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000716)
        self.add_effect_nif(spawn_id=2002, nif_path='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=0):
            return DetectItem_30000716(self.ctx)


class DetectItem_30000716(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9202], item_id=30000716):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9202], item_id=30000716):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=2002)
        self.set_dialogue(type=1, spawn_id=2002, script='$02000387_BF__2002_CUSTOMER__0$', time=3)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_222')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9302, spawn_ids=[2002]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=2002)
        self.set_dialogue(type=1, spawn_id=2002, script='$02000387_BF__2002_CUSTOMER__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') == 30000617:
            return PickItem_30000617(self.ctx)
        if self.user_value(key='ItemNumber') == 30000618:
            return PickItem_30000618(self.ctx)
        if self.user_value(key='ItemNumber') == 30000619:
            return PickItem_30000619(self.ctx)
        if self.user_value(key='ItemNumber') == 30000620:
            return PickItem_30000620(self.ctx)
        if self.user_value(key='ItemNumber') == 30000621:
            return PickItem_30000621(self.ctx)
        if self.user_value(key='ItemNumber') == 30000622:
            return PickItem_30000622(self.ctx)
        if self.user_value(key='ItemNumber') == 30000623:
            return PickItem_30000623(self.ctx)
        if self.user_value(key='ItemNumber') == 30000624:
            return PickItem_30000624(self.ctx)
        if self.user_value(key='ItemNumber') == 30000625:
            return PickItem_30000625(self.ctx)
        if self.user_value(key='ItemNumber') == 30000626:
            return PickItem_30000626(self.ctx)
        if self.user_value(key='ItemNumber') == 30000627:
            return PickItem_30000627(self.ctx)
        if self.user_value(key='ItemNumber') == 30000628:
            return PickItem_30000628(self.ctx)
        if self.user_value(key='ItemNumber') == 30000629:
            return PickItem_30000629(self.ctx)
        if self.user_value(key='ItemNumber') == 30000630:
            return PickItem_30000630(self.ctx)
        if self.user_value(key='ItemNumber') == 30000631:
            return PickItem_30000631(self.ctx)
        if self.user_value(key='ItemNumber') == 30000632:
            return PickItem_30000632(self.ctx)
        if self.user_value(key='ItemNumber') == 30000633:
            return PickItem_30000633(self.ctx)
        if self.user_value(key='ItemNumber') == 30000634:
            return PickItem_30000634(self.ctx)
        if self.user_value(key='ItemNumber') == 30000635:
            return PickItem_30000635(self.ctx)
        if self.user_value(key='ItemNumber') == 30000636:
            return PickItem_30000636(self.ctx)
        if self.user_value(key='ItemNumber') == 30000637:
            return PickItem_30000637(self.ctx)
        if self.user_value(key='ItemNumber') == 30000638:
            return PickItem_30000638(self.ctx)
        if self.user_value(key='ItemNumber') == 30000639:
            return PickItem_30000639(self.ctx)
        if self.user_value(key='ItemNumber') == 30000640:
            return PickItem_30000640(self.ctx)
        if self.user_value(key='ItemNumber') == 30000641:
            return PickItem_30000641(self.ctx)
        if self.user_value(key='ItemNumber') == 30000642:
            return PickItem_30000642(self.ctx)
        if self.user_value(key='ItemNumber') == 30000643:
            return PickItem_30000643(self.ctx)
        if self.user_value(key='ItemNumber') == 30000644:
            return PickItem_30000644(self.ctx)
        if self.user_value(key='ItemNumber') == 30000645:
            return PickItem_30000645(self.ctx)
        if self.user_value(key='ItemNumber') == 30000646:
            return PickItem_30000646(self.ctx)
        if self.user_value(key='ItemNumber') == 30000647:
            return PickItem_30000647(self.ctx)
        if self.user_value(key='ItemNumber') == 30000648:
            return PickItem_30000648(self.ctx)
        if self.user_value(key='ItemNumber') == 30000649:
            return PickItem_30000649(self.ctx)
        if self.user_value(key='ItemNumber') == 30000650:
            return PickItem_30000650(self.ctx)
        if self.user_value(key='ItemNumber') == 30000651:
            return PickItem_30000651(self.ctx)
        if self.user_value(key='ItemNumber') == 30000652:
            return PickItem_30000652(self.ctx)
        if self.user_value(key='ItemNumber') == 30000653:
            return PickItem_30000653(self.ctx)
        if self.user_value(key='ItemNumber') == 30000654:
            return PickItem_30000654(self.ctx)
        if self.user_value(key='ItemNumber') == 30000655:
            return PickItem_30000655(self.ctx)
        if self.user_value(key='ItemNumber') == 30000656:
            return PickItem_30000656(self.ctx)
        if self.user_value(key='ItemNumber') == 30000657:
            return PickItem_30000657(self.ctx)
        if self.user_value(key='ItemNumber') == 30000658:
            return PickItem_30000658(self.ctx)
        if self.user_value(key='ItemNumber') == 30000659:
            return PickItem_30000659(self.ctx)
        if self.user_value(key='ItemNumber') == 30000660:
            return PickItem_30000660(self.ctx)
        if self.user_value(key='ItemNumber') == 30000661:
            return PickItem_30000661(self.ctx)
        if self.user_value(key='ItemNumber') == 30000662:
            return PickItem_30000662(self.ctx)
        if self.user_value(key='ItemNumber') == 30000663:
            return PickItem_30000663(self.ctx)
        if self.user_value(key='ItemNumber') == 30000664:
            return PickItem_30000664(self.ctx)
        if self.user_value(key='ItemNumber') == 30000665:
            return PickItem_30000665(self.ctx)
        if self.user_value(key='ItemNumber') == 30000666:
            return PickItem_30000666(self.ctx)
        if self.user_value(key='ItemNumber') == 30000667:
            return PickItem_30000667(self.ctx)
        if self.user_value(key='ItemNumber') == 30000668:
            return PickItem_30000668(self.ctx)
        if self.user_value(key='ItemNumber') == 30000669:
            return PickItem_30000669(self.ctx)
        if self.user_value(key='ItemNumber') == 30000670:
            return PickItem_30000670(self.ctx)
        if self.user_value(key='ItemNumber') == 30000671:
            return PickItem_30000671(self.ctx)
        if self.user_value(key='ItemNumber') == 30000672:
            return PickItem_30000672(self.ctx)
        if self.user_value(key='ItemNumber') == 30000673:
            return PickItem_30000673(self.ctx)
        if self.user_value(key='ItemNumber') == 30000674:
            return PickItem_30000674(self.ctx)
        if self.user_value(key='ItemNumber') == 30000675:
            return PickItem_30000675(self.ctx)
        if self.user_value(key='ItemNumber') == 30000676:
            return PickItem_30000676(self.ctx)
        if self.user_value(key='ItemNumber') == 30000677:
            return PickItem_30000677(self.ctx)
        if self.user_value(key='ItemNumber') == 30000678:
            return PickItem_30000678(self.ctx)
        if self.user_value(key='ItemNumber') == 30000679:
            return PickItem_30000679(self.ctx)
        if self.user_value(key='ItemNumber') == 30000680:
            return PickItem_30000680(self.ctx)
        if self.user_value(key='ItemNumber') == 30000681:
            return PickItem_30000681(self.ctx)
        if self.user_value(key='ItemNumber') == 30000682:
            return PickItem_30000682(self.ctx)
        if self.user_value(key='ItemNumber') == 30000683:
            return PickItem_30000683(self.ctx)
        if self.user_value(key='ItemNumber') == 30000684:
            return PickItem_30000684(self.ctx)
        if self.user_value(key='ItemNumber') == 30000685:
            return PickItem_30000685(self.ctx)
        if self.user_value(key='ItemNumber') == 30000686:
            return PickItem_30000686(self.ctx)
        if self.user_value(key='ItemNumber') == 30000687:
            return PickItem_30000687(self.ctx)
        if self.user_value(key='ItemNumber') == 30000688:
            return PickItem_30000688(self.ctx)
        if self.user_value(key='ItemNumber') == 30000689:
            return PickItem_30000689(self.ctx)
        if self.user_value(key='ItemNumber') == 30000690:
            return PickItem_30000690(self.ctx)
        if self.user_value(key='ItemNumber') == 30000691:
            return PickItem_30000691(self.ctx)
        if self.user_value(key='ItemNumber') == 30000692:
            return PickItem_30000692(self.ctx)
        if self.user_value(key='ItemNumber') == 30000693:
            return PickItem_30000693(self.ctx)
        if self.user_value(key='ItemNumber') == 30000694:
            return PickItem_30000694(self.ctx)
        if self.user_value(key='ItemNumber') == 30000695:
            return PickItem_30000695(self.ctx)
        if self.user_value(key='ItemNumber') == 30000696:
            return PickItem_30000696(self.ctx)
        if self.user_value(key='ItemNumber') == 30000697:
            return PickItem_30000697(self.ctx)
        if self.user_value(key='ItemNumber') == 30000698:
            return PickItem_30000698(self.ctx)
        if self.user_value(key='ItemNumber') == 30000699:
            return PickItem_30000699(self.ctx)
        if self.user_value(key='ItemNumber') == 30000700:
            return PickItem_30000700(self.ctx)
        if self.user_value(key='ItemNumber') == 30000701:
            return PickItem_30000701(self.ctx)
        if self.user_value(key='ItemNumber') == 30000702:
            return PickItem_30000702(self.ctx)
        if self.user_value(key='ItemNumber') == 30000703:
            return PickItem_30000703(self.ctx)
        if self.user_value(key='ItemNumber') == 30000704:
            return PickItem_30000704(self.ctx)
        if self.user_value(key='ItemNumber') == 30000705:
            return PickItem_30000705(self.ctx)
        if self.user_value(key='ItemNumber') == 30000706:
            return PickItem_30000706(self.ctx)
        if self.user_value(key='ItemNumber') == 30000707:
            return PickItem_30000707(self.ctx)
        if self.user_value(key='ItemNumber') == 30000708:
            return PickItem_30000708(self.ctx)
        if self.user_value(key='ItemNumber') == 30000709:
            return PickItem_30000709(self.ctx)
        if self.user_value(key='ItemNumber') == 30000710:
            return PickItem_30000710(self.ctx)
        if self.user_value(key='ItemNumber') == 30000711:
            return PickItem_30000711(self.ctx)
        if self.user_value(key='ItemNumber') == 30000712:
            return PickItem_30000712(self.ctx)
        if self.user_value(key='ItemNumber') == 30000713:
            return PickItem_30000713(self.ctx)
        if self.user_value(key='ItemNumber') == 30000714:
            return PickItem_30000714(self.ctx)
        if self.user_value(key='ItemNumber') == 30000715:
            return PickItem_30000715(self.ctx)
        if self.user_value(key='ItemNumber') == 30000716:
            return PickItem_30000716(self.ctx)


initial_state = Wait
