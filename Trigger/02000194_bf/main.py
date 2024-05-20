""" trigger/02000194_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10001054], state=2)
        self.set_interact_object(trigger_ids=[10001055], state=2)
        self.set_interact_object(trigger_ids=[10001056], state=2)
        self.set_interact_object(trigger_ids=[10001057], state=2)
        self.set_interact_object(trigger_ids=[11000004], state=2)
        self.set_mesh(trigger_ids=[3005,3006,3007], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20001941, text_id=20001941, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10001054], state=1)
        self.set_interact_object(trigger_ids=[10001055], state=1)
        self.set_interact_object(trigger_ids=[10001056], state=1)
        self.set_interact_object(trigger_ids=[10001057], state=1)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,2000], auto_target=False)
        self.select_camera(trigger_id=301)
        self.add_buff(box_ids=[101], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.set_skip(state=시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=301, enable=False)
        self.set_mesh(trigger_ids=[3005,3006,3007])
        self.remove_buff(box_id=101, skill_id=70000107)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20001942, text_id=20001942, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작2(self.ctx)


class 시작2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001054], state=0):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104])
            return 오브젝트2(self.ctx)


class 오브젝트2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001055], state=0):
            self.set_mesh(trigger_ids=[3201,3202,3203])
            return 오브젝트3(self.ctx)


class 오브젝트3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001056], state=0):
            self.set_mesh(trigger_ids=[3301,3302,3303,3304])
            return 오브젝트4(self.ctx)


class 오브젝트4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001057], state=0):
            self.show_guide_summary(entity_id=20001944, text_id=20001944, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.set_mesh(trigger_ids=[3001,3002,3003,3004])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
