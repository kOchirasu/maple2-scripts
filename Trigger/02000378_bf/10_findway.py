""" trigger/02000378_bf/10_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4030], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3010], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3110]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3010], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3110]) # CrystalOn
        self.set_effect(trigger_ids=[5210]) # Sound_CrystalOn
        # self.set_user_value(key='FindWayLeft', value=0)
        # self.set_user_value(key='FindWayRight', value=0)
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn_FromPortal(self.ctx)


"""
20170223 업데이트 던전 개편 단축
왼쪽에서 진입
"""

"""
class ReadyToWalkIn_FromLeft01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4030])
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_110L')
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_210L')
        self.set_dialogue(type=1, spawn_id=207, script='$02000378_BF__10_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromLeft02(self.ctx)
"""

"""
class ReadyToWalkIn_FromLeft02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1310, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2310, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromLeft03(self.ctx)
"""

"""
class ReadyToWalkIn_FromLeft03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__10_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round10_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[107,207])
"""

# 오른쪽에서 진입

"""
class ReadyToWalkIn_FromRight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4030])
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_110R')
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_210R')
        self.set_dialogue(type=1, spawn_id=208, script='$02000378_BF__10_FINDWAY__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromRight02(self.ctx)
"""

"""
class ReadyToWalkIn_FromRight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1310, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2310, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromRight03(self.ctx)
"""

"""
class ReadyToWalkIn_FromRight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=108, script='$02000378_BF__10_FINDWAY__3$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round10_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[108,208])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4030]) # RoundBarrier
        self.set_user_value(trigger_id=1310, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2310, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[2010], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=110, script='$02000378_BF__10_FINDWAY__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round10_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[110])


class Round10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1010], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1010, script='$02000378_BF__10_FINDWAY__4$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=910, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='10RoundSuccess') == 1:
            return Round10_Sucess01(self.ctx)


class Round10_Sucess01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2010, patrol_name='MS2PatrolData_2010')
        self.destroy_monster(spawn_ids=[1010])
        self.spawn_monster(spawn_ids=[110], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3010], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3110], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3010]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3110], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5210], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=110, script='$02000378_BF__10_FINDWAY__5$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round10_RouteSelect(self.ctx)


class Round10_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2010])
        self.spawn_monster(spawn_ids=[210], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round10_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round10_PickRoute_Right(self.ctx)


class Round10_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1310, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2310, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal17(self.ctx)


class GoToPortal17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_17')
        self.move_npc(spawn_id=210, patrol_name='MS2PatrolData_27')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round10_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1310, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2310, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal18(self.ctx)


class GoToPortal18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_18')
        self.move_npc(spawn_id=210, patrol_name='MS2PatrolData_28')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[110,210])


initial_state = Wait
