""" trigger/82000012_survival/02_ride.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7100,7200,7300,7400,7500,7600,7700,7800]) # MushBalloon Regen Sound
        self.set_effect(trigger_ids=[5100,5200,5300,5400,5500,5600,5700,5800]) # MushBalloon Rise Sound
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6100,6200,6300,6400,6500,6600,6700,6800])
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
        self.set_effect(trigger_ids=[7100], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[110], auto_target=False) # North_To_South
        self.write_log(log_name='Survival', event='bus_01') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride01_StartPatrolDelay(self.ctx)


class Ride01_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5100], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_111')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride01_StartPatrol(self.ctx)


class Ride01_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[110], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_110') # North_To_South

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[110])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6100], visible=True)


# South_To_North
class Ride02_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7200], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[120], auto_target=False) # South_To_North
        self.write_log(log_name='Survival', event='bus_02') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride02_StartPatrolDelay(self.ctx)


class Ride02_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5200], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_121')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride02_StartPatrol(self.ctx)


class Ride02_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[120], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_120') # South_To_North

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[120])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6200], visible=True)


# East_To_West
class Ride03_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7300], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[130], auto_target=False) # East_To_West
        self.write_log(log_name='Survival', event='bus_03') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride03_StartPatrolDelay(self.ctx)


class Ride03_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=130, patrol_name='MS2PatrolData_131')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride03_StartPatrol(self.ctx)


class Ride03_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[130], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=130, patrol_name='MS2PatrolData_130') # East_To_West

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[130])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6300], visible=True)


# West_To_East
class Ride04_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7400], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[140], auto_target=False) # West_To_East
        self.write_log(log_name='Survival', event='bus_04') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride04_StartPatrolDelay(self.ctx)


class Ride04_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=140, patrol_name='MS2PatrolData_141')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride04_StartPatrol(self.ctx)


class Ride04_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[140], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=140, patrol_name='MS2PatrolData_140') # North_To_South

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[140])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6400], visible=True)


# West_To_East
class Ride05_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7500], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[150], auto_target=False) # NorthWest_To_SouthEast
        self.write_log(log_name='Survival', event='bus_05') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride05_StartPatrolDelay(self.ctx)


class Ride05_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5500], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_151')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride05_StartPatrol(self.ctx)


class Ride05_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[150], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_150') # NorthWest_To_SouthEast

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[150])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6500], visible=True)


# NorthEast_To_SouthWest
class Ride06_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7600], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[160], auto_target=False) # NorthEast_To_SouthWest
        self.write_log(log_name='Survival', event='bus_06') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride06_StartPatrolDelay(self.ctx)


class Ride06_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5600], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=160, patrol_name='MS2PatrolData_161')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride06_StartPatrol(self.ctx)


class Ride06_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[160], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=160, patrol_name='MS2PatrolData_160') # NorthEast_To_SouthWest

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[160])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6600], visible=True)


# SouthWest_To_NorthEast
class Ride07_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7700], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[170], auto_target=False) # SouthWest_To_NorthEast
        self.write_log(log_name='Survival', event='bus_07') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride07_StartPatrolDelay(self.ctx)


class Ride07_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5700], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=170, patrol_name='MS2PatrolData_171')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride07_StartPatrol(self.ctx)


class Ride07_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[170], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=170, patrol_name='MS2PatrolData_170') # SouthWest_To_NorthEast

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[170])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6700], visible=True)


# SouthEast_To_NorthWest
class Ride08_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7800], visible=True) # MushBalloon Regen Sound
        self.spawn_monster(spawn_ids=[180], auto_target=False) # SouthEast_To_NorthWest
        self.write_log(log_name='Survival', event='bus_08') # 서바이벌 버스 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartPatrol') == 1:
            return Ride08_StartPatrolDelay(self.ctx)


class Ride08_StartPatrolDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5800], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawn_id=180, patrol_name='MS2PatrolData_181')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ride08_StartPatrol(self.ctx)


class Ride08_StartPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MushBalloon Flying Loop Sound
        self.add_buff(box_ids=[180], skill_id=70001081, level=1, is_skill_set=False)
        self.move_npc(spawn_id=180, patrol_name='MS2PatrolData_180') # SouthEast_To_NorthWest

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[180])
        # MushBalloon Disappear Sound
        self.set_effect(trigger_ids=[6800], visible=True)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='bus_end') # 서바이벌 버스 로그


initial_state = Wait
