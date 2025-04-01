""" trigger/02000318_bf/mobspawn_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True) # EnteranceBarrier
        self.set_mesh(trigger_ids=[3001], visible=True) # 1stBarrier
        self.set_mesh(trigger_ids=[3002], visible=True) # 2ndBarrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], visible=True) # EnteranceBarrier
        self.set_user_value(key='ShipMove', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304,305], auto_target=False)
        self.spawn_monster(spawn_ids=[201,202,203,204,205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.set_event_ui_script(type=BannerType.Text, script='$02000318_BF__MOBSPAWN_01__0$', duration=3000, box_ids=['0'])
        self.set_mesh(trigger_ids=[3000]) # EnteranceBarrier
        self.set_random_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], start_delay=29, interval=500, fade=30) # EnteranceBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle01(self.ctx)


class Battle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031801, text_id=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303,304,305]):
            return Battle02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[301,302,303,304,305])


class Battle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,112,113,114,115,116,501], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Battle03(self.ctx)


class Battle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031801)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요
        self.show_guide_summary(entity_id=20031802, text_id=20031802)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114,115,116]):
            return MoveShip01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[111,112,113,114,115,116,501])


class MoveShip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031802)
        self.set_user_value(trigger_id=2, key='ShipSet', value=1)
        self.set_mesh(trigger_ids=[3001]) # 1stBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ShipMove') == 1:
            return MoveShip02(self.ctx)


class MoveShip02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return Battle11(self.ctx)


class Battle11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031801, text_id=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205]):
            return Battle12(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[201,202,203,204,205])


class Battle12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211,212,213,214,215,216,217,218,219,502,503], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Battle13(self.ctx)


class Battle13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031801)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요
        self.show_guide_summary(entity_id=20031802, text_id=20031802)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211,212,213,214,215,216,217,218,219]):
            return CannonSpawn01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[211,212,213,214,215,216,217,218,219,502,503])


class CannonSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CannonSpawn02(self.ctx)


class CannonSpawn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031802)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031804, text_id=20031804) # 대포를 이용해 다음 지역으로 이동하세요
        self.set_mesh(trigger_ids=[3002]) # 2ndBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031804)


initial_state = Setting
