""" trigger/02000353_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[6001])
        self.set_effect(trigger_ids=[6002])
        self.set_effect(trigger_ids=[6003])
        self.set_effect(trigger_ids=[6004])
        self.set_effect(trigger_ids=[6101])
        self.set_effect(trigger_ids=[6301])
        self.set_effect(trigger_ids=[6302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작_03(self.ctx)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작_04(self.ctx)


class 시작_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[901,902,903], fade=10.0) # 벽 해제
        self.set_skill(trigger_ids=[2020], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 시작_05(self.ctx)


class 시작_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=101, text_id=40010) # 적을 모두 처치하시오
        self.set_effect(trigger_ids=[6001], visible=True)
        self.set_effect(trigger_ids=[6002], visible=True)
        self.set_effect(trigger_ids=[6003], visible=True)
        self.set_effect(trigger_ids=[6004], visible=True)
        self.set_effect(trigger_ids=[6101], visible=True)
        self.set_actor(trigger_id=3001, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3002, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3003, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3004, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3101, initial_sequence='Dmg_A')
        self.spawn_monster(spawn_ids=[11,12,13,14,15], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[11,12,13,14,15]):
            return 관문_01_개방전(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 관문_01_개방전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__2$', arg3='2000')
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 관문_01_개방(self.ctx)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=관문_02_스킵)
        self.select_camera(trigger_id=8001)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_01_개방_이벤트_00(self.ctx)


class 관문_01_개방_이벤트_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_01_개방_이벤트_01(self.ctx)


class 관문_01_개방_이벤트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2001], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[2002], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_01_개방_이벤트_02(self.ctx)


class 관문_01_개방_이벤트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2003], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_01_개방_이벤트_03(self.ctx)


class 관문_01_개방_이벤트_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2004], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 관문_02_시작(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 관문_02_스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2001], enable=True)
        self.set_skill(trigger_ids=[2002], enable=True)
        self.set_skill(trigger_ids=[2003], enable=True)
        self.set_skill(trigger_ids=[2004], enable=True)
        self.set_skip() # Missing State: State
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            self.remove_buff(box_id=199, skill_id=70000107)
            return 관문_02_시작(self.ctx)


class 관문_02_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.select_camera(trigger_id=8001, enable=False)
        self.show_guide_summary(entity_id=103, text_id=40011) # 다음 지역으로 이동하세요
        # self.set_event_ui(type=1, arg2='다음 지역으로 이동하세요.', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 관문_02_시작_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=103)


class 관문_02_시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6005], visible=True)
        self.set_effect(trigger_ids=[6006], visible=True)
        self.set_effect(trigger_ids=[6007], visible=True)
        self.set_effect(trigger_ids=[6008], visible=True)
        self.set_actor(trigger_id=3005, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3006, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3007, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3008, initial_sequence='Dmg_A')
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=101, text_id=40010) # 적을 모두 처치하시오
        self.spawn_monster(spawn_ids=[21,22,23,24,25,26,27], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[21,22,23,24,25,26,27]):
            return 관문_02_개방전(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 관문_02_개방전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__3$', arg3='2000')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_02_개방(self.ctx)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 관문_02_개방_이벤트_01(self.ctx)


class 관문_02_개방_이벤트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2006], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_02_개방_이벤트_02(self.ctx)


class 관문_02_개방_이벤트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2007], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_02_개방_이벤트_03(self.ctx)


class 관문_02_개방_이벤트_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2008], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_03_시작_01(self.ctx)


class 관문_03_시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=103, text_id=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 관문_03_시작_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=103)


class 관문_03_시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=101, text_id=40010) # 적을 모두 처치하시오
        self.set_effect(trigger_ids=[6301], visible=True)
        self.set_effect(trigger_ids=[6302], visible=True)
        self.set_actor(trigger_id=3301, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=3302, initial_sequence='Dmg_A')
        self.spawn_monster(spawn_ids=[31,32,33], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[31,32,33]):
            return 관문_03_개방전(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 관문_03_개방전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__4$', arg3='2000')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 관문_03_개방_이벤트_01(self.ctx)


class 관문_03_개방_이벤트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2009], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_03_개방_이벤트_02(self.ctx)


class 관문_03_개방_이벤트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2010], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_03_개방_이벤트_03(self.ctx)


class 관문_03_개방_이벤트_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2011], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 지역클리어(self.ctx)


class 지역클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=103, text_id=40009) # 포탈로 이동하세요
        self.set_mesh(trigger_ids=[6006], fade=10.0) # 벽 해제
        self.set_mesh(trigger_ids=[6007], visible=True, fade=10.0) # 화살표 표시
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
