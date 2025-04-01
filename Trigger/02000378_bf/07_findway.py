""" trigger/02000378_bf/07_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=22) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4027], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3007], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3107]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3007], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3107]) # CrystalOn
        self.set_effect(trigger_ids=[5207]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn_FromPortal(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4027])
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_107')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_207')
        self.set_dialogue(type=1, spawn_id=202, script='$02000378_BF__07_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)
"""

"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1307, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2307, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)
"""

"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000378_BF__07_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round07_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102,202])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4027]) # RoundBarrier
        self.set_user_value(trigger_id=1307, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2307, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[2007], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__07_FINDWAY__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round07_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[107])


class Round07_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1007], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1007, script='$02000378_BF__07_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=907, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='07RoundSuccess') == 1:
            return Round07_Sucess02(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class Round07_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[2207]):
            return Round07_Sucess02(self.ctx)
"""

class Round07_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2007, patrol_name='MS2PatrolData_2007')
        # self.move_npc(spawn_id=2207, patrol_name='MS2PatrolData_2007')
        self.destroy_monster(spawn_ids=[1007])
        self.spawn_monster(spawn_ids=[107], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3007], start_delay=100) # CrystalOff
        # self.set_mesh(trigger_ids=[3107], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3007]) # CrystalOff
        # self.set_mesh_animation(trigger_ids=[3107], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5207], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=22, visible=True, enable=True)
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__07_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round07_RouteSelect(self.ctx)


class Round07_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[2207])
        self.destroy_monster(spawn_ids=[2007])
        self.spawn_monster(spawn_ids=[207], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_107New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50.0):
            return Round07_PickRoute_Left(self.ctx)
        """
        """
        if self.random_condition(weight=50.0):
            return Round07_PickRoute_Right(self.ctx)
        """
        if self.wait_tick(wait_tick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[107])
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_207New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[207])


initial_state = Wait
