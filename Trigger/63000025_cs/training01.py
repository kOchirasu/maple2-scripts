""" trigger/63000025_cs/training01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5101]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5102]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5103]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5104]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5105]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5200]) # 점프 경로 안내
        self.set_effect(trigger_ids=[5203]) # 점프 경로 안내
        self.set_effect(trigger_ids=[5301]) # 화살표 안내
        self.set_effect(trigger_ids=[5400]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5401]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5402]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5403]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5404]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5405]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5406]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5407]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5408]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5409]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5410]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5500]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5501]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5502]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5503]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5504]) # NPC 경로 안내
        self.set_effect(trigger_ids=[6000]) # Voice_Tinchai_00001676
        self.set_effect(trigger_ids=[6001]) # Voice_Tinchai_00001677
        self.set_effect(trigger_ids=[6002]) # Voice_Tinchai_00001678
        self.set_effect(trigger_ids=[6003]) # Voice_Tinchai_00001714
        self.set_effect(trigger_ids=[6004]) # Voice_Tinchai_00001679
        self.set_effect(trigger_ids=[6005]) # Voice_Tinchai_00001680
        self.set_effect(trigger_ids=[6006]) # Voice_Tinchai_00001720
        self.set_effect(trigger_ids=[6100]) # Voice_Junta_00001760
        self.set_effect(trigger_ids=[6101]) # Voice_Junta_00001761
        self.set_effect(trigger_ids=[6102]) # Voice_Junta_00001762
        self.set_effect(trigger_ids=[6103]) # Voice_Junta_00001763
        self.set_effect(trigger_ids=[6104]) # Voice_Junta_00001764
        self.set_effect(trigger_ids=[6105]) # Voice_Junta_00001765
        self.set_effect(trigger_ids=[6106]) # Voice_Junta_00001766
        self.set_effect(trigger_ids=[6107]) # Voice_Junta_00001767
        self.set_effect(trigger_ids=[6108]) # Voice_Junta_00001768
        self.set_effect(trigger_ids=[6109]) # Voice_Junta_00001769
        self.set_effect(trigger_ids=[6110]) # Voice_Junta_00001770
        self.set_effect(trigger_ids=[6111]) # Voice_Junta_00001771
        self.set_effect(trigger_ids=[6112]) # Voice_Junta_00001772
        self.set_interact_object(trigger_ids=[10001003], state=0) # Training

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000448], quest_states=[1]):
            # 마스터의 부르심 퀘스트 수락한 상태
            return TimeToLeave02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000447], quest_states=[3]):
            # 신속한 응집과 방출 퀘스트 완료 상태 : 스킬 사용 가이드 종료 후
            return ReadyToMove02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000447], quest_states=[2]):
            # 신속한 응집과 방출 퀘스트 완료 가능 상태
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000447], quest_states=[1]):
            # 신속한 응집과 방출 퀘스트 수락한 상태
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000446], quest_states=[3]):
            # 애니마르의 정석 기본편 퀘스트 완료 상태
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000446], quest_states=[2]):
            # 애니마르의 정석 기본편 퀘스트 완료 가능 상태
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000446], quest_states=[1]):
            # 애니마르의 정석 기본편 퀘스트 수락한 상태
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[3]):
            # 엄격한 대제자의 지도 퀘스트 완료 상태
            return QuestOnGoing31(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[2]):
            # 엄격한 대제자의 지도 퀘스트 완료 가능 상태
            return QuestOnGoing21(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[1]):
            # 엄격한 대제자의 지도 퀘스트 수락한 상태
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000444], quest_states=[3]):
            # 가이던스의 대제자 퀘스트 완료 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000444], quest_states=[2]):
            # 가이던스의 대제자 퀘스트 완료 가능 상태  : 최초 입장
            return Enter02(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


# 스킬 사용 가이드 진행 중인 상태
class QuestOnGoing41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000025, portal_id=10, box_id=9900)
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return QuestOnGoing42(self.ctx)


class QuestOnGoing42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SkillUseGuide02(self.ctx)


# 엄격한 대제자의 지도 퀘스트 완료 상태
class QuestOnGoing31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000025, portal_id=10, box_id=9900)
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return QuestOnGoing32(self.ctx)


class QuestOnGoing32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SkillUseGuide01(self.ctx)


# 엄격한 대제자의 지도 퀘스트 완료 가능 상태
class QuestOnGoing21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000025, portal_id=10, box_id=9900)
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return QuestOnGoing22(self.ctx)


class QuestOnGoing22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SecondQuestEnd01(self.ctx)


# 엄격한 대제자의 지도 퀘스트 수락한 상태
class QuestOnGoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000025, portal_id=30, box_id=9900)
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return QuestOnGoing12(self.ctx)


class QuestOnGoing12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JumpPointGuide01(self.ctx)


# 가이던스의 대제자 퀘스트 완료 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000025, portal_id=30, box_id=9900)
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SecondQuestStart01(self.ctx)


# 최초 입장
class Enter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=Dialogue10, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Enter03(self.ctx)


class Enter03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Enter04(self.ctx)


class Enter04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Enter05(self.ctx)


class Enter05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Enter06(self.ctx)


class Enter06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6100], visible=True) # Voice_Junta_00001760
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__0$', time=5) # 준타 00001760

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
        self.set_effect(trigger_ids=[6101], visible=True) # Voice_Junta_00001761
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__1$', time=7) # 준타 00001761
        self.set_skip(state=Dialogue04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue05(self.ctx)


class Dialogue05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Tinchai_00001676
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__2$', time=6) # 틴차이 00001676
        self.set_skip(state=Dialogue06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return Dialogue06(self.ctx)


class Dialogue06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue07(self.ctx)


class Dialogue07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6102], visible=True) # Voice_Junta_00001762
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__3$', time=6) # 준타 00001762
        self.set_skip(state=Dialogue08)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Dialogue08(self.ctx)


class Dialogue08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue09(self.ctx)


class Dialogue09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001677
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__4$', time=4) # 틴차이 00001677

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Dialogue10(self.ctx)


class Dialogue10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=502, enable=False)
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031010, text_id=10031010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000444], quest_states=[3]):
            # 가이던스의 대제자 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.hide_guide_summary(entity_id=10031010)
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031020, text_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[1]):
            # 엄격한 대제자의 지도 퀘스트 수락한 상태
            return JumpPointGuide01(self.ctx)


class JumpPointGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10031020)
        self.show_guide_summary(entity_id=10031030, text_id=10031030) # 가이드 : 물가로 이동하기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5100], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5101], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5102], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5103], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5104], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5105], visible=True) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5200], visible=True) # 점프 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 점프 경로 안내
        self.set_effect(trigger_ids=[5301], visible=True) # 화살표 안내
        self.destroy_monster(spawn_ids=[102,202])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JumpPointGuide02(self.ctx)


class JumpPointGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6103], visible=True) # Voice_Junta_00001763
        self.set_dialogue(type=1, spawn_id=103, script='$63000025_CS__TRAINING01__5$', time=3) # 준타 00001763
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # Water
            return JumpPointGuide03(self.ctx)


class JumpPointGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10031030)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : C키로 점프해 기둥 위로 올라가기
        self.show_guide_summary(entity_id=10031031, text_id=10031031)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            # TrainingPoint
            return JumpPointGuide04(self.ctx)


class JumpPointGuide04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001003], state=1) # Training
        self.hide_guide_summary(entity_id=10031031)
        # 가이드 : 스페이스 키를 눌러 기둥 위에서 수련하기
        self.show_guide_summary(entity_id=10031032, text_id=10031032)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5301]) # 화살표 안내
        self.set_effect(trigger_ids=[5100]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5101]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5102]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5103]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5104]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5105]) # 웅덩이 경로 안내
        self.set_effect(trigger_ids=[5200]) # 점프 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[2]):
            # 엄격한 대제자의 지도 퀘스트 완료 가능 상태
            return SecondQuestEnd01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103,203])
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)
        self.hide_guide_summary(entity_id=10031032)


class SecondQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5203]) # 점프 경로 안내
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10031050, text_id=10031050) # 가이드 : 준타를 향해 이동하기
        self.set_effect(trigger_ids=[5500], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5501], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5502], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5503], visible=True) # NPC 경로 안내
        self.set_effect(trigger_ids=[5504], visible=True) # NPC 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            # NPC
            return SecondQuestEnd02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031050)
        self.set_effect(trigger_ids=[5500]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5501]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5502]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5503]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5504]) # NPC 경로 안내
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5203]) # 점프 경로 안내


class SecondQuestEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031010, text_id=10031010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000445], quest_states=[3]):
            # 엄격한 대제자의 지도 퀘스트 완료 상태
            return SkillUseGuide01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031010)


# 스킬 사용 퀘스트 2개 90000446, 90000447 가이드
class SkillUseGuide01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SkillUseGuide02(self.ctx)


class SkillUseGuide02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000447], quest_states=[3]):
            # 신속한 응집과 방출 퀘스트 완료 상태
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToMove01(self.ctx)


class ReadyToMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ReadyToMove02(self.ctx)


class ReadyToMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.destroy_monster(spawn_ids=[104,204]) # Talk
        self.spawn_monster(spawn_ids=[105,205], auto_target=False) # Actor
        self.move_user(map_id=63000025, portal_id=10, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PatrolWalk01(self.ctx)


class PatrolWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolWalk02(self.ctx)


class PatrolWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FeelStrange01(self.ctx)


class FeelStrange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6104], visible=True) # Voice_Junta_00001764
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__6$', time=5) # 준타 00001764
        self.set_scene_skip(state=FeelStrange18, action='nextState')
        self.set_skip(state=FeelStrange02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FeelStrange02(self.ctx)


class FeelStrange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange03(self.ctx)


class FeelStrange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6105], visible=True) # Voice_Junta_00001765
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__7$', time=3) # 준타 00001765
        self.set_skip(state=FeelStrange04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FeelStrange04(self.ctx)


class FeelStrange04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange05(self.ctx)


class FeelStrange05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Tinchai_00001678
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__8$', time=4) # 틴차이 00001678
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FeelStrange06(self.ctx)


class FeelStrange06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange07(self.ctx)


class FeelStrange07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6106], visible=True) # Voice_Junta_00001766
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__9$', time=4) # 준타 00001766
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange08)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FeelStrange08(self.ctx)


class FeelStrange08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange09(self.ctx)


class FeelStrange09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Voice_Tinchai_00001714
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__10$', time=4) # 틴차이 00001714
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FeelStrange10(self.ctx)


class FeelStrange10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange11(self.ctx)


class FeelStrange11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6107], visible=True) # Voice_Junta_00001767
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__11$', time=6) # 준타 00001767
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return FeelStrange12(self.ctx)


class FeelStrange12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange13(self.ctx)


class FeelStrange13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6004], visible=True) # Voice_Tinchai_00001679
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__12$', time=4) # 틴차이 00001679
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FeelStrange14(self.ctx)


class FeelStrange14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange15(self.ctx)


class FeelStrange15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6108], visible=True) # Voice_Junta_00001768
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__13$', time=5) # 준타 00001768
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')
        self.set_skip(state=FeelStrange16)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FeelStrange16(self.ctx)


class FeelStrange16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FeelStrange17(self.ctx)


class FeelStrange17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6005], visible=True) # Voice_Tinchai_00001680
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000025_CS__TRAINING01__14$', time=3) # 틴차이 00001680

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FeelStrange18(self.ctx)


class FeelStrange18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[105,205]) # Actor
        self.spawn_monster(spawn_ids=[106,206], auto_target=False) # Talk

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LastQuestStart01(self.ctx)


class LastQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031020, text_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000448], quest_states=[1]):
            # 마스터의 부르심 수락한 상태
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MinimapGuide01(self.ctx)


class MinimapGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[6109], visible=True) # Voice_Junta_00001769
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000025_CS__TRAINING01__19$', time=7) # 준타 00001769
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Talk_A')
        self.set_skip(state=MinimapGuide02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return MinimapGuide02(self.ctx)


class MinimapGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return MinimapGuide03(self.ctx)


# 미니맵 가이드 : 트리거 To 가이드
class MinimapGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기
        self.guide_event(event_id=10031080)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10031083:
            # 가이드 To 트리거 -: 미니맵 크게 보기 완료
            return Delay03(self.ctx)


class Delay03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True)
        self.move_user(map_id=63000025, portal_id=20, box_id=9900)
        self.destroy_monster(spawn_ids=[106,206]) # Talk
        self.spawn_monster(spawn_ids=[107,207], auto_target=False) # Actor
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=NpcLeave_CSkip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Monologue01(self.ctx)


class Monologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6110], visible=True) # Voice_Junta_00001770
        self.set_dialogue(type=1, spawn_id=107, script='$63000025_CS__TRAINING01__15$', time=2) # 준타 00001770

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return Monologue02(self.ctx)


class Monologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_104')
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_204')
        self.set_effect(trigger_ids=[6111], visible=True) # Voice_Junta_00001771
        self.set_dialogue(type=1, spawn_id=107, script='$63000025_CS__TRAINING01__16$', time=3) # 준타 00001771

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Monologue03(self.ctx)


class Monologue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6006], visible=True) # Voice_Tinchai_00001720
        self.set_dialogue(type=1, spawn_id=207, script='$63000025_CS__TRAINING01__17$', time=3) # 틴차이 00001720

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Monologue04(self.ctx)


class Monologue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=702)
        self.set_effect(trigger_ids=[6112], visible=True) # Voice_Junta_00001772
        self.set_dialogue(type=1, spawn_id=107, script='$63000025_CS__TRAINING01__18$', time=2) # 준타 00001772

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2200):
            return NpcLeave01(self.ctx)


class NpcLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[107])
        self.move_user(map_id=63000025, portal_id=40, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return NpcLeave02(self.ctx)


class NpcLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[207])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GuideNextMap01(self.ctx)


class NpcLeave_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[107])
        self.destroy_monster(spawn_ids=[207])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=702, enable=False)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10020012, text_id=10020012)
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5400], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5401], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5402], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5403], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5404], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5405], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5406], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5407], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5408], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5409], visible=True) # 포털 경로 안내
        self.set_effect(trigger_ids=[5410], visible=True) # 포털 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10020012)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=1060, text_id=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.hide_guide_summary(entity_id=1060)
        self.set_effect(trigger_ids=[5400]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5401]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5402]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5403]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5404]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5405]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5406]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5407]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5408]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5409]) # 포털 경로 안내
        self.set_effect(trigger_ids=[5410]) # 포털 경로 안내


initial_state = Wait
