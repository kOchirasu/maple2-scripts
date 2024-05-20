""" trigger/02000335_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6901,6902,6903,6904,6905,6906,6907,6908], fade=10.0) # 벽 해제
        self.spawn_monster(spawn_ids=[101,102,103,104,106,107,111,120,121,124,125,131,132,133,134,135,140,143,144,145,147,148], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217], auto_target=False) # 기본 배치 될 NPC 등장
        self.set_effect(trigger_ids=[6901])
        self.set_effect(trigger_ids=[6902])
        self.set_effect(trigger_ids=[6903])
        self.set_effect(trigger_ids=[6904])
        self.set_effect(trigger_ids=[6905])
        self.set_effect(trigger_ids=[6906])
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=992)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=700) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=시작_03)
        self.set_dialogue(type=1, spawn_id=203, script='$02000335_BF__MAIN__0$', time=2)
        self.select_camera_path(path_ids=[80001,80002,80003,80004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 시작_03(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui(type=1, arg2='$02000335_BF__MAIN__1$', arg3='3000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 시작_04(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[6401,6402,6403,6404], fade=10.0) # 벽 해제


class 시작_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[107]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[6101,6102,6103,6104,6105,6106,6107,6108], fade=10.0) # 벽 해제
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 관문_01_개방_02(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 관문_02_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=106)


class 관문_01_개방_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106]):
            return 관문_02_개방(self.ctx)
        if self.count_users(box_id=702) >= 1:
            return 관문_01_개방_03(self.ctx)


class 관문_01_개방_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106]):
            return 관문_02_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=991, is_enable=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[6111,6112,6113,6114,6115,6116,6117,6118], fade=10.0) # 벽 해제
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 관문_02_개방_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=106)


class 관문_02_개방_02(trigger_api.Trigger):
    pass


initial_state = idle
