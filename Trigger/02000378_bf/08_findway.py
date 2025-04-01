""" trigger/02000378_bf/08_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=23) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4028], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3008], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3108]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3008], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3108]) # CrystalOn
        self.set_effect(trigger_ids=[5208]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn_FromPortal(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4028])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_108')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_208')
        self.set_dialogue(type=1, spawn_id=203, script='$02000378_BF__08_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)
"""

"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1308, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2308, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)
"""

"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=103, script='$02000378_BF__08_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round08_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103,203])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4028]) # RoundBarrier
        self.set_user_value(trigger_id=1308, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2308, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[2008], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__08_FINDWAY__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round08_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[108])


class Round08_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1008], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1008, script='$02000378_BF__08_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=908, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='08RoundSuccess') == 1:
            return Round08_Sucess02(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class Round08_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9008, spawn_ids=[2208]):
            return Round08_Sucess02(self.ctx)
"""

class Round08_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2008, patrol_name='MS2PatrolData_2008')
        # self.move_npc(spawn_id=2208, patrol_name='MS2PatrolData_2008')
        self.destroy_monster(spawn_ids=[1008])
        self.spawn_monster(spawn_ids=[108], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3008], start_delay=100) # CrystalOff
        # self.set_mesh(trigger_ids=[3108], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3008]) # CrystalOff
        # self.set_mesh_animation(trigger_ids=[3108], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5208], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=23, visible=True, enable=True) # 20170223 업데이트 던전 개편 단축
        self.set_dialogue(type=1, spawn_id=108, script='$02000378_BF__08_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round08_RouteSelect(self.ctx)


class Round08_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2008])
        # self.destroy_monster(spawn_ids=[2208])
        self.spawn_monster(spawn_ids=[208], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_108New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50.0):
            return Round08_PickRoute_Left(self.ctx)
        """
        """
        if self.random_condition(weight=50.0):
            return Round08_PickRoute_Right(self.ctx)
        """
        if self.wait_tick(wait_tick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108])
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_208New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[208])


initial_state = Wait
