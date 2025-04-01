""" trigger/52000052_qd/02_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4022], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3002], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3102]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3002], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3102]) # CrystalOn
        self.set_effect(trigger_ids=[5202]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4022]) # RoundBarrier
        # self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # 레이저 토템
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')
        self.set_dialogue(type=1, spawn_id=201, script='$52000052_QD__02_FINDWAY__0$', time=2) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1302, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2302, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000052_QD__02_FINDWAY__2$', time=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round02_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[101,201])


class Round02_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 전투용 준타
        self.set_dialogue(type=1, spawn_id=1002, script='$52000052_QD__02_FINDWAY__3$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=902, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='02RoundSuccess') == 1:
            return Round02_Sucess01(self.ctx)


class Round02_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9002, spawn_ids=[2202]):
            return Round02_Sucess02(self.ctx)


class Round02_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2202, patrol_name='MS2PatrolData_2002')
        self.destroy_monster(spawn_ids=[1002])
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3002], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3102], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3002]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3102], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5202], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=102, script='$52000052_QD__02_FINDWAY__4$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round02_RouteSelect(self.ctx)


class Round02_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2202])
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round02_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round02_PickRoute_Right(self.ctx)


class Round02_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1302, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2302, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound04(self.ctx)


class GoToRound04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='FindWayLeft', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Round02_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1302, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2302, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound07(self.ctx)


class GoToRound07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[901,902,903]) # 레이저 토템
        pass


initial_state = Wait
