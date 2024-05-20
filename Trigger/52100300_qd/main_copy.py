""" trigger/52100300_qd/main_copy.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104,105]) # 몬스터 등장
        self.set_ladder(trigger_ids=[1011], enable=True)
        self.set_ladder(trigger_ids=[1012], enable=True)
        self.set_ladder(trigger_ids=[1013], enable=True)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207,208,209]) # 마지막 섹터 몬스터 등장
        self.set_mesh(trigger_ids=[29991,29992,29993,29994,29995,29996,29997,29998,29999]) # 안보이는 상태
        self.set_effect(trigger_ids=[7010], visible=True) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7011], visible=True) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7012], visible=True) # 전원 붙는 소리
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=992)
        self.enable_spawn_point_pc(spawn_id=993)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=시작_03)
        self.select_camera_path(path_ids=[80001,80002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작_03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[80003])
        self.set_event_ui(type=1, arg2='$02010086_BF__MAIN__0$', arg3='3000')
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[1002], fade=10.0) # 벽 해제
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작_04(self.ctx)


class 시작_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 전투_01(self.ctx)


class 전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[999]) # 몬스터 등장
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105]):
            return 관문_01_개방(self.ctx)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_actor(trigger_id=1003, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=5001, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=5002, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_mesh(trigger_ids=[1004], fade=10.0) # 벽 해제
        self.set_effect(trigger_ids=[7020]) # 알람 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 전투_02(self.ctx)


class 전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[111,112,113,114,115,116,117,118,119]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114,115,116,117,118,119]):
            return 관문_02_개방(self.ctx)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[1011], visible=True, enable=True)
        self.set_ladder(trigger_ids=[1012], visible=True, enable=True)
        self.set_ladder(trigger_ids=[1013], visible=True, enable=True)
        self.set_actor(trigger_id=5003, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=5004, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=5005, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.set_effect(trigger_ids=[7021]) # 알람 소리
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 전투_03(self.ctx)


class 전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[121,122,123,124,125,126,127,128,129]) # 몬스터 등장
        self.spawn_monster(spawn_ids=[994]) # 새틀라이트 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122,123,124,125,126,127,128,129]):
            return 관문_03_개방(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return 전투_04(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000896], state=1)
        self.destroy_monster(spawn_ids=[994])


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=991, is_enable=True)
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return 전투_04(self.ctx)


class 전투_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[131,132,133,134,135,136,137,138,139]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[131,132,133,134,135,136,137,138,139]):
            return 관문_04_개방(self.ctx)


class 관문_04_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=5006, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=5007, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=1006, visible=True, initial_sequence='Opened') # 문 열림
        self.set_mesh(trigger_ids=[1007], fade=10.0) # 벽 해제
        self.set_effect(trigger_ids=[7022]) # 알람 소리
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return 전투_05(self.ctx)


class 전투_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1009, visible=True, initial_sequence='Opened') # 문 열림
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[141,142,143,144,145,146,147,148,149]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[141,142,143,144,145,146,147,148,149]):
            return 관문_05_개방(self.ctx)
        if self.count_users(box_id=707) >= 1:
            return 전투_06(self.ctx)


class 관문_05_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=992, is_enable=True)
        self.set_actor(trigger_id=5008, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(trigger_id=5009, visible=True, initial_sequence='sf_quest_light_A01_Off') # 알람 꺼
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=707) >= 1:
            return 전투_06(self.ctx)


class 전투_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[151,152,153,154,155,156,157,158,159]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[151,152,153,154,155,156,157,158,159]):
            return 관문_06_개방_02(self.ctx)


class 관문_06_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002,2003], interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[2011,2012,2013], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 관문_06_개방_02(self.ctx)


class 관문_06_개방_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[161,162,163,164,165,166,167,168,169]) # 몬스터 등장
        self.set_mesh(trigger_ids=[2014,2015,2016], interval=30) # 문 폭발
        self.set_mesh(trigger_ids=[2011,2012,2013], fade=10.0) # 파란 선도 마저 삭제
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=708) >= 1:
            return 전투_07(self.ctx)


class 전투_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[171,172,173,174,175,176,177,178,179]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[171,172,173,174,175,176,177,178,179]):
            return 관문_07_개방(self.ctx)


class 관문_07_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=992)
        self.enable_spawn_point_pc(spawn_id=993, is_enable=True)
        self.set_mesh(trigger_ids=[2021,2022,2023]) # 관문 개방
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,206,207,208,209]):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000897], state=1)


initial_state = idle
