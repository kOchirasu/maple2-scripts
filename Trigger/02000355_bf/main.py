""" trigger/02000355_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=299, visible=True, initial_sequence='Dead_Idle_A')
        self.spawn_monster(spawn_ids=[2101,2102,2103,2104,2105,2106,2107,2108], auto_target=False)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[699])
        self.set_mesh(trigger_ids=[3999], visible=True)
        self.set_mesh(trigger_ids=[3900], visible=True)
        self.set_mesh(trigger_ids=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808])
        self.set_skill(trigger_ids=[7001])
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_effect(trigger_ids=[699], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카드반교체(self.ctx)


class 카드반교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=299, initial_sequence='Dead_Idle_A')
        self.spawn_monster(spawn_ids=[2097], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카드반대사01(self.ctx)


class 카드반대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000355_BF__MAIN__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카트반이동(self.ctx)


class 카트반이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True)
        self.set_mesh(trigger_ids=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716])
        self.select_camera_path(path_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2097, patrol_name='MS2PatrolData2097_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_mesh(trigger_ids=[3900])
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(trigger_id=301, enable=False)
            self.show_guide_summary(entity_id=20003552, text_id=20003552, duration=4000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 카트반소멸(self.ctx)


class 카트반소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[2099], auto_target=False)
            self.destroy_monster(spawn_ids=[2097])
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 종료연출시작(self.ctx)


class 종료연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 카드반대사02(self.ctx)


class 카드반대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000355_BF__MAIN__1$', time=4)
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_clear()
            self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808], visible=True, interval=50, fade=2.0)
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
