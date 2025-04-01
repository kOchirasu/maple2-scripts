""" trigger/99999913/02_ride.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='SetRide', value=0)
        self.set_user_value(key='StartPatrol', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetRide') == 1:
            # North_To_South
            return Ride01_Ready(self.ctx)
        if self.user_value(key='SetRide') == 2:
            # South_To_North
            return Ride02_Ready(self.ctx)
        if self.user_value(key='SetRide') == 3:
            # East_To_West
            return Ride03_Ready(self.ctx)
        if self.user_value(key='SetRide') == 4:
            # West_To_East
            return Ride04_Ready(self.ctx)
        if self.user_value(key='SetRide') == 5:
            # NorthWest_To_SouthEast
            return Ride05_Ready(self.ctx)
        if self.user_value(key='SetRide') == 6:
            # NorthEast_To_SouthWest
            return Ride06_Ready(self.ctx)
        if self.user_value(key='SetRide') == 7:
            # SouthWest_To_NorthEast
            return Ride07_Ready(self.ctx)
        if self.user_value(key='SetRide') == 8:
            # SouthEast_To_NorthWest
            return Ride08_Ready(self.ctx)


# North_To_South
class Ride01_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[110], auto_target=False) # North_To_South
        self.write_log(log_name='Survival', event='bus_01') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride01_StartPatrolDelay(self.ctx)


class Ride01_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride01_StartPatrol(self.ctx)


class Ride01_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_110') # North_To_South

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# South_To_North
class Ride02_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[120], auto_target=False) # South_To_North
        self.write_log(log_name='Survival', event='bus_02') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride02_StartPatrolDelay(self.ctx)


class Ride02_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride02_StartPatrol(self.ctx)


class Ride02_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_120') # South_To_North

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# East_To_West
class Ride03_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[130], auto_target=False) # East_To_West
        self.write_log(log_name='Survival', event='bus_03') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride03_StartPatrolDelay(self.ctx)


class Ride03_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride03_StartPatrol(self.ctx)


class Ride03_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=130, patrol_name='MS2PatrolData_130') # East_To_West

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# West_To_East
class Ride04_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[140], auto_target=False) # West_To_East
        self.write_log(log_name='Survival', event='bus_04') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride04_StartPatrolDelay(self.ctx)


class Ride04_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride04_StartPatrol(self.ctx)


class Ride04_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=140, patrol_name='MS2PatrolData_140') # North_To_South

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# West_To_East
class Ride05_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[150], auto_target=False) # NorthWest_To_SouthEast
        self.write_log(log_name='Survival', event='bus_05') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride05_StartPatrolDelay(self.ctx)


class Ride05_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride05_StartPatrol(self.ctx)


class Ride05_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_150') # NorthWest_To_SouthEast

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# NorthEast_To_SouthWest
class Ride06_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[160], auto_target=False) # NorthEast_To_SouthWest
        self.write_log(log_name='Survival', event='bus_06') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride06_StartPatrolDelay(self.ctx)


class Ride06_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride06_StartPatrol(self.ctx)


class Ride06_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=160, patrol_name='MS2PatrolData_160') # NorthEast_To_SouthWest

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# SouthWest_To_NorthEast
class Ride07_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[170], auto_target=False) # SouthWest_To_NorthEast
        self.write_log(log_name='Survival', event='bus_07') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride07_StartPatrolDelay(self.ctx)


class Ride07_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride07_StartPatrol(self.ctx)


class Ride07_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=170, patrol_name='MS2PatrolData_170') # SouthWest_To_NorthEast

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


# SouthEast_To_NorthWest
class Ride08_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[180], auto_target=False) # SouthEast_To_NorthWest
        self.write_log(log_name='Survival', event='bus_08') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride08_StartPatrolDelay(self.ctx)


class Ride08_StartPatrolDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ride08_StartPatrol(self.ctx)


class Ride08_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=180, patrol_name='MS2PatrolData_180') # SouthEast_To_NorthWest

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=36000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[110,120,130,140,150,160,170,180])
        self.write_log(log_name='Survival', event='bus_end') # 서바이벌 버스 로그


initial_state = Wait
