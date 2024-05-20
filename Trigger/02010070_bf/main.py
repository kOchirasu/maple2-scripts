""" trigger/02010070_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=800, visible=True, initial_sequence='Closed') # Door
        self.set_mesh(trigger_ids=[699], visible=True) # Invisible_EnterBlock
        self.set_mesh(trigger_ids=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737], visible=True) # Invisible_EnterBlock
        self.set_skill(trigger_ids=[7004])
        self.set_effect(trigger_ids=[7000]) # 스킬 준비 효과음
        self.set_effect(trigger_ids=[7001]) # 스킬 발동 효과음
        self.set_effect(trigger_ids=[7002]) # 스킬 발동 이펙트
        self.set_effect(trigger_ids=[7003]) # 스킬 발동 이펙트
        self.set_effect(trigger_ids=[7010]) # Arrow
        self.set_effect(trigger_ids=[7011]) # Arrow
        self.set_effect(trigger_ids=[7012]) # Arrow
        self.destroy_monster(spawn_ids=[22201,22202,22203,22204])
        self.destroy_monster(spawn_ids=[1000,1001,1002,1003,1004,1005,1006])
        self.set_effect(trigger_ids=[95222])
        self.spawn_monster(spawn_ids=[1007,1008], auto_target=False) # bunnygirl
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=800, visible=True, initial_sequence='Opend') # Door
        self.set_mesh(trigger_ids=[699]) # Invisible_EnterBlock

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen(self.ctx)


class GateOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=800, initial_sequence='Opend') # Door
        self.set_random_mesh(trigger_ids=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737], start_delay=38, interval=50, fade=2) # Invisible_EnterBlock
        self.set_effect(trigger_ids=[7010], visible=True) # Arrow
        self.set_effect(trigger_ids=[7011], visible=True) # Arrow
        self.set_effect(trigger_ids=[7012], visible=True) # Arrow
        self.spawn_monster(spawn_ids=[22201,22202,22203,22204], auto_target=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20100701, text_id=20100701, duration=5000) # 화살표를 따라 이동하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999992]):
            return 시작1(self.ctx)


class 시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[95222], visible=True)
        self.set_event_ui(type=1, arg2='$02010070_BF__MAIN__3$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 시작2(self.ctx)


class 시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1007,1008])
        self.spawn_monster(spawn_ids=[1000,1001,1002])
        self.set_effect(trigger_ids=[7010])
        self.set_effect(trigger_ids=[7011])
        self.set_effect(trigger_ids=[7012])
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 욕망이 불러낸 몬스터를 모두 처치해야 합니다.
        self.show_guide_summary(entity_id=20100702, text_id=20100702, duration=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1000,1001,1002]):
            return 시작3(self.ctx)


class 시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003,1004,1005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 시작4(self.ctx)


class 시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1003,1004,1005,1006]):
            return 시간1(self.ctx)


class 시간1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='150', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작5(self.ctx)


class 시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_effect(trigger_ids=[7003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_effect(trigger_ids=[7001], visible=True)
            self.set_skill(trigger_ids=[7004], enable=True)
            return 시작6(self.ctx)


class 시작6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=6)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user(map_id=2010070, portal_id=3)
            return 시작7(self.ctx)


class 시작7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작8(self.ctx)


class 시작8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=5, visible=True, enable=True)


initial_state = 대기
