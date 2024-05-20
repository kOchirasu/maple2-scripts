""" trigger/63000028_cs/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # Sound_ShadowApp_Loop
        self.set_effect(trigger_ids=[6000]) # Voice_Tinchai_00001684
        self.set_effect(trigger_ids=[6001]) # Voice_Tinchai_00001685
        self.set_effect(trigger_ids=[6002]) # Voice_Tinchai_00001686
        self.set_effect(trigger_ids=[6003]) # Voice_Tinchai_00001717
        self.set_effect(trigger_ids=[6004]) # Voice_Tinchai_00001687
        self.set_effect(trigger_ids=[6100]) # Voice_Junta_00001773
        self.set_effect(trigger_ids=[6101]) # Voice_Junta_00001774
        self.set_effect(trigger_ids=[6102]) # Voice_Junta_00001775
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.set_agent(trigger_ids=[8105])
        self.set_agent(trigger_ids=[8106])
        self.set_agent(trigger_ids=[8107])
        self.set_agent(trigger_ids=[8108])
        self.set_agent(trigger_ids=[8109])
        self.set_agent(trigger_ids=[8110])
        self.set_agent(trigger_ids=[8111])
        self.set_agent(trigger_ids=[8112])
        self.set_agent(trigger_ids=[8113])
        self.set_agent(trigger_ids=[8114])
        self.set_agent(trigger_ids=[8115])
        self.set_skill(trigger_ids=[7000]) # 올킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000452], quest_states=[1]):
            # 그림자의 파도 퀘스트 수락한 상태
            return QuestOnGoing21(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000451], quest_states=[3]):
            # 별, 수정, 그리고 퀘스트 완료 상태
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000451], quest_states=[2]):
            # 별, 수정, 그리고 퀘스트 완료 가능 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000451], quest_states=[1]):
            # 별, 수정, 그리고 퀘스트 진행중 상태
            return PCWakeUp01(self.ctx)


# 별, 수정, 그리고 퀘스트 완료 가능 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FirstQuestEnd01(self.ctx)


# 별, 수정, 그리고 퀘스트 완료 상태
class QuestOnGoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SecondQuestStart01(self.ctx)


# 그림자의 파도 퀘스트 수락한 상태
class QuestOnGoing21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGoing22(self.ctx)


class QuestOnGoing22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000028, portal_id=11, box_id=9900)
        self.spawn_monster(spawn_ids=[104,203], auto_target=False)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGoing23(self.ctx)


class QuestOnGoing23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return ShadowWaveAgain02(self.ctx)


# 최초 입장
class PCWakeUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCWakeUp02(self.ctx)


class PCWakeUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=TinChaiTalk02_CSkip, action='nextState')
        self.spawn_monster(spawn_ids=[101,900,901,902], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCWakeUp03(self.ctx)


class PCWakeUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCWakeUp04(self.ctx)


class PCWakeUp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Bore_C'])
        self.set_dialogue(type=1, script='$63000028_CS__BATTLE01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return PCWakeUp05(self.ctx)


class PCWakeUp05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$63000028_CS__BATTLE01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleING01(self.ctx)


class BattleING01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleING02(self.ctx)


class BattleING02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Tinchai_00001684
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000028_CS__BATTLE01__2$', time=5) # 틴차이 00001684
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ReadyToBattle01(self.ctx)


class TinChaiTalk02_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return ReadyToBattle01(self.ctx)


class ReadyToBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.select_camera(trigger_id=501, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return ReadyToBattle02(self.ctx)


# HP 가이드
class ReadyToBattle02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 틴차이를 도와 검은 그림자 처치하기
        self.show_guide_summary(entity_id=10035010, text_id=10035010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleStart02(self.ctx)


class BattleStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : HP가 0이 되면 비석에 깔리니 조심
        self.guide_event(event_id=10035020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900,901,902]):
            return BattleEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10035010)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[900,901,902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000028, portal_id=10, box_id=9900)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleEnd04(self.ctx)


class BattleEnd04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=MeetJunta05_Cskip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleEnd05(self.ctx)


class BattleEnd05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$63000028_CS__BATTLE01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ShadowWave01(self.ctx)


class ShadowWave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.set_agent(trigger_ids=[8102], visible=True)
        self.set_agent(trigger_ids=[8103], visible=True)
        self.set_agent(trigger_ids=[8104], visible=True)
        self.set_agent(trigger_ids=[8105], visible=True)
        self.set_agent(trigger_ids=[8106], visible=True)
        self.set_agent(trigger_ids=[8107], visible=True)
        self.set_agent(trigger_ids=[8108], visible=True)
        self.set_agent(trigger_ids=[8109], visible=True)
        self.set_agent(trigger_ids=[8110], visible=True)
        self.set_agent(trigger_ids=[8111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowWave02(self.ctx)


class ShadowWave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.set_effect(trigger_ids=[5100], visible=True) # Sound_ShadowApp_Loop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWave03(self.ctx)


# 정면 1차 스폰 후 다리 패트롤 바로 시작
class ShadowWave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910,911,912,913])
        self.move_npc(spawn_id=910, patrol_name='MS2PatrolData_910')
        self.move_npc(spawn_id=911, patrol_name='MS2PatrolData_911')
        self.move_npc(spawn_id=912, patrol_name='MS2PatrolData_912')
        self.move_npc(spawn_id=913, patrol_name='MS2PatrolData_913')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowWave04(self.ctx)


# 정면 2차 스폰 후 다리 패트롤 바로 시작
class ShadowWave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[920,921,922,923,924])
        self.move_npc(spawn_id=920, patrol_name='MS2PatrolData_920')
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_922')
        self.move_npc(spawn_id=923, patrol_name='MS2PatrolData_923')
        self.move_npc(spawn_id=924, patrol_name='MS2PatrolData_924')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWave05(self.ctx)


# 카메라 워크
class ShadowWave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_101')
        self.move_user_path(patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowWave06(self.ctx)


class ShadowWave06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[930,931,932,933,950,951,952,953])
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_930')
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_931')
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_932')
        self.move_npc(spawn_id=933, patrol_name='MS2PatrolData_933')
        self.move_npc(spawn_id=950, patrol_name='MS2PatrolData_950')
        self.move_npc(spawn_id=951, patrol_name='MS2PatrolData_951')
        self.move_npc(spawn_id=952, patrol_name='MS2PatrolData_952')
        self.move_npc(spawn_id=953, patrol_name='MS2PatrolData_953')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWave07(self.ctx)


# 양측 2차 스폰
class ShadowWave07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$63000028_CS__BATTLE01__4$', time=3) # 틴차이
        self.spawn_monster(spawn_ids=[940,941,942,943,944,945,960,961,962,963,964,965])
        self.move_npc(spawn_id=940, patrol_name='MS2PatrolData_940')
        self.move_npc(spawn_id=941, patrol_name='MS2PatrolData_941')
        self.move_npc(spawn_id=942, patrol_name='MS2PatrolData_942')
        self.move_npc(spawn_id=943, patrol_name='MS2PatrolData_943')
        self.move_npc(spawn_id=944, patrol_name='MS2PatrolData_944')
        self.move_npc(spawn_id=945, patrol_name='MS2PatrolData_945')
        self.move_npc(spawn_id=960, patrol_name='MS2PatrolData_960')
        self.move_npc(spawn_id=961, patrol_name='MS2PatrolData_961')
        self.move_npc(spawn_id=962, patrol_name='MS2PatrolData_962')
        self.move_npc(spawn_id=963, patrol_name='MS2PatrolData_963')
        self.move_npc(spawn_id=964, patrol_name='MS2PatrolData_964')
        self.move_npc(spawn_id=965, patrol_name='MS2PatrolData_965')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TinChaiDesperate01(self.ctx)


class TinChaiDesperate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Attack_Idle_A', duration=12000.0)
        self.set_pc_emotion_loop(sequence_name='Orb_Attack_Idle_A', duration=12000.0)
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001685
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000028_CS__BATTLE01__5$', time=5) # 틴차이 00001685
        self.set_skip(state=TinChaiDesperate02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TinChaiDesperate02(self.ctx)


class TinChaiDesperate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JuntaApp01(self.ctx)


class JuntaApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JuntaApp02(self.ctx)


class JuntaApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700)
        self.destroy_monster(spawn_ids=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        self.spawn_monster(spawn_ids=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JuntaApp03(self.ctx)


class JuntaApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.set_agent(trigger_ids=[8105])
        self.set_agent(trigger_ids=[8106])
        self.set_agent(trigger_ids=[8107])
        self.set_agent(trigger_ids=[8108])
        self.set_agent(trigger_ids=[8109])
        self.set_agent(trigger_ids=[8110])
        self.set_agent(trigger_ids=[8111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JuntaApp04(self.ctx)


class JuntaApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 11001742_M_Junta 준타 Regen_A
        self.spawn_monster(spawn_ids=[201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return JuntaTalk01(self.ctx)

    def on_exit(self) -> None:
        self.set_skill(trigger_ids=[7000], enable=True) # 올킬


class JuntaTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5100]) # Sound_ShadowApp_Loop
        self.set_effect(trigger_ids=[6100], visible=True) # Voice_Junta_00001773
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000028_CS__BATTLE01__6$', time=4) # 준타 00001773

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return MeetJunta01(self.ctx)


class MeetJunta01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        self.move_user_path(patrol_name='MS2PatrolData_1003')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MeetJunta02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class MeetJunta02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Tinchai_00001686
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000028_CS__BATTLE01__7$', time=5) # 틴차이 00001686

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return MeetJunta03(self.ctx)


class MeetJunta03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return MeetJunta04(self.ctx)


class MeetJunta04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6101], visible=True) # Voice_Junta_00001774
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000028_CS__BATTLE01__8$', time=7) # 준타 00001774

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return MeetJunta05(self.ctx)


class MeetJunta05_Cskip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.set_effect(trigger_ids=[5100]) # Sound_ShadowApp_Loop
        self.destroy_monster(spawn_ids=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        self.move_user_path(patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MeetJunta05_Cskip2(self.ctx)


class MeetJunta05_Cskip2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        self.destroy_monster(spawn_ids=[102,201])
        self.spawn_monster(spawn_ids=[103,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetJunta06(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class MeetJunta05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[102,201])
        self.spawn_monster(spawn_ids=[103,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MeetJunta06(self.ctx)


class MeetJunta06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9900, type='trigger', achieve='complete_airstrikeofjunta')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000451], quest_states=[2]):
            # 별, 수정, 그리고 퀘스트 완료 가능 상태
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031010, text_id=10031010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000451], quest_states=[3]):
            # 별, 수정, 그리고 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031010)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031020, text_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000452], quest_states=[1]):
            # 그림자의 파도 퀘스트 수락한 상태
            return Delay01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031020)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowWaveAgain01(self.ctx)


class ShadowWaveAgain01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000028, portal_id=12, box_id=9900)
        self.destroy_monster(spawn_ids=[103,202])
        self.spawn_monster(spawn_ids=[104,203], auto_target=False)
        self.select_camera(trigger_id=600)
        self.set_scene_skip(state=TimeToLeave05, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowWaveAgain02(self.ctx)


# 정면 1차 스폰 후 다리 패트롤 바로 시작
class ShadowWaveAgain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.set_agent(trigger_ids=[8102], visible=True)
        self.set_agent(trigger_ids=[8103], visible=True)
        self.set_agent(trigger_ids=[8106], visible=True)
        self.set_agent(trigger_ids=[8107], visible=True)
        self.set_agent(trigger_ids=[8108], visible=True)
        self.set_agent(trigger_ids=[8109], visible=True)
        self.set_agent(trigger_ids=[8110], visible=True)
        self.set_agent(trigger_ids=[8111], visible=True)
        self.set_agent(trigger_ids=[8112], visible=True)
        self.set_agent(trigger_ids=[8113], visible=True)
        self.set_agent(trigger_ids=[8114], visible=True)
        self.set_agent(trigger_ids=[8115], visible=True)
        self.spawn_monster(spawn_ids=[910,911,912,913])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWaveAgain03(self.ctx)


# 정면 2차 스폰 후 다리 패트롤 바로 시작
class ShadowWaveAgain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.set_effect(trigger_ids=[5100], visible=True) # Sound_ShadowApp_Loop
        self.set_effect(trigger_ids=[6003], visible=True) # Voice_Tinchai_00001717
        self.set_dialogue(type=1, spawn_id=104, script='$63000028_CS__BATTLE01__9$', time=3, arg5=1) # 틴차이 00001717
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_103')
        self.move_user_path(patrol_name='MS2PatrolData_1004')
        self.spawn_monster(spawn_ids=[920,921,922,923,924])
        self.move_npc(spawn_id=910, patrol_name='MS2PatrolData_910')
        self.move_npc(spawn_id=911, patrol_name='MS2PatrolData_911')
        self.move_npc(spawn_id=912, patrol_name='MS2PatrolData_912')
        self.move_npc(spawn_id=913, patrol_name='MS2PatrolData_913')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWaveAgain04(self.ctx)


# 카메라 워크
class ShadowWaveAgain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=920, patrol_name='MS2PatrolData_920')
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_922')
        self.move_npc(spawn_id=923, patrol_name='MS2PatrolData_923')
        self.move_npc(spawn_id=924, patrol_name='MS2PatrolData_924')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ShadowWaveAgain05(self.ctx)


class ShadowWaveAgain05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6102], visible=True) # Voice_Junta_00001775
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000028_CS__BATTLE01__10$', time=4) # 준타 00001775
        self.spawn_monster(spawn_ids=[930,931,932,933,950,951,952,953])
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_930')
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_931')
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_932')
        self.move_npc(spawn_id=933, patrol_name='MS2PatrolData_933')
        self.move_npc(spawn_id=950, patrol_name='MS2PatrolData_950')
        self.move_npc(spawn_id=951, patrol_name='MS2PatrolData_951')
        self.move_npc(spawn_id=952, patrol_name='MS2PatrolData_952')
        self.move_npc(spawn_id=953, patrol_name='MS2PatrolData_953')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowWaveAgain06(self.ctx)


# 양측 2차 스폰
class ShadowWaveAgain06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[940,941,942,943,944,945,960,961,962,963,964,965])
        self.move_npc(spawn_id=940, patrol_name='MS2PatrolData_940')
        self.move_npc(spawn_id=941, patrol_name='MS2PatrolData_941')
        self.move_npc(spawn_id=942, patrol_name='MS2PatrolData_942')
        self.move_npc(spawn_id=943, patrol_name='MS2PatrolData_943')
        self.move_npc(spawn_id=944, patrol_name='MS2PatrolData_944')
        self.move_npc(spawn_id=945, patrol_name='MS2PatrolData_945')
        self.move_npc(spawn_id=960, patrol_name='MS2PatrolData_960')
        self.move_npc(spawn_id=961, patrol_name='MS2PatrolData_961')
        self.move_npc(spawn_id=962, patrol_name='MS2PatrolData_962')
        self.move_npc(spawn_id=963, patrol_name='MS2PatrolData_963')
        self.move_npc(spawn_id=964, patrol_name='MS2PatrolData_964')
        self.move_npc(spawn_id=965, patrol_name='MS2PatrolData_965')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602)
        self.set_effect(trigger_ids=[6004], visible=True) # Voice_Tinchai_00001687
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000028_CS__BATTLE01__11$', time=4) # 틴차이 00001687
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave04(self.ctx)


class TimeToLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1005')
        self.select_camera(trigger_id=602, enable=False)
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return TimeToLeave05(self.ctx)


class TimeToLeave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104,203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=63000029, portal_id=1, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
