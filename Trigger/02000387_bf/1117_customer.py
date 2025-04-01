""" trigger/02000387_bf/1117_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001099], state=0) # Greeting
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
        self.spawn_monster(spawn_ids=[1117], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9110, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9111, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1117, patrol_name='MS2PatrolData_101')

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
        self.move_npc(spawn_id=1117, patrol_name='MS2PatrolData_102')

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
        self.move_npc(spawn_id=1117, patrol_name='MS2PatrolData_103')

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
        if self.npc_detected(box_id=9113, spawn_ids=[1117]):
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
            return PickItem_30000639(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000640(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000702(self.ctx)
        if self.random_condition(weight=1.0):
            return PickItem_30000713(self.ctx)


# 30000639
class PickItem_30000639(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000639)
        self.add_effect_nif(spawn_id=1117, nif_path='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000639(self.ctx)


class DetectItem_30000639(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000639):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000639):
            # 오답
            return WrongItem(self.ctx)


# 30000640
class PickItem_30000640(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000640)
        self.add_effect_nif(spawn_id=1117, nif_path='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000640(self.ctx)


class DetectItem_30000640(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000640):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000640):
            # 오답
            return WrongItem(self.ctx)


# 30000702
class PickItem_30000702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000702)
        self.add_effect_nif(spawn_id=1117, nif_path='Map/Tria/Indoor/tr_in_prop_workit_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000702(self.ctx)


class DetectItem_30000702(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000702):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000702):
            # 오답
            return WrongItem(self.ctx)


# 30000713
class PickItem_30000713(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000713)
        self.add_effect_nif(spawn_id=1117, nif_path='Map/Steampunk/Indoor/sp_in_prop_desk_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=0):
            return DetectItem_30000713(self.ctx)


class DetectItem_30000713(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9201], item_id=30000713):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9201], item_id=30000713):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=1117)
        self.set_dialogue(type=1, spawn_id=1117, script='$02000387_BF__1117_CUSTOMER__0$', time=3)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1117, patrol_name='MS2PatrolData_111')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9301, spawn_ids=[1117]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1117])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=1117)
        self.set_dialogue(type=1, spawn_id=1117, script='$02000387_BF__1117_CUSTOMER__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') == 30000617:
            return None # Missing State: PickItem_30000617
        if self.user_value(key='ItemNumber') == 30000618:
            return None # Missing State: PickItem_30000618
        if self.user_value(key='ItemNumber') == 30000619:
            return None # Missing State: PickItem_30000619
        if self.user_value(key='ItemNumber') == 30000620:
            return None # Missing State: PickItem_30000620
        if self.user_value(key='ItemNumber') == 30000621:
            return None # Missing State: PickItem_30000621
        if self.user_value(key='ItemNumber') == 30000622:
            return None # Missing State: PickItem_30000622
        if self.user_value(key='ItemNumber') == 30000623:
            return None # Missing State: PickItem_30000623
        if self.user_value(key='ItemNumber') == 30000624:
            return None # Missing State: PickItem_30000624
        if self.user_value(key='ItemNumber') == 30000625:
            return None # Missing State: PickItem_30000625
        if self.user_value(key='ItemNumber') == 30000626:
            return None # Missing State: PickItem_30000626
        if self.user_value(key='ItemNumber') == 30000627:
            return None # Missing State: PickItem_30000627
        if self.user_value(key='ItemNumber') == 30000628:
            return None # Missing State: PickItem_30000628
        if self.user_value(key='ItemNumber') == 30000629:
            return None # Missing State: PickItem_30000629
        if self.user_value(key='ItemNumber') == 30000630:
            return None # Missing State: PickItem_30000630
        if self.user_value(key='ItemNumber') == 30000631:
            return None # Missing State: PickItem_30000631
        if self.user_value(key='ItemNumber') == 30000632:
            return None # Missing State: PickItem_30000632
        if self.user_value(key='ItemNumber') == 30000633:
            return None # Missing State: PickItem_30000633
        if self.user_value(key='ItemNumber') == 30000634:
            return None # Missing State: PickItem_30000634
        if self.user_value(key='ItemNumber') == 30000635:
            return None # Missing State: PickItem_30000635
        if self.user_value(key='ItemNumber') == 30000636:
            return None # Missing State: PickItem_30000636
        if self.user_value(key='ItemNumber') == 30000637:
            return None # Missing State: PickItem_30000637
        if self.user_value(key='ItemNumber') == 30000638:
            return None # Missing State: PickItem_30000638
        if self.user_value(key='ItemNumber') == 30000639:
            return PickItem_30000639(self.ctx)
        if self.user_value(key='ItemNumber') == 30000640:
            return PickItem_30000640(self.ctx)
        if self.user_value(key='ItemNumber') == 30000641:
            return None # Missing State: PickItem_30000641
        if self.user_value(key='ItemNumber') == 30000642:
            return None # Missing State: PickItem_30000642
        if self.user_value(key='ItemNumber') == 30000643:
            return None # Missing State: PickItem_30000643
        if self.user_value(key='ItemNumber') == 30000644:
            return None # Missing State: PickItem_30000644
        if self.user_value(key='ItemNumber') == 30000645:
            return None # Missing State: PickItem_30000645
        if self.user_value(key='ItemNumber') == 30000646:
            return None # Missing State: PickItem_30000646
        if self.user_value(key='ItemNumber') == 30000647:
            return None # Missing State: PickItem_30000647
        if self.user_value(key='ItemNumber') == 30000648:
            return None # Missing State: PickItem_30000648
        if self.user_value(key='ItemNumber') == 30000649:
            return None # Missing State: PickItem_30000649
        if self.user_value(key='ItemNumber') == 30000650:
            return None # Missing State: PickItem_30000650
        if self.user_value(key='ItemNumber') == 30000651:
            return None # Missing State: PickItem_30000651
        if self.user_value(key='ItemNumber') == 30000652:
            return None # Missing State: PickItem_30000652
        if self.user_value(key='ItemNumber') == 30000653:
            return None # Missing State: PickItem_30000653
        if self.user_value(key='ItemNumber') == 30000654:
            return None # Missing State: PickItem_30000654
        if self.user_value(key='ItemNumber') == 30000655:
            return None # Missing State: PickItem_30000655
        if self.user_value(key='ItemNumber') == 30000656:
            return None # Missing State: PickItem_30000656
        if self.user_value(key='ItemNumber') == 30000657:
            return None # Missing State: PickItem_30000657
        if self.user_value(key='ItemNumber') == 30000658:
            return None # Missing State: PickItem_30000658
        if self.user_value(key='ItemNumber') == 30000659:
            return None # Missing State: PickItem_30000659
        if self.user_value(key='ItemNumber') == 30000660:
            return None # Missing State: PickItem_30000660
        if self.user_value(key='ItemNumber') == 30000661:
            return None # Missing State: PickItem_30000661
        if self.user_value(key='ItemNumber') == 30000662:
            return None # Missing State: PickItem_30000662
        if self.user_value(key='ItemNumber') == 30000663:
            return None # Missing State: PickItem_30000663
        if self.user_value(key='ItemNumber') == 30000664:
            return None # Missing State: PickItem_30000664
        if self.user_value(key='ItemNumber') == 30000665:
            return None # Missing State: PickItem_30000665
        if self.user_value(key='ItemNumber') == 30000666:
            return None # Missing State: PickItem_30000666
        if self.user_value(key='ItemNumber') == 30000667:
            return None # Missing State: PickItem_30000667
        if self.user_value(key='ItemNumber') == 30000668:
            return None # Missing State: PickItem_30000668
        if self.user_value(key='ItemNumber') == 30000669:
            return None # Missing State: PickItem_30000669
        if self.user_value(key='ItemNumber') == 30000670:
            return None # Missing State: PickItem_30000670
        if self.user_value(key='ItemNumber') == 30000671:
            return None # Missing State: PickItem_30000671
        if self.user_value(key='ItemNumber') == 30000672:
            return None # Missing State: PickItem_30000672
        if self.user_value(key='ItemNumber') == 30000673:
            return None # Missing State: PickItem_30000673
        if self.user_value(key='ItemNumber') == 30000674:
            return None # Missing State: PickItem_30000674
        if self.user_value(key='ItemNumber') == 30000675:
            return None # Missing State: PickItem_30000675
        if self.user_value(key='ItemNumber') == 30000676:
            return None # Missing State: PickItem_30000676
        if self.user_value(key='ItemNumber') == 30000677:
            return None # Missing State: PickItem_30000677
        if self.user_value(key='ItemNumber') == 30000678:
            return None # Missing State: PickItem_30000678
        if self.user_value(key='ItemNumber') == 30000679:
            return None # Missing State: PickItem_30000679
        if self.user_value(key='ItemNumber') == 30000680:
            return None # Missing State: PickItem_30000680
        if self.user_value(key='ItemNumber') == 30000681:
            return None # Missing State: PickItem_30000681
        if self.user_value(key='ItemNumber') == 30000682:
            return None # Missing State: PickItem_30000682
        if self.user_value(key='ItemNumber') == 30000683:
            return None # Missing State: PickItem_30000683
        if self.user_value(key='ItemNumber') == 30000684:
            return None # Missing State: PickItem_30000684
        if self.user_value(key='ItemNumber') == 30000685:
            return None # Missing State: PickItem_30000685
        if self.user_value(key='ItemNumber') == 30000686:
            return None # Missing State: PickItem_30000686
        if self.user_value(key='ItemNumber') == 30000687:
            return None # Missing State: PickItem_30000687
        if self.user_value(key='ItemNumber') == 30000688:
            return None # Missing State: PickItem_30000688
        if self.user_value(key='ItemNumber') == 30000689:
            return None # Missing State: PickItem_30000689
        if self.user_value(key='ItemNumber') == 30000690:
            return None # Missing State: PickItem_30000690
        if self.user_value(key='ItemNumber') == 30000691:
            return None # Missing State: PickItem_30000691
        if self.user_value(key='ItemNumber') == 30000692:
            return None # Missing State: PickItem_30000692
        if self.user_value(key='ItemNumber') == 30000693:
            return None # Missing State: PickItem_30000693
        if self.user_value(key='ItemNumber') == 30000694:
            return None # Missing State: PickItem_30000694
        if self.user_value(key='ItemNumber') == 30000695:
            return None # Missing State: PickItem_30000695
        if self.user_value(key='ItemNumber') == 30000696:
            return None # Missing State: PickItem_30000696
        if self.user_value(key='ItemNumber') == 30000697:
            return None # Missing State: PickItem_30000697
        if self.user_value(key='ItemNumber') == 30000698:
            return None # Missing State: PickItem_30000698
        if self.user_value(key='ItemNumber') == 30000699:
            return None # Missing State: PickItem_30000699
        if self.user_value(key='ItemNumber') == 30000700:
            return None # Missing State: PickItem_30000700
        if self.user_value(key='ItemNumber') == 30000701:
            return None # Missing State: PickItem_30000701
        if self.user_value(key='ItemNumber') == 30000702:
            return PickItem_30000702(self.ctx)
        if self.user_value(key='ItemNumber') == 30000703:
            return None # Missing State: PickItem_30000703
        if self.user_value(key='ItemNumber') == 30000704:
            return None # Missing State: PickItem_30000704
        if self.user_value(key='ItemNumber') == 30000705:
            return None # Missing State: PickItem_30000705
        if self.user_value(key='ItemNumber') == 30000706:
            return None # Missing State: PickItem_30000706
        if self.user_value(key='ItemNumber') == 30000707:
            return None # Missing State: PickItem_30000707
        if self.user_value(key='ItemNumber') == 30000708:
            return None # Missing State: PickItem_30000708
        if self.user_value(key='ItemNumber') == 30000709:
            return None # Missing State: PickItem_30000709
        if self.user_value(key='ItemNumber') == 30000710:
            return None # Missing State: PickItem_30000710
        if self.user_value(key='ItemNumber') == 30000711:
            return None # Missing State: PickItem_30000711
        if self.user_value(key='ItemNumber') == 30000712:
            return None # Missing State: PickItem_30000712
        if self.user_value(key='ItemNumber') == 30000713:
            return PickItem_30000713(self.ctx)
        if self.user_value(key='ItemNumber') == 30000714:
            return None # Missing State: PickItem_30000714
        if self.user_value(key='ItemNumber') == 30000715:
            return None # Missing State: PickItem_30000715
        if self.user_value(key='ItemNumber') == 30000716:
            return None # Missing State: PickItem_30000716


initial_state = Wait
