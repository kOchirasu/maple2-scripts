""" trigger/52000053_qd/fakelaoz01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # CollapseBridge
        self.set_effect(trigger_ids=[5200]) # Summon
        self.set_effect(trigger_ids=[5300]) # StairsApp
        self.set_effect(trigger_ids=[5400]) # ShadowMon
        self.set_effect(trigger_ids=[5500]) # LaozAllKill_01
        self.set_effect(trigger_ids=[5501]) # LaozAllKill_02
        self.set_effect(trigger_ids=[5502]) # LaozAllKill_03
        # Voice_LaozBattle_Attack_00001875
        self.set_effect(trigger_ids=[5600])
        self.set_mesh(trigger_ids=[3000], visible=True, fade=2.0) # Lamp_A02_OFF
        self.set_mesh(trigger_ids=[3001], fade=2.0) # Lamp_A03_ON
        self.set_mesh(trigger_ids=[3002], fade=2.0) # Lamp_A01_Disappear
        self.set_mesh_animation(trigger_ids=[3000], visible=True) # Lamp_A02_OFF
        self.set_mesh_animation(trigger_ids=[3001]) # Lamp_A03_ON
        self.set_mesh_animation(trigger_ids=[3002]) # Lamp_A01_Disappear
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106], visible=True) # Invisible_Barrier
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True) # Invisibble_TotemBarrier
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323]) # StairsToLeave
        self.set_skill(trigger_ids=[2000]) # 큐브 부수기 스킬 1단계
        self.set_skill(trigger_ids=[2001]) # 큐브 부수기 스킬 2단계
        self.set_skill(trigger_ids=[2002]) # 큐브 부수기 스킬 3단계
        self.set_skill(trigger_ids=[2003]) # 그림자 소멸 스킬
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.spawn_monster(spawn_ids=[101,201], auto_target=False)
        self.spawn_monster(spawn_ids=[910,911,912,920,921,922], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay03(self.ctx)


class LodingDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ZoomInLamp01(self.ctx)


class ZoomInLamp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ZoomInLamp02(self.ctx)


class ZoomInLamp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000053_QD__FAKELAOZ01__0$', time=4) # 틴차이
        self.set_skip(state=ZoomInLamp02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ZoomInLamp02Skip(self.ctx)


class ZoomInLamp02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return MoveToLamp01(self.ctx)


class MoveToLamp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=510)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MoveToLamp02(self.ctx)


class MoveToLamp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000053_QD__FAKELAOZ01__1$', time=2, arg5=1) # 틴차이
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_110')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_210')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return MoveToLamp03(self.ctx)


class MoveToLamp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_dialogue(type=1, spawn_id=201, script='$52000053_QD__FAKELAOZ01__2$', time=3, arg5=1) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PCStop01(self.ctx)


class PCStop01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=1, script='$52000053_QD__FAKELAOZ01__3$', time=3) # PC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCStop02(self.ctx)


class PCStop02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=511)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_111') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        self.set_dialogue(type=1, spawn_id=101, script='$52000053_QD__FAKELAOZ01__4$', time=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCStop03(self.ctx)


class PCStop03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_211') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        self.set_dialogue(type=1, spawn_id=201, script='$52000053_QD__FAKELAOZ01__5$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return KanduraApp00(self.ctx)


class KanduraApp00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_212') # AirPatrol

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KanduraApp01(self.ctx)


class KanduraApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_112') # AirPatrol

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KanduraApp02(self.ctx)


class KanduraApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return KanduraApp03(self.ctx)


class KanduraApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=512)
        self.set_dialogue(type=2, spawn_id=11001559, script='$52000053_QD__FAKELAOZ01__6$', time=3) # 칸두라
        self.set_skip(state=KanduraApp03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return KanduraApp03Skip(self.ctx)


class KanduraApp03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KanduraApp04(self.ctx)


class KanduraApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[104,204], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Event_A')
        self.set_dialogue(type=2, spawn_id=11001559, script='$52000053_QD__FAKELAOZ01__7$', time=5) # 칸두라
        self.set_skip(state=KanduraApp04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return KanduraApp04Skip(self.ctx)


class KanduraApp04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=520)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_113')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_213')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CollapseBridge01(self.ctx)


class CollapseBridge01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2000], enable=True) # 큐브 부수기 스킬 1단계
        self.set_effect(trigger_ids=[5100], visible=True) # CollapseBridge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return CollapseBridge02(self.ctx)


class CollapseBridge02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2001], enable=True) # 큐브 부수기 스킬 2단계

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return CollapseBridge03(self.ctx)


class CollapseBridge03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2002], enable=True) # 큐브 부수기 스킬 3단계

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return CollapseBridge04(self.ctx)


class CollapseBridge04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000053_QD__FAKELAOZ01__31$', time=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return KanduraSummon01(self.ctx)


# 칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출
class KanduraSummon01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KanduraSummon02(self.ctx)


class KanduraSummon02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Event_A')
        self.set_dialogue(type=2, spawn_id=11001559, script='$52000053_QD__FAKELAOZ01__8$', time=4) # 칸두라
        self.set_skip(state=KanduraSummon03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return KanduraSummon03(self.ctx)


class KanduraSummon03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FakeLaozApp01(self.ctx)


class FakeLaozApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5200], visible=True) # Summon

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozApp02(self.ctx)


class FakeLaozApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[900], auto_target=False) # ,901,902 토템 몬스터 스폰 제거

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozApp03(self.ctx)


class FakeLaozApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=603)
        self.move_user_path(patrol_name='MS2PatrolData_1003')
        self.set_dialogue(type=1, script='$52000053_QD__FAKELAOZ01__9$', time=2) # PC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozApp04(self.ctx)


class FakeLaozApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000053_QD__FAKELAOZ01__10$', time=4) # 틴차이
        self.set_skip(state=FakeLaozApp04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FakeLaozApp04Skip(self.ctx)


class FakeLaozApp04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ReachToLamp01(self.ctx)


class ReachToLamp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000053_QD__FAKELAOZ01__11$', time=4) # 준타
        self.set_skip(state=ReachToLamp02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ReachToLamp02(self.ctx)


class ReachToLamp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ReachToLamp03(self.ctx)


class ReachToLamp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ReachToLamp04(self.ctx)


class ReachToLamp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104,204])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False)
        self.select_camera(trigger_id=700, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
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
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return KanduraDisapp01(self.ctx)


# 칸두라 염탐 트리거 신호 보내기
class KanduraDisapp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='SpyKandura', value=1)
        self.destroy_monster(spawn_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            return KanduraDisapp02(self.ctx)


# 가짜 라오즈 처치
class KanduraDisapp02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozDie01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[900,910,911,912,920,921,922])


class FakeLaozDie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], start_delay=200, fade=5.0) # Lamp_A02_OFF
        self.set_mesh(trigger_ids=[3001], visible=True, fade=5.0) # Lamp_A03_ON
        self.set_mesh_animation(trigger_ids=[3000]) # Lamp_A02_OFF
        self.set_mesh_animation(trigger_ids=[3001], visible=True, start_delay=200) # Lamp_A03_ON
        self.set_user_value(trigger_id=2, key='SpyKandura', value=2)
        self.destroy_monster(spawn_ids=[102,202])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LampLightUp01(self.ctx)


class LampLightUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300], visible=True) # StairsApp
        self.set_random_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=True, start_delay=24, interval=100, fade=70) # StairsToLeave
        self.set_mesh(trigger_ids=[3202,3203,3204]) # Invisibble_TotemBarrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106]) # Invisible_Barrier
        self.select_camera(trigger_id=700)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=LampLightUp02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LampLightUp02(self.ctx)


class LampLightUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LampLightUp03(self.ctx)


class LampLightUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000053, portal_id=11, box_id=9900)
        self.set_dialogue(type=1, spawn_id=103, script='$52000053_QD__FAKELAOZ01__12$', time=3) # 틴차이
        self.set_dialogue(type=1, spawn_id=203, script='$52000053_QD__FAKELAOZ01__13$', time=3, arg5=3) # 준타
        self.set_skip(state=LampLightUp04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LampLightUp04(self.ctx)


class LampLightUp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LampLightUp05(self.ctx)


class LampLightUp05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_202')
        self.set_dialogue(type=1, spawn_id=103, script='$52000053_QD__FAKELAOZ01__14$', time=3, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LampLightUp06(self.ctx)


class LampLightUp06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.set_dialogue(type=1, spawn_id=203, script='$52000053_QD__FAKELAOZ01__15$', time=3) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NpcWalkDown01(self.ctx)


class NpcWalkDown01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=702)
        self.move_user_path(patrol_name='MS2PatrolData_1004')
        self.set_dialogue(type=1, spawn_id=103, script='$52000053_QD__FAKELAOZ01__16$', time=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NpcWalkDown02(self.ctx)


class NpcWalkDown02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[302], auto_target=False) # 칸두라
        self.set_dialogue(type=1, spawn_id=203, script='$52000053_QD__FAKELAOZ01__17$', time=3) # 준타
        self.set_dialogue(type=1, script='$52000053_QD__FAKELAOZ01__18$', time=3, arg5=3) # PC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NpcWalkDown03(self.ctx)


class NpcWalkDown03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001]) # Lamp_A03_ON
        self.set_mesh(trigger_ids=[3002], visible=True, fade=5.0) # Lamp_A01_Disappear
        self.set_mesh_animation(trigger_ids=[3001]) # Lamp_A03_ON
        self.set_mesh_animation(trigger_ids=[3002], visible=True, start_delay=200) # Lamp_A01_Disappear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return KanduraAppAgain01(self.ctx)


class KanduraAppAgain01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$52000053_QD__FAKELAOZ01__19$', time=4) # 칸두라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KanduraAppAgain02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103,203])
        self.spawn_monster(spawn_ids=[105,205], auto_target=False)


class KanduraAppAgain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_104')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_204')
        self.set_skip(state=KanduraAppAgain03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return KanduraAppAgain03(self.ctx)


class KanduraAppAgain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=710)
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_303')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NoticeLampDisapp01(self.ctx)


class NoticeLampDisapp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000053_QD__FAKELAOZ01__20$', time=4) # 준타
        self.set_skip(state=NoticeLampDisapp01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NoticeLampDisapp01Skip(self.ctx)


class NoticeLampDisapp01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NoticeLampDisapp02(self.ctx)


class NoticeLampDisapp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000053_QD__FAKELAOZ01__21$', time=4) # 틴차이
        self.set_skip(state=NoticeLampDisapp02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NoticeLampDisapp02Skip(self.ctx)


class NoticeLampDisapp02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=711)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KanduraReadyToLeave01(self.ctx)


class KanduraReadyToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KanduraReadyToLeave02(self.ctx)


class KanduraReadyToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$52000053_QD__FAKELAOZ01__22$', time=5) # 칸두라
        self.set_effect(trigger_ids=[5400], visible=True) # ShadowMon
        self.set_skip(state=KanduraReadyToLeave03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return KanduraReadyToLeave03(self.ctx)


class KanduraReadyToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShadowApp01(self.ctx)


class ShadowApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ShadowApp02(self.ctx)


class ShadowApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[302])
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_105')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.select_camera(trigger_id=720)
        self.move_user_path(patrol_name='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTired01(self.ctx)


class NpcTired01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=105, script='$52000053_QD__FAKELAOZ01__23$', time=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTired02(self.ctx)


class NpcTired02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Down_Idle_A', duration=20000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcTired03(self.ctx)


class NpcTired03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=205, script='$52000053_QD__FAKELAOZ01__24$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTired04(self.ctx)


class NpcTired04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=205, sequence_name='Down_Idle_A', duration=20000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTired05(self.ctx)


class NpcTired05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=205, script='$52000053_QD__FAKELAOZ01__25$', time=3) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcTired06(self.ctx)


class NpcTired06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000053_QD__FAKELAOZ01__26$', time=3) # PC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return RealLaozApp01(self.ctx)


class RealLaozApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001556, script='$52000053_QD__FAKELAOZ01__27$', time=4) # 라오즈
        self.destroy_monster(spawn_ids=[105,205])
        self.spawn_monster(spawn_ids=[106,206], auto_target=False)
        self.set_skip(state=RealLaozApp02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RealLaozApp02(self.ctx)


class RealLaozApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[400], auto_target=False)
        self.spawn_monster(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RealLaozApp03(self.ctx)


class RealLaozApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=721)
        self.destroy_monster(spawn_ids=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899])
        self.set_dialogue(type=1, spawn_id=400, script='$52000053_QD__FAKELAOZ01__28$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LaozKillAll01(self.ctx)


class LaozKillAll01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice_LaozBattle_Attack_00001875
        self.set_effect(trigger_ids=[5600], visible=True)
        self.set_npc_emotion_sequence(spawn_id=400, sequence_name='Attack_01_D') # 임시
        self.set_effect(trigger_ids=[5501], visible=True) # LaozAllKill_02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1400):
            return LaozKillAll02(self.ctx)


class LaozKillAll02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5500], visible=True) # LaozAllKill_01
        self.set_effect(trigger_ids=[5502], visible=True) # LaozAllKill_03
        self.set_skill(trigger_ids=[2003], enable=True) # 그림자 소멸 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LaozKillAll03(self.ctx)


class LaozKillAll03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400]) # ShadowMon
        self.destroy_monster(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetRealLaoz01(self.ctx)


class MeetRealLaoz01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=730)
        self.set_dialogue(type=1, spawn_id=400, script='$52000053_QD__FAKELAOZ01__29$', time=3, arg5=1) # 라오즈
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_400')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MeetRealLaoz02(self.ctx)


class MeetRealLaoz02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000053_QD__FAKELAOZ01__30$', time=2) # PC
        self.move_user_path(patrol_name='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return QuestLaozApp01(self.ctx)


class QuestLaozApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[400])
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.select_camera(trigger_id=730, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ReturnLaoz01(self.ctx)


# 퀘스트 시작
class ReturnLaoz01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='ReturnLaoz')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003058], quest_states=[1]):
            # 운명의 계시 퀘스트 수락한 상태
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000050, portal_id=2, box_id=9900)


initial_state = Wait
