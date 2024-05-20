""" trigger/63000030_cs/flyingcloud01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # DownArrow
        self.set_effect(trigger_ids=[5200]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5201]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5202]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5203]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5204]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5205]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5300]) # FlyingCloud
        self.set_effect(trigger_ids=[5400]) # ShadowApp
        self.set_effect(trigger_ids=[6000]) # Voice_Tinchai_00001689
        self.set_effect(trigger_ids=[6001]) # Voice_Tinchai_00001690
        self.set_effect(trigger_ids=[6002]) # Voice_Tinchai_00001691
        self.set_effect(trigger_ids=[6003]) # Voice_Tinchai_00001692
        self.set_effect(trigger_ids=[6004]) # Voice_Tinchai_00001694
        self.set_effect(trigger_ids=[6005]) # Voice_Tinchai_00001695
        self.set_effect(trigger_ids=[6100]) # Voice_Junta_00001820
        self.set_effect(trigger_ids=[6101]) # Voice_Junta_00001780
        self.set_effect(trigger_ids=[6102]) # Voice_Junta_00001781
        self.set_effect(trigger_ids=[6103]) # Voice_Junta_00001782
        self.set_effect(trigger_ids=[6104]) # Voice_Junta_00001783
        self.set_effect(trigger_ids=[6105]) # Voice_Junta_00001792
        self.set_effect(trigger_ids=[6106]) # Voice_Junta_00001798
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_interact_object(trigger_ids=[10001010], state=0) # FlyingCloud
        self.set_breakable(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.set_mesh(trigger_ids=[3000,3001], visible=True) # Invisible_Bounding

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000455], quest_states=[1]):
            # 하산 퀘스트 수락한 상태
            return QuestOnGiong21(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000454], quest_states=[3]):
            # 여정의 명분 퀘스트 완료 상태
            return QuestOnGiong11(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000454], quest_states=[2]):
            # 여정의 명분 퀘스트 완료 가능 상태
            return QuestOnGiong01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000453], quest_states=[3]):
            # 무나크라의 계시 완료 상태
            return Delay01(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


# 하산 퀘스트 수락한 상태
class QuestOnGiong21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)
        self.move_user(map_id=63000030, portal_id=11, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestOnGiong22(self.ctx)


class QuestOnGiong22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PatrolWhileTalking03(self.ctx)


# 여정의 명분 퀘스트 완료 상태
class QuestOnGiong11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestOnGiong12(self.ctx)


class QuestOnGiong12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SecondQuestStart01(self.ctx)


# 여정의 명분 퀘스트 완료 가능 상태
class QuestOnGiong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestOnGiong02(self.ctx)


class QuestOnGiong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FirstQuestStart01(self.ctx)


# 최초 진입
class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[920,921,922,923,924,925,926,927,928,929,930,931], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,201], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=LookAround07_CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000030_CS__FLYINGCLOUD01__0$', time=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround05(self.ctx)


class LookAround05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6100], visible=True) # Voice_Junta_00001820
        self.set_dialogue(type=1, spawn_id=201, script='$63000030_CS__FLYINGCLOUD01__1$', time=2) # 준타 00001820
        self.move_npc(spawn_id=920, patrol_name='MS2PatrolData_920')
        self.move_npc(spawn_id=923, patrol_name='MS2PatrolData_923')
        self.move_npc(spawn_id=925, patrol_name='MS2PatrolData_925')
        self.move_npc(spawn_id=927, patrol_name='MS2PatrolData_927')
        self.move_npc(spawn_id=928, patrol_name='MS2PatrolData_928')
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_931')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround06(self.ctx)


class LookAround06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_922')
        self.move_npc(spawn_id=924, patrol_name='MS2PatrolData_924')
        self.move_npc(spawn_id=926, patrol_name='MS2PatrolData_926')
        self.move_npc(spawn_id=929, patrol_name='MS2PatrolData_929')
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_930')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround07(self.ctx)


class LookAround07_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=920, patrol_name='MS2PatrolData_920')
        self.move_npc(spawn_id=923, patrol_name='MS2PatrolData_923')
        self.move_npc(spawn_id=925, patrol_name='MS2PatrolData_925')
        self.move_npc(spawn_id=927, patrol_name='MS2PatrolData_927')
        self.move_npc(spawn_id=928, patrol_name='MS2PatrolData_928')
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_931')
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_922')
        self.move_npc(spawn_id=924, patrol_name='MS2PatrolData_924')
        self.move_npc(spawn_id=926, patrol_name='MS2PatrolData_926')
        self.move_npc(spawn_id=929, patrol_name='MS2PatrolData_929')
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_930')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround07(self.ctx)


class LookAround07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)
        self.select_camera(trigger_id=500, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10037010, text_id=10037010) # 가이드 : 검은 그림자 무리 처치하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[920,921,922,923,924,925,926,927,928,929,930,931]):
            return BattleEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10037010)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000030, portal_id=10, box_id=9900)
        self.destroy_monster(spawn_ids=[102,202])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False)
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=DialogueSkip10, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Dialogue01(self.ctx)


# 시네마틱 대화 연출
class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6101], visible=True) # Voice_Junta_00001780
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__FLYINGCLOUD01__2$', time=7) # 준타 00001780

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return DialogueSkip01(self.ctx)


class DialogueSkip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Tinchai_00001689
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__3$', time=6) # 틴차이 00001689

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DialogueSkip02(self.ctx)


class DialogueSkip02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001690
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__4$', time=6) # 틴차이 00001690

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DialogueSkip03(self.ctx)


class DialogueSkip03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6102], visible=True) # Voice_Junta_00001781
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__FLYINGCLOUD01__5$', time=6) # 준타 00001781

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DialogueSkip04(self.ctx)


class DialogueSkip04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue05(self.ctx)


class Dialogue05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Tinchai_00001691
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__6$', time=6) # 틴차이 00001691

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return DialogueSkip05(self.ctx)


class DialogueSkip05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue06(self.ctx)


class Dialogue06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Voice_Tinchai_00001692
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__7$', time=6) # 틴차이 00001692

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DialogueSkip06(self.ctx)


class DialogueSkip06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue07(self.ctx)


class Dialogue07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6103], visible=True) # Voice_Junta_00001782
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__FLYINGCLOUD01__8$', time=5) # 준타 00001782

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DialogueSkip07(self.ctx)


class DialogueSkip07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue08(self.ctx)


class Dialogue08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__9$', time=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return DialogueSkip08(self.ctx)


class DialogueSkip08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue09(self.ctx)


class Dialogue09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6104], visible=True) # Voice_Junta_00001783
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__FLYINGCLOUD01__10$', time=8) # 준타 00001783

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return DialogueSkip09(self.ctx)


class DialogueSkip09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue10(self.ctx)


class Dialogue10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6004], visible=True) # Voice_Tinchai_00001694
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__11$', time=5) # 틴차이 00001694
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DialogueSkip10(self.ctx)


class DialogueSkip10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.select_camera(trigger_id=501, enable=False)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FirstQuestStart01(self.ctx)


class FirstQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030160, text_id=10030160)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000454], quest_states=[2]):
            # 여정의 명분 퀘스트 바로 완료 가능 상태
            return FirstQuestEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030160)


class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031010, text_id=10031010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000454], quest_states=[3]):
            # 여정의 명분 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031010)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031020, text_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000455], quest_states=[1]):
            # 하산 퀘스트 수락한 상태
            return PatrolWhileTalking01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031020)


class PatrolWhileTalking01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PatrolWhileTalking02(self.ctx)


class PatrolWhileTalking02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103,203])
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)
        self.move_user(map_id=63000030, portal_id=11, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PatrolWhileTalking03(self.ctx)


class PatrolWhileTalking03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=FightBack01, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_203')
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolWhileTalking04(self.ctx)


class PatrolWhileTalking04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=204, script='$63000030_CS__FLYINGCLOUD01__12$', time=2)
        self.set_dialogue(type=1, spawn_id=204, script='$63000030_CS__FLYINGCLOUD01__13$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PatrolWhileTalking05(self.ctx)


class PatrolWhileTalking05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$63000030_CS__FLYINGCLOUD01__14$', time=2)
        self.set_dialogue(type=1, spawn_id=104, script='$63000030_CS__FLYINGCLOUD01__15$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=104, script='$63000030_CS__FLYINGCLOUD01__16$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return ShadowApp01(self.ctx)


class ShadowApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400], visible=True) # ShadowApp
        self.spawn_monster(spawn_ids=[940,941,942,943,944,945,946,947,948,949], auto_target=False)
        self.select_camera(trigger_id=600)
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowApp02(self.ctx)


class ShadowApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104')
        self.set_effect(trigger_ids=[6105], visible=True) # Voice_Junta_00001792
        self.set_dialogue(type=1, spawn_id=204, script='$63000030_CS__FLYINGCLOUD01__17$', time=2) # 준타 00001792

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return ShadowApp03(self.ctx)


class ShadowApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowApp04(self.ctx)


class ShadowApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$63000030_CS__FLYINGCLOUD01__18$', time=2)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ShadowApp05(self.ctx)


class ShadowApp05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FightBack01(self.ctx)


class FightBack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_205')
        self.set_effect(trigger_ids=[6106], visible=True) # Voice_Junta_00001798
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__FLYINGCLOUD01__19$', time=4) # 준타 00001798

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FightBack02(self.ctx)


class FightBack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FightBack03(self.ctx)


class FightBack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_105')
        self.set_effect(trigger_ids=[6005], visible=True) # Voice_Tinchai_00001695
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__FLYINGCLOUD01__20$', time=5) # 틴차이 00001695

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FightBack04(self.ctx)


class FightBack04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[5400]) # ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FightBack05(self.ctx)


class FightBack05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000030, portal_id=20, box_id=9900)
        self.destroy_monster(spawn_ids=[940,941,942,943,944,945,946,947,948,949])
        self.spawn_monster(spawn_ids=[910,911,912,913,914,915,916,917,918,919], auto_target=False)
        self.destroy_monster(spawn_ids=[104,204])
        self.spawn_monster(spawn_ids=[105,205], auto_target=False)
        self.select_camera(trigger_id=602)
        self.set_user_value(trigger_id=3, key='SafetyStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return FightBack06(self.ctx)


class FightBack06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_user_value(trigger_id=2, key='PushStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GotoTria01(self.ctx)


# 암벽등반 가이드 ClimbingGuide01
class GotoTria01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602, enable=False)
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5204], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5205], visible=True) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5100], visible=True) # DownArrow
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10037020, text_id=10037020) # 가이드 : 트라이아행 구름에 가까이 가기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return GotoTria02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10037020)


class GotoTria02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10037030, text_id=10037030) # 가이드 : 트라이아행 구름에 타기
        self.set_interact_object(trigger_ids=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001010], state=0):
            return TakeOffFlyingCloud01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10037030)
        self.set_effect(trigger_ids=[5100]) # DownArrow
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5201]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5202]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5203]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5204]) # 구름터 경로 안내
        self.set_effect(trigger_ids=[5205]) # 구름터 경로 안내


class TakeOffFlyingCloud01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True)
        self.set_breakable(trigger_ids=[4000], enable=True)
        self.set_interact_object(trigger_ids=[10001010], state=2) # FlyingCloud 숨기기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TakeOffFlyingCloud02(self.ctx)


class TakeOffFlyingCloud02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300], visible=True) # FlyingCloud
        self.set_mesh(trigger_ids=[3000,3001]) # Invisible_Bounding
        self.move_user(map_id=63000030, portal_id=30, box_id=9900)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TakeOffFlyingCloud03(self.ctx)


class TakeOffFlyingCloud03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TakeOffFlyingCloud04(self.ctx)


class TakeOffFlyingCloud04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000036, portal_id=1)
        self.select_camera(trigger_id=701, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
