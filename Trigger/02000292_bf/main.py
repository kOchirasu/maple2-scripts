""" trigger/02000292_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=101, visible=True, initial_sequence='Closed') # Door
        self.set_mesh(trigger_ids=[102,103,104], visible=True) # InvisibleBarrier
        self.set_mesh(trigger_ids=[105,106,107,108], visible=True) # EnterBarrierCube

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1110], auto_target=False)
        self.move_npc(spawn_id=1110, patrol_name='MS2PatrolData_1110')
        self.select_camera(trigger_id=601)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1110, script='$02000292_BF__MAIN__0$', time=3)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=601, enable=False)
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonOpen(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1110])


class DungeonOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=101, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[102,103,104], start_delay=100, interval=100, fade=2.0) # InvisibleBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonPlay01(self.ctx)


class DungeonPlay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002922, text_id=20002922, duration=5000)
        self.set_actor(trigger_id=101, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[105,106,107,108]) # EnterBarrierCube

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return DungeonPlay02(self.ctx)


class DungeonPlay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002924, text_id=20002924)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002924)


initial_state = Wait
