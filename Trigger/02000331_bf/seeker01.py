""" trigger/02000331_bf/seeker01.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[11000]) # 입구로 되돌아 가는 길 막기
        self.set_agent(trigger_ids=[11001]) # 입구로 되돌아 가는 길 막기
        self.set_agent(trigger_ids=[13001], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[13002], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[13003], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[13004], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[13005], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[13006], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(trigger_ids=[15000]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15001]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15002]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[16000]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16001]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16002]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16003]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16004]) # 새로운 다리 길 막기
        self.set_mesh(trigger_ids=[90000]) # 1st barrier ON
        self.set_mesh(trigger_ids=[90001]) # 2st barrier OFF
        self.set_mesh(trigger_ids=[90002], visible=True) # 3rd barrier ON
        self.set_mesh(trigger_ids=[90003], visible=True) # 4th barrier ON
        self.set_mesh(trigger_ids=[90004], visible=True) # 5th barrier ON
        self.set_mesh(trigger_ids=[90005], visible=True) # 6th barrier ON
        self.set_mesh(trigger_ids=[90006], visible=True) # 7th barrier ON
        self.set_mesh(trigger_ids=[90007], visible=True) # 8th barrier ON
        self.set_mesh(trigger_ids=[90008], visible=True) # 9th barrier ON
        self.set_mesh(trigger_ids=[98880], visible=True) # 마지막꼬마 CAGE 메시 켜기
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # EnterDoor
        self.set_mesh(trigger_ids=[89999], visible=True) # EnterDoorInvisibleBlock
        self.set_actor(trigger_id=92220, visible=True, initial_sequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(trigger_id=92221, visible=True, initial_sequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(trigger_id=92222, visible=True, initial_sequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(trigger_id=92223, visible=True, initial_sequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(trigger_id=92224, visible=True, initial_sequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(trigger_id=93330, visible=True, initial_sequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(trigger_id=93331, visible=True, initial_sequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(trigger_id=93332, visible=True, initial_sequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(trigger_id=93333, visible=True, initial_sequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(trigger_id=93334, visible=True, initial_sequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(trigger_id=94440, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94441, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94442, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94443, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94444, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94445, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94446, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94447, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94448, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94449, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94450, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94451, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94452, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94453, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=94454, visible=True, initial_sequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(trigger_id=96660, visible=True, initial_sequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(trigger_id=96661, visible=True, initial_sequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(trigger_id=96662, visible=True, initial_sequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(trigger_id=96663, visible=True, initial_sequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(trigger_id=96664, visible=True, initial_sequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(trigger_id=97770, visible=True, initial_sequence='Closed') # 마지막꼬마 CAGE 액터 보여주기
        self.set_mesh(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], visible=True) # 1st bridge ON
        self.set_mesh(trigger_ids=[10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033], visible=True) # 2nd bridge ON
        self.set_mesh(trigger_ids=[10040,10041,10042,10043,10044]) # 3rd bridge OFF
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]) # 1st 꼬마01 Hint OFF
        self.set_mesh(trigger_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117]) # 1st 꼬마02 Hint OFF
        self.set_mesh(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220]) # 1st 꼬마03 Hint OFF
        self.set_mesh(trigger_ids=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315]) # 1st 꼬마04 Hint OFF
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018]) # 2nd Hint OFF
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116]) # 2nd Hint OFF
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221]) # 2nd Hint OFF
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318]) # 2nd Hint OFF
        self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419]) # 2nd Hint OFF
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008]) # 3rd Hint OFF
        self.set_mesh(trigger_ids=[90090,90091,90092,90093,90094,90095,90096,90097,90098,90099], visible=True) # 클리어포털감춤
        self.set_interact_object(trigger_ids=[10000766], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(trigger_ids=[10000767], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(trigger_ids=[10000768], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(trigger_ids=[10000769], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(trigger_ids=[10000771], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(trigger_ids=[10000772], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(trigger_ids=[10000773], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(trigger_ids=[10000774], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(trigger_ids=[10000775], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(trigger_ids=[10000784], state=2) # 발판내리기 레버 감춤 랜덤01
        self.set_interact_object(trigger_ids=[10000792], state=2) # 발판내리기 레버 감춤 랜덤02
        self.set_interact_object(trigger_ids=[10000793], state=2) # 발판내리기 레버 감춤 랜덤03
        self.set_interact_object(trigger_ids=[10000794], state=2) # 발판내리기 레버 감춤 랜덤04
        self.set_interact_object(trigger_ids=[10000795], state=2) # 발판내리기 레버 감춤 랜덤05
        self.set_interact_object(trigger_ids=[10000785], state=2) # 외다리 생성하는 레버 감춤 랜덤01
        self.set_interact_object(trigger_ids=[10000796], state=2) # 외다리 생성하는 레버 감춤 랜덤02
        self.set_interact_object(trigger_ids=[10000797], state=2) # 외다리 생성하는 레버 감춤 랜덤03
        self.set_interact_object(trigger_ids=[10000798], state=2) # 외다리 생성하는 레버 감춤 랜덤04
        self.set_interact_object(trigger_ids=[10000799], state=2) # 외다리 생성하는 레버 감춤 랜덤05
        self.set_interact_object(trigger_ids=[10000776], state=2) # 열 수 있는 철창 감춤
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.spawn_monster(spawn_ids=[610], auto_target=False)
        self.set_effect(trigger_ids=[99999]) # 치유 이펙트
        self.set_effect(trigger_ids=[7771]) # UI  메시지 알림 사운드
        self.set_effect(trigger_ids=[7772]) # 치유 스킬 이펙트 사운드
        self.set_effect(trigger_ids=[777401]) # 덤불 제거01 사운드
        self.set_effect(trigger_ids=[777402]) # 덤불 제거02 사운드
        self.set_effect(trigger_ids=[777403]) # 덤불 제거03 사운드
        self.set_effect(trigger_ids=[777404]) # 덤불 제거04 사운드
        self.set_effect(trigger_ids=[777405]) # 덤불 제거05 사운드
        self.set_effect(trigger_ids=[777501]) # 발자국 나타남01 사운드
        self.set_effect(trigger_ids=[777502]) # 발자국 나타남02 사운드
        self.set_effect(trigger_ids=[7776]) # 추격 소음01 사운드
        self.set_effect(trigger_ids=[777701]) # 길 나타남01 사운드 / 첫 번째 다리
        self.set_effect(trigger_ids=[777702]) # 길 나타남02 사운드 / 외다리
        self.set_effect(trigger_ids=[777801]) # 길 없어짐01 사운드  / 첫 번째 다리
        self.set_effect(trigger_ids=[777802]) # 길 없어짐02 사운드 /  외다리
        self.set_effect(trigger_ids=[777803]) # 길 없어짐02 사운드 / 막힌 길
        self.set_effect(trigger_ids=[777901]) # KaseMu Voice01
        self.set_effect(trigger_ids=[777902]) # KaseMu Voice02
        self.set_effect(trigger_ids=[777903]) # KaseMu Voice03
        self.set_effect(trigger_ids=[777904]) # KaseMu Voice04
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Opened') # EnterDoor
        self.set_mesh(trigger_ids=[89999]) # EnterDoorInvisibleBlock

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선01(self.ctx)


class 술래말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__0$', time=2)
        self.set_mesh(trigger_ids=[90000]) # 1st barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 술래패트롤01(self.ctx)


class 술래패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003311, text_id=20003311) # 가이드 : 메린이를 따라가 보세요.
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9002, spawn_ids=[100]):
            return 몬스터출현01_시작(self.ctx)


class 몬스터출현01_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='Opened') # EnterDoor
        self.hide_guide_summary(entity_id=20003311)
        self.spawn_monster(spawn_ids=[900], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현01_연출01(self.ctx)


class 몬스터출현01_연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            return 몬스터출현01_연출02(self.ctx)


class 몬스터출현01_연출02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 몬스터출현01_생성랜덤01(self.ctx)


class 몬스터출현01_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현01_1번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_2번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_3번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_4번생성(self.ctx)


class 몬스터출현01_1번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902], auto_target=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_2번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902,904], auto_target=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_3번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[903,905], auto_target=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_4번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,905], auto_target=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현01_5번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_6번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_7번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_8번생성(self.ctx)


class 몬스터출현01_5번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[905,906,907], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_6번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[906,907,909], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_7번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907,909,910], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_8번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907,908,909], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현01_9번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_10번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_11번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현01_12번생성(self.ctx)


class 몬스터출현01_9번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_10번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902,903,904], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_11번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,904,905], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_12번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[903,904,905], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째다리붕괴01(self.ctx)


class 첫번째다리붕괴01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[11000], visible=True)
        self.set_agent(trigger_ids=[11001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99990]):
            return 첫번째무너짐연출시작01(self.ctx)


class 첫번째무너짐연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__900$')
        self.select_camera(trigger_id=802)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_999')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째다리붕괴02(self.ctx)


class 첫번째다리붕괴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], start_delay=16, interval=100, fade=100)
        self.set_effect(trigger_ids=[777801], visible=True) # 길 없어짐01 사운드  / 첫 번째 다리
        self.set_mesh(trigger_ids=[90001], visible=True) # 2st barrier ON
        self.set_mesh(trigger_ids=[90000], visible=True) # 1st barrier ON
        self.set_skip(state=첫번째무너짐연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째무너짐연출종료01(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=18, key='clearafter', value=1)


class 첫번째무너짐연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[777801]) # 길 없어짐01 사운드  / 첫 번째 다리
        self.select_camera(trigger_id=802, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선02(self.ctx)


class 술래말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=16, key='FirstBridgeOff', value=1)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__3$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__4$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 술래패트롤02(self.ctx)


class 술래패트롤02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__5$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__24$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[91002], auto_target=False) # 첫 번째 꽃덤불 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째덤불등장01(self.ctx)


class 첫번째덤불등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.show_guide_summary(entity_id=20003312, text_id=20003312)
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91002]):
            # 첫 번째 꽃덤불 제거
            return 첫번째덤불제거01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[777401], visible=True) # 덤불 제거01 사운드
        self.hide_guide_summary(entity_id=20003312)


class 첫번째덤불제거01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=92220, visible=True, initial_sequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(trigger_ids=[90002]) # 1st barrier OFF
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째꼬마찾기시작(self.ctx)


class 첫번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=92000, initial_sequence='Dead_A') # 첫번째장벽 덤불
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9003, spawn_ids=[100]):
            return 첫번째꼬마랜덤(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=92220, initial_sequence='Dead_A') # 첫번째장벽 덤불 제거
        self.set_effect(trigger_ids=[777401]) # 덤불 제거01 사운드


class 첫번째꼬마랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 첫번째힌트발견01(self.ctx) # 10000766, 201
        if self.random_condition(weight=25.0):
            return 첫번째힌트발견02(self.ctx) # 10000767, 202
        if self.random_condition(weight=25.0):
            return 첫번째힌트발견03(self.ctx) # 10000768, 203
        if self.random_condition(weight=25.0):
            return 첫번째힌트발견04(self.ctx) # 10000769, 204


# 첫번째힌트발견01 - 110000766, 201
class 첫번째힌트발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True, start_delay=16, interval=100, fade=100) # 1st Hint ON
        self.set_effect(trigger_ids=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(trigger_ids=[10000766], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 첫번째힌트수색01(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 첫번째힌트수색01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000766], state=0):
            return 첫번째꼬마발견01(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000766], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 첫번째꼬마발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.set_dialogue(type=1, spawn_id=201, script='$02000331_BF__Seeker01__11$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째꼬마만남01(self.ctx)


class 첫번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__12$', time=2, arg5=1)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[201]):
            return 첫번째꼬마교체딜레이01(self.ctx)


class 첫번째꼬마교체딜레이01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째꼬마교체01(self.ctx)


class 첫번째꼬마교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=201, to_spawn_id=200)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_998')
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__13$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__14$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9012, spawn_ids=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견02 - 110000767, 202
class 첫번째힌트발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(trigger_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117], visible=True, start_delay=17, interval=100, fade=100) # 1st Hint ON
        self.set_effect(trigger_ids=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(trigger_ids=[10000767], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 첫번째힌트수색02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 첫번째힌트수색02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000767], state=0):
            return 첫번째꼬마발견02(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000767], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 첫번째꼬마발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.set_dialogue(type=1, spawn_id=202, script='$02000331_BF__Seeker01__15$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째꼬마만남02(self.ctx)


class 첫번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__12$', time=2, arg5=1)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[202]):
            return 첫번째꼬마교체딜레이02(self.ctx)


class 첫번째꼬마교체딜레이02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째꼬마교체02(self.ctx)


class 첫번째꼬마교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=202, to_spawn_id=200)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_998')
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__18$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__19$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9012, spawn_ids=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견03 - 10000768, 203
class 첫번째힌트발견03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True, start_delay=20, interval=100, fade=100) # 1st Hint ON
        self.set_effect(trigger_ids=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(trigger_ids=[10000768], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 첫번째힌트수색03(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 첫번째힌트수색03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000768], state=0):
            return 첫번째꼬마발견03(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000768], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 첫번째꼬마발견03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.set_dialogue(type=1, spawn_id=203, script='$02000331_BF__Seeker01__16$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째꼬마만남03(self.ctx)


class 첫번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__12$', time=2, arg5=1)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_2203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[203]):
            return 첫번째꼬마교체딜레이03(self.ctx)


class 첫번째꼬마교체딜레이03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째꼬마교체03(self.ctx)


class 첫번째꼬마교체03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=203, to_spawn_id=200)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_998')
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__20$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__21$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9012, spawn_ids=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견04 - 10000769, 204
class 첫번째힌트발견04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(trigger_ids=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315], visible=True, start_delay=15, interval=100, fade=100) # 1st Hint ON
        self.set_effect(trigger_ids=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(trigger_ids=[10000769], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 첫번째힌트수색04(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 첫번째힌트수색04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000769], state=0):
            return 첫번째꼬마발견04(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000769], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 첫번째꼬마발견04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.set_dialogue(type=1, spawn_id=204, script='$02000331_BF__Seeker01__17$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫번째꼬마만남04(self.ctx)


class 첫번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__12$', time=2, arg5=1)
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_2204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[204]):
            return 첫번째꼬마교체딜레이04(self.ctx)


class 첫번째꼬마교체딜레이04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째꼬마교체04(self.ctx)


class 첫번째꼬마교체04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=204, to_spawn_id=200)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_998')
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__22$', time=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__23$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9012, spawn_ids=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


"""
첫번째 꼬마 찾기 랜덤 스테이트 종료
두번째 꼬마 찾기 전에 전투용 몬스터 미리 스폰
"""
class 몬스터출현02_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현02_1번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현02_2번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현02_3번생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현02_4번생성(self.ctx)


class 몬스터출현02_1번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[9223,9224,9225,921,922,924,925,927,928], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 두명패트롤01(self.ctx)


class 몬스터출현02_2번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[9221,9223,9225,920,922,924,925,926,929], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 두명패트롤01(self.ctx)


class 몬스터출현02_3번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[9221,9222,9224,920,922,924,925,926,928], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 두명패트롤01(self.ctx)


class 몬스터출현02_4번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[9222,9223,9225,922,923,925,926,927,929], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 두명패트롤01(self.ctx)


class 두명패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1003')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9016, spawn_ids=[100]):
            return 두번째덤불등장01(self.ctx)


class 두번째덤불등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.show_guide_summary(entity_id=20003312, text_id=20003312)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__24$', time=3)
        self.spawn_monster(spawn_ids=[91003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91003]):
            # 첫 번째 꽃덤불 제거
            return 두번째덤불제거01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003312)
        self.set_effect(trigger_ids=[777402], visible=True) # 덤불 제거02 사운드


class 두번째덤불제거01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=93330, visible=True, initial_sequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(trigger_ids=[90003]) # 4th barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째꼬마찾기시작(self.ctx)


class 두번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__25$', time=3)
        self.set_effect(trigger_ids=[777402]) # 덤불 제거02 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1004')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9005, spawn_ids=[100]):
            return 두번째몬스터발견01(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=93330, initial_sequence='Dead_A') # 첫번째장벽 덤불


class 두번째몬스터발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__30$', time=2)
        self.set_agent(trigger_ids=[13001]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(trigger_ids=[13002]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(trigger_ids=[13003]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(trigger_ids=[13004]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(trigger_ids=[13005]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(trigger_ids=[13006]) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__31$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[9221,9222,9223,9224,9225,920,921,922,923,924,925,926,927,928,929]):
            return 두번째꼬마랜덤(self.ctx)


class 두번째꼬마랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 두번째힌트발견01(self.ctx) # 10000771, 301, 311
        if self.random_condition(weight=20.0):
            return 두번째힌트발견02(self.ctx) # 10000772, 302, 312
        if self.random_condition(weight=20.0):
            return 두번째힌트발견03(self.ctx) # 10000773, 303, 313
        if self.random_condition(weight=20.0):
            return 두번째힌트발견04(self.ctx) # 10000774, 304, 314
        if self.random_condition(weight=20.0):
            return 두번째힌트발견05(self.ctx) # 100007775, 305, 315


# 두번째힌트발견01 - 10000771, 301, 311
class 두번째힌트발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_997')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2013')
        self.set_random_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018], visible=True, start_delay=18, interval=50, fade=50) # 2nd Hint ON
        self.set_effect(trigger_ids=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 두번째힌트수색01(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 두번째힌트수색01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[311], auto_target=False)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9301]):
            return 두번째꼬마도움01(self.ctx)


class 두번째꼬마도움01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=311, script='$02000331_BF__Seeker01__33$', time=2)
        self.set_interact_object(trigger_ids=[10000771], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마발견01(self.ctx)


class 두번째꼬마발견01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000771], state=0):
            return 두번째꼬마구출01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003313)
        self.set_interact_object(trigger_ids=[10000771], state=2)


class 두번째꼬마구출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=311, to_spawn_id=301)
        self.set_dialogue(type=1, spawn_id=301, script='$02000331_BF__Seeker01__38$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째꼬마이동01(self.ctx)


class 두번째꼬마이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마만남01(self.ctx)


class 두번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$02000331_BF__Seeker01__39$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마대화01(self.ctx)


class 두번째꼬마대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__40$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[301]):
            return 두번째꼬마교체딜레이01(self.ctx)


class 두번째꼬마교체딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__41$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째꼬마교체01(self.ctx)


class 두번째꼬마교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=301, to_spawn_id=300)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_996')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__42$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견02 - 10000772, 302, 312
class 두번째힌트발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_997')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2013')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, start_delay=16, interval=50, fade=50) # 2nd Hint ON
        self.set_effect(trigger_ids=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 두번째힌트수색02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 두번째힌트수색02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[312], auto_target=False)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9302]):
            return 두번째꼬마도움02(self.ctx)


class 두번째꼬마도움02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=312, script='$02000331_BF__Seeker01__34$', time=2)
        self.set_interact_object(trigger_ids=[10000772], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마발견02(self.ctx)


class 두번째꼬마발견02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000772], state=0):
            return 두번째꼬마구출02(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000772], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 두번째꼬마구출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=312, to_spawn_id=302)
        self.set_dialogue(type=1, spawn_id=302, script='$02000331_BF__Seeker01__43$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째꼬마이동02(self.ctx)


class 두번째꼬마이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마만남02(self.ctx)


class 두번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=302, script='$02000331_BF__Seeker01__44$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마대화02(self.ctx)


class 두번째꼬마대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__45$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[302]):
            return 두번째꼬마교체딜레이02(self.ctx)


class 두번째꼬마교체딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__46$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째꼬마교체02(self.ctx)


class 두번째꼬마교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=302, to_spawn_id=300)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_996')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__47$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견03 - 10000773, 303, 313
class 두번째힌트발견03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_997')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2013')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=True, start_delay=21, interval=50, fade=50) # 2nd Hint ON
        self.set_effect(trigger_ids=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 두번째힌트수색03(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 두번째힌트수색03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[313], auto_target=False)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9303]):
            return 두번째꼬마도움03(self.ctx)


class 두번째꼬마도움03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=313, script='$02000331_BF__Seeker01__35$', time=2)
        self.set_interact_object(trigger_ids=[10000773], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마발견03(self.ctx)


class 두번째꼬마발견03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000773], state=0):
            return 두번째꼬마구출03(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000773], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 두번째꼬마구출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=313, to_spawn_id=303)
        self.set_dialogue(type=1, spawn_id=303, script='$02000331_BF__Seeker01__48$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째꼬마이동03(self.ctx)


class 두번째꼬마이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_3303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마만남03(self.ctx)


class 두번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=303, script='$02000331_BF__Seeker01__49$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마대화03(self.ctx)


class 두번째꼬마대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__50$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[303]):
            return 두번째꼬마교체딜레이03(self.ctx)


class 두번째꼬마교체딜레이03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__51$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마교체03(self.ctx)


class 두번째꼬마교체03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=303, to_spawn_id=300)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_996')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__52$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견04 - 10000774, 304, 314
class 두번째힌트발견04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_997')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2013')
        self.set_random_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318], visible=True, start_delay=18, interval=50, fade=50) # 2nd Hint ON
        self.set_effect(trigger_ids=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 두번째힌트수색04(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 두번째힌트수색04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[314], auto_target=False)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9304]):
            return 두번째꼬마도움04(self.ctx)


class 두번째꼬마도움04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000774], state=1)
        self.set_dialogue(type=1, spawn_id=314, script='$02000331_BF__Seeker01__36$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마발견04(self.ctx)


class 두번째꼬마발견04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000774], state=0):
            return 두번째꼬마구출04(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000774], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 두번째꼬마구출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=314, to_spawn_id=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마이동04(self.ctx)


class 두번째꼬마이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=304, patrol_name='MS2PatrolData_3304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마만남04(self.ctx)


class 두번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=304, script='$02000331_BF__Seeker01__54$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마대화04(self.ctx)


class 두번째꼬마대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__55$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[304]):
            return 두번째꼬마교체딜레이04(self.ctx)


class 두번째꼬마교체딜레이04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__56$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째꼬마교체04(self.ctx)


class 두번째꼬마교체04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=304, to_spawn_id=300)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_996')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__57$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견05 - 10000775, 305, 315
class 두번째힌트발견05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_997')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2013')
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419], visible=True, start_delay=19, interval=50, fade=50) # 2nd Hint ON
        self.set_effect(trigger_ids=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 두번째힌트수색05(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.
        self.show_guide_summary(entity_id=20003313, text_id=20003313)


class 두번째힌트수색05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[315], auto_target=False)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9305]):
            return 두번째꼬마도움05(self.ctx)


class 두번째꼬마도움05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000775], state=1)
        self.set_dialogue(type=1, spawn_id=315, script='$02000331_BF__Seeker01__37$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 두번째꼬마발견05(self.ctx)


class 두번째꼬마발견05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000775], state=0):
            return 두번째꼬마구출05(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000775], state=2)
        self.hide_guide_summary(entity_id=20003313)


class 두번째꼬마구출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=315, to_spawn_id=305)
        self.set_dialogue(type=1, spawn_id=305, script='$02000331_BF__Seeker01__58$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마이동05(self.ctx)


class 두번째꼬마이동05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_3305')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마만남05(self.ctx)


class 두번째꼬마만남05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=305, script='$02000331_BF__Seeker01__59$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째꼬마대화05(self.ctx)


class 두번째꼬마대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__60$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[305]):
            return 두번째꼬마교체딜레이05(self.ctx)


class 두번째꼬마교체딜레이05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__61$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째꼬마교체05(self.ctx)


class 두번째꼬마교체05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=305, to_spawn_id=300)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_996')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__62$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[100]):
            return 세명패트롤01(self.ctx)


# 두번째 꼬마 찾기 랜덤 스테이트 종료
class 세명패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1005')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9008, spawn_ids=[100]):
            return 세명패트롤02(self.ctx)


class 세명패트롤02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__70$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세번째덤불등장01(self.ctx)


# 세명 패트롤 하다가 덩굴에 막힘
class 세번째덤불등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.show_guide_summary(entity_id=20003312, text_id=20003312)
        self.spawn_monster(spawn_ids=[91004], auto_target=False) # 3다시1 꽃덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91004]):
            # 3다시1 꽃덤불 제거
            return 세번째덤불등장02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[777403], visible=True) # 덤불 제거03 사운드


class 세번째덤불등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1006')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2005')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3003')
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__71$', time=2)
        self.spawn_monster(spawn_ids=[91005], auto_target=False) # 3다시2 꽃덤불
        self.set_mesh(trigger_ids=[90004]) # 4th barrier OFF
        self.set_actor(trigger_id=94440, visible=True, initial_sequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91005]):
            # 3다시2 꽃덤불 제거
            return 세번째덤불등장03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003312)
        self.set_effect(trigger_ids=[777404], visible=True) # 덤불 제거04 사운드


class 세번째덤불등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__72$', time=2)
        self.set_mesh(trigger_ids=[90005]) # 5th barrier OFF
        self.set_actor(trigger_id=94450, visible=True, initial_sequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세번째꼬마찾기시작(self.ctx)


class 세번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[777403]) # 덤불 제거03 사운드
        self.set_effect(trigger_ids=[777404]) # 덤불 제거04 사운드
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__73$', time=2)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1016')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2015')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3013')
        self.set_actor(trigger_id=94440, initial_sequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 꼬마셋대화연출01(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=94450, initial_sequence='Dead_A') # 첫번째장벽 덤불


class 꼬마셋대화연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__74$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세명패트롤03(self.ctx)


class 세명패트롤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9009, spawn_ids=[100]):
            return 세번째스위치랜덤(self.ctx)


# 고립된 세번째 꼬마 발견, 세번째스위치 랜덤
class 세번째스위치랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 세번째스위치출현01(self.ctx) # 세번째스위치01 - 10000784
        if self.random_condition(weight=20.0):
            return 세번째스위치출현02(self.ctx) # 세번째스위치02 - 10000792
        if self.random_condition(weight=20.0):
            return 세번째스위치출현03(self.ctx) # 세번째스위치03 - 10000793
        if self.random_condition(weight=20.0):
            return 세번째스위치출현04(self.ctx) # 세번째스위치04 - 10000794
        if self.random_condition(weight=20.0):
            return 세번째스위치출현05(self.ctx) # 세번째스위치05 - 10000795


# 세번째스위치01 - 10000784
class 세번째스위치출현01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000784], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 고립연출시작01(self.ctx)


class 고립연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(trigger_id=804)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 고립연출종료01(self.ctx)


class 고립연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내01_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구출안내01_01(self.ctx)


class 구출안내01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구출안내01_02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)


class 구출안내01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__80$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내01_03(self.ctx)


class 구출안내01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__81$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내01_04(self.ctx)


class 구출안내01_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__82$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000784], state=0):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 세번째스위치02 - 10000792
class 세번째스위치출현02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000792], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 고립연출시작02(self.ctx)


class 고립연출시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(trigger_id=804)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 고립연출종료02(self.ctx)


class 고립연출종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내02_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구출안내02_01(self.ctx)


class 구출안내02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구출안내02_02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)


class 구출안내02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__80$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내02_03(self.ctx)


class 구출안내02_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__81$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내02_04(self.ctx)


class 구출안내02_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__82$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000792], state=0):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 세번째스위치03 - 10000793
class 세번째스위치출현03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000793], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 고립연출시작03(self.ctx)


class 고립연출시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(trigger_id=804)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 고립연출종료03(self.ctx)


class 고립연출종료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내03_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구출안내03_01(self.ctx)


class 구출안내03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구출안내03_02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)


class 구출안내03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__80$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내03_03(self.ctx)


class 구출안내03_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__81$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내03_04(self.ctx)


class 구출안내03_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__82$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000793], state=0):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 세번째스위치04 - 10000794
class 세번째스위치출현04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000794], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 고립연출시작04(self.ctx)


class 고립연출시작04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(trigger_id=804)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 고립연출종료04(self.ctx)


class 고립연출종료04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내04_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구출안내04_01(self.ctx)


class 구출안내04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구출안내04_02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)


class 구출안내04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__80$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내04_03(self.ctx)


class 구출안내04_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__81$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내04_04(self.ctx)


class 구출안내04_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__82$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000794], state=0):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 세번째스위치05 - 10000795
class 세번째스위치출현05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000795], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 고립연출시작05(self.ctx)


class 고립연출시작05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(trigger_id=804)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 고립연출종료05(self.ctx)


class 고립연출종료05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내05_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구출안내05_01(self.ctx)


class 구출안내05_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 구출안내05_02(self.ctx)

    def on_exit(self) -> None:
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)


class 구출안내05_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__80$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내05_03(self.ctx)


class 구출안내05_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__81$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구출안내05_04(self.ctx)


class 구출안내05_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__82$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000795], state=0):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=401, to_spawn_id=400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 세번째꼬마탈출(self.ctx)


class 세번째꼬마탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=400, script='$02000331_BF__Seeker01__83$', time=2)
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9010, spawn_ids=[400]):
            return 세번째꼬마만남01(self.ctx)


class 세번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1008')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2007')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3005')
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__84$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째꼬마만남02(self.ctx)


class 세번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=400, script='$02000331_BF__Seeker01__85$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세번째꼬마만남03(self.ctx)


class 세번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__86$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 네명패트롤01(self.ctx)


# 고립된 세번째 꼬마 구출 완료
class 네명패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__87$', time=2)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9011, spawn_ids=[100]):
            return 네명패트롤02(self.ctx)


class 네명패트롤02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2008')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3006')
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4002')
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__88$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9017, spawn_ids=[100]):
            return 네번째덤불등장01(self.ctx)


# 네명 패트롤 하다가 세번째 덩굴에 막힘
class 네번째덤불등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.show_guide_summary(entity_id=20003312, text_id=20003312)
        self.spawn_monster(spawn_ids=[91006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91006]):
            # 네 번째 꽃덤불 제거
            return 네번째덤불제거01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003312)
        self.set_effect(trigger_ids=[777405], visible=True) # 덤불 제거05 사운드


class 네번째덤불제거01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=96660, visible=True, initial_sequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(trigger_ids=[90006]) # 7th barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 네번째꼬마찾기시작(self.ctx)


class 네번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='401', seconds=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__89$', time=2)
        self.set_effect(trigger_ids=[777405]) # 덤불 제거05 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1010')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2009')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3007')
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4003')
        self.set_actor(trigger_id=96660, initial_sequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9013, spawn_ids=[100]):
            return 몬스터출현05_꼬마생성(self.ctx)


# 네번째 꼬마 쫓기는 웨이브 시작
class 몬스터출현05_꼬마생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_5001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현05_생성랜덤01(self.ctx)


class 몬스터출현05_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현05_1번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_2번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_3번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_4번대장생성(self.ctx)


class 몬스터출현05_1번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[991], auto_target=False)
        self.move_npc(spawn_id=991, patrol_name='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_2번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[992], auto_target=False)
        self.move_npc(spawn_id=992, patrol_name='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_3번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[992], auto_target=False)
        self.move_npc(spawn_id=992, patrol_name='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_4번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[991], auto_target=False)
        self.move_npc(spawn_id=991, patrol_name='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현05_1번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_2번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_3번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_4번자코생성(self.ctx)


class 몬스터출현05_1번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5001', seconds=1)
        self.spawn_monster(spawn_ids=[930], auto_target=False)
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_901')
        self.spawn_monster(spawn_ids=[935], auto_target=False)
        self.move_npc(spawn_id=935, patrol_name='MS2PatrolData_904')
        self.spawn_monster(spawn_ids=[937], auto_target=False)
        self.move_npc(spawn_id=937, patrol_name='MS2PatrolData_906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5001'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_2번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5002', seconds=1)
        self.spawn_monster(spawn_ids=[931], auto_target=False)
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_902')
        self.spawn_monster(spawn_ids=[936], auto_target=False)
        self.move_npc(spawn_id=936, patrol_name='MS2PatrolData_901')
        self.spawn_monster(spawn_ids=[937], auto_target=False)
        self.move_npc(spawn_id=937, patrol_name='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5002'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_3번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5003', seconds=1)
        self.spawn_monster(spawn_ids=[932], auto_target=False)
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_903')
        self.spawn_monster(spawn_ids=[938], auto_target=False)
        self.move_npc(spawn_id=938, patrol_name='MS2PatrolData_907')
        self.spawn_monster(spawn_ids=[936], auto_target=False)
        self.move_npc(spawn_id=936, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5003'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_4번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5004', seconds=1)
        self.spawn_monster(spawn_ids=[932], auto_target=False)
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_905')
        self.spawn_monster(spawn_ids=[934], auto_target=False)
        self.move_npc(spawn_id=934, patrol_name='MS2PatrolData_903')
        self.spawn_monster(spawn_ids=[938], auto_target=False)
        self.move_npc(spawn_id=938, patrol_name='MS2PatrolData_906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5004'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현05_5번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_6번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_7번대장생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_8번대장생성(self.ctx)


class 몬스터출현05_5번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[991], auto_target=False)
        self.move_npc(spawn_id=991, patrol_name='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_6번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[992], auto_target=False)
        self.move_npc(spawn_id=992, patrol_name='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_7번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[993], auto_target=False)
        self.move_npc(spawn_id=993, patrol_name='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_8번대장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[994], auto_target=False)
        self.move_npc(spawn_id=994, patrol_name='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_생성랜덤04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 몬스터출현05_5번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_6번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_7번자코생성(self.ctx)
        if self.random_condition(weight=25.0):
            return 몬스터출현05_8번자코생성(self.ctx)


class 몬스터출현05_5번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[930], auto_target=False)
        self.move_npc(spawn_id=930, patrol_name='MS2PatrolData_902')
        self.spawn_monster(spawn_ids=[935], auto_target=False)
        self.move_npc(spawn_id=935, patrol_name='MS2PatrolData_905')
        self.spawn_monster(spawn_ids=[937], auto_target=False)
        self.move_npc(spawn_id=937, patrol_name='MS2PatrolData_909')

    def on_tick(self) -> trigger_api.Trigger:
        return 추격연출시작01(self.ctx)


class 몬스터출현05_6번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[931], auto_target=False)
        self.move_npc(spawn_id=931, patrol_name='MS2PatrolData_901')
        self.spawn_monster(spawn_ids=[934], auto_target=False)
        self.move_npc(spawn_id=934, patrol_name='MS2PatrolData_909')
        self.spawn_monster(spawn_ids=[937], auto_target=False)
        self.move_npc(spawn_id=937, patrol_name='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        return 추격연출시작01(self.ctx)


class 몬스터출현05_7번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[932], auto_target=False)
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_903')
        self.spawn_monster(spawn_ids=[935], auto_target=False)
        self.move_npc(spawn_id=935, patrol_name='MS2PatrolData_904')
        self.spawn_monster(spawn_ids=[936], auto_target=False)
        self.move_npc(spawn_id=936, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        return 추격연출시작01(self.ctx)


class 몬스터출현05_8번자코생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[932], auto_target=False)
        self.move_npc(spawn_id=932, patrol_name='MS2PatrolData_906')
        self.spawn_monster(spawn_ids=[934], auto_target=False)
        self.move_npc(spawn_id=934, patrol_name='MS2PatrolData_901')
        self.spawn_monster(spawn_ids=[937], auto_target=False)
        self.move_npc(spawn_id=937, patrol_name='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        return 추격연출시작01(self.ctx)


class 추격연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7776], visible=True) # 추격 소음01 사운드
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__902$')
        self.select_camera(trigger_id=800)
        self.set_skip(state=추격연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 추격연출종료01(self.ctx)


class 추격연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__803$', arg3='2000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.select_camera(trigger_id=800, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__90$', time=2)
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__91$', time=2)
        self.set_dialogue(type=1, spawn_id=500, script='$02000331_BF__Seeker01__92$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[930,931,932,933,934,935,936,937,938,991,992,993,994]):
            return 네번째꼬마만남01(self.ctx)


class 네번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7776]) # 추격 소음01 사운드
        self.set_dialogue(type=1, spawn_id=500, script='$02000331_BF__Seeker01__93$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 네번째꼬마만남02(self.ctx)


class 네번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__94$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 네번째꼬마만남03(self.ctx)


class 네번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__95$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 네번째꼬마만남04(self.ctx)


class 네번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=400, script='$02000331_BF__Seeker01__96$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다섯명패트롤01(self.ctx)


class 다섯명패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__97$', time=2)
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9014, spawn_ids=[100]):
            return 다섯명패트롤02(self.ctx)


class 다섯명패트롤02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2010')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3008')
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4004')
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_5002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9015, spawn_ids=[100]):
            return 두번째무너짐연출시작01(self.ctx)


class 두번째무너짐연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__903$')
        self.select_camera(trigger_id=806)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째다리붕괴02(self.ctx)


class 두번째다리붕괴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033], start_delay=14, interval=100, fade=100)
        self.set_effect(trigger_ids=[777803], visible=True) # 길 없어짐02 사운드 / 막힌 길
        self.set_agent(trigger_ids=[15000], visible=True) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15001], visible=True) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15002], visible=True) # 끊어진 다리 길 막기
        self.set_skip(state=두번째무너짐연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째무너짐연출종료01(self.ctx)


class 두번째무너짐연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=806, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=술래말풍선06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선06(self.ctx)


class 술래말풍선06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[777803]) # 길 없어짐02 사운드 / 막힌 길
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1012')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선07(self.ctx)


class 술래말풍선07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__100$', time=2)
        self.set_dialogue(type=1, spawn_id=200, script='$02000331_BF__Seeker01__101$', time=2, arg5=1)
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_5003')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3009')
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 술래말풍선08(self.ctx)


class 술래말풍선08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=500, script='$02000331_BF__Seeker01__102$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선09(self.ctx)


class 술래말풍선09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__103$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 술래말풍선10(self.ctx)


class 술래말풍선10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=400, script='$02000331_BF__Seeker01__104$', time=2)
        self.set_dialogue(type=1, spawn_id=300, script='$02000331_BF__Seeker01__105$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 외다리생성랜덤(self.ctx)


# 다섯번째  외다리 생성 스위치 랜덤
class 외다리생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 외다리스위치출현01(self.ctx) # 외다리스위치01 - 10000785
        if self.random_condition(weight=20.0):
            return 외다리스위치출현02(self.ctx) # 외다리스위치02 - 10000796
        if self.random_condition(weight=20.0):
            return 외다리스위치출현03(self.ctx) # 외다리스위치03 - 10000797
        if self.random_condition(weight=20.0):
            return 외다리스위치출현04(self.ctx) # 외다리스위치04 - 10000798
        if self.random_condition(weight=20.0):
            return 외다리스위치출현05(self.ctx) # 외다리스위치05 - 10000799


# 외다리스위치출현01 -  10000785
class 외다리스위치출현01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000785], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000785], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 외다리스위치반응01(self.ctx)


class 외다리스위치반응01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000785]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 외다리스위치출현02 -  10000796
class 외다리스위치출현02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000796], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000796], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 외다리스위치반응02(self.ctx)


class 외다리스위치반응02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000796]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 외다리스위치출현03 -  10000797
class 외다리스위치출현03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000797], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000797], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 외다리스위치반응03(self.ctx)


class 외다리스위치반응03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000797]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 외다리스위치출현04 -  10000798
class 외다리스위치출현04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000798], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000798], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 외다리스위치반응04(self.ctx)


class 외다리스위치반응04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000798]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


# 외다리스위치출현05 -  10000799
class 외다리스위치출현05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000799], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000799], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 외다리스위치반응05(self.ctx)


class 외다리스위치반응05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 주변에서 레버를 찾아 당겨 보세요.
        self.show_guide_summary(entity_id=20003314, text_id=20003314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000799]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003314)


class 외다리생성시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[90008]) # 9th barrier OFF
        self.set_effect(trigger_ids=[777702], visible=True) # 길 나타남02 사운드 / 외다리
        self.set_random_mesh(trigger_ids=[10040,10041,10042,10043,10044], visible=True, start_delay=5, interval=150, fade=150) # 3rd bridge ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 다리건너갈준비01(self.ctx)


class 다리건너갈준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__805$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 다리건너갈준비02(self.ctx)


class 다리건너갈준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__110$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99992]):
            return 다리건너가기01(self.ctx)
        if self.user_detected(box_ids=[99993]):
            return 다리건너가기01(self.ctx)


class 다리건너가기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_1014')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_2014')
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_3010')
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_4006')
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_5004')
        self.set_dialogue(type=1, spawn_id=100, script='$02000331_BF__Seeker01__111$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다리건너가기02(self.ctx)


class 다리건너가기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99996]):
            return 다리건너가기03(self.ctx)


class 다리건너가기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=610, script='$02000331_BF__Seeker01__112$', time=3)
        self.set_mesh(trigger_ids=[90008], visible=True) # 9th barrier ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다리건너가기04(self.ctx)


class 다리건너가기04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9018, spawn_ids=[300]):
            return 보스등장연출시작01(self.ctx)


class 보스등장연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[990], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__904$')
        self.set_effect(trigger_ids=[777901], visible=True) # KaseMu Voice01
        self.select_camera(trigger_id=808)
        self.set_skip(state=보스등장연출중01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스등장연출중01(self.ctx)


class 보스등장연출중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__905$')
        self.set_skip(state=보스등장연출중01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스등장연출중01Skip(self.ctx)


class 보스등장연출중01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 보스등장연출중02(self.ctx)


class 보스등장연출중02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__906$')
        self.change_monster(from_spawn_id=100, to_spawn_id=601) # 디펜스용 NPC로 교체 메린
        self.change_monster(from_spawn_id=200, to_spawn_id=602) # 디펜스용 NPC로 교체 이지
        self.change_monster(from_spawn_id=300, to_spawn_id=603) # 디펜스용 NPC로 교체 플린
        self.change_monster(from_spawn_id=400, to_spawn_id=604) # 디펜스용 NPC로 교체 스틴
        self.change_monster(from_spawn_id=500, to_spawn_id=605) # 디펜스용 NPC로 교체 토리
        self.select_camera(trigger_id=809)
        self.set_skip(state=보스등장연출중02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스등장연출중02Skip(self.ctx)


class 보스등장연출중02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 보스등장연출중03(self.ctx)


class 보스등장연출중03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[10040,10041,10042,10043,10044], start_delay=5, interval=150, fade=150) # 3rd bridge OFF
        self.set_effect(trigger_ids=[777802], visible=True) # 길 없어짐02 사운드 /  외다리
        self.set_agent(trigger_ids=[16000], visible=True) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16001], visible=True) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16002], visible=True) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16003], visible=True) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16004], visible=True) # 새로운 다리 길 막기
        self.set_skip(state=보스등장연출중03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스등장연출중03Skip(self.ctx)


class 보스등장연출중03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 보스등장연출중04(self.ctx)


class 보스등장연출중04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=809, enable=False)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__907$')
        self.set_effect(trigger_ids=[777901]) # KaseMu Voice01
        self.set_effect(trigger_ids=[777902], visible=True) # KaseMu Voice02
        self.set_skip(state=보스등장연출끝01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스등장연출끝01(self.ctx)


class 보스등장연출끝01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=808, enable=False)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[777802]) # 길 없어짐02 사운드 /  외다리
        self.set_user_value(trigger_id=15, key='SecondBridgeOff', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마지막웨이브알림01(self.ctx)


class 마지막웨이브알림01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__806$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 몬스터출현06_생성랜덤01(self.ctx)


# 마지막 웨이브 : 첫 번째 소환 : 근거리4/근거리4
class 몬스터출현06_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 몬스터출현06_1번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_2번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_3번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_4번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_5번생성(self.ctx)


class 몬스터출현06_1번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[940,941,950,951], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_2번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[942,943,952,953], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_3번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6003', seconds=1)
        self.spawn_monster(spawn_ids=[944,945,954,955], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_4번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[946,947,956,957], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_5번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[948,949,958,959], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


# 마지막 웨이브 : 두 번째 소환
class 몬스터출현06_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 몬스터출현06_6번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_7번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_8번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_9번생성(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_10번생성(self.ctx)


class 몬스터출현06_6번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[960,961,962,963], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_7번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[962,963,964,965], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_8번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,966,967], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_9번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[966,967,968,969], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_10번생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[968,969,960,961], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 두번째웨이브대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 몬스터출현06_생성랜덤03(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 : 원거리4 근거리12
class 몬스터출현06_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 몬스터출현06_11번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_12번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_13번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_14번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_15번생성_01(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 : 패턴1 : 근2-2-3-2-3-2, 원3,5빼고
class 몬스터출현06_11번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[940,941,971], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_11번생성_02(self.ctx)


class 몬스터출현06_11번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[950,951,970], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_11번생성_03(self.ctx)


class 몬스터출현06_11번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[960,961,962], auto_target=False) # 원거리없음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_11번생성_04(self.ctx)


class 몬스터출현06_11번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[945,946,976], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_11번생성_05(self.ctx)


class 몬스터출현06_11번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[955,956,957], auto_target=False) # 원거리없음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 몬스터출현06_11번생성_06(self.ctx)


class 몬스터출현06_11번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[965,966,975], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴2  : 근2-3-2-3-2-2, 원2,5빼고
class 몬스터출현06_12번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[958,959,978], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_12번생성_02(self.ctx)


class 몬스터출현06_12번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[968,969,960], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_12번생성_03(self.ctx)


class 몬스터출현06_12번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[948,949,979], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_12번생성_04(self.ctx)


class 몬스터출현06_12번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[943,944,945,975], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_12번생성_05(self.ctx)


class 몬스터출현06_12번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_12번생성_06(self.ctx)


class 몬스터출현06_12번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,974], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴3 : 근2-3-3-2-2-2, 원1,6빼고
class 몬스터출현06_13번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[946,947], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_13번생성_02(self.ctx)


class 몬스터출현06_13번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[955,956,957,976], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_13번생성_03(self.ctx)


class 몬스터출현06_13번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[965,966,967,977], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_13번생성_04(self.ctx)


class 몬스터출현06_13번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[969,960,979], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_13번생성_05(self.ctx)


class 몬스터출현06_13번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[949,940,970], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_13번생성_06(self.ctx)


class 몬스터출현06_13번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[950,959], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴4 : 근2-3-3-2-2-2, 원2,3빼고
class 몬스터출현06_14번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[941,942,972], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_14번생성_02(self.ctx)


class 몬스터출현06_14번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[961,962,963], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_14번생성_03(self.ctx)


class 몬스터출현06_14번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[951,952,953], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_14번생성_04(self.ctx)


class 몬스터출현06_14번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,974], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_14번생성_05(self.ctx)


class 몬스터출현06_14번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[944,946,975], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_14번생성_06(self.ctx)


class 몬스터출현06_14번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[955,956,976], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴5  : 근2-3-2-2-3-2, 원3,6빼고
class 몬스터출현06_15번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[948,949,979], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_15번생성_02(self.ctx)


class 몬스터출현06_15번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[968,969,960,978], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_15번생성_03(self.ctx)


class 몬스터출현06_15번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[948,949], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_15번생성_04(self.ctx)


class 몬스터출현06_15번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[963,964,973], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_15번생성_05(self.ctx)


class 몬스터출현06_15번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954,955,974], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_15번생성_06(self.ctx)


class 몬스터출현06_15번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[943,944], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 전방향 순차적 소환 : 근거리4 원거리 1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_생성랜덤04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터출현06_16번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_17번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_18번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_19번생성_01(self.ctx)
        if self.random_condition(weight=20.0):
            return 몬스터출현06_20번생성_01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴1 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_16번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[941,942,971], auto_target=False) # 근거리4 원거리1 , 123

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_16번생성_02(self.ctx)


class 몬스터출현06_16번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[951,953], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_16번생성_03(self.ctx)


class 몬스터출현06_16번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[954,955,956,986], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_16번생성_04(self.ctx)


class 몬스터출현06_16번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,985], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_16번생성_05(self.ctx)


class 몬스터출현06_16번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_16번생성_06(self.ctx)


class 몬스터출현06_16번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,974], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_16번생성_07(self.ctx)


class 몬스터출현06_16번생성_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[947,948,949,988], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_16번생성_08(self.ctx)


class 몬스터출현06_16번생성_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[967,968,987], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴2 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_17번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[954,955,956,986], auto_target=False) # 근거리5 원거리2 ,456

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_17번생성_02(self.ctx)


class 몬스터출현06_17번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,985], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_17번생성_03(self.ctx)


class 몬스터출현06_17번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[941,942,971], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_17번생성_04(self.ctx)


class 몬스터출현06_17번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[951,953], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_17번생성_05(self.ctx)


class 몬스터출현06_17번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[947,948,949,988], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_17번생성_06(self.ctx)


class 몬스터출현06_17번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[967,968,987], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_17번생성_07(self.ctx)


class 몬스터출현06_17번생성_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_17번생성_08(self.ctx)


class 몬스터출현06_17번생성_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[964,965,974], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴3 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_18번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[959,958], auto_target=False) # 근거리4 원거리1 , 890

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_18번생성_02(self.ctx)


class 몬스터출현06_18번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[949,940,970], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_18번생성_03(self.ctx)


class 몬스터출현06_18번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954,955,983], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_18번생성_04(self.ctx)


class 몬스터출현06_18번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[943,945,984], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_18번생성_05(self.ctx)


class 몬스터출현06_18번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[961,962], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_18번생성_06(self.ctx)


class 몬스터출현06_18번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[952,953,972], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_18번생성_07(self.ctx)


class 몬스터출현06_18번생성_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[945,946,947,985], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_18번생성_08(self.ctx)


class 몬스터출현06_18번생성_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[966,967,986], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴4 : 근거리5 원거리1/ 근거리4 원거리2/ 근거리5 원거리 1/ 근거리4 원거리2
class 몬스터출현06_19번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[943,944,945,974], auto_target=False) # 근거리5 원거리1 , 345

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_19번생성_02(self.ctx)


class 몬스터출현06_19번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[963,965], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_19번생성_03(self.ctx)


class 몬스터출현06_19번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[951,950,980], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_19번생성_04(self.ctx)


class 몬스터출현06_19번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[941,942,981], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_19번생성_05(self.ctx)


class 몬스터출현06_19번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[957,958], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_19번생성_06(self.ctx)


class 몬스터출현06_19번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[966,968,977], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_19번생성_07(self.ctx)


class 몬스터출현06_19번생성_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[948,949,989], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_19번생성_08(self.ctx)


class 몬스터출현06_19번생성_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[959,958,988], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴5 : 근거리5 원거리1/ 근거리4 원거리2/ 근거리5 원거리 1/ 근거리4 원거리2
class 몬스터출현06_20번생성_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[967,968,969], auto_target=False) # 근거리5 원거리1 , 789

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_20번생성_02(self.ctx)


class 몬스터출현06_20번생성_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[957,959,978], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_20번생성_03(self.ctx)


class 몬스터출현06_20번생성_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[953,954,984], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_20번생성_04(self.ctx)


class 몬스터출현06_20번생성_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[943,944,983], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_20번생성_05(self.ctx)


class 몬스터출현06_20번생성_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[951,952,950], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_20번생성_06(self.ctx)


class 몬스터출현06_20번생성_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[962,961,970], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터출현06_20번생성_07(self.ctx)


class 몬스터출현06_20번생성_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[946,947,986], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터출현06_20번생성_08(self.ctx)


class 몬스터출현06_20번생성_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[955,956,985], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


class 보스전투_준비01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전투_준비02(self.ctx)


class 보스전투_준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=811)
        self.set_skip(state=보스전투_준비04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전투_준비03(self.ctx)


class 보스전투_준비03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__908$')
        self.set_effect(trigger_ids=[777902]) # KaseMu Voice02
        self.set_effect(trigger_ids=[777903], visible=True) # KaseMu Voice03

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스전투_준비04(self.ctx)


class 보스전투_준비04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=811, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스전투_시작01(self.ctx)


class 보스전투_시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[990])
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__807$', arg3='3000', arg4='0')
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.spawn_monster(spawn_ids=[999], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 보스도망준비01(self.ctx)


class 보스도망준비01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보스도망연출01(self.ctx)


class 보스도망연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1000], auto_target=False)
        self.set_interact_object(trigger_ids=[10000776], state=0) # 마지막꼬마 CAGE 열수있는 철창 켜기
        self.set_interact_object(trigger_ids=[10000776], state=1) # 마지막꼬마 CAGE 열수있는 철창 켜기
        self.set_actor(trigger_id=97770, initial_sequence='Closed') # 마지막꼬마 CAGE 액터 감추기
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__909$')
        self.select_camera(trigger_id=812)
        self.set_skip(state=보스도망연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보스도망연출02(self.ctx)


class 보스도망연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__910$')
        self.set_effect(trigger_ids=[777903]) # KaseMu Voice03
        self.set_effect(trigger_ids=[777904], visible=True) # KaseMu Voice04
        self.set_skip(state=보스도망연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스도망연출03(self.ctx)


class 보스도망연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=812, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.change_monster(from_spawn_id=610, to_spawn_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스전투_끝01(self.ctx)


class 보스전투_끝01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__808$', arg3='3000', arg4='0')
        self.set_dialogue(type=1, spawn_id=600, script='$02000331_BF__Seeker01__120$', time=2, arg5=1)
        self.destroy_monster(spawn_ids=[1000])
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마지막연출_준비01(self.ctx)


class 마지막연출_준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003315, text_id=20003315) # 가이드 : 갇혀 있는 리안을 구해 주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000776]):
            return 마지막연출_포털출현01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20003315)
        self.set_interact_object(trigger_ids=[10000776], state=0) # 마지막꼬마 CAGE 열수있는 철창 켜기


class 마지막연출_포털출현01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=7, arg2='$02000331_BF__Seeker01__809$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마지막연출_포털출현02(self.ctx)


class 마지막연출_포털출현02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=600, patrol_name='MS2PatrolData_6001')
        self.set_effect(trigger_ids=[777904]) # KaseMu Voice04

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마지막연출_포털출현03(self.ctx)


class 마지막연출_포털출현03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=600, script='$02000331_BF__Seeker01__130$', time=2)
        self.set_effect(trigger_ids=[99999], visible=True) # 치유 이펙트
        self.set_effect(trigger_ids=[7772], visible=True) # 치유 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9020, spawn_ids=[600]):
            return 마지막연출_포털출현04(self.ctx)


class 마지막연출_포털출현04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[99999]) # 치유 이펙트
        self.change_monster(from_spawn_id=601, to_spawn_id=110)
        self.change_monster(from_spawn_id=602, to_spawn_id=210)
        self.change_monster(from_spawn_id=603, to_spawn_id=310)
        self.change_monster(from_spawn_id=604, to_spawn_id=410)
        self.change_monster(from_spawn_id=605, to_spawn_id=510)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마지막연출_시작01(self.ctx)


class 마지막연출_시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=410, patrol_name='MS2PatrolData_4007')
        self.move_npc(spawn_id=510, patrol_name='MS2PatrolData_5005')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_1015')
        self.move_npc(spawn_id=210, patrol_name='MS2PatrolData_2012')
        self.move_npc(spawn_id=310, patrol_name='MS2PatrolData_3011')
        self.move_npc(spawn_id=600, patrol_name='MS2PatrolData_6002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마지막연출_시작02(self.ctx)


class 마지막연출_시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=110, script='$02000331_BF__Seeker01__131$', time=2)
        self.set_dialogue(type=1, spawn_id=310, script='$02000331_BF__Seeker01__132$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=410, script='$02000331_BF__Seeker01__133$', time=2, arg5=4)
        self.set_dialogue(type=1, spawn_id=600, script='$02000331_BF__Seeker01__136$', time=2, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 던전클리어01(self.ctx)


class 던전클리어01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[90090,90091,90092,90093,90094,90095,90096,90097,90098,90099], start_delay=10, interval=100, fade=100) # 클리어포털 나타남
        self.change_monster(from_spawn_id=110, to_spawn_id=111) # Quest Npc 교체

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 퇴장시작01(self.ctx)

    def on_exit(self) -> None:
        self.dungeon_clear()
        self.set_achievement(trigger_id=99998, type='trigger', achieve='ClearHideandSeek') # ClearHideandSeek 퀘스트
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True) # 클리어포털 나타남


class 퇴장시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_1017')
        # self.move_npc(spawn_id=410, patrol_name='MS2PatrolData_4008')
        # self.move_npc(spawn_id=510, patrol_name='MS2PatrolData_5006')
        # self.move_npc(spawn_id=210, patrol_name='MS2PatrolData_2016')
        # self.move_npc(spawn_id=310, patrol_name='MS2PatrolData_3012')
        # self.move_npc(spawn_id=600, patrol_name='MS2PatrolData_6003')
        self.set_dialogue(type=1, spawn_id=210, script='$02000331_BF__Seeker01__134$', time=2)
        self.set_dialogue(type=1, spawn_id=510, script='$02000331_BF__Seeker01__135$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=111, script='$02000331_BF__Seeker01__137$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[11000]) # 입구로 되돌아 가는 길 막기
        self.set_agent(trigger_ids=[11001]) # 입구로 되돌아 가는 길 막기
        self.set_agent(trigger_ids=[15000]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15001]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[15002]) # 끊어진 다리 길 막기
        self.set_agent(trigger_ids=[16000]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16001]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16002]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16003]) # 새로운 다리 길 막기
        self.set_agent(trigger_ids=[16004]) # 새로운 다리 길 막기


initial_state = 대기
