""" trigger/02000315_bf/battle_01.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # UI
        self.set_ladder(trigger_ids=[510]) # LadderEnterance
        self.set_ladder(trigger_ids=[511]) # LadderEnterance
        self.set_ladder(trigger_ids=[512]) # LadderEnterance
        self.set_ladder(trigger_ids=[513]) # LadderEnterance
        self.set_mesh(trigger_ids=[3000,3001], visible=True) # Invisible_Barrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109]) # 1stBridge
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209]) # 2ndBridge
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309]) # 3rdBridge
        self.set_mesh(trigger_ids=[3110], visible=True) # 1stBridgeBarrier
        self.set_mesh(trigger_ids=[3210], visible=True) # 2ndBridgeBarrier
        self.set_mesh(trigger_ids=[3310], visible=True) # 3rdBridgeBarrier
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_interact_object(trigger_ids=[10001043], state=1) # 1stBridge
        self.set_interact_object(trigger_ids=[10001044], state=1) # 2ndBridge
        self.set_interact_object(trigger_ids=[10001035], state=1) # 3rdBridge
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=992)
        self.enable_spawn_point_pc(spawn_id=993)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        self.spawn_monster(spawn_ids=[99], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[600,601], return_view=False)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[601,600])
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FirstBattle(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_ladder(trigger_ids=[510], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[511], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[512], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[513], visible=True, enable=True) # LadderEnterance
        self.set_mesh(trigger_ids=[3000,3001]) # Invisible_Barrier


class FirstBattle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3, key='CameraWalkEnd', value=1)
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001043], state=0):
            return FirstBridgeOn(self.ctx)


class FirstBridgeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.destroy_monster(spawn_ids=[901,902,903])
        self.set_mesh(trigger_ids=[3110]) # 1stBridgeBarrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=True, interval=100, fade=10.0) # 1stBridge
        self.set_user_value(trigger_id=101, key='BridgeOpen', value=1)
        self.set_user_value(trigger_id=102, key='BridgeOpen', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[504]):
            # 두 번째 전투판 진입
            return SecondBattle(self.ctx)


class SecondBattle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=991, is_enable=True)
        self.spawn_monster(spawn_ids=[904,905,906], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001044], state=0):
            return SecondBridgeOn(self.ctx)


class SecondBridgeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.destroy_monster(spawn_ids=[904,905,906])
        self.set_mesh(trigger_ids=[3210]) # 2ndBridgeBarrier
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, interval=100, fade=10.0) # 2ndBridge
        self.set_user_value(trigger_id=101, key='BridgeOpen', value=2)
        self.set_user_value(trigger_id=102, key='BridgeOpen', value=2)
        self.set_user_value(trigger_id=103, key='BridgeOpen', value=2)
        self.set_user_value(trigger_id=104, key='BridgeOpen', value=2)
        self.set_user_value(trigger_id=105, key='BridgeOpen', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[507]):
            # 세 번째 전투판 진입
            return ThirdBattle(self.ctx)


class ThirdBattle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=993, is_enable=True)
        self.spawn_monster(spawn_ids=[907,908,909], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001035], state=0):
            return ThirdBridgeOn(self.ctx)


class ThirdBridgeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.destroy_monster(spawn_ids=[907,908,909])
        self.set_mesh(trigger_ids=[3310]) # 3rdBridgeBarrier
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309], visible=True, interval=100, fade=10.0) # 3rdBridge
        self.set_user_value(trigger_id=101, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=102, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=103, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=104, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=105, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=106, key='BridgeOpen', value=3)
        self.set_user_value(trigger_id=107, key='BridgeOpen', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[402]):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=993)
        self.enable_spawn_point_pc(spawn_id=992, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return Success(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[99])


class Success(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = Setting
