""" trigger/52000052_qd/09_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4029], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3009], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3109]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3009], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3109]) # CrystalOn
        self.set_effect(trigger_ids=[5209]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn01(self.ctx)


# 왼쪽에서 진입
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4029]) # RoundBarrier
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_109')
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_209')
        self.set_dialogue(type=1, spawn_id=207, script='$52000052_QD__04_FINDWAY__0$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1309, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2309, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=107, script='$52000052_QD__04_FINDWAY__1$', time=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round09_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[107,207])


class Round09_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1009], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2009], auto_target=False) # 전투용 준타
        self.set_dialogue(type=1, spawn_id=1009, script='$52000052_QD__04_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=909, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='09RoundSuccess') == 1:
            return Round09_Sucess(self.ctx)


class Round09_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2009, patrol_name='MS2PatrolData_2009')
        self.destroy_monster(spawn_ids=[1009])
        self.spawn_monster(spawn_ids=[109], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3009], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3109], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3009]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3109], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5209], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=109, script='$52000052_QD__04_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round09_RouteSelect(self.ctx)


class Round09_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2009])
        self.spawn_monster(spawn_ids=[209], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round09_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round09_PickRoute_Right(self.ctx)


class Round09_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1309, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2309, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal15(self.ctx)


class GoToPortal15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_15')
        self.move_npc(spawn_id=209, patrol_name='MS2PatrolData_25')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round09_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1309, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2309, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal16(self.ctx)


class GoToPortal16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12, key='FindWay', value=1)
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_16')
        self.move_npc(spawn_id=209, patrol_name='MS2PatrolData_26')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109,209])


initial_state = Wait
