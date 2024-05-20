""" trigger/02000290_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=3010, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=3020, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=3040, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002,3003,3004,3005,3006,3007,3008], visible=True)
        self.set_mesh(trigger_ids=[3011], visible=True)
        self.set_mesh(trigger_ids=[3012,3013,3014,3015,3016], visible=True)
        self.set_mesh(trigger_ids=[3021], visible=True)
        self.set_mesh(trigger_ids=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], visible=True)
        self.set_mesh(trigger_ids=[3041], visible=True)
        self.set_mesh(trigger_ids=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], visible=True)
        self.set_effect(trigger_ids=[5000]) # GuideUI
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[2001])
        self.destroy_monster(spawn_ids=[2002])
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=9991)
        self.enable_spawn_point_pc(spawn_id=9992)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 로딩딜레이(self.ctx)


class 로딩딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[802,800], return_view=False)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[800,802])
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_event_ui(type=1, arg2='$02000290_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거01시작(self.ctx)


# 첫 번째 문 열림
class 트리거01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3001])
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거01진행(self.ctx)


class 트리거01진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3002,3003,3004,3005,3006,3007,3008], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return 트리거02시작(self.ctx)
        if self.wait_tick(wait_tick=7000):
            return 트리거02시작(self.ctx)


# 두 번째 문 열림
class 트리거02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3010, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3011])
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거02진행(self.ctx)


class 트리거02진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3010, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3012,3013,3014,3015,3016], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1002,1003]):
            return 트리거03시작(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 트리거03시작(self.ctx)


# 세 번째 문 열림
class 트리거03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3020, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3021])
        self.spawn_monster(spawn_ids=[1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거03진행(self.ctx)


class 트리거03진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3020, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1004]):
            return 트리거04시작(self.ctx)
        if self.wait_tick(wait_tick=7000):
            return 트리거04시작(self.ctx)


class 트리거04시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3040, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3041])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거04진행(self.ctx)


class 트리거04진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002902)
        self.set_actor(trigger_id=3040, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
