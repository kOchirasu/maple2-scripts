""" trigger/63000023_cs/gototria01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001001], state=0) # car
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 목표 바닥 지점 자동차 옆
        self.set_effect(trigger_ids=[5300]) # 자동차 화살표
        self.set_effect(trigger_ids=[5100]) # 경로 안내
        self.set_effect(trigger_ids=[5101]) # 경로 안내
        self.set_effect(trigger_ids=[5102]) # 경로 안내
        self.set_effect(trigger_ids=[5103]) # 경로 안내
        self.set_effect(trigger_ids=[5104]) # 경로 안내
        self.spawn_monster(spawn_ids=[201,301,401,501,601], auto_target=False)
        self.set_breakable(trigger_ids=[4000])
        self.set_effect(trigger_ids=[6000]) # CarIdle
        self.set_effect(trigger_ids=[6001]) # CarMovingAway
        self.set_effect(trigger_ids=[7000]) # Voice Bravo 00001460
        self.set_effect(trigger_ids=[7001]) # Voice Bravo 00001461
        self.set_effect(trigger_ids=[7002]) # Voice Bravo 00001462
        self.set_effect(trigger_ids=[7003]) # Voice Bravo 00001463
        self.set_effect(trigger_ids=[7100]) # Voice Jabeth 00001548
        self.set_effect(trigger_ids=[7101]) # Voice Jabeth 00001549
        self.set_effect(trigger_ids=[7102]) # Voice Jabeth 00001550
        self.set_effect(trigger_ids=[7103]) # Voice Jabeth 00001551
        # Voice BravoNJabeth 00001598
        self.set_effect(trigger_ids=[7200])

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
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000440], quest_states=[3]):
            # 이전 퀘스트 완료 상태
            return QuestOngoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000441], quest_states=[1]):
            # 다음 퀘스트 진행중 상태
            return QuestOngoing11(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return WalkWithJacey01(self.ctx)


# 첫번째  퀘스트 이미 완료한 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.destroy_monster(spawn_ids=[201,301])
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOngoing02(self.ctx)


class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NextQuestStart01(self.ctx)


# 새로운  퀘스트 이미 수락한 상태
class QuestOngoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.destroy_monster(spawn_ids=[201,301])
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOngoing12(self.ctx)


class QuestOngoing12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GetCloseToTheCar01(self.ctx)


# 최초 입장
class WalkWithJacey01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WalkWithJacey02(self.ctx)


class WalkWithJacey02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return WalkWithJacey03(self.ctx)


class WalkWithJacey03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7000], visible=True) # Voice Bravo 00001460
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__0$', time=6) # 브라보
        # Voice 00001460
        self.set_skip(state=Dialogue02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7000]) # Voice Bravo 00001460
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7100], visible=True) # Voice Jabeth 00001548
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000023_CS__GOTOTRIA01__1$', time=6) # 자베스
        # Voice 00001548
        self.set_skip(state=Dialogue04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7100]) # Voice Jabeth 00001548
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue05(self.ctx)


class Dialogue05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7001], visible=True) # Voice Bravo 00001461
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__2$', time=6) # 브라보
        # Voice 00001461
        self.set_skip(state=Dialogue06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Dialogue06(self.ctx)


class Dialogue06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001]) # Voice Bravo 00001461
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue07(self.ctx)


class Dialogue07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__3$', time=4) # 브라보
        self.set_skip(state=Dialogue08)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue08(self.ctx)


class Dialogue08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue09(self.ctx)


class Dialogue09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7101], visible=True) # Voice Jabeth 00001549
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000023_CS__GOTOTRIA01__4$', time=5) # 자베스
        # Voice 00001549
        self.set_skip(state=Dialogue10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue10(self.ctx)


class Dialogue10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7101]) # Voice Jabeth 00001549
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue11(self.ctx)


class Dialogue11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7002], visible=True) # Voice Bravo 00001462
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__5$', time=5) # 브라보
        # Voice 00001462
        self.set_skip(state=Dialogue12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue12(self.ctx)


class Dialogue12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002]) # Voice Bravo 00001462
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue13(self.ctx)


class Dialogue13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7102], visible=True) # Voice Jabeth 00001550
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000023_CS__GOTOTRIA01__6$', time=5) # 자베스
        # Voice 00001550
        self.set_skip(state=Dialogue14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue14(self.ctx)


class Dialogue14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7102]) # Voice Jabeth 00001550
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue15(self.ctx)


class Dialogue15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7003], visible=True) # Voice Bravo 00001463
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__7$', time=5) # 브라보
        # Voice 00001463
        self.set_skip(state=Dialogue16)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue16(self.ctx)


class Dialogue16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue17(self.ctx)


class Dialogue17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000023_CS__GOTOTRIA01__8$', time=4) # 브라보
        self.set_skip(state=Dialogue18)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue18(self.ctx)


class Dialogue18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003]) # Voice Bravo 00001463
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue19(self.ctx)


class Dialogue19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7103], visible=True) # Voice Jabeth 00001551
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000023_CS__GOTOTRIA01__9$', time=5) # 자베스
        # Voice 00001551
        self.set_skip(state=Dialogue20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue20(self.ctx)


class Dialogue20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue21(self.ctx)


class Dialogue21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000023_CS__GOTOTRIA01__10$', time=4) # 자베스
        self.set_skip(state=Dialogue22)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue22(self.ctx)


class Dialogue22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7103]) # Voice Jabeth 00001551
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return AttackIdle01(self.ctx)


class AttackIdle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')
        # Voice BravoNJabeth 00001598
        self.set_effect(trigger_ids=[7200], visible=True)
        self.set_dialogue(type=1, spawn_id=201, script='$63000023_CS__GOTOTRIA01__11$', time=3) # 둘이 함께  Voice 00001598
        self.set_dialogue(type=1, spawn_id=301, script='$63000023_CS__GOTOTRIA01__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkJacey01(self.ctx)


class TalkJacey01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkJacey02(self.ctx)


class TalkJacey02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkJacey03(self.ctx)


class TalkJacey03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice BravoNJabeth 00001598
        self.set_effect(trigger_ids=[7200])
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyTalk04(self.ctx)


class JaceyTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000023_CS__GOTOTRIA01__13$', time=5) # 제이시
        self.set_skip(state=JaceyTalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JaceyTalk05(self.ctx)


class JaceyTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return JaceyLeave01(self.ctx)


class JaceyLeave01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return JaceyLeave02(self.ctx)


class JaceyLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyLeave03(self.ctx)


class JaceyLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.select_camera_path(path_ids=[701,702], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return JaceyLeave04(self.ctx)


class JaceyLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000023_CS__GOTOTRIA01__14$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return JaceyLeave05(self.ctx)


class JaceyLeave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,301])
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyLeave06(self.ctx)


class JaceyLeave06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=702, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.show_guide_summary(entity_id=10028010, text_id=10028010) # 가이드 : 브라보와 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000440], quest_states=[3]):
            # 이전 퀘스트 완료 상태
            return NextQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10028010)


class NextQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10028020, text_id=10028020) # 가이드 : 브라보와 대화하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000441], quest_states=[1]):
            # 다음 퀘스트 진행중 상태
            return GetCloseToTheCar01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10028020)


class GetCloseToTheCar01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # CarIdle
        self.show_guide_summary(entity_id=10028030, text_id=10028030) # 가이드 : 트라이아행 차에 가까이 가기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200], visible=True) # 목표 바닥 지점 자동차 옆
        self.set_effect(trigger_ids=[5100], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5101], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5102], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5103], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5104], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return GetCloseToTheCar02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10028030)


class GetCloseToTheCar02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_302')
        self.show_guide_summary(entity_id=10028040, text_id=10028040) # 가이드 : 차에 탑승해 트라이아로 이동하기
        self.set_interact_object(trigger_ids=[10001001], state=1) # car
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5300], visible=True) # 자동차 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001001], state=0):
            return GetInTheCar01(self.ctx)


class GetInTheCar01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000], enable=True)
        self.hide_guide_summary(entity_id=10028040)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 목표 바닥 지점 자동차 옆
        self.set_effect(trigger_ids=[5100]) # 경로 안내
        self.set_effect(trigger_ids=[5101]) # 경로 안내
        self.set_effect(trigger_ids=[5102]) # 경로 안내
        self.set_effect(trigger_ids=[5103]) # 경로 안내
        self.set_effect(trigger_ids=[5104]) # 경로 안내
        self.set_effect(trigger_ids=[5300]) # 자동차 화살표
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GetInTheCar02(self.ctx)


class GetInTheCar02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000]) # CarIdle
        self.set_effect(trigger_ids=[6001], visible=True) # CarMovingAway
        self.move_user(map_id=63000023, portal_id=2, box_id=9900)
        self.select_camera(trigger_id=800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GetInTheCar03(self.ctx)


class GetInTheCar03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CarMoving01(self.ctx)


class CarMoving01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return CarMoving02(self.ctx)


class CarMoving02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=800, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CarMoving03(self.ctx)


class CarMoving03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001]) # CarMovingAway
        self.move_user(map_id=2000062, portal_id=13, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
