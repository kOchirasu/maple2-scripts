""" trigger/02000099_bf/bossspawn.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20000991, text_id=20000991, duration=5000)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,2000], auto_target=False)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=301, enable=False)
        self.remove_buff(box_id=199, skill_id=70000107)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20000992, text_id=20000992, duration=3000)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작가이드2(self.ctx)


class 시작가이드2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 차등장1(self.ctx)


class 차등장1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillA') == 1:
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106])
            return 차등장대기2(self.ctx)


class 차등장대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 차등장2(self.ctx)


class 차등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillB') == 1:
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208])
            return 엘리트등장(self.ctx)


class 엘리트등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entity_id=20000993, text_id=20000993, duration=5000)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311])
            return 엘리트처치(self.ctx)


class 엘리트처치(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entity_id=20000994, text_id=20000994, duration=3000)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
