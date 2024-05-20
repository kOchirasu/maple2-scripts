""" trigger/63000029_cs/cave01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5003]) # BlockApp 사운드 이펙트
        # EnteranceExplosion Vibrate 사운드 이펙트
        self.set_effect(trigger_ids=[5004])
        # GroundSplit Vibrate 사운드 이펙트
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5100]) # LiftableTargetBox
        self.set_effect(trigger_ids=[5200]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5201]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5202]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5203]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5300]) # DownArrow
        self.set_effect(trigger_ids=[5400]) # RockDeris_Enterance
        self.set_effect(trigger_ids=[5500]) # Dust_Enterance
        self.set_effect(trigger_ids=[5501]) # Dust_Enterance
        self.set_effect(trigger_ids=[5502]) # Dust_Enterance
        self.set_effect(trigger_ids=[5503]) # Dust_Enterance
        self.set_effect(trigger_ids=[5504]) # Dust_Enterance
        self.set_effect(trigger_ids=[5505]) # Dust_Enterance
        self.set_effect(trigger_ids=[5506]) # Dust_Enterance
        self.set_effect(trigger_ids=[5507]) # Dust_Enterance
        self.set_effect(trigger_ids=[5700]) # Dust_Split
        self.set_effect(trigger_ids=[5701]) # Dust_Split
        self.set_effect(trigger_ids=[5702]) # Dust_Split
        self.set_effect(trigger_ids=[5703]) # Dust_Split
        self.set_effect(trigger_ids=[5704]) # Dust_Split
        self.set_effect(trigger_ids=[5705]) # Dust_Split
        self.set_effect(trigger_ids=[5706]) # Dust_Split
        self.set_effect(trigger_ids=[5707]) # Dust_Split
        self.set_effect(trigger_ids=[5708]) # Dust_Split
        self.set_effect(trigger_ids=[5709]) # Dust_Split
        # SandStormSmall_GroundCollapse
        self.set_effect(trigger_ids=[5600])
        self.set_effect(trigger_ids=[5800]) # Rumble
        self.set_effect(trigger_ids=[5801]) # Earthquake
        # LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5820])
        # LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5821])
        self.set_effect(trigger_ids=[5900]) # StoneGate
        self.set_effect(trigger_ids=[5901]) # ShadowApp
        # Sound_LaozExplosionRumble
        self.set_effect(trigger_ids=[5920])
        # Voice_LaozBattle_Attack_00001875
        self.set_effect(trigger_ids=[5921])
        # Voice_LaozBattle_Attack_00001874
        self.set_effect(trigger_ids=[5922])
        # Sound_LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5930])
        # Sound_LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5931])
        self.set_effect(trigger_ids=[6000]) # Voice_Laoz_00001847
        self.set_effect(trigger_ids=[6001]) # Voice_Laoz_00001822
        self.set_effect(trigger_ids=[6002]) # Voice_Laoz_00001823
        self.set_effect(trigger_ids=[6003]) # Voice_Laoz_00001824
        self.set_effect(trigger_ids=[6004]) # Voice_Laoz_00001825
        self.set_effect(trigger_ids=[6005]) # Voice_Laoz_00001826
        self.set_effect(trigger_ids=[6006]) # Voice_Laoz_00001827
        self.set_effect(trigger_ids=[6007]) # Voice_Laoz_00001828
        self.set_effect(trigger_ids=[6008]) # Voice_Laoz_00001829
        self.set_effect(trigger_ids=[6009]) # Voice_Laoz_00001831
        self.set_effect(trigger_ids=[6010]) # Voice_Laoz_00001834
        self.set_effect(trigger_ids=[6100]) # Voice_Kandura_00001855
        self.set_effect(trigger_ids=[6101]) # Voice_Kandura_00001856
        self.set_effect(trigger_ids=[6102]) # Voice_Kandura_00001857
        self.set_effect(trigger_ids=[6103]) # Voice_Kandura_00001858
        self.set_effect(trigger_ids=[6104]) # Voice_Kandura_00001859
        self.set_effect(trigger_ids=[6105]) # Voice_Kandura_00001860
        self.set_effect(trigger_ids=[6106]) # Voice_Kandura_00001861
        self.set_effect(trigger_ids=[6107]) # Voice_Kandura_00001862
        self.set_effect(trigger_ids=[6200]) # Voice_Junta_00001779
        self.set_effect(trigger_ids=[6201]) # Voice_Junta_00001770
        self.set_effect(trigger_ids=[6300]) # Voice_Tinchai_00001688
        self.set_effect(trigger_ids=[6301]) # Voice_Tinchai_00001717
        # Voice_JuntaNTinchai_00001873
        self.set_effect(trigger_ids=[6400])
        # Invisible_EnteranceBlock
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_mesh(trigger_ids=[3002,3003,3004]) # Invisible_SplitBlock
        self.set_mesh(trigger_ids=[3005], visible=True) # Invisible_StoneGate
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108]) # MeshGroup01_Block
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], visible=True) # MeshGroup03_SplitTop
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True) # MeshGroup04_SplitSide
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='or_fi_struc_stonegate_A01_off') # StoneGate
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509]) # CollapseStart
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
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.set_agent(trigger_ids=[8016])
        self.set_agent(trigger_ids=[8017])
        self.set_agent(trigger_ids=[8018])
        self.set_agent(trigger_ids=[8019])
        self.set_agent(trigger_ids=[8020])
        self.set_agent(trigger_ids=[8021])
        self.set_agent(trigger_ids=[8022])
        self.set_agent(trigger_ids=[8023])
        self.set_agent(trigger_ids=[8024])
        self.set_agent(trigger_ids=[8025])
        self.set_agent(trigger_ids=[8026])
        self.set_agent(trigger_ids=[8027])
        self.spawn_monster(spawn_ids=[101,201], auto_target=False)
        self.set_skill(trigger_ids=[7000]) # 바닥 큐브 부수기 스킬
        self.set_skill(trigger_ids=[7001]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[7002]) # 그림자 소멸 스킬
        self.set_skill(trigger_ids=[7003]) # 천장 부수기 스킬
        self.set_skill(trigger_ids=[7100]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7101]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7102]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7103]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7104]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7105]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7106]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7107]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7108]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(trigger_ids=[7109]) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_breakable(trigger_ids=[4000])
        self.set_breakable(trigger_ids=[4001])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000453], quest_states=[3]):
            # 무나크라의 계시 퀘스트 완료 상태
            return QuestOnGiong11(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000453], quest_states=[2]):
            # 무나크라의 계시 퀘스트 완료 가능 상태
            return QuestOnGiong01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000453], quest_states=[1]):
            # 무나크라의 계시 퀘스트 수락한 상태
            return LiftRock01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000452], quest_states=[3]):
            # 그림자의 파도 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000452], quest_states=[2]):
            # 그림자의 파도 퀘스트 완료 가능 상태
            return FirstQuestEnd01(self.ctx)


# 무나크라의 계시 퀘스트 완료 상태
class QuestOnGiong11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGiong12(self.ctx)


class QuestOnGiong12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000029, portal_id=30, box_id=9900)
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[110,210,302], auto_target=False)
        # Invisible_EnteranceBlock
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_random_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, start_delay=9) # MeshGroup01_Block

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGiong13(self.ctx)


class QuestOnGiong13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Delay01(self.ctx)


# 무나크라의 계시 퀘스트 완료 가능 상태
class QuestOnGiong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGiong02(self.ctx)


class QuestOnGiong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000029, portal_id=20, box_id=9900)
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)
        # Invisible_EnteranceBlock
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_random_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, start_delay=9) # MeshGroup01_Block

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return QuestOnGiong03(self.ctx)


class QuestOnGiong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_dialogue(type=1, spawn_id=102, script='$63000029_CS__CAVE01__0$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestOnGiong04(self.ctx)


class QuestOnGiong04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LaozApp01(self.ctx)


# 최초 입장
class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기
        self.show_guide_summary(entity_id=10030100, text_id=10030100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000452], quest_states=[3]):
            # 그림자의 파도 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030100)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entity_id=10031020, text_id=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000453], quest_states=[1]):
            # 무나크라의 계시 퀘스트 수락한 상태
            return LiftRock01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10031020)


# 바위로 동굴 입구 막기
class LiftRock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entity_id=10036010, text_id=10036010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기
        self.set_effect(trigger_ids=[5300], visible=True) # DownArrow
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if not self.detect_liftable_object(box_ids=[9001], item_id=30000441):
            # 돌이 없어지면
            return LiftRock02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10036010)


class LiftRock02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300]) # DownArrow
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 알림 사운드
        # 가이드 : 스페이스 키로 방위덩이 내려놔 동굴 입구 막기
        self.show_guide_summary(entity_id=10036011, text_id=10036011)
        self.set_effect(trigger_ids=[5100], visible=True) # LiftableTargetBox
        self.set_effect(trigger_ids=[5200], visible=True) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5201], visible=True) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5202], visible=True) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5203], visible=True) # LiftableTargetGuide

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9002], item_id=30000441):
            # 돌을 타겟 박스에 놓으면
            return LiftRock03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10036011)


class LiftRock03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # LiftableTargetBox
        self.set_effect(trigger_ids=[5200]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5201]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5202]) # LiftableTargetGuide
        self.set_effect(trigger_ids=[5203]) # LiftableTargetGuide

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return EnteranceBlock01(self.ctx)


class EnteranceBlock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return EnteranceBlock02(self.ctx)


class EnteranceBlock02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000029, portal_id=10, box_id=9900)
        self.select_camera(trigger_id=500)
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return EnteranceBlock03(self.ctx)


class EnteranceBlock03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=LaozApp05_CSkip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5003], visible=True) # BlockApp 사운드 이펙트
        # Invisible_EnteranceBlock
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_random_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, start_delay=9, interval=100, fade=100) # MeshGroup01_Block

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TimeToMoveIn01(self.ctx)


class TimeToMoveIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TimeToMoveIn02(self.ctx)


class TimeToMoveIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$63000029_CS__CAVE01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TimeToMoveIn03(self.ctx)


class TimeToMoveIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$63000029_CS__CAVE01__2$', time=2)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LaozApp01(self.ctx)


class LaozApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')
        # Voice_JuntaNTinchai_00001873
        self.set_effect(trigger_ids=[6400], visible=True)
        self.set_dialogue(type=1, spawn_id=202, script='$63000029_CS__CAVE01__3$', time=2) # Voice 둘이 함께 00001873
        self.set_dialogue(type=1, spawn_id=102, script='$63000029_CS__CAVE01__4$', time=2)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LaozApp02(self.ctx)


class LaozApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return LaozApp03(self.ctx)


class LaozApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return LaozApp04(self.ctx)


class LaozApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$63000029_CS__CAVE01__5$', time=3)
        self.set_dialogue(type=1, spawn_id=102, script='$63000029_CS__CAVE01__6$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozApp05(self.ctx)


class LaozApp05_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000029, portal_id=10, box_id=9900)
        self.destroy_monster(spawn_ids=[101,201])
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_201')
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LaozTalk01(self.ctx)


class LaozApp05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LaozTalk01(self.ctx)


class LaozTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Laoz_00001847
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__7$', time=5) # 라오즈 00001847
        self.set_skip(state=LaozTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LaozTalk02(self.ctx)


class LaozTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozTalk03(self.ctx)


class LaozTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__8$', time=4) # 라오즈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozTalk04(self.ctx)


class LaozTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[301])
        self.spawn_monster(spawn_ids=[302], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=601, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetLaoz01(self.ctx)


class MeetLaoz01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10036020, text_id=10036020) # 가이드 : 라오즈에게 가까이 가기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return SecondQuestEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10036020)


class SecondQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 라오즈와 대화하기
        self.show_guide_summary(entity_id=10036030, text_id=10036030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000453], quest_states=[3]):
            # 무나크라의 계시 퀘스트 완료 상태
            return Delay01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10036030)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3, key='SafetyStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # EnteranceExplosion 사운드 이펙트
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnteranceBlockExplosion01(self.ctx)


class EnteranceBlockExplosion01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=LaozNKahnTalk18_CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return EnteranceBlockExplosion02(self.ctx)


class EnteranceBlockExplosion02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000029, portal_id=11, box_id=9900)
        self.select_camera(trigger_id=610)
        self.destroy_monster(spawn_ids=[102,202,302,110,210])
        self.spawn_monster(spawn_ids=[103,203,303], auto_target=False)
        self.set_random_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108], start_delay=9, interval=100, fade=100) # MeshGroup01_Block

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return EnteranceBlockExplosion03(self.ctx)


class EnteranceBlockExplosion03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5400], visible=True) # RockDeris_Enterance
        # Invisible_EnteranceBlock
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_skill(trigger_ids=[7001], enable=True) # 입구 큐브 부수기 스킬
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_401')
        self.set_effect(trigger_ids=[5500], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5501], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5502], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5503], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5504], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5505], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5506], visible=True) # Dust_Enterance
        self.set_effect(trigger_ids=[5507], visible=True) # Dust_Enterance

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KahnWalkIn01(self.ctx)


class KahnWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5901], visible=True) # ShadowApp
        self.set_effect(trigger_ids=[6100], visible=True) # Voice_Kandura_00001855
        self.set_dialogue(type=1, spawn_id=401, script='$63000029_CS__CAVE01__9$', time=3) # 칸두라 00001855
        self.spawn_monster(spawn_ids=[900,901,902,903], auto_target=False)
        self.move_npc(spawn_id=900, patrol_name='MS2PatrolData_900')
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_901')
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_902')
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_903')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return KahnWalkIn02(self.ctx)


class KahnWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[904,905,906], auto_target=False)
        self.move_npc(spawn_id=904, patrol_name='MS2PatrolData_904')
        self.move_npc(spawn_id=905, patrol_name='MS2PatrolData_905')
        self.move_npc(spawn_id=906, patrol_name='MS2PatrolData_906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return KahnWalkIn03(self.ctx)


class KahnWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907,908,909], auto_target=False)
        self.move_npc(spawn_id=907, patrol_name='MS2PatrolData_907')
        self.move_npc(spawn_id=908, patrol_name='MS2PatrolData_908')
        self.move_npc(spawn_id=909, patrol_name='MS2PatrolData_909')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return KahnWalkIn04(self.ctx)


class KahnWalkIn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[940,941,942,943], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KahnWalkIn05(self.ctx)


class KahnWalkIn05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[920,921,922,923,924,925,926,927,928,929,930,931], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KahnWalkIn06(self.ctx)


class KahnWalkIn06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=611)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KahnWalkIn07(self.ctx)


class KahnWalkIn07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_302')
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Laoz_00001822
        self.set_dialogue(type=1, spawn_id=303, script='$63000029_CS__CAVE01__10$', time=3) # 라오즈 00001822

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToFight01(self.ctx)


class ReadyToFight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_202')
        self.set_dialogue(type=1, spawn_id=203, script='$63000029_CS__CAVE01__11$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ReadyToFight02(self.ctx)


class ReadyToFight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_102')
        self.set_dialogue(type=1, spawn_id=103, script='$63000029_CS__CAVE01__12$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ReadyToFight03(self.ctx)


class ReadyToFight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Attack_Idle_A', duration=90000.0)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Attack_Idle_A', duration=90000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return MeetKahn01(self.ctx)


class MeetKahn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6101], visible=True) # Voice_Kandura_00001856
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__13$', time=9) # 칸두라 00001856
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return MeetKahn02(self.ctx)


class MeetKahn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return MeetKahn03(self.ctx)


class MeetKahn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Laoz_00001823
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__14$', time=4) # 라오즈 00001823
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MeetKahn04(self.ctx)


class MeetKahn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=620)

    def on_tick(self) -> trigger_api.Trigger:
        return LaozTalkToJuntaNTinChai01(self.ctx)


class LaozTalkToJuntaNTinChai01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Voice_Laoz_00001824
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__15$', time=8) # 라오즈 00001824
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return LaozTalkToJuntaNTinChai02(self.ctx)


class LaozTalkToJuntaNTinChai02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozTalkToJuntaNTinChai03(self.ctx)


class LaozTalkToJuntaNTinChai03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000029_CS__CAVE01__16$', time=4) # 준타
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozTalkToJuntaNTinChai04(self.ctx)


class LaozTalkToJuntaNTinChai04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozTalkToJuntaNTinChai05(self.ctx)


class LaozTalkToJuntaNTinChai05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000029_CS__CAVE01__17$', time=4) # 틴차이
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozTalkToJuntaNTinChai06(self.ctx)


class LaozTalkToJuntaNTinChai06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozTalkToJuntaNTinChai07(self.ctx)


class LaozTalkToJuntaNTinChai07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Laoz_00001847
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__18$', time=4) # 라오즈 00001847
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozTalkToJuntaNTinChai08(self.ctx)


class LaozTalkToJuntaNTinChai08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=611)
        self.spawn_monster(spawn_ids=[945,946], auto_target=False)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_402')
        self.move_npc(spawn_id=900, patrol_name='MS2PatrolData_910')
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_911')
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_912')
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_913')
        self.move_npc(spawn_id=904, patrol_name='MS2PatrolData_914')
        self.move_npc(spawn_id=905, patrol_name='MS2PatrolData_915')
        self.move_npc(spawn_id=906, patrol_name='MS2PatrolData_916')
        self.move_npc(spawn_id=907, patrol_name='MS2PatrolData_917')
        self.move_npc(spawn_id=908, patrol_name='MS2PatrolData_918')
        self.move_npc(spawn_id=909, patrol_name='MS2PatrolData_919')
        self.move_npc(spawn_id=920, patrol_name='MS2PatrolData_920')
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_922')
        self.move_npc(spawn_id=923, patrol_name='MS2PatrolData_923')
        self.move_npc(spawn_id=924, patrol_name='MS2PatrolData_924')
        self.move_npc(spawn_id=925, patrol_name='MS2PatrolData_925')
        self.move_npc(spawn_id=926, patrol_name='MS2PatrolData_926')
        self.move_npc(spawn_id=927, patrol_name='MS2PatrolData_927')
        self.move_npc(spawn_id=928, patrol_name='MS2PatrolData_928')
        self.move_npc(spawn_id=929, patrol_name='MS2PatrolData_929')
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_930')
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_931')
        self.move_npc(spawn_id=940, patrol_name='MS2PatrolData_940')
        self.move_npc(spawn_id=941, patrol_name='MS2PatrolData_941')
        self.move_npc(spawn_id=942, patrol_name='MS2PatrolData_942')
        self.move_npc(spawn_id=943, patrol_name='MS2PatrolData_943')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LaozNKahnTalk01(self.ctx)


class LaozNKahnTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[947,948,949], auto_target=False)
        self.move_npc(spawn_id=945, patrol_name='MS2PatrolData_945')
        self.move_npc(spawn_id=946, patrol_name='MS2PatrolData_946')
        self.spawn_monster(spawn_ids=[950,951,952,953,954,955,956,957,958,959], auto_target=False)
        self.move_npc(spawn_id=950, patrol_name='MS2PatrolData_900')
        self.move_npc(spawn_id=951, patrol_name='MS2PatrolData_901')
        self.move_npc(spawn_id=952, patrol_name='MS2PatrolData_902')
        self.move_npc(spawn_id=953, patrol_name='MS2PatrolData_903')
        self.move_npc(spawn_id=954, patrol_name='MS2PatrolData_904')
        self.move_npc(spawn_id=955, patrol_name='MS2PatrolData_905')
        self.move_npc(spawn_id=956, patrol_name='MS2PatrolData_906')
        self.move_npc(spawn_id=957, patrol_name='MS2PatrolData_907')
        self.move_npc(spawn_id=958, patrol_name='MS2PatrolData_908')
        self.move_npc(spawn_id=959, patrol_name='MS2PatrolData_909')
        self.set_effect(trigger_ids=[6004], visible=True) # Voice_Laoz_00001825
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__19$', time=9) # 라오즈 00001825
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.select_camera(trigger_id=612)
        self.set_skip(state=LaozNKahnTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return LaozNKahnTalk02(self.ctx)


class LaozNKahnTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LaozNKahnTalk03(self.ctx)


class LaozNKahnTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')
        self.set_effect(trigger_ids=[6102], visible=True) # Voice_Kandura_00001857
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__20$', time=9) # 칸두라 00001857

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return LaozNKahnTalk04(self.ctx)


class LaozNKahnTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozNKahnTalk05(self.ctx)


class LaozNKahnTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')
        self.set_effect(trigger_ids=[6103], visible=True) # Voice_Kandura_00001858
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__21$', time=6) # 칸두라 00001858
        self.set_skip(state=LaozNKahnTalk06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LaozNKahnTalk06(self.ctx)


class LaozNKahnTalk06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozNKahnTalk07(self.ctx)


class LaozNKahnTalk07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6005], visible=True) # Voice_Laoz_00001826
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__22$', time=7) # 라오즈 00001826

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LaozNKahnTalk08(self.ctx)


class LaozNKahnTalk08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozNKahnTalk09(self.ctx)


class LaozNKahnTalk09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6006], visible=True) # Voice_Laoz_00001827
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__23$', time=7) # 라오즈 00001827

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LaozNKahnTalk10(self.ctx)


class LaozNKahnTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozNKahnTalk11(self.ctx)


class LaozNKahnTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')
        self.set_effect(trigger_ids=[6104], visible=True) # Voice_Kandura_00001859
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__24$', time=7) # 칸두라 00001859

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LaozNKahnTalk12(self.ctx)


class LaozNKahnTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozNKahnTalk13(self.ctx)


class LaozNKahnTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6007], visible=True) # Voice_Laoz_00001828
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__25$', time=8) # 라오즈 00001828

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return LaozNKahnTalk14(self.ctx)


class LaozNKahnTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozNKahnTalk15(self.ctx)


class LaozNKahnTalk15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6105], visible=True) # Voice_Kandura_00001860
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__26$', time=7) # 칸두라 00001860
        self.select_camera(trigger_id=621)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return LaozNKahnTalk16(self.ctx)


class LaozNKahnTalk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LaozNKahnTalk17(self.ctx)


class LaozNKahnTalk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6106], visible=True) # Voice_Kandura_00001861
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__27$', time=4) # 칸두라 00001861
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LaozNKahnTalk18(self.ctx)


class LaozNKahnTalk18_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,202,302,110,210])
        self.spawn_monster(spawn_ids=[103,203,303], auto_target=False)
        self.move_user(map_id=63000029, portal_id=12, box_id=9900)
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleReady01(self.ctx)


class LaozNKahnTalk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return BattleReady01(self.ctx)


class BattleReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=630)
        self.move_user(map_id=63000029, portal_id=12, box_id=9900)
        self.destroy_monster(spawn_ids=[103,203,303,401])
        self.spawn_monster(spawn_ids=[105,205,305,403], auto_target=False)
        self.destroy_monster(spawn_ids=[900,901,902,903,904,905,906,907,908,909,920,921,922,923,924,925,926,927,928,929,930,931,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959])
        self.spawn_monster(spawn_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleReady02(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=205, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=305, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=403, sequence_name='Attack_Idle_A', duration=15000.0)


class BattleReady02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=631)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LaozKillAll01(self.ctx)


class LaozKillAll01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_303')
        self.set_dialogue(type=1, spawn_id=305, script='$63000029_CS__CAVE01__28$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LaozKillAll02(self.ctx)


class LaozKillAll02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice_LaozBattle_Attack_00001875
        self.set_effect(trigger_ids=[5921], visible=True)
        self.set_npc_emotion_sequence(spawn_id=305, sequence_name='Attack_01_D') # 임시
        self.select_camera(trigger_id=632)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return LaozKillAll03(self.ctx)


class LaozKillAll03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # GroundSplit Vibrate 사운드 이펙트
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_skill(trigger_ids=[7002], enable=True) # 그림자 소멸 스킬
        # Sound_LaozExplosionRumble
        self.set_effect(trigger_ids=[5920], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return LaozSplitGround01(self.ctx)


class LaozSplitGround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=305, sequence_name='Attack_01_B') # 임시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LaozSplitGround02(self.ctx)


class LaozSplitGround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice_LaozBattle_Attack_00001874
        self.set_effect(trigger_ids=[5922], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LaozSplitGround03(self.ctx)


class LaozSplitGround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5901]) # ShadowApp
        # GroundSplit Vibrate 사운드 이펙트
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_mesh(trigger_ids=[3002,3003,3004], visible=True) # Invisible_SplitBlock
        self.set_random_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], start_delay=36, fade=25) # MeshGroup03_SplitTop
        self.set_random_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], start_delay=17, fade=25) # MeshGroup04_SplitSide

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LaozSplitGround04(self.ctx)


class LaozSplitGround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5700], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5701], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5702], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5703], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5704], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5705], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5706], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5707], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5708], visible=True) # Dust_Split
        self.set_effect(trigger_ids=[5709], visible=True) # Dust_Split

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LeftBehind00(self.ctx)


class LeftBehind00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=633)
        self.set_scene_skip(state=Earthquake_CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LeftBehind01(self.ctx)


class LeftBehind01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6008], visible=True) # Voice_Laoz_00001829
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__29$', time=8) # 라오즈 00001829
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
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_agent(trigger_ids=[8014], visible=True)
        self.set_agent(trigger_ids=[8015], visible=True)
        self.set_agent(trigger_ids=[8016], visible=True)
        self.set_agent(trigger_ids=[8017], visible=True)
        self.set_agent(trigger_ids=[8018], visible=True)
        self.set_agent(trigger_ids=[8019], visible=True)
        self.set_agent(trigger_ids=[8020], visible=True)
        self.set_agent(trigger_ids=[8021], visible=True)
        self.set_agent(trigger_ids=[8022], visible=True)
        self.set_agent(trigger_ids=[8023], visible=True)
        self.set_agent(trigger_ids=[8024], visible=True)
        self.set_agent(trigger_ids=[8025], visible=True)
        self.set_agent(trigger_ids=[8026], visible=True)
        self.set_agent(trigger_ids=[8027], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return LeftBehind02(self.ctx)


class LeftBehind02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LeftBehind03(self.ctx)


class LeftBehind03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6200], visible=True) # Voice_Junta_00001779
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000029_CS__CAVE01__30$', time=6) # 준타 00001779

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LeftBehind04(self.ctx)


class LeftBehind04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LeftBehind05(self.ctx)


class LeftBehind05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[6009], visible=True) # Voice_Laoz_00001831
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__31$', time=7) # 라오즈 00001831

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LeftBehind06(self.ctx)


class LeftBehind06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=303, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LeftBehind07(self.ctx)


class LeftBehind07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000029_CS__CAVE01__32$', time=4) # 틴차이 00001688

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LeftBehind08(self.ctx)


class LeftBehind08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LeftBehind09(self.ctx)


class LeftBehind09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=634)
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Event_A')
        self.set_effect(trigger_ids=[6107], visible=True) # Voice_Kandura_00001862
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000029_CS__CAVE01__33$', time=6) # 칸두라 00001862

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LeftBehind10(self.ctx)


class LeftBehind10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LeftBehind11(self.ctx)


class LeftBehind11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=635)
        self.set_effect(trigger_ids=[6010], visible=True) # Voice_Laoz_00001834
        self.set_dialogue(type=2, spawn_id=11001556, script='$63000029_CS__CAVE01__34$', time=5) # 라오즈 00001834

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LeftBehind12(self.ctx)


class LeftBehind12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return LaozVersusKahnAttack01(self.ctx)


# 전투 연출 교전
class LaozVersusKahnAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_304')
        self.move_npc(spawn_id=403, patrol_name='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return LaozVersusKahnAttack02(self.ctx)


# 전투 연출 대치
class LaozVersusKahnAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozVersusKahnAttack03(self.ctx)


class LaozVersusKahnAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=651) # zoomin
        # LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5820], visible=True)
        self.set_npc_emotion_loop(spawn_id=305, sequence_name='Bore_B', duration=15000.0) # 라오즈
        self.set_npc_emotion_loop(spawn_id=403, sequence_name='Attack_02_F', duration=15000.0) # 칸두라
        # Sound_LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5930], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return LaozVersusKahnCrash01(self.ctx)


class LaozVersusKahnCrash01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # SandStormSmall_GroundCollapse
        self.set_effect(trigger_ids=[5600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LaozVersusKahnCrash02(self.ctx)


class LaozVersusKahnCrash02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=650) # zoomout
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509], visible=True) # CollapseStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapaseStart01(self.ctx)


# 전투 연출 격돌
class CollapaseStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5800], visible=True) # Rumble
        self.set_mesh(trigger_ids=[3505]) # CollapseStart
        self.set_mesh(trigger_ids=[3509], start_delay=100) # CollapseStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapaseStart02(self.ctx)


class CollapaseStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3504]) # CollapseStart
        self.set_mesh(trigger_ids=[3501], start_delay=50) # CollapseStart
        self.set_mesh(trigger_ids=[3507], start_delay=100) # CollapseStart
        # Sound_LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5931], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapaseStart03(self.ctx)


class CollapaseStart03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5821], visible=True)
        self.set_mesh(trigger_ids=[3502]) # CollapseStart
        self.set_mesh(trigger_ids=[3508], start_delay=50) # CollapseStart
        self.set_mesh(trigger_ids=[3506], start_delay=100) # CollapseStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapaseStart04(self.ctx)


class CollapaseStart04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3503]) # CollapseStart
        self.set_mesh(trigger_ids=[3500], start_delay=100) # CollapseStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapaseAbove01(self.ctx)


class CollapaseAbove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7003], enable=True) # 천장 부수기 스킬
        self.set_effect(trigger_ids=[5801], visible=True) # Earthquake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CollapaseGround01(self.ctx)


class CollapaseGround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[305,403])
        self.set_breakable(trigger_ids=[4000], enable=True)
        self.set_breakable(trigger_ids=[4001], enable=True)
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True)
        self.set_visible_breakable_object(trigger_ids=[4001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return CollapaseGround02(self.ctx)


class CollapaseGround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        # LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5820])
        # LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5821])
        self.set_skill(trigger_ids=[7000], enable=True) # 바닥 큐브 부수기 스킬
        self.set_effect(trigger_ids=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_dialogue(type=1, spawn_id=105, script='$63000029_CS__CAVE01__35$', time=3) # 틴차이 00001688

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return CollapaseGround03(self.ctx)


class CollapaseGround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000])
        self.set_breakable(trigger_ids=[4001])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Earthquake01(self.ctx)


# 동굴이 무너질 것 같은 연출
class Earthquake_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7003], enable=True) # 천장 부수기 스킬
        self.set_effect(trigger_ids=[5801], visible=True) # Earthquake
        self.set_breakable(trigger_ids=[4000], enable=True)
        self.set_breakable(trigger_ids=[4001], enable=True)
        # LaozVsKandura_FightBlending
        self.set_effect(trigger_ids=[5820])
        # LaozVsKandura_FightExplosion
        self.set_effect(trigger_ids=[5821])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Earthquake_CSkip2(self.ctx)


class Earthquake_CSkip2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000], enable=True) # 바닥 큐브 부수기 스킬
        self.set_effect(trigger_ids=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True)
        self.set_visible_breakable_object(trigger_ids=[4001], visible=True)
        self.set_dialogue(type=1, spawn_id=105, script='$63000029_CS__CAVE01__35$', time=3) # 틴차이 00001688
        self.destroy_monster(spawn_ids=[305,403])
        self.set_breakable(trigger_ids=[4000])
        self.set_breakable(trigger_ids=[4001])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Earthquake01(self.ctx)


class Earthquake01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=660) # zoomout
        self.set_user_value(trigger_id=2, key='EarthquakeStart', value=1)
        self.set_dialogue(type=1, spawn_id=105, script='$63000029_CS__CAVE01__39$', time=4, arg5=2) # 틴차이
        self.set_dialogue(type=1, spawn_id=205, script='$63000029_CS__CAVE01__40$', time=3, arg5=4) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Earthquake02(self.ctx)


class Earthquake02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=640)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Earthquake03(self.ctx)


class Earthquake03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_105')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Earthquake04(self.ctx)


class Earthquake04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.set_effect(trigger_ids=[6301], visible=True) # Voice_Tinchai_00001717
        self.set_dialogue(type=1, spawn_id=105, script='$63000029_CS__CAVE01__36$', time=3) # 틴차이 00001717
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Earthquake05(self.ctx)


class Earthquake05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Idle_A')
        self.set_effect(trigger_ids=[6201], visible=True) # Voice_Junta_00001770
        self.set_dialogue(type=1, spawn_id=205, script='$63000029_CS__CAVE01__37$', time=4) # 준타 00001770
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TimeToLeave01(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Idle_A')


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=641)
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=641, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 준타, 틴차이를 따라 동굴에서 빠져나가기
        self.show_guide_summary(entity_id=10036040, text_id=10036040)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9004]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5900], visible=True) # StoneGate
        self.set_dialogue(type=1, spawn_id=205, script='$63000029_CS__CAVE01__38$', time=3)
        self.hide_guide_summary(entity_id=10036040)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return OpenTheStoneGate01(self.ctx)


class OpenTheStoneGate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='or_fi_struc_stonegate_A01_on') # StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return OpenTheStoneGate02(self.ctx)


class OpenTheStoneGate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=1060, text_id=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MoveToNextMap01(self.ctx)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MoveToNextMap02(self.ctx)


class MoveToNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return MoveToNextMap03(self.ctx)


class MoveToNextMap03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return MoveToNextMap04(self.ctx)


class MoveToNextMap04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[205])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=1060)


initial_state = Wait
