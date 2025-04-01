""" trigger/02000378_bf/05_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4025], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3005], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3105]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3005], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3105]) # CrystalOn
        self.set_effect(trigger_ids=[5205]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn_FromPortal(self.ctx)


"""
20170223 업데이트 던전 개편 단축
왼쪽에서 진입
"""

"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4025])
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_105')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_205')
        self.set_dialogue(type=1, spawn_id=204, script='$02000378_BF__05_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)
"""

"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1305, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2305, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)
"""

"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$02000378_BF__05_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round05_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[104,204])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4025]) # RoundBarrier
        self.set_user_value(trigger_id=1305, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2305, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[2005], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=105, script='$02000378_BF__05_FINDWAY__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round05_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[105])


class Round05_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1005, script='$02000378_BF__05_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=905, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='05RoundSuccess') == 1:
            return Round05_Sucess(self.ctx)


class Round05_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData_2005')
        self.destroy_monster(spawn_ids=[1005])
        self.spawn_monster(spawn_ids=[105], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3005], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3105], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3005]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3105], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5205], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=105, script='$02000378_BF__05_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round05_RouteSelect(self.ctx)


class Round05_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2005])
        self.spawn_monster(spawn_ids=[205], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round05_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round05_PickRoute_Right(self.ctx)


class Round05_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1305, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2305, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal11(self.ctx)


class GoToPortal11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_11')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_21')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round05_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1305, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2305, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal12(self.ctx)


class GoToPortal12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12, key='FindWay', value=1)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_12')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_22')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105,205])


initial_state = Wait
