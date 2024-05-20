""" trigger/63000021_cs/wakup01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000], visible=True) # monitor off
        self.set_mesh(trigger_ids=[3001]) # monitor on
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내
        self.set_effect(trigger_ids=[5206]) # 경로 안내
        self.set_effect(trigger_ids=[5207]) # 경로 안내
        self.set_effect(trigger_ids=[5208]) # 경로 안내
        self.set_effect(trigger_ids=[5209]) # 경로 안내
        self.set_effect(trigger_ids=[5210]) # 경로 안내
        self.set_effect(trigger_ids=[5211]) # 경로 안내
        self.set_effect(trigger_ids=[5212]) # 경로 안내
        self.set_effect(trigger_ids=[5213]) # 경로 안내
        self.set_effect(trigger_ids=[5214]) # 경로 안내
        self.set_effect(trigger_ids=[5215]) # 경로 안내
        self.set_effect(trigger_ids=[5216]) # 경로 안내
        self.set_effect(trigger_ids=[5217]) # 경로 안내
        self.set_effect(trigger_ids=[7000]) # Voice Jabeth 00001545
        self.set_effect(trigger_ids=[7001]) # Voice Jabeth 00001546
        self.set_effect(trigger_ids=[7002]) # Voice Jabeth 00001547
        # Voice Jabeth 00001596 monologue
        self.set_effect(trigger_ids=[7003])
        # Voice Jabeth 00001597 monologue
        self.set_effect(trigger_ids=[7004])
        self.set_effect(trigger_ids=[7100]) # Voice Bravo 00001457
        self.set_effect(trigger_ids=[7101]) # Voice Bravo 00001458
        self.set_effect(trigger_ids=[7102]) # Voice Bravo 00001459
        # Voice Bravo 00001525 monologue
        self.set_effect(trigger_ids=[7103])
        # Voice Bravo 00001526 monologue
        self.set_effect(trigger_ids=[7104])
        self.set_effect(trigger_ids=[6000]) # RadioInterference

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
        if self.wait_tick(wait_tick=2000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_D', duration=6600.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000439], quest_states=[1]):
            # 퀘스트 진행중 상태
            return QuestOngoing01(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return WakeUp01(self.ctx)


# 이미 퀘스트 수락한 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOngoing02(self.ctx)


class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=63000021, portal_id=10, box_id=9002)
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CallNextRoom01(self.ctx)


# 최초 입장
class WakeUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return WakeUp02(self.ctx)


class WakeUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WakeUp03(self.ctx)


class WakeUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=60000.0)
        self.spawn_monster(spawn_ids=[101,201,301], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WakeUp04(self.ctx)


class WakeUp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=599)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WakeUp05(self.ctx)


class WakeUp05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000021_CS__WAKUP01__0$', time=4) # 자베스
        # Voice 00001545
        self.set_effect(trigger_ids=[7000], visible=True) # Voice Jabeth 00001545
        self.set_skip(state=Dialogue02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.set_effect(trigger_ids=[7000]) # Voice Jabeth 00001545
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_200')
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000021_CS__WAKUP01__1$', time=4) # 브라보
        # Voice 00001457
        self.set_effect(trigger_ids=[7100], visible=True) # Voice Bravo 00001457

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_300')
        self.set_skip(state=Dialogue05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Dialogue05(self.ctx)


class Dialogue05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7100]) # Voice Bravo 00001457
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Dialogue06(self.ctx)


class Dialogue06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000021_CS__WAKUP01__2$', time=4) # 자베스
        # Voice 00001546
        self.set_effect(trigger_ids=[7001], visible=True) # Voice Jabeth 00001546
        self.set_skip(state=Dialogue07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue07(self.ctx)


class Dialogue07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001]) # Voice Jabeth 00001546
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return JaceyWalkIn01(self.ctx)


class JaceyWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyWalkIn02(self.ctx)


class JaceyWalkIn02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Trialogue01(self.ctx)


class Trialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__3$', time=4) # 제이시
        self.set_skip(state=Trialogue02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Trialogue02(self.ctx)


class Trialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=602)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Trialogue03(self.ctx)


class Trialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000021_CS__WAKUP01__4$', time=4) # 브라보
        # Voice 00001458
        self.set_effect(trigger_ids=[7101], visible=True) # Voice Bravo 00001458
        self.set_skip(state=Trialogue04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Trialogue04(self.ctx)


class Trialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7101]) # Voice Bravo 00001458
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Trialogue05(self.ctx)


class Trialogue05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001546, script='$63000021_CS__WAKUP01__5$', time=4) # 자베스
        # Voice 00001547
        self.set_effect(trigger_ids=[7002], visible=True) # Voice Jabeth 00001547
        self.set_skip(state=Trialogue06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Trialogue06(self.ctx)


class Trialogue06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002]) # Voice Jabeth 00001547
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Trialogue07(self.ctx)


class Trialogue07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001545, script='$63000021_CS__WAKUP01__6$', time=4) # 브라보
        # Voice 00001459
        self.set_effect(trigger_ids=[7102], visible=True) # Voice Bravo 00001459
        self.set_skip(state=Trialogue08)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Trialogue08(self.ctx)


class Trialogue08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7102]) # Voice Bravo 00001459
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Trialogue09(self.ctx)


class Trialogue09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__7$', time=4) # 제이시
        self.set_skip(state=Trialogue10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Trialogue10(self.ctx)


class Trialogue10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TwoMenWalkOut01(self.ctx)


class TwoMenWalkOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TwoMenWalkOut02(self.ctx)


class TwoMenWalkOut02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$63000021_CS__WAKUP01__8$', time=3) # Voice 00001525
        # Voice Bravo 00001525 monologue
        self.set_effect(trigger_ids=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TwoMenWalkOut03(self.ctx)


class TwoMenWalkOut03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TwoMenWalkOut04(self.ctx)


class TwoMenWalkOut04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TwoMenWalkOut05(self.ctx)


class TwoMenWalkOut05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice Bravo 00001525 monologue
        self.set_effect(trigger_ids=[7103])
        # Voice Jabeth 00001596 monologue
        self.set_effect(trigger_ids=[7003], visible=True)
        self.set_dialogue(type=1, spawn_id=301, script='$63000021_CS__WAKUP01__9$', time=3) # Voice 00001596

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TwoMenWalkOut06(self.ctx)


class TwoMenWalkOut06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice Jabeth 00001596 monologue
        self.set_effect(trigger_ids=[7003])
        self.select_camera_path(path_ids=[701,702], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TwoMenWalkOut07(self.ctx)


class TwoMenWalkOut07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice Bravo 00001526 monologue
        self.set_effect(trigger_ids=[7104], visible=True)
        self.set_dialogue(type=1, spawn_id=201, script='$63000021_CS__WAKUP01__10$', time=4) # Voice 00001526

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TwoMenWalkOut08(self.ctx)


class TwoMenWalkOut08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice Bravo 00001526 monologue
        self.set_effect(trigger_ids=[7104])
        # Voice Jabeth 00001597 monologue
        self.set_effect(trigger_ids=[7004], visible=True)
        self.set_dialogue(type=1, spawn_id=301, script='$63000021_CS__WAKUP01__11$', time=4) # Voice 00001597

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return StandUp01(self.ctx)


class StandUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000021, portal_id=10, box_id=9900)
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=2000.0)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=703)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyTalk01(self.ctx)


class JaceyTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice Jabeth 00001597 monologue
        self.set_effect(trigger_ids=[7004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return JaceyTalk02(self.ctx)


class JaceyTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__12$', time=3) # 제이시
        self.set_skip(state=JaceyTalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JaceyTalk03(self.ctx)


class JaceyTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return JaceyTalk04(self.ctx)


class JaceyTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__13$', time=5) # 제이시
        self.set_skip(state=JaceyTalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JaceyTalk05(self.ctx)


class JaceyTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,301])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=703, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyQuest01(self.ctx)


class JaceyQuest01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10021030, text_id=10021030) # 가이드 : 제이시와 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000439], quest_states=[1]):
            # 퀘스트 진행중 상태
            return JaceyQuest02(self.ctx)


class JaceyQuest02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10021030)
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CallNextRoom01(self.ctx)


class CallNextRoom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CallNextRoom02(self.ctx)


class CallNextRoom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], start_delay=100) # MonitorOff
        self.set_mesh(trigger_ids=[3001], visible=True) # MonitorOn
        self.set_effect(trigger_ids=[6000], visible=True) # RadioInterference

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CallNextRoom03(self.ctx)


class CallNextRoom03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # RadioInterference
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__14$', time=4) # 제이시
        self.set_skip(state=CallNextRoom04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CallNextRoom04(self.ctx)


class CallNextRoom04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CallNextRoom05(self.ctx)


class CallNextRoom05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # RadioInterference
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__15$', time=3) # 제이시
        self.set_skip(state=CallNextRoom06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CallNextRoom06(self.ctx)


class CallNextRoom06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return SayGoodBye01(self.ctx)


class SayGoodBye01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_104')
        self.set_effect(trigger_ids=[6000]) # RadioInterference

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SayGoodBye02(self.ctx)


class SayGoodBye02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000021_CS__WAKUP01__16$', time=5) # 제이시
        self.set_skip(state=SayGoodBye03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SayGoodBye03(self.ctx)


class SayGoodBye03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10026010, text_id=10026010)
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5204], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5205], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5206], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5207], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5208], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5209], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5210], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5211], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5212], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5213], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5214], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5215], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5216], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5217], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10026010)
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내
        self.set_effect(trigger_ids=[5206]) # 경로 안내
        self.set_effect(trigger_ids=[5207]) # 경로 안내
        self.set_effect(trigger_ids=[5208]) # 경로 안내
        self.set_effect(trigger_ids=[5209]) # 경로 안내
        self.set_effect(trigger_ids=[5210]) # 경로 안내
        self.set_effect(trigger_ids=[5211]) # 경로 안내
        self.set_effect(trigger_ids=[5212]) # 경로 안내
        self.set_effect(trigger_ids=[5213]) # 경로 안내
        self.set_effect(trigger_ids=[5214]) # 경로 안내
        self.set_effect(trigger_ids=[5215]) # 경로 안내
        self.set_effect(trigger_ids=[5216]) # 경로 안내
        self.set_effect(trigger_ids=[5217]) # 경로 안내


initial_state = Wait
