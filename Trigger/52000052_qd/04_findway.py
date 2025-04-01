""" trigger/52000052_qd/04_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=21) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4024], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3004], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3104]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3004], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3104]) # CrystalOn
        self.set_effect(trigger_ids=[5204]) # Sound_CrystalOn
        self.set_user_value(key='FindWayLeft', value=0)
        self.set_user_value(key='FindWayRight', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWayLeft') == 1:
            return ReadyToWalkIn_FromLeft01(self.ctx)
        if self.user_value(key='FindWayRight') == 1:
            return ReadyToWalkIn_FromRight01(self.ctx)


# 왼쪽에서 진입
class ReadyToWalkIn_FromLeft01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4024]) # RoundBarrier
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_104L')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_204L')
        self.set_dialogue(type=1, spawn_id=202, script='$52000052_QD__04_FINDWAY__0$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromLeft02(self.ctx)


class ReadyToWalkIn_FromLeft02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1304, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromLeft03(self.ctx)


class ReadyToWalkIn_FromLeft03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52000052_QD__04_FINDWAY__1$', time=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round04_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102,202])


# 오른쪽에서 진입
class ReadyToWalkIn_FromRight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4024]) # RoundBarrier
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_104R')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_204R')
        self.set_dialogue(type=1, spawn_id=203, script='$52000052_QD__04_FINDWAY__0$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromRight02(self.ctx)


class ReadyToWalkIn_FromRight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1304, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn_FromRight03(self.ctx)


class ReadyToWalkIn_FromRight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=103, script='$52000052_QD__04_FINDWAY__1$', time=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round04_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103,203])


class Round04_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2004], auto_target=False) # 전투용 준타
        self.set_dialogue(type=1, spawn_id=1004, script='$52000052_QD__04_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=904, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='04RoundSuccess') == 1:
            return Round04_Sucess02(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class Round04_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[2204]):
            return Round04_Sucess02(self.ctx)
"""

class Round04_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=2204, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData_2004')
        self.destroy_monster(spawn_ids=[1004])
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3004], start_delay=100) # CrystalOff
        # self.set_mesh(trigger_ids=[3104], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3004]) # CrystalOff
        # self.set_mesh_animation(trigger_ids=[3104], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5204], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=21, visible=True, enable=True)
        self.set_dialogue(type=1, spawn_id=104, script='$52000052_QD__04_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round04_RouteSelect(self.ctx)


class Round04_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[2204])
        self.destroy_monster(spawn_ids=[2004])
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50.0):
            return Round04_PickRoute_Left(self.ctx)
        """
        """
        if self.random_condition(weight=50.0):
            return Round04_PickRoute_Right(self.ctx)
        """
        if self.wait_tick(wait_tick=1000):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[204])


# 20170223 업데이트 던전 개편 단축
class Round04_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1304, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2304, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound05(self.ctx)


class GoToRound05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=5, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Round04_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1304, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2304, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound06(self.ctx)


class GoToRound06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=6, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
