""" trigger/02000351_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[31,32], auto_target=False)
        self.spawn_monster(spawn_ids=[11,12,13,14,15,16,17], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[21,22,23,24,25,26,27,28,29], auto_target=False) # 기본 배치 될 몬스터 등장
        self.set_interact_object(trigger_ids=[10000818], state=0)
        self.set_effect(trigger_ids=[9000001])
        self.set_effect(trigger_ids=[9000002])
        self.set_effect(trigger_ids=[9000003])
        self.set_effect(trigger_ids=[9000004])
        self.set_effect(trigger_ids=[9000005])
        self.set_effect(trigger_ids=[9000006])
        self.set_effect(trigger_ids=[9000007])
        self.set_effect(trigger_ids=[9000008])
        self.set_effect(trigger_ids=[9000009])
        self.set_effect(trigger_ids=[9000010])
        self.set_mesh(trigger_ids=[6007], fade=10.0) # 화살표 표시 안함

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=Start)
        self.select_camera_path(path_ids=[80001,80002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Start(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000351_BF__MAIN__0$', arg3='3000')
        self.select_camera_path(path_ids=[80003])
        self.set_mesh(trigger_ids=[6900], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 관문_01_개방(self.ctx)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000818], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 관문_02_개방(self.ctx)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=111, text_id=20000080) # 스위치를 정지하세요
        self.set_interact_object(trigger_ids=[10000819], state=1)
        self.set_interact_object(trigger_ids=[10000820], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 관문_03_시작(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)


class 관문_03_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[33], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[31,32]):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.set_mesh(trigger_ids=[6006], fade=10.0)
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=112)


initial_state = idle
