""" trigger/02000378_bf/903_mobwave_03round.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5103]) # 03Round_ShadowApp

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
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__903_MOBWAVE_03ROUND__0$', duration=6000, box_ids=['0'])
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5103], visible=True) # 03Round_ShadowApp
        self.spawn_monster(spawn_ids=[90300,90302,90304], auto_target=False) # ,90306,90308

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90301,90303,90305], auto_target=False) # ,90307,90309

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
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90310,90312,90314], auto_target=False) # ,90316,90318

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90311,90313,90315], auto_target=False) # ,90317,90319

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return SecondWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(weight=30.0):
            return SecondWaveDelay5000(self.ctx)


class SecondWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(trigger_id=703, key='TotemApp', value=1)
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return ThirdWaveDirectionRandom(self.ctx)


class ThirdWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection10(self.ctx)
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection20(self.ctx)
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection30(self.ctx)
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection40(self.ctx)
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection50(self.ctx)
        if self.random_condition(weight=20.0):
            return ThirdWaveDirection60(self.ctx)


# 왼쪽 위
class ThirdWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90320,90322,90324], auto_target=False) # ,90326,90328

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90321,90323,90325], auto_target=False) # ,90327,90329

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class ThirdWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90330,90332,90334], auto_target=False) # ,90336,90338

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90331,90333,90335], auto_target=False) # ,90337,90339

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class ThirdWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90340,90342,90344], auto_target=False) # ,90346,90348

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90341,90343,90345], auto_target=False) # ,90347,90349

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class ThirdWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90350,90352,90354], auto_target=False) # ,90356,90358

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90351,90353,90355], auto_target=False) # ,90357,90359

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class ThirdWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90360,90362,90364], auto_target=False) # ,90366,90368

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90361,90363,90365], auto_target=False) # ,90367,90369

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class ThirdWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90370,90372,90374], auto_target=False) # ,90376,90378

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90371,90373,90375], auto_target=False) # ,90377,90379

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay4000(self.ctx)
        if self.random_condition(weight=30.0):
            return ThirdWaveDelay2000(self.ctx)


class ThirdWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay2000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return FourthWaveDirectionRandom(self.ctx)


class FourthWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return FourthWaveDirection10(self.ctx)
        if self.random_condition(weight=20.0):
            return FourthWaveDirection20(self.ctx)
        if self.random_condition(weight=20.0):
            return FourthWaveDirection30(self.ctx)
        if self.random_condition(weight=20.0):
            return FourthWaveDirection40(self.ctx)
        if self.random_condition(weight=20.0):
            return FourthWaveDirection50(self.ctx)
        if self.random_condition(weight=20.0):
            return FourthWaveDirection60(self.ctx)


# 왼쪽 위
class FourthWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90320,90322,90324], auto_target=False) # ,90326,90328

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90321,90323,90325], auto_target=False) # ,90327,90329

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FourthWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90330,90332,90334], auto_target=False) # ,90336,90338

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90331,90333,90335], auto_target=False) # ,90337,90339

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FourthWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90340,90342,90344], auto_target=False) # ,90346,90348

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90341,90343,90345], auto_target=False) # ,90347,90349

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FourthWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90350,90352,90354], auto_target=False) # ,90356,90358

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90351,90353,90355], auto_target=False) # ,90357,90359

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FourthWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90360,90362,90364], auto_target=False) # ,90366,90368

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90361,90363,90365], auto_target=False) # ,90367,90369

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FourthWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90370,90372,90374], auto_target=False) # ,90376,90378

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90371,90373,90375], auto_target=False) # ,90377,90379

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90320,90322,90324], auto_target=False) # ,90326,90328

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 20170223 업데이트 던전 개편 단축

"""
class FourthWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return FourthWaveDelay3000(self.ctx)
        if self.random_condition(weight=30.0):
            return FourthWaveDelay4000(self.ctx)
        if self.random_condition(weight=30.0):
            return FourthWaveDelay2000(self.ctx)
"""

"""
class FourthWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FourthWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FourthWaveDelay2000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return FifthWaveDirectionRandom(self.ctx)
"""

"""
class FifthWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return FifthWaveDirection10(self.ctx)
        if self.random_condition(weight=20.0):
            return FifthWaveDirection20(self.ctx)
        if self.random_condition(weight=20.0):
            return FifthWaveDirection30(self.ctx)
        if self.random_condition(weight=20.0):
            return FifthWaveDirection40(self.ctx)
        if self.random_condition(weight=20.0):
            return FifthWaveDirection50(self.ctx)
        if self.random_condition(weight=20.0):
            return FifthWaveDirection60(self.ctx)
"""

# 왼쪽 위

"""
class FifthWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90320,90322,90324], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90321,90323,90325], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

# 오른쪽 위

"""
class FifthWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90330,90332,90334], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90331,90333,90335], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

# 왼쪽 중앙

"""
class FifthWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90340,90342,90344], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90341,90343,90345], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

# 오른쪽 중앙

"""
class FifthWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90350,90352,90354], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90351,90353,90355], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

# 왼쪽 아래

"""
class FifthWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90360,90362,90364], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90361,90363,90365], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

# 오른쪽 아래

"""
class FifthWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90370,90372,90374], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

"""
class FifthWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90371,90373,90375], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return NpcDownPenaltyStart(self.ctx)
"""

class SixthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=6) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90390,90392,90394,90396,90398], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SixthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SixthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90391,90393,90395], auto_target=False) # ,90397,90399

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90300,90301,90302,90303,90304,90305,90306,90307,90308,90309,90310,90311,90312,90313,90314,90315,90316,90317,90318,90319,90320,90321,90322,90323,90324,90325,90326,90327,90328,90329,90330,90331,90332,90333,90334,90335,90336,90337,90338,90339,90340,90341,90342,90343,90344,90345,90346,90347,90348,90349,90350,90351,90352,90353,90354,90355,90356,90357,90358,90359,90360,90361,90362,90363,90364,90365,90366,90367,90368,90369,90370,90371,90372,90373,90374,90375,90376,90377,90378,90379,90380,90381,90382,90383,90384,90385,90386,90387,90388,90389,90390,90391,90392,90393,90394,90395,90396,90397,90398,90399]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5103]) # 03Round_ShadowApp
        self.set_user_value(trigger_id=3, key='03RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=803, key='PenaltyMob', value=1)
        self.destroy_monster(spawn_ids=[1003]) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[1103], auto_target=False) # 쓰러진 틴차이
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__903_MOBWAVE_03ROUND__1$', duration=4000, box_ids=['0'])
        self.set_dialogue(type=1, spawn_id=1103, script='$02000378_BF__903_MOBWAVE_03ROUND__2$', time=4, arg5=4) # 틴차이

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
        self.set_event_ui_script(type=BannerType.Text, script='$02000378_BF__903_MOBWAVE_03ROUND__3$', duration=4000, box_ids=['0'])
        self.destroy_monster(spawn_ids=[1103]) # 쓰러진 틴차이
        self.spawn_monster(spawn_ids=[1003], auto_target=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawn_id=1103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveTime') == 1:
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime') == 2:
            return ThirdWaveStart(self.ctx)
        if self.user_value(key='WaveTime') == 3:
            return FourthWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime') == 5:
            return SixthWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime') == 4:
            return SixthWaveStart(self.ctx)
        if self.user_value(key='WaveTime') == 6:
            return SixthWaveStart(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
