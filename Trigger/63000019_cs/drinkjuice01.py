""" trigger/63000019_cs/drinkjuice01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300]) # 목표지점 바닥 웨이홍 앞
        self.set_effect(trigger_ids=[5400]) # 목표지점 바닥 바텐더 앞
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 목료 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5101]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5102]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5103]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5200]) # 제 2경로 안내
        self.set_effect(trigger_ids=[5201]) # 제 2경로 안내
        self.set_effect(trigger_ids=[5202]) # 제 2경로 안내
        self.set_effect(trigger_ids=[8000]) # WeiHong 00001395
        self.set_effect(trigger_ids=[8001]) # VasaraChen 00001348
        self.set_effect(trigger_ids=[8002]) # WeiHong 00001396
        self.spawn_monster(spawn_ids=[101,201,301,401,501], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000438], quest_states=[3]):
            # 웨이홍과 마지막 퀘스트 마치고 맵 이동할 차례
            return QuestComplete01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000442], quest_states=[3]):
            # 주스 마시기 퀘스트 완료 후 맵 이동할 차례
            return QuestComplete01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000442], quest_states=[2]):
            # 바텐더 만나기 퀘스트 진행중
            return MoveToBartender01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000437], quest_states=[3]):
            # 맵 입장 직후 웨이홍과 대화하기 퀘스트 완료 후 다음 퀘스트 수락할 차례
            return TalkToWeiHong02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000437], quest_states=[2]):
            # 맵 입장 직후 웨이홍과 대화하기 퀘스트 완료 가능 상태
            return MoveToWeiHong01(self.ctx)


# 첫 번째 퀘스트 완료 가능 상태
class MoveToWeiHong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024010, text_id=10024010) # 가이드 : 웨이 홍을 향해 이동하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 사운드 이펙트
        self.set_effect(trigger_ids=[5100], visible=True) # 제 1경로 안내
        self.set_effect(trigger_ids=[5101], visible=True) # 제 1경로 안내
        self.set_effect(trigger_ids=[5102], visible=True) # 제 1경로 안내
        self.set_effect(trigger_ids=[5103], visible=True) # 제 1경로 안내
        self.set_effect(trigger_ids=[5300], visible=True) # 목표지점 바닥 웨이홍 앞

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return TalkToWeiHong01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10024010)
        self.set_effect(trigger_ids=[5100]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5101]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5102]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5103]) # 제 1경로 안내
        self.set_effect(trigger_ids=[5300]) # 목표지점 바닥 웨이홍 앞


class TalkToWeiHong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024020, text_id=10024020) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000437], quest_states=[3]):
            # 맵 입장 직후 웨이홍과 대화하기 퀘스트 완료 후 다음 퀘스트 수락할 차례
            return TalkToWeiHong02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10024020)


class TalkToWeiHong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024030, text_id=10024030) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000438], quest_states=[2]):
            # 바텐더 만나기 퀘스트 완료 가능 상태
            return MoveToBartender01(self.ctx)


class MoveToBartender01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10024040, text_id=10024040)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 사운드 이펙트
        self.set_effect(trigger_ids=[5200], visible=True) # 제 2경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 제 2경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 제 2경로 안내
        self.set_effect(trigger_ids=[5400], visible=True) # 목표지점 바닥 바텐더 앞

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return MoveToBartender02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10024040)
        self.set_effect(trigger_ids=[5400]) # 목표지점 바닥 바텐더 앞
        self.set_effect(trigger_ids=[5001]) # 화살표 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 제 2경로 안내
        self.set_effect(trigger_ids=[5201]) # 제 2경로 안내
        self.set_effect(trigger_ids=[5202]) # 제 2경로 안내


class MoveToBartender02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024050, text_id=10024050) # 가이드 : 바텐더와 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        return TalkToBartender01(self.ctx)


class TalkToBartender01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000438], quest_states=[3]):
            # 바텐더에게 첫 번째 퀘스트 완료한 상태
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10024050)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000442], quest_states=[3]):
            # 주스 마시기 퀘스트 완료 후 맵 이동할 차례
            return TalkingDelay01(self.ctx)


# 두번째 퀘스트 및 가이드 완료 상태
class TalkingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeiHongTalk01(self.ctx)


class WeiHongTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000019_CS__DRINKJUICE01__0$', time=5) # Voice 00001395
        self.set_effect(trigger_ids=[8000], visible=True) # WeiHong 00001395
        self.set_skip(state=WeiHongTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WeiHongTalk02(self.ctx)


class WeiHongTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8000]) # WeiHong 00001395

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeiHongTalk03(self.ctx)


class WeiHongTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000019_CS__DRINKJUICE01__1$', time=4) # Voice 00001348
        self.set_effect(trigger_ids=[8001], visible=True) # VasaraChen 00001348
        self.set_skip(state=WeiHongTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return WeiHongTalk04(self.ctx)


class WeiHongTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8001]) # VasaraChen 00001348

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeiHongTalk05(self.ctx)


class WeiHongTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000019_CS__DRINKJUICE01__2$', time=8) # Voice 00001396
        self.set_effect(trigger_ids=[8002], visible=True) # WeiHong 00001396
        self.set_skip(state=MovingDelay01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return MovingDelay01(self.ctx)


class MovingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8002]) # WeiHong 00001396

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=63000020, portal_id=1, box_id=9900)


initial_state = Wait
