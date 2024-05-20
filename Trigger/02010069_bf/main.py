""" trigger/02010069_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=True)
        self.set_effect(trigger_ids=[33000])
        self.set_effect(trigger_ids=[34001])
        self.set_effect(trigger_ids=[34002])
        self.set_effect(trigger_ids=[34022])
        self.set_effect(trigger_ids=[34023])
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.set_interact_object(trigger_ids=[10000817], state=0)
        self.destroy_monster(spawn_ids=[44441,44442,44443])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[101], sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10000817], state=1)
        self.show_guide_summary(entity_id=20100691, text_id=20100691, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000817], state=0):
            return 차어나운스1(self.ctx)


class 차어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entity_id=20100691)
        self.set_effect(trigger_ids=[32000], visible=True)
        self.set_effect(trigger_ids=[34001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차어나운스2(self.ctx)


class 차어나운스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[33000], visible=True)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], start_delay=200, interval=50)
        self.move_user(map_id=2010069, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999997]):
            self.spawn_monster(spawn_ids=[44441,44442,44443], auto_target=False)
            return 연출1(self.ctx)


class 연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=999900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출22(self.ctx)


class 연출22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=44441, script='$02010069_BF__MAIN__1$', time=3, arg5=1)
        self.move_npc(spawn_id=44441, patrol_name='MS2PatrolData2')
        self.set_skip(state=연출25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출23(self.ctx)


class 연출23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=44443, script='$02010069_BF__MAIN__2$', time=3, arg5=1)
        self.move_npc(spawn_id=44443, patrol_name='MS2PatrolData1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출24(self.ctx)


class 연출24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=44442, script='$02010069_BF__MAIN__3$', time=3, arg5=1)
        self.move_npc(spawn_id=44442, patrol_name='MS2PatrolData0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출25(self.ctx)


class 연출25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출2(self.ctx)


class 연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=5)
        self.set_cinematic_ui(type=6)
        self.set_effect(trigger_ids=[34022], visible=True)
        self.set_effect(trigger_ids=[34023], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출3(self.ctx)


class 연출3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=999900, enable=False)
        self.move_user(map_id=2010069, portal_id=2)
        self.set_portal(portal_id=2, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출4(self.ctx)


class 연출4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[34022])
        self.set_effect(trigger_ids=[34023])


initial_state = Setting
