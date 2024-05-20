""" trigger/52000033_qd/audiencewithereb_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,201,301,401,501,502,503,504,505,506,507,508,509,510], auto_target=False)
        self.set_effect(trigger_ids=[5000]) # SpotLight_01
        self.set_effect(trigger_ids=[5001]) # SpotLight_02
        self.set_effect(trigger_ids=[5002]) # GuardBow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001301], quest_states=[3]):
            # 두 번째 퀘스트 완료 상태
            return QuestOngoing02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001300], quest_states=[3]):
            # 첫 번째 퀘스트 완료 상태
            return QuestOngoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001300], quest_states=[2]):
            # 첫 번째 퀘스트 완료 가능 상태
            return PCWalkIn01(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return PCtoLeave01(self.ctx)


# 첫 번째 퀘스트 완료 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SecondQuestCheck02(self.ctx)


# 두 번째 퀘스트 완료 상태
class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCGoCenter01(self.ctx)


# 첫 번째 퀘스트 완료 가능 상태
class PCWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCWalkIn02(self.ctx)


class PCWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCWalkIn03(self.ctx)


class PCWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCWalkIn04(self.ctx)


class PCWalkIn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BowAction01(self.ctx)


class BowAction01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=502, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=503, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=504, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=505, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=506, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=507, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=508, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=509, sequence_name='Bow_A')
        self.set_npc_emotion_sequence(spawn_id=510, sequence_name='Bow_A')
        self.set_effect(trigger_ids=[5002], visible=True) # GuardBow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BowAction02(self.ctx)


class BowAction02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ErebTalk01(self.ctx)


class ErebTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ErebTalk02(self.ctx)


class ErebTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__0$', time=4)
        self.set_skip(state=ErebTalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ErebTalk03(self.ctx)


class ErebTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ErebTalk04(self.ctx)


class ErebTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondQuestCheck01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SecondQuestCheck01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001300], quest_states=[3]):
            # 첫 번째 퀘스트 완료 상태
            return SecondQuestCheck02(self.ctx)


class SecondQuestCheck02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001301], quest_states=[3]):
            # 두 번째 퀘스트 완료 상태
            return PCGoCenter01(self.ctx)


class PCGoCenter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCGoCenter02(self.ctx)


class PCGoCenter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCGoCenter03(self.ctx)


class PCGoCenter03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000033, portal_id=10, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCGoCenter04(self.ctx)


class PCGoCenter04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=800)
        self.move_user_path(patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCGoCenter05(self.ctx)


class PCGoCenter05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCSpotLighting01(self.ctx)


class PCSpotLighting01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # SpotLight_01
        self.set_effect(trigger_ids=[5001], visible=True) # SpotLight_02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCSpotLighting02(self.ctx)


class PCSpotLighting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Happy_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCSpotLighting03(self.ctx)


class PCSpotLighting03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1003')
        self.select_camera(trigger_id=801)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ErebTalk11(self.ctx)


class ErebTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__1$', time=5)
        self.set_skip(state=ErebTalk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ErebTalk12(self.ctx)


class ErebTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ErebTalk13(self.ctx)


class ErebTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCtoLeave01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5000]) # SpotLight_01
        self.set_effect(trigger_ids=[5001]) # SpotLight_02


class PCtoLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
