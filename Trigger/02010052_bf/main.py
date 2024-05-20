""" trigger/02010052_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5)
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[81004])
        self.spawn_monster(spawn_ids=[101,102,103,107,108,109,110,111,112], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[421,422,423], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[431,432,433,434,435,436,437], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613], auto_target=False) # 기본 배치 될 몬스터 등장
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[75011,75012,75013], visible=True, start_delay=1000, interval=500, fade=8.0) # 물 삭제
        self.set_mesh(trigger_ids=[75001,75002,75003], start_delay=1000, interval=500, fade=8.0) # 물 삭제
        self.spawn_monster(spawn_ids=[991], auto_target=False) # 카나의 분신 991 (Battle_01)
        self.spawn_monster(spawn_ids=[992], auto_target=False) # 카나의 분신 992 (Battle_02)
        self.spawn_monster(spawn_ids=[993], auto_target=False) # 카나의 분신 993 (Battle_03)
        self.spawn_monster(spawn_ids=[994], auto_target=False) # 카나의 분신 994 (Battle_04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start_03(self.ctx)


class Start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[80010,80011])
        self.set_mesh(trigger_ids=[22201,22202,22203,22204,22205,22206,22207,22208,22209,22210,22211,22212,22213,22214,22215,22216,22217,22218,22219,22220,22221,22222,22223,22224,22225,22226,22227,22228,22229,22230,22231,22232,22233,22234,22235,22236,22237,22238,22239,22240,22241,22242,22243,22244,22245,22246,22247,22248,22249,22250,22251,22252,22253,22254,22255,22256,22257,22258,22259,22260,22261,22262,22263,22264,22265,22266,22267,22268,22269,22270,22271,22272,22273,22274,22275,22276,22277,22278,22279,22280,22281,22282,22283,22284,22285,22286,22287,22288,22289,22290,22291,22292,22293,22294,22295,22296,22297,22298,22299], start_delay=800, interval=100) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start_04(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02010052_BF__MAIN__6$', arg3='3000')
        # self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # self.show_guide_summary(entity_id=20105205, text_id=20105205)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=80001)
        self.set_dialogue(type=2, spawn_id=21800073, script='$02010052_BF__MAIN__1$', time=3) # 카나 대사
        self.move_npc(spawn_id=991, patrol_name='MS2PatrolData_1001') # 카나의 분신 991 (이동)
        self.set_skip(state=Event_01_02)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_01_02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=21800073, script='$02010052_BF__MAIN__2$', time=3) # 카나 대사
        self.move_npc(spawn_id=991, patrol_name='MS2PatrolData_1002') # 카나의 분신 991 (이동)
        self.set_skip(state=Event_01_03)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_01_03(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera(trigger_id=80001, enable=False)


class Event_01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.set_effect(trigger_ids=[7901], visible=True) # 카나 사라짐
        self.destroy_monster(spawn_ids=[991]) # 카나 사라짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=992, script='$02010052_BF__MAIN__3$', time=3) # 카나 말풍선 대사
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_02_02(self.ctx)


class Event_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.set_dialogue(type=1, spawn_id=992, script='$02010052_BF__MAIN__4$', time=3) # 카나 말풍선 대사
        self.move_npc(spawn_id=992, patrol_name='MS2PatrolData_1003') # 카나의 분신 992 (이동)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_02_03(self.ctx)


class Event_02_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[992])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=80002)
        self.set_dialogue(type=2, spawn_id=21800073, script='$02010052_BF__MAIN__5$', time=3) # 카나 대사
        self.move_npc(spawn_id=993, patrol_name='MS2PatrolData_1004') # 카나의 분신 993 (이동)
        self.set_skip(state=Event_03_02)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_03_02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera(trigger_id=80002, enable=False)


class Event_03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.destroy_monster(spawn_ids=[993]) # 카나 사라짐
        self.spawn_monster(spawn_ids=[9999]) # 공격 카나 생성


initial_state = idle
