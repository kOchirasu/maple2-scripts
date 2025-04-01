""" trigger/02000378_bf/11_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4031], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3011], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3111]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3011], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3111]) # CrystalOn
        self.set_effect(trigger_ids=[5211]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn_FromPortal(self.ctx)


# 왼쪽에서 진입

"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4031])
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_111')
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_211')
        self.set_dialogue(type=1, spawn_id=208, script='$02000378_BF__11_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)
"""

"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1311, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2311, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)
"""

"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=108, script='$02000378_BF__11_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round11_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[108,208])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4031]) # RoundBarrier
        self.set_user_value(trigger_id=1311, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2311, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[2011], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=111, script='$02000378_BF__11_FINDWAY__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round11_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[111])


class Round11_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1011], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1011, script='$02000378_BF__11_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=911, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='11RoundSuccess') == 1:
            return Round11_Sucess(self.ctx)


class Round11_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2011, patrol_name='MS2PatrolData_2011')
        self.destroy_monster(spawn_ids=[1011])
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3011], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3111], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3011]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3111], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5211], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=111, script='$02000378_BF__11_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Round11_RouteSelect(self.ctx)


class Round11_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2011])
        self.spawn_monster(spawn_ids=[211], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round11_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round11_PickRoute_Right(self.ctx)


class Round11_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1311, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2311, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal19(self.ctx)


class GoToPortal19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_19')
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_29')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round11_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1311, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2311, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal10(self.ctx)


class GoToPortal10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12, key='FindWay', value=1)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_10')
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_20')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,211])


initial_state = Wait
