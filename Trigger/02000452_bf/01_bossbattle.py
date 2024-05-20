""" trigger/02000452_bf/01_bossbattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[901,902,903])
        self.set_portal(portal_id=10) # ExitTop
        self.set_portal(portal_id=11) # ExitUnder
        self.enable_spawn_point_pc(spawn_id=10000, is_enable=True) # PC스포너 제어
        self.enable_spawn_point_pc(spawn_id=10001)
        self.enable_spawn_point_pc(spawn_id=10002)
        self.enable_spawn_point_pc(spawn_id=10003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return Boss01SpawnDelay(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return Boss02SpawnDelay(self.ctx)
        if self.user_detected(box_ids=[9003]):
            return Boss03SpawnDelay(self.ctx)


# 오른쪽
class Boss01SpawnDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=10000) # 기본 스포너
        self.enable_spawn_point_pc(spawn_id=10001, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Boss01Spawn(self.ctx)


class Boss01Spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901], auto_target=False) # 23100084
        self.set_user_value(trigger_id=1122330, key='AgentOff', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss01Talk01(self.ctx)


class Boss01Talk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003068, script='$02000452_BF__01_BOSSBATTLE__0$', time=4) # 설눈이
        self.set_skip(state=Boss01Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Boss01Talk01Skip(self.ctx)


class Boss01Talk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss01Talk02(self.ctx)


class Boss01Talk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003069, script='$02000452_BF__01_BOSSBATTLE__1$', time=5) # 에르다
        self.set_skip(state=Boss01Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Boss01Talk02Skip(self.ctx)


class Boss01Talk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901]):
            return LeavePortalOn(self.ctx)


# 중앙
class Boss02SpawnDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=10000) # 기본 스포너
        self.enable_spawn_point_pc(spawn_id=10002, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Boss02Spawn(self.ctx)


class Boss02Spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902], auto_target=False) # 23000086

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss02CameraSet(self.ctx)


class Boss02CameraSet(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=511)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss02Talk01(self.ctx)


class Boss02Talk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003068, script='$02000452_BF__01_BOSSBATTLE__0$', time=3) # 설눈이
        self.set_skip(state=Boss02Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Boss02Talk01Skip(self.ctx)


class Boss02Talk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=512)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss02Talk02(self.ctx)


class Boss02Talk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003069, script='$02000452_BF__01_BOSSBATTLE__1$', time=4) # 에르다
        self.set_skip(state=Boss02Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Boss02Talk02Skip(self.ctx)


class Boss02Talk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return LeavePortalOn(self.ctx)


# 왼쪽
class Boss03SpawnDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=10000) # 기본 스포너
        self.enable_spawn_point_pc(spawn_id=10003, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Boss03Spawn(self.ctx)


class Boss03Spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[903], auto_target=False) # 23000087
        self.set_user_value(trigger_id=1122330, key='AgentOff', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=521)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss03Talk01(self.ctx)


class Boss03Talk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003068, script='$02000452_BF__01_BOSSBATTLE__0$', time=4) # 설눈이
        self.set_skip(state=Boss03Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Boss03Talk01Skip(self.ctx)


class Boss03Talk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=522)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Boss03Talk02(self.ctx)


class Boss03Talk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003069, script='$02000452_BF__01_BOSSBATTLE__1$', time=5) # 에르다
        self.set_skip(state=Boss03Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Boss03Talk02Skip(self.ctx)


class Boss03Talk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[903]):
            return LeavePortalOn(self.ctx)


# 종료
class LeavePortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='BossKill', value=1)
        self.destroy_monster(spawn_ids=[901,902,903])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_achievement(trigger_id=9900, type='trigger', achieve='ClearSnowQueen')
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True) # ExitTop
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True) # ExitUnder


initial_state = Wait
