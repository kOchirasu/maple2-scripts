""" trigger/02000378_bf/12_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='or_fi_struc_stonegate_A01_off') # StoneGate
        self.set_effect(trigger_ids=[5012]) # 12Round_BridgeApp
        self.set_effect(trigger_ids=[5013]) # Sound_StoneGate
        self.set_mesh(trigger_ids=[331200,331201,331202,331203,331204,331205,331206,331207,331208,331209,331210,331211,331212,331213,331214,331215,331216,331217,331218,331219,331220,331221,331222,331223,331224,331225,331226,331227,331228,331229,331230,331231,331232,331233,331234,331235,331236,331237,331238,331239,331240,331241,331242,331243,331244,331245,331246,331247,331248,331249,331250,331251,331252,331253,331254,331255,331256,331257,331258,331259,331260,331261,331262,331263,331264,331265,331266,331267,331268,331269,331270,331271,331272,331273,331274,331275,331276,331277]) # Stairs
        self.set_mesh(trigger_ids=[4032], visible=True) # RoundBarrier
        self.set_mesh(trigger_ids=[3012], visible=True) # CrystalOff
        self.set_mesh(trigger_ids=[3112]) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3012], visible=True) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3112]) # CrystalOn
        self.set_effect(trigger_ids=[5212]) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)
        self.set_agent(trigger_ids=[28120], visible=True)
        self.set_agent(trigger_ids=[28121], visible=True)
        self.set_agent(trigger_ids=[28122], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay') == 1:
            return MovingDelay01(self.ctx)


class MovingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907,908,909], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112,212], auto_target=False) # 연출용
        self.set_mesh(trigger_ids=[4032]) # RoundBarrier
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_112')
        self.move_npc(spawn_id=212, patrol_name='MS2PatrolData_212')
        self.set_dialogue(type=1, spawn_id=212, script='$02000378_BF__12_FINDWAY__0$', time=3, arg5=1) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=112, script='$02000378_BF__12_FINDWAY__1$', time=3, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round12_Start(self.ctx)


class Round12_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[112,212])
        self.spawn_monster(spawn_ids=[1012], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2012], auto_target=False) # 전투용 준타
        self.set_dialogue(type=1, spawn_id=1012, script='$02000378_BF__12_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=912, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='12RoundSuccess') == 1:
            return Round12_Sucess01(self.ctx)


# 20170223 업데이트 던전 개편 단축
class Round12_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9012, spawn_ids=[2212]):
            return Round12_Sucess02(self.ctx)


class Round12_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2212, patrol_name='MS2PatrolData_2012')
        self.destroy_monster(spawn_ids=[1012])
        self.spawn_monster(spawn_ids=[113], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3012], start_delay=100) # CrystalOff
        self.set_mesh(trigger_ids=[3112], visible=True) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3012]) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3112], visible=True) # CrystalOn
        self.set_effect(trigger_ids=[5212], visible=True) # Sound_CrystalOn
        self.set_agent(trigger_ids=[28120])
        self.set_agent(trigger_ids=[28121])
        self.set_agent(trigger_ids=[28122])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round12_RouteSelect(self.ctx)


class Round12_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2213,2212])
        self.spawn_monster(spawn_ids=[213], auto_target=False) # 연출용 준타
        self.set_dialogue(type=1, spawn_id=113, script='$02000378_BF__12_FINDWAY__3$', time=3) # 틴차이
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_199')
        self.move_npc(spawn_id=213, patrol_name='MS2PatrolData_299')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Round12_RouteApp01(self.ctx)


class Round12_RouteApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5012], visible=True) # 12Round_BridgeApp
        self.set_random_mesh(trigger_ids=[331200,331201,331202,331203,331204,331205,331206,331207,331208,331209,331210,331211,331212,331213,331214,331215,331216,331217,331218,331219,331220,331221,331222,331223,331224,331225,331226,331227,331228,331229,331230,331231,331232,331233,331234,331235,331236,331237,331238,331239,331240,331241,331242,331243,331244,331245,331246,331247,331248,331249,331250,331251,331252,331253,331254,331255,331256,331257,331258,331259,331260,331261,331262,331263,331264,331265,331266,331267,331268,331269,331270,331271,331272,331273,331274,331275,331276,331277], visible=True, start_delay=78, interval=100, fade=30) # Stairs
        self.destroy_monster(spawn_ids=[907,908,909])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round12_RouteApp02(self.ctx)


class Round12_RouteApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5013]) # Sound_StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Round12_RouteApp03(self.ctx)


class Round12_RouteApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='or_fi_struc_stonegate_A01_on') # StoneGate
        self.set_portal(portal_id=2, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9013, spawn_ids=[213]):
            return GoToNextMap01(self.ctx)


class GoToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToNextMap02(self.ctx)


class GoToNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
