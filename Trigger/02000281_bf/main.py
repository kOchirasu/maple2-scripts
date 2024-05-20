""" trigger/02000281_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302], visible=True)
        self.set_interact_object(trigger_ids=[10000414], state=0)
        self.set_ladder(trigger_ids=[321])
        self.set_ladder(trigger_ids=[322])
        self.set_ladder(trigger_ids=[323])
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015], auto_target=False)
        self.set_interact_object(trigger_ids=[10000414], state=1)
        self.select_camera(trigger_id=3001)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라대기(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 카메라대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002810, text_id=20002810, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 생성(self.ctx)

    def on_exit(self) -> None:
        self.remove_buff(box_id=199, skill_id=70000107)
        self.select_camera(trigger_id=3002, enable=False)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000414], state=0):
            return 보스(self.ctx)


class 보스(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.show_guide_summary(entity_id=20002816, text_id=20002816, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            self.show_guide_summary(entity_id=20002812, text_id=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(trigger_ids=[321], visible=True, enable=True)
            self.set_ladder(trigger_ids=[322], visible=True, enable=True)
            self.set_ladder(trigger_ids=[323], visible=True, enable=True)
            self.set_portal(portal_id=2, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
