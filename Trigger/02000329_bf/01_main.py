""" trigger/02000329_bf/01_main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701], auto_target=False)
        self.set_effect(trigger_ids=[6701], visible=True)
        self.spawn_monster(spawn_ids=[5001,5002,1301,1302,1303,1304], auto_target=False) # 보스 소환

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=scene_02)
        self.select_camera_path(path_ids=[80001,80002,80003,80004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_02)
        self.set_dialogue(type=1, spawn_id=1301, script='$02000329_BF__01_MAIN__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_02(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera_path(path_ids=[80005])
        self.set_event_ui(type=1, arg2='$02000329_BF__01_MAIN__1$', arg3='3000', arg4='0')
        self.spawn_monster(spawn_ids=[2001,2002,2003,2004,2005], auto_target=False)
        self.set_mesh(trigger_ids=[10000,11001,11002,11003,19999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=105) >= 1:
            return npc_talk(self.ctx)


class npc_talk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1301, sequence_name='Talk_A')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=101, text_id=20000051, duration=5000) # 닭들을 찾아주세요
        self.set_dialogue(type=1, spawn_id=1301, script='$02000329_BF__01_MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return npc_talk_02(self.ctx)


class npc_talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1301, sequence_name='Talk_A')
        self.set_dialogue(type=1, spawn_id=1301, script='$02000329_BF__01_MAIN__3$', time=2)


initial_state = idle
