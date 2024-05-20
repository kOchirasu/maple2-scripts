""" trigger/02010049_bf/main01.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # Voice 60000509
        self.set_mesh(trigger_ids=[10000], visible=True) # battle02
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True) # battle02 flag
        self.set_mesh(trigger_ids=[20000], visible=True) # battle03
        self.set_mesh(trigger_ids=[30000], visible=True) # battle04
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=True) # battle03 flag
        self.set_mesh(trigger_ids=[9990,9991,9992,9993], visible=True) # startzone
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017], visible=True) # startzone flag
        self.set_mesh(trigger_ids=[7000,7001,7002,7003]) # bridge

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102,103,104,105,107,108], auto_target=False)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206], auto_target=False)
        self.show_guide_summary(entity_id=20104901, text_id=20104901, duration=3000) # 벌레떼가 모여들고 있습니다.
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_skip(state=CameraWalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CameraWalk02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9990,9991,9992,9993]) # startzone
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017], fade=10.0) # startzone flag

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 전투지역01시작(self.ctx)


class 전투지역01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104902, text_id=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,103,104,105,107,108]):
            return 전투지역02대기(self.ctx)


class 전투지역02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000]) # battle02
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], fade=10.0) # battle02 flag
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104903, text_id=20104903, duration=5000) # 안 쪽에 벌레들이 더 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 전투지역02시작(self.ctx)


class 전투지역02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104902, text_id=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투지역02추가(self.ctx)


class 전투지역02추가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104904, text_id=20104904, duration=5000) # 화장실 악취에는 벌레도 기절합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,206]):
            return 전투지역03대기(self.ctx)


class 전투지역03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20000]) # battle03
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], fade=10.0) # battle03 flag
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104903, text_id=20104903, duration=5000) # 안 쪽에 벌레들이 더 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return 전투지역03시작(self.ctx)


class 전투지역03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[399], auto_target=False) # boss
        self.spawn_monster(spawn_ids=[302,303,304,305,306,307], auto_target=False)
        self.spawn_monster(spawn_ids=[309], auto_target=False) # elite
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104902, text_id=20104902, duration=5000) # 달려드는 벌레들을 모두 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[302,303,304,305,306,307]):
            return 전투지역04시작(self.ctx)


class 전투지역04시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=20104904, text_id=20104904, duration=5000) # 화장실 악취에는 벌레도 기절합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[309]):
            return 퇴장연출01(self.ctx)


class 퇴장연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[399])
        self.spawn_monster(spawn_ids=[400], auto_target=False)
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_399')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 퇴장연출02(self.ctx)


class 퇴장연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # Voice 60000509

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퇴장연출03(self.ctx)


class 퇴장연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8000, spawn_ids=[400]):
            return 다리생성01(self.ctx)


class 다리생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[400])
        self.set_mesh(trigger_ids=[30000]) # battle04
        self.set_random_mesh(trigger_ids=[7000,7001,7002,7003], visible=True, start_delay=4, interval=100, fade=100) # bridge
        self.show_guide_summary(entity_id=20104905, text_id=20104905, duration=6000) # 포탈을 타세요
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9010]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
