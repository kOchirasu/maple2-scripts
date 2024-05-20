""" trigger/02000379_bf/fakelaoz01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # CollapseBridge
        self.set_effect(trigger_ids=[5200]) # Summon
        self.set_effect(trigger_ids=[5300]) # StairsApp
        self.set_mesh(trigger_ids=[3000], visible=True, fade=2.0) # Lamp_A02_OFF
        self.set_mesh(trigger_ids=[3001], fade=2.0) # Lamp_A03_ON
        self.set_mesh(trigger_ids=[3002], fade=2.0) # Lamp_A01_Disappear
        self.set_mesh_animation(trigger_ids=[3000], visible=True) # Lamp_A02_OFF
        self.set_mesh_animation(trigger_ids=[3001]) # Lamp_A03_ON
        self.set_mesh_animation(trigger_ids=[3002]) # Lamp_A01_Disappear
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106], visible=True) # Invisible_Barrier
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206], visible=True) # Invisibble_TotemBarrier
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323]) # StairsToLeave
        self.set_skill(trigger_ids=[2000]) # 큐브 부수기 스킬 1단계
        self.set_skill(trigger_ids=[2001]) # 큐브 부수기 스킬 2단계
        self.set_skill(trigger_ids=[2002]) # 큐브 부수기 스킬 3단계
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
        self.spawn_monster(spawn_ids=[101,201,301], auto_target=False)
        self.spawn_monster(spawn_ids=[910,911,912,920,921,922], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay03(self.ctx)


class LodingDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraAct01(self.ctx)


class CameraAct01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_dialogue(type=1, spawn_id=101, script='$02000379_BF__FAKELAOZ01__0$', time=3, arg5=1) # 틴차이
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.set_skip(state=CameraAct02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CameraAct02(self.ctx)


class CameraAct02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CameraAct03(self.ctx)


class CameraAct03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_dialogue(type=1, spawn_id=201, script='$02000379_BF__FAKELAOZ01__1$', time=3) # 준타
        self.set_skip(state=CameraAct04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraAct04(self.ctx)


class CameraAct04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=600, enable=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KanduraTalk01(self.ctx)


class KanduraTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$02000379_BF__FAKELAOZ01__2$', time=3, arg5=2) # 칸두라
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Event_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            # 다리 위
            return CollapseBridge01(self.ctx)
        if self.wait_tick(wait_tick=4000):
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
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraAct11(self.ctx)


# 칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출
class CameraAct11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)
        self.set_skip(state=CameraAct13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraAct12(self.ctx)


class CameraAct12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$02000379_BF__FAKELAOZ01__3$', time=3) # 칸두라
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Event_A')
        self.set_skip(state=CameraAct13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraAct13(self.ctx)


class CameraAct13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601, enable=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FakeLaozApp01(self.ctx)


class FakeLaozApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FakeLaozApp02(self.ctx)


class FakeLaozApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5200], visible=True) # Summon

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozApp03(self.ctx)


class FakeLaozApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202,900], auto_target=False) # ,901,902 토템 몬스터 스폰 제거
        self.set_skip(state=FakeLaozApp04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FakeLaozApp04(self.ctx)


class FakeLaozApp04(trigger_api.Trigger):
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
        self.select_camera(trigger_id=602, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State
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


class KanduraDisapp02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FakeLaozDie01(self.ctx)


class FakeLaozDie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], start_delay=200, fade=5.0) # Lamp_A02_OFF
        self.set_mesh(trigger_ids=[3001], visible=True, fade=5.0) # Lamp_A03_ON
        self.set_mesh_animation(trigger_ids=[3000]) # Lamp_A02_OFF
        self.set_mesh_animation(trigger_ids=[3001], visible=True, start_delay=200) # Lamp_A03_ON
        self.set_user_value(trigger_id=2, key='SpyKandura', value=2)
        self.destroy_monster(spawn_ids=[900,910,911,912,920,921,922])
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
        # 유저 위치 보정, 계단에 끼이는 문제 해결을 위한 장치
        self.move_user(map_id=2000379, portal_id=11, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        return LampLightUp03(self.ctx)


class LampLightUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=103, script='$02000379_BF__FAKELAOZ01__4$', time=3) # 틴차이
        self.set_dialogue(type=1, spawn_id=203, script='$02000379_BF__FAKELAOZ01__5$', time=3, arg5=3) # 준타
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
        self.set_dialogue(type=1, spawn_id=103, script='$02000379_BF__FAKELAOZ01__6$', time=3, arg5=2) # 틴차이
        self.set_dialogue(type=1, spawn_id=203, script='$02000379_BF__FAKELAOZ01__7$', time=3, arg5=6) # 준타
        self.set_skip(state=TimeToLeave01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear()


initial_state = Wait
