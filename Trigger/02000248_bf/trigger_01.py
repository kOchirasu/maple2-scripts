""" trigger/02000248_bf/trigger_01.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110])
        self.set_effect(trigger_ids=[2001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=201) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[201]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[798,799])
        self.set_timer(timer_id='89', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='89'):
            return 공격(self.ctx)


class 공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103])
        self.set_effect(trigger_ids=[2001], visible=True)
        self.set_event_ui(type=1, arg2='$02000248_BF__TRIGGER_01__0$', arg3='5000', arg4='0')
        self.set_timer(timer_id='1', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            return 공격1(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104,105])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104,105]):
            return 공격2(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[106,107,108])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106,107,108]):
            return 공격2_2(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109,110])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109,110]):
            return 공격3(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114,115,116])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[114,115,116]):
            return 공격3_2(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,112,113])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113]):
            return 공격3_3(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격3_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[117,118,119,120])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[117,118,119,120]):
            return 공격4(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121,122,123,124,125])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122,123,124,125]):
            return 공격4_2(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[126,127,128,129,130])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[126,127,128,129,130]):
            return 공격5(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[131,132,133,134,135,136])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[131,132,133,134,135,136]):
            return 공격5_2(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격5_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[137,138,139,140])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[137,138,139,140]):
            return 공격6(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[141,142,143,144,145,146,148])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[141,142,143,144,145,146,148]):
            return 공격7(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[151,153,154,155,156,157,158])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[151,153,154,155,156,157,158]):
            return 공격8(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 공격8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[161,162,163,164,167,168,169,170])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[161,162,163,164,167,168,169,170])
            return 끝연출(self.ctx)
        if not self.user_detected(box_ids=[999]):
            return 대기(self.ctx)


class 끝연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8003,8002], return_view=False)
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000249, portal_id=2)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 차진입대기2(self.ctx)


class 차진입대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


initial_state = 대기
