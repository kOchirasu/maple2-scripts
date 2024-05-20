""" trigger/63000022_cs/business01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내
        self.set_effect(trigger_ids=[8000]) # Voice 00001397
        self.set_effect(trigger_ids=[8001]) # Voice 00001398
        self.set_effect(trigger_ids=[8002]) # Voice 00001399
        self.spawn_monster(spawn_ids=[101,201,301,401], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000439], quest_states=[3]):
            # 이전 퀘스트 완료 상태
            return QuestOngoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000440], quest_states=[1]):
            # 새로운퀘스트 진행중 상태
            return QuestOngoing11(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return TalkWeiHong01(self.ctx)


# 이전  퀘스트 이미 완료한 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.select_camera(trigger_id=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOngoing02(self.ctx)


class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NextQuestStart01(self.ctx)


# 새로운  퀘스트 이미 수락한 상태
class QuestOngoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.select_camera(trigger_id=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOngoing12(self.ctx)


class QuestOngoing12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return MoveToNextMap01(self.ctx)


# 최초 입장
class TalkWeiHong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkWeiHong02(self.ctx)


class TalkWeiHong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TalkWeiHong03(self.ctx)


class TalkWeiHong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkWeiHong04(self.ctx)


class TalkWeiHong04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000022_CS__BUSINESS01__0$', time=6) # Voice 00001397
        self.set_effect(trigger_ids=[8000], visible=True) # Voice 00001397
        self.set_skip(state=TalkWeiHong05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TalkWeiHong05(self.ctx)


class TalkWeiHong05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkWeiHong06(self.ctx)


class TalkWeiHong06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000022_CS__BUSINESS01__1$', time=6) # Voice 00001398
        self.set_effect(trigger_ids=[8001], visible=True) # Voice 00001398
        self.set_skip(state=TalkWeiHong07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return TalkWeiHong07(self.ctx)


class TalkWeiHong07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return TalkWeiHong08(self.ctx)


class TalkWeiHong08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000022_CS__BUSINESS01__3$', time=3)
        self.set_skip(state=TalkWeiHong09)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TalkWeiHong09(self.ctx)


class TalkWeiHong09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TalkWeiHong10(self.ctx)


class TalkWeiHong10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000022_CS__BUSINESS01__2$', time=6) # Voice 00001399
        self.set_effect(trigger_ids=[8002], visible=True) # Voice 00001399
        self.set_skip(state=TalkWeiHong11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return TalkWeiHong11(self.ctx)


class TalkWeiHong11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=501, enable=False)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024020, text_id=10024020) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000439], quest_states=[3]):
            # 이전 퀘스트 완료 상태
            return NextQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10024020)


class NextQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10024030, text_id=10024030) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000440], quest_states=[1]):
            # 다음 퀘스트 진행중 상태
            return MoveToNextMap01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10024030)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 포털을 타고 흑성회 고물 처리장으로 이동하기
        self.show_guide_summary(entity_id=10027010, text_id=10027010)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5204], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5205], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return MoveToNextMap02(self.ctx)


class MoveToNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10027010)
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내


initial_state = Wait
