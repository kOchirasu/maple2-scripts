""" trigger/02000354_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7701])
        self.set_effect(trigger_ids=[7702])
        self.set_effect(trigger_ids=[7703])
        self.set_effect(trigger_ids=[7704])
        self.set_effect(trigger_ids=[7705])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작_04(self.ctx)


class 시작_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7701], visible=True) # 벽 녹이는 사운드
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012], fade=10.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 시작_05(self.ctx)


class 시작_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[11,12,13,14,15,16,17], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[11,12,13,14,15,16,17]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7702], visible=True) # 벽 녹이는 사운드
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=113, text_id=40011) # 다음 지역으로 이동하세요
        self.set_mesh(trigger_ids=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033], fade=10.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 관문_02_시작(self.ctx)


class 관문_02_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[21,22,23,24,25,26,27], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[21,22,23,24,25,26,27]):
            return 관문_02_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7703], visible=True) # 벽 녹이는 사운드
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=113, text_id=40011) # 다음 지역으로 이동하세요
        self.set_mesh(trigger_ids=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066,6067,6068,6069,6070,6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082,6083], fade=10.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 관문_03_시작(self.ctx)


class 관문_03_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[31,32,33,34,35,36,37,38,39], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[31,32,33,34,35,36,37,38,39]):
            return 관문_03_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7704], visible=True) # 벽 녹이는 사운드
        self.set_mesh(trigger_ids=[6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123], fade=10.0) # 벽 해제
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=113, text_id=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return 관문_04_시작(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_04_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[41,42,43,44,45,46,47,48], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[341,42,43,44,45,46,47,48]):
            return 관문_04_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_04_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7705], visible=True) # 벽 녹이는 사운드
        self.set_mesh(trigger_ids=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166], fade=10.0) # 벽 해제
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=113, text_id=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return 관문_05_시작(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 관문_05_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[51], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[51]):
            return 관문_05_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_05_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=112)


initial_state = idle
