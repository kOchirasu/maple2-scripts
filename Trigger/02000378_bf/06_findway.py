""" trigger/02000378_bf/06_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4026], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3006], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3106]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3006], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3106]) # CrystalOn
        self.set_effect(trigger_ids=[5206]) # Sound_CrystalOn
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
        self.set_mesh(trigger_ids=[4026])
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_106')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_206')
        self.set_dialogue(type=1, spawn_id=204, script='$02000378_BF__06_FINDWAY__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn02(self.ctx)
"""

"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1306, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2306, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToWalkIn03(self.ctx)
"""

"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$02000378_BF__06_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round06_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[104,204])
"""

# 포탈로 진입

class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4026]) # RoundBarrier
        self.set_user_value(trigger_id=1306, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2306, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[2006], auto_target=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=106, script='$02000378_BF__06_FINDWAY__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round06_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[106])


class Round06_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1006, script='$02000378_BF__06_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=906, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='06RoundSuccess') == 1:
            return Round06_Sucess(self.ctx)


class Round06_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2006, patrol_name='MS2PatrolData_2006')
        self.destroy_monster(spawn_ids=[1006])
        self.spawn_monster(spawn_ids=[106], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3006], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3106], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3006]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3106], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5206], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=106, script='$02000378_BF__06_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Round06_RouteSelect(self.ctx)


class Round06_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2006])
        self.spawn_monster(spawn_ids=[206], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round06_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50.0):
            return Round06_PickRoute_Right(self.ctx)


class Round06_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1306, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2306, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal13(self.ctx)


class GoToPortal13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_13')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_23')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round06_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1306, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2306, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal14(self.ctx)


class GoToPortal14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12, key='FindWay', value=1)
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_14')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_24')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[106,206])


initial_state = Wait
