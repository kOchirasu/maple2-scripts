""" trigger/02000312_bf/mobspawn_11.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3005,3006,3007,3008,3009,3010], visible=True) # Invisible_Barrier
        self.set_ladder(trigger_ids=[510]) # LadderEnterance
        self.set_ladder(trigger_ids=[511]) # LadderEnterance
        self.set_ladder(trigger_ids=[512]) # LadderEnterance
        self.set_ladder(trigger_ids=[513]) # LadderEnterance
        self.set_mesh(trigger_ids=[3002,3003,3004], visible=True) # Invisible_Barrier
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108], visible=True) # 덩굴
        self.set_mesh(trigger_ids=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], visible=True) # 덩굴
        self.set_mesh(trigger_ids=[1120,1121,1122,1123,1124,1125,1126], visible=True) # 덩굴
        self.set_mesh(trigger_ids=[1130,1131,1132,1133,1134,1135,1136,1137], visible=True) # 덩굴
        self.set_mesh(trigger_ids=[1140], visible=True) # 씨앗
        self.set_mesh_animation(trigger_ids=[1140], visible=True) # 씨앗
        self.set_effect(trigger_ids=[5000]) # UI
        self.set_effect(trigger_ids=[5001]) # Vine
        self.set_user_value(key='MobWaveStop', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
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
            return Battle01(self.ctx)

    def on_exit(self) -> None:
        self.set_ladder(trigger_ids=[510], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[511], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[512], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[513], visible=True, enable=True) # LadderEnterance
        self.set_mesh(trigger_ids=[3005,3006,3007,3008,3009,3010]) # Invisible_Barrier
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class Battle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)
        self.set_effect(trigger_ids=[5000], visible=True) # UI
        self.show_guide_summary(entity_id=20031201, text_id=20031201) # 몬스터를 모두 처치하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            return Battle02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[101,102,103])


class Battle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031201)
        self.spawn_monster(spawn_ids=[111,112,113,114], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114]):
            return Battle03(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[111,112,113,114])


class Battle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # UI
        self.show_guide_summary(entity_id=20031202, text_id=20031202) # 어둠의 씨앗 제거하기
        self.spawn_monster(spawn_ids=[130], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[130]):
            return VineRemove01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[130])


class VineRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031202)
        self.set_effect(trigger_ids=[5001], visible=True) # Vine
        self.set_mesh(trigger_ids=[3002,3003,3004], start_delay=500) # Invisible_Barrier
        self.set_random_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108], start_delay=9, fade=50) # 덩굴
        self.set_random_mesh(trigger_ids=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], start_delay=10, interval=300, fade=50) # 덩굴
        self.set_random_mesh(trigger_ids=[1120,1121,1122,1123,1124,1125,1126], start_delay=7, interval=200, fade=50) # 덩굴
        self.set_random_mesh(trigger_ids=[1130,1131,1132,1133,1134,1135,1136,1137], start_delay=8, interval=100, fade=50) # 덩굴
        self.set_mesh(trigger_ids=[1140], start_delay=200, fade=10.0) # 씨앗
        self.set_mesh_animation(trigger_ids=[1140]) # 씨앗

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return MobWaveStart(self.ctx)


class MobWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # UI
        self.show_guide_summary(entity_id=20031203, text_id=20031203) # 어둠의 씨앗 모두 제거하기
        self.spawn_monster(spawn_ids=[121,122,123,124,125,126,127,128], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122,123,124,125,126,127,128]):
            return MobWaveDelayRandom(self.ctx)
        if self.user_value(key='MobWaveStop') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[121,122,123,124,125,126,127,128])


class MobWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=60.0):
            # 기본 12초
            return MobWaveDelay01(self.ctx)
        if self.random_condition(weight=20.0):
            # 17초
            return MobWaveDelay02(self.ctx)
        if self.random_condition(weight=20.0):
            # 7초
            return MobWaveDelay03(self.ctx)
        if self.user_value(key='MobWaveStop') == 1:
            return Quit(self.ctx)


class MobWaveDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop') == 1:
            return Quit(self.ctx)


class MobWaveDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop') == 1:
            return Quit(self.ctx)


class MobWaveDelay03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031203)


initial_state = Setting
