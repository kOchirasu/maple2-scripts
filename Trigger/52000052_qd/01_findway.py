""" trigger/52000052_qd/01_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212]) # MobGround_AlawaysOff
        # LaserTotemBarrier_AlawaysOn
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008], visible=True)
        # JuntaFlyGround_AlawaysOff
        self.set_mesh(trigger_ids=[4100,4101,4102,4103,4104,4105,4106])
        self.set_mesh(trigger_ids=[3001], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3101]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3001], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3101]) # CrystalOn
        self.set_effect(trigger_ids=[5201]) # Sound_CrystalOn
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) >= 1:
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100,200], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000052_QD__01_FINDWAY__0$', time=5) # 준타
        self.set_skip(state=Dialogue02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Dialogue02Skip(self.ctx)


class Dialogue02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_100')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_200')
        self.set_dialogue(type=1, spawn_id=200, time=3) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1301, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2301, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$52000052_QD__01_FINDWAY__1$', time=3) # 준타
        self.set_dialogue(type=1, spawn_id=100, script='$52000052_QD__01_FINDWAY__2$', time=2, arg5=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return Round01_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[100,200])


class Round01_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 전투용 준타
        self.set_user_value(trigger_id=901, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='01RoundSuccess') == 1:
            return Round01_Sucess(self.ctx)


class Round01_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001')
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 연출용 틴차이
        self.set_effect(trigger_ids=[5201], visible=True) # Sound_CrystalOn
        self.set_mesh(trigger_ids=[3001], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3101], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3001]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3101], visible=True) # CrystalOn
        self.set_dialogue(type=1, spawn_id=101, script='$52000052_QD__01_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round01_RouteSelect(self.ctx)


class Round01_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round01_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round01_PickRoute_Right(self.ctx)


class Round01_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1301, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2301, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound02(self.ctx)


class GoToRound02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Round01_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1301, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2301, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToRound03(self.ctx)


class GoToRound03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
