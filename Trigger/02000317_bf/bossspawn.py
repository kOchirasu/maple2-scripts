""" trigger/02000317_bf/bossspawn.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=3)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Step_1(self.ctx)


class Step_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7]) # 다리안보임
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.spawn_monster(spawn_ids=[205], auto_target=False)
        self.spawn_monster(spawn_ids=[206], auto_target=False)
        self.spawn_monster(spawn_ids=[207], auto_target=False)
        self.spawn_monster(spawn_ids=[208], auto_target=False)
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.spawn_monster(spawn_ids=[302], auto_target=False)
        self.spawn_monster(spawn_ids=[303], auto_target=False)
        self.spawn_monster(spawn_ids=[304], auto_target=False)
        self.spawn_monster(spawn_ids=[305], auto_target=False)
        self.spawn_monster(spawn_ids=[306], auto_target=False)
        self.spawn_monster(spawn_ids=[307], auto_target=False)
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.spawn_monster(spawn_ids=[402], auto_target=False)
        self.spawn_monster(spawn_ids=[403], auto_target=False)
        self.spawn_monster(spawn_ids=[404], auto_target=False)
        self.spawn_monster(spawn_ids=[405], auto_target=False)
        self.spawn_monster(spawn_ids=[406], auto_target=False)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return Step_1_B_Ready(self.ctx)
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_1_B_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=100, text_id=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[205,208]):
            return Step_1_B(self.ctx)


class Step_1_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return Step_1_C(self.ctx)
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_1_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=100, text_id=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302]):
            return Step_1_D_Ready(self.ctx)
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_1_D_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8,9,10,11]) # 다리안보임

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return Step_1_D(self.ctx)
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_1_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=100, text_id=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[405]):
            return Step_1_E(self.ctx)
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_1_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return Step_2(self.ctx)


class Step_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        self.spawn_monster(spawn_ids=[100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[100]):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[100])


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)


initial_state = idle
