""" trigger/52000037_qd/lookinto_striker_01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='Dead_A') # NelfActor
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10000175], state=0) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[40002604], quest_states=[3], job_code=100):
            # 스트라이커 넬프의 죽음 퀘스트 완료
            return StrikerSetting04(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[40002604], quest_states=[2], job_code=100):
            # 스트라이커 넬프의 죽음 퀘스트 완료 가능
            return StrikerSetting03(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[40002604], quest_states=[1], job_code=100):
            # 스트라이커 넬프의 죽음 퀘스트 진행중
            return StrikerSetting05(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100065], quest_states=[3], job_code=100):
            # 스트라이커 랄프의 정보 퀘스트 완료
            return StrikerSetting02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100065], quest_states=[2], job_code=100):
            # 스트라이커 랄프의 정보 퀘스트 완료 가능
            return StrikerSetting01(self.ctx)


# 스트라이커 연출 2차 입장
class StrikerSetting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[202,302], auto_target=False) # StrikerNPC
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # QuestZone
            return NextQuestStart01(self.ctx)


# 스트라이커 연출 2.5차 입장
class StrikerSetting05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000175], state=1) # Bag
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[202,302], auto_target=False) # StrikerNPC
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # QuestZone
            return NextQuestStart01(self.ctx)


# 스트라이커 연출 3차 입장
class StrikerSetting03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


# 스트라이커 연출 상황 종료
class StrikerSetting04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


# 스트라이커 연출 최초 입장
class StrikerSetting01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[201,301], auto_target=False) # StrikerNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            # Mid
            return SayHi01(self.ctx)


class SayHi01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000037_QD__LOOKINTO_STRIKER_01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCMove01(self.ctx)


class PCMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCMove02(self.ctx)


class PCMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000037, portal_id=10, box_id=9900)
        self.spawn_monster(spawn_ids=[401], auto_target=False) # StrikerNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.set_dialogue(type=1, spawn_id=201, script='$52000037_QD__LOOKINTO_STRIKER_01__1$', time=3)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Patrol04(self.ctx)


class Patrol04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000037_QD__LOOKINTO_STRIKER_01__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ComeAcrossSB01(self.ctx)


class ComeAcrossSB01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ComeAcrossSB02(self.ctx)


class ComeAcrossSB02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000037_QD__LOOKINTO_STRIKER_01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ComeAcrossSB03(self.ctx)


class ComeAcrossSB03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SBRunAway01(self.ctx)


class SBRunAway01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=401, script='$52000037_QD__LOOKINTO_STRIKER_01__14$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SBRunAway02(self.ctx)


class SBRunAway02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SBRunAway03(self.ctx)


class SBRunAway03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__4$', time=5) # 자베스
        self.set_skip(state=Dialogue02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[401])
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__5$', time=5) # 브라보
        self.set_skip(state=Dialogue04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=701, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return StepInside01(self.ctx)


class StepInside01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000037_QD__LOOKINTO_STRIKER_01__6$', time=4)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return StepInside02(self.ctx)


class StepInside02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000037_QD__LOOKINTO_STRIKER_01__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstQuestStart01(self.ctx)


class FirstQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC
        self.set_interact_object(trigger_ids=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100065], quest_states=[3], job_code=100):
            # 스트라이커  랄프의 정보 퀘스트 완료 상태
            return TalkJabethNBravo01(self.ctx)


class TalkJabethNBravo01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__8$', time=5) # 자베스
        self.set_skip(state=TalkJabethNBravo02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TalkJabethNBravo02(self.ctx)


class TalkJabethNBravo02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TalkJabethNBravo03(self.ctx)


class TalkJabethNBravo03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__9$', time=5) # 브라보
        self.set_skip(state=TalkJabethNBravo04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TalkJabethNBravo04(self.ctx)


class TalkJabethNBravo04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NPCChange01(self.ctx)


class NPCChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,301])
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NextQuestStart01(self.ctx)


class NextQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$52000037_QD__LOOKINTO_STRIKER_01__10$', time=4)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NextQuestStart02(self.ctx)


class NextQuestStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002604], quest_states=[2], job_code=100):
            # 스트라이커  넬프의 죽음 퀘스트 완료 상태
            return ReadyToLeave01(self.ctx)


class ReadyToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__11$', time=6) # 브라보
        self.set_skip(state=ReadyToLeave02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return ReadyToLeave02(self.ctx)


class ReadyToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToLeave03(self.ctx)


class ReadyToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_304')
        self.set_dialogue(type=1, spawn_id=302, script='$52000037_QD__LOOKINTO_STRIKER_01__12$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToLeave04(self.ctx)


class ReadyToLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToLeave05(self.ctx)


class ReadyToLeave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$52000037_QD__LOOKINTO_STRIKER_01__13$', time=3)
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_305')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPCLeave01(self.ctx)


class NPCLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[302])
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPCLeave02(self.ctx)


class NPCLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
