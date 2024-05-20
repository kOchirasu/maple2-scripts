""" trigger/63000014_cs/checkstone01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10001004], state=2) # Stone
        self.set_mesh(trigger_ids=[3000], visible=True) # Stone_Off
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5101]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5102]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5103]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5200]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5201]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5202]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5203]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5204]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5205]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5206]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5207]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5208]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5209]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5210]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5300]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5301]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5302]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5303]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5304]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5305]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5306]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5307]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5308]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5309]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5310]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5311]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5312]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5313]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5400]) # 결계석 화살표
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000450], quest_states=[1]):
            # 기묘한 조짐 퀘스트 수락한 상태
            return QuestOnGoing30(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[3]):
            # 기너울빛 산의 결계 퀘스트 완료 상태
            return QuestOnGoing22(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[2]):
            # 기너울빛 산의 결계 퀘스트 완료 가능 상태
            return QuestOnGoing21(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[1]):
            # 기너울빛 산의 결계 퀘스트 수락한 상태
            return QuestOnGoing20(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000448], quest_states=[3]):
            # 마스터의 부르심 퀘스트 완료 상태
            return QuestOnGoing10(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000448], quest_states=[2]):
            # 마스터의 부르심 퀘스트 완료 가능 상태 : 최초 입장
            return FirstQuestEnd01(self.ctx)


# 첫 번째 퀘스트 완료 상태
class QuestOnGoing10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return SecondQuestStart01(self.ctx)


# 두 번째 퀘스트 수락한 상태
class QuestOnGoing20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return MoveToFindStone01(self.ctx)


# 두 번째 퀘스트 완료 가능 상태
class QuestOnGoing21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return SecondQuestEnd01(self.ctx)


# 두 번째 퀘스트 완료 상태
class QuestOnGoing22(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return ThirdQuestStart01(self.ctx)


# 세 번째 퀘스트 수락한 상태
class QuestOnGoing30(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return MoveToNextMap01(self.ctx)


# 최초 입장
class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030100, text_id=10030100)
        self.set_effect(trigger_ids=[5100], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5101], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5102], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5103], visible=True) # NPC 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return FirstQuestEnd02(self.ctx)


class FirstQuestEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5101]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5102]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5103]) # NPC 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000448], quest_states=[3]):
            # 마스터의 부르심 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030100)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : [[icon:questaccept]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030160, text_id=10030160)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[1]):
            # 기너울빛 산의 결계 퀘스트 수락한 상태
            return MoveToFindStone01(self.ctx)


class MoveToFindStone01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001004], state=1) # Stone
        self.set_mesh(trigger_ids=[3000], start_delay=50) # Stone_Off
        self.hide_guide_summary(entity_id=10030160)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10032010, text_id=10032010) # 가이드 : 연꽃 쉼터의 결계석 찾기
        self.set_effect(trigger_ids=[5400], visible=True) # 결계석 화살표
        self.set_effect(trigger_ids=[5200], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5204], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5205], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5206], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5207], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5208], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5209], visible=True) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5210], visible=True) # 결계석 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return MoveToFindStone02(self.ctx)


class MoveToFindStone02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.hide_guide_summary(entity_id=10032010)
        # 가이드 : 스페이스 키를 눌러 파손된 결계석 복원하기
        self.show_guide_summary(entity_id=10032020, text_id=10032020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[2]):
            # 기너울빛 산의 결계 퀘스트 완료 가능 상태
            return SecondQuestEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10032020)
        self.set_effect(trigger_ids=[5400]) # 결계석 화살표
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트


class SecondQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030100, text_id=10030100)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return SecondQuestEnd02(self.ctx)


class SecondQuestEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5200]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5201]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5202]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5203]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5204]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5205]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5206]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5207]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5208]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5209]) # 결계석 경로 안내
        self.set_effect(trigger_ids=[5210]) # 결계석 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000449], quest_states=[3]):
            # 기너울빛 산의 결계 퀘스트 완료 상태
            return ThirdQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030100)


class ThirdQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : [[icon:questaccept]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030160, text_id=10030160)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000450], quest_states=[1]):
            # 기묘한 조짐 퀘스트 수락한 상태
            return MoveToNextMap01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030160)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 연꽃 쉼터 북부로 연결되는 포털을 향해 이동하기
        self.show_guide_summary(entity_id=10032030, text_id=10032030)
        self.set_effect(trigger_ids=[5300], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5301], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5302], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5303], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5304], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5305], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5306], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5307], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5308], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5309], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5310], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5311], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5312], visible=True) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5313], visible=True) # 다음 맵 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return MoveToNextMap02(self.ctx)


class MoveToNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10032030)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=1060, text_id=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=1060)
        self.destroy_monster(spawn_ids=[101])
        self.set_effect(trigger_ids=[5300]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5301]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5302]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5303]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5304]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5305]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5306]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5307]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5308]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5309]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5310]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5311]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5312]) # 다음 맵 경로 안내
        self.set_effect(trigger_ids=[5313]) # 다음 맵 경로 안내


initial_state = Wait
