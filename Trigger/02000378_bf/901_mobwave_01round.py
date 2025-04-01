""" trigger/02000378_bf/901_mobwave_01round.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5101]) # 01Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWaveStart') == 1:
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__901_MOBWAVE_01ROUND__0$', duration=6000, box_ids=['0'])
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5101], visible=True) # 01Round_ShadowApp
        self.spawn_monster(spawn_ids=[90100,90102,90104], auto_target=False) # ,90106,90108

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90101,90103,90105], auto_target=False) # 90107,90109

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return FirstWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return FirstWaveDelay4000(self.ctx)
        if self.random_condition(weight=30.0):
            return FirstWaveDelay5000(self.ctx)


class FirstWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90110,90112,90114], auto_target=False) # ,90116,90118

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90111,90113,90115], auto_target=False) # ,90117,90119

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return SecondWaveDelay2000(self.ctx)
        if self.random_condition(weight=30.0):
            return SecondWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return SecondWaveDelay4000(self.ctx)


class SecondWaveDelay2000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90120,90122,90124], auto_target=False) # ,90126,90128

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90131,90133,90135], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)


"""
class ThirdWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90121,90123,90125], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay4000(self.ctx)
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay5000(self.ctx)
"""

"""
class ThirdWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class ThirdWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class ThirdWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FourthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=4)
        self.spawn_monster(spawn_ids=[90130,90132,90134], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FourthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90131,90133,90135], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return NpcDownPenaltyStart(self.ctx)
"""

class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90190,90192,90194], auto_target=False) # ,90196,90198

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90191,90193,90195], auto_target=False) # ,90197,90199

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90100,90101,90102,90103,90104,90105,90106,90107,90108,90109,90110,90111,90112,90113,90114,90115,90116,90117,90118,90119,90120,90121,90122,90123,90124,90125,90126,90127,90128,90129,90130,90131,90132,90133,90134,90135,90136,90137,90138,90139,90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # 01Round_ShadowApp
        self.set_user_value(trigger_id=1, key='01RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=801, key='PenaltyMob', value=1)
        self.destroy_monster(spawn_ids=[1001]) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[1101], auto_target=False) # 쓰러진 틴차이
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__901_MOBWAVE_01ROUND__1$', duration=4000, box_ids=['0'])
        self.set_dialogue(type=1, spawn_id=1101, script='$02000378_BF__901_MOBWAVE_01ROUND__2$', time=4, arg5=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyFinish') == 1:
            return ReturnToWave(self.ctx)


class ReturnToWave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__901_MOBWAVE_01ROUND__3$', duration=4000, box_ids=['0'])
        self.destroy_monster(spawn_ids=[1101]) # 쓰러진 틴차이
        self.spawn_monster(spawn_ids=[1001], auto_target=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawn_id=1101)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveTime') == 1:
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime') == 2:
            return ThirdWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime') == 4:
            return FifthWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime') == 3:
            return FifthWaveStart(self.ctx)
        if self.user_value(key='WaveTime') == 5:
            return FifthWaveStart(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
