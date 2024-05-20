""" trigger/02000356_bf/bossspawn.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030], auto_target=False)
        self.set_interact_object(trigger_ids=[10000259,10000260,10000261], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라이동01(self.ctx)


class 카메라이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013])
        self.add_buff(box_ids=[102], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.show_guide_summary(entity_id=20003563, text_id=20003563, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라이동02(self.ctx)


class 카메라이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동03(self.ctx)


class 카메라이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.show_guide_summary(entity_id=20003562, text_id=20003562, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305, enable=False)
        self.remove_buff(box_id=102, skill_id=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000259,10000260,10000261], state=2):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1099])
        self.select_camera(trigger_id=306)
        self.add_buff(box_ids=[102], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.show_guide_summary(entity_id=20003561, text_id=20003561, duration=6000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.select_camera(trigger_id=306, enable=False)
            self.remove_buff(box_id=102, skill_id=70000107)
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_clear()
            self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
