""" trigger/02000387_bf/01_playparttimejob.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[2000,2001,2002,2003,2004], visible=True) # Barrier
        self.set_mesh(trigger_ids=[2005], visible=True) # Barrier
        # 테스트용 임시
        self.set_mesh(trigger_ids=[2006], visible=True) # Barrier
        self.set_mesh(trigger_ids=[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031], visible=True) # Barrier
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='ry_functobj_door_E01_off') # RevolvingDoor
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_E01_off') # RevolvingDoor
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='ry_functobj_door_E01_off') # RevolvingDoor
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='ry_functobj_door_E01_off') # RevolvingDoor
        self.set_effect(trigger_ids=[5000]) # GuideUI
        self.set_effect(trigger_ids=[5101]) # DownArrow
        self.set_effect(trigger_ids=[5102]) # DownArrow
        self.set_effect(trigger_ids=[5103]) # DownArrow
        self.set_effect(trigger_ids=[5104]) # DownArrow
        self.set_effect(trigger_ids=[5105]) # DownArrow
        self.set_effect(trigger_ids=[5106]) # DownArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100], auto_target=False) # 캐시 카탈리나

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=9001) # 해킹 보안용 시작 box 설정
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideTalk01(self.ctx)


class GuideTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__0$', time=4) # 잡담에서 캐시마트에 대해 설명해주기
        self.set_skip(state=GuideTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GuideTalk01Skip(self.ctx)


class GuideTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return GuideTalk02(self.ctx)


class GuideTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__1$', time=4)
        self.set_skip(state=GuideTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GuideTalk02Skip(self.ctx)


class GuideTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return GuideTalk03(self.ctx)


class GuideTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__2$', time=4)
        self.set_skip(state=GuideTalk03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GuideTalk03Skip(self.ctx)


class GuideTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return GuideTalk04(self.ctx)


class GuideTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__3$', time=4)
        self.set_skip(state=GuideTalk04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GuideTalk04Skip(self.ctx)


class GuideTalk04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCPlacement01(self.ctx)


class PCPlacement01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=10, key='RandomPortalOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9005) == 1:
            # 카운터 1명
            return PCPlacement02(self.ctx) # 1인 테스트용 임시


class PCPlacement02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9006) == 3:
            return PCPlacement03(self.ctx)


class PCPlacement03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MartOpen(self.ctx)


class MartOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='ry_functobj_door_E01_on') # RevolvingDoor
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_E01_on') # RevolvingDoor
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='ry_functobj_door_E01_on') # RevolvingDoor
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='ry_functobj_door_E01_on') # RevolvingDoor
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__01_PLAYPARTTIMEJOB__4$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R01Start(self.ctx)


class R01Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__01_PLAYPARTTIMEJOB__5$', duration=3000, box_ids=['0'])
        self.set_event_ui_round(rounds=[1,3]) # Round1
        self.set_effect(trigger_ids=[5105], visible=True) # DownArrow
        self.set_effect(trigger_ids=[5106], visible=True) # DownArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01Customer01Row03Random(self.ctx)


# 1Round 1번 고객  : 3번 레일
class R01Customer01Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=10103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup3003(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup3007(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup3011(self.ctx)


# 1Round 2번 고객  : 2번 레일
class R01Customer02Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=10202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup2002(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup2006(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup2010(self.ctx)


# 1Round 3번 고객  : 4번 레일
class R01Customer03Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=10304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return None # Missing State: NpcGroup4205
        if self.random_condition(weight=14.0):
            return NpcGroup4208(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4212(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4216(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4220(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4224(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup4228(self.ctx)


# 1Round 4번 고객  : 1번 레일
class R01Customer04Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=10401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup1101(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1105(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1109(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1113(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup1117(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup1121(self.ctx)


class R01End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9007, spawn_ids=[0]):
            # 가게에 손님이 없으면
            return R02StartDelay01(self.ctx)


class R02StartDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02Start(self.ctx)


class R02Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__01_PLAYPARTTIMEJOB__6$', duration=3000, box_ids=['0'])
        self.set_event_ui_round(rounds=[2,3]) # Round2

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R02Customer01Row02Random(self.ctx)


# 2Round 1번 고객  : 2번 레일
class R02Customer01Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup2102(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2106(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2110(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2114(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup2118(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup2122(self.ctx)


# 2Round 2번 고객  : 3번 레일
class R02Customer02Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20203)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup3203(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3207(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3211(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3215(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3219(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3223(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup3227(self.ctx)


# 2Round 3번 고객  : 1번 레일
class R02Customer03Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup1001(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup1005(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup1009(self.ctx)


# 2Round 4번 고객  : 4번 레일
class R02Customer04Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20404)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup4104(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4108(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4112(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4116(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup4120(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup4124(self.ctx)


# 2Round 5번 고객  : 2번 레일
class R02Customer05Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup2202(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2206(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2210(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2214(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2218(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2222(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup2226(self.ctx)


# 2Round 6번 고객  : 3번 레일
class R02Customer06Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup3103(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3107(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3111(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3115(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup3119(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup3123(self.ctx)


# 2Round 7번 고객  : 1번 레일
class R02Customer07Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup1201(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1205(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1209(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1213(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1217(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1221(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup1225(self.ctx)


# 2Round 8번 고객  : 4번 레일
class R02Customer08Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=20804)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup4004(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup4008(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup4012(self.ctx)


class R02End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9007, spawn_ids=[0]):
            # 가게에 손님이 없으면
            return R03StartDelay01(self.ctx)


class R03StartDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03Start(self.ctx)


class R03Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__01_PLAYPARTTIMEJOB__7$', duration=3000, box_ids=['0'])
        self.set_event_ui_round(rounds=[3,3]) # Round3

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R03Customer01Row04Random(self.ctx)


# 3Round 1번 고객  : 4번 레일
class R03Customer01Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup4104(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4108(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4112(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup4116(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup4120(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup4124(self.ctx)


# 3Round 2번 고객  : 3번 레일
class R03Customer02Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup2202(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2206(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2210(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2214(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2218(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup2222(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup2226(self.ctx)


# 3Round 3번 고객  : 2번 레일
class R03Customer03Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup3003(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup3007(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup3011(self.ctx)


# 3Round 4번 고객  : 1번 레일
class R03Customer04Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup1001(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup1005(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup1009(self.ctx)


# 3Round 5번 고객  : 2번 레일
class R03Customer05Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup2002(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup2006(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup2010(self.ctx)


# 3Round 6번 고객  : 4번 레일
class R03Customer06Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30604)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup4204(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4208(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4212(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4216(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4220(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup4224(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup4228(self.ctx)


# 3Round 7번 고객  : 3번 레일
class R03Customer07Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30703)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup3103(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3107(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3111(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup3115(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup3119(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup3123(self.ctx)


# 3Round 8번 고객  : 1번 레일
class R03Customer08Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30801)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup1101(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1105(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1109(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup1113(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup1117(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup1121(self.ctx)


# 3Round 9번 고객  : 1번 레일
class R03Customer09Row01Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=30901)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup1201(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1205(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1209(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1213(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1217(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup1221(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup1225(self.ctx)


# 3Round 10번 고객  : 4번 레일
class R03Customer10Row04Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=31004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return NpcGroup4004(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup4008(self.ctx)
        if self.random_condition(weight=33.0):
            return NpcGroup4012(self.ctx)


# 3Round 11번 고객  : 2번 레일
class R03Customer11Row02Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=31102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return NpcGroup2102(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2106(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2110(self.ctx)
        if self.random_condition(weight=17.0):
            return NpcGroup2114(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup2118(self.ctx)
        if self.random_condition(weight=16.0):
            return NpcGroup2122(self.ctx)


# 3Round 12번 고객  : 3번 레일
class R03Customer12Row03Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RoundCustomerRow', value=31203)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return NpcGroup3203(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3207(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3211(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3215(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3219(self.ctx)
        if self.random_condition(weight=14.0):
            return NpcGroup3223(self.ctx)
        if self.random_condition(weight=15.0):
            return NpcGroup3227(self.ctx)


class R03End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9007, spawn_ids=[0]):
            # 가게에 손님이 없으면
            return GameEndNotice01(self.ctx)


class GameEndNotice01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=2000387, portal_id=1, box_id=9900) # 사무실로 강제 이동
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__8$', time=4)
        self.set_skip(state=GameEndNotice01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GameEndNotice01Skip(self.ctx)


class GameEndNotice01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_user_value(trigger_id=10, key='DungeonClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GameWrapUp(self.ctx)


class GameWrapUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCLeave01(self.ctx)


class PCLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__01_PLAYPARTTIMEJOB__10$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return PCLeave02(self.ctx)


class PCLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


# NPC 그룹 랜덤
class NpcGroup1001(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1001, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1005(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1005, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1009(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1009, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2002(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2002, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2006(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2006, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2010(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2010, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3003, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3007(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3007, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3011(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3011, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4004(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4004, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4008(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4008, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4012(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4012, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1101, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1105, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1109, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1113, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1117(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1117, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1121(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1121, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2102, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2106, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2110, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2114, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2118(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2118, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2122(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2122, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3103, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3107, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3111(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3111, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3115, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3119(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3119, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3123(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3123, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4104, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4108, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4112, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4116(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4116, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4120(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4120, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4124(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4124, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1201, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1205, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1209, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1213, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1217, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1221(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1221, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup1225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1225, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2202, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2206, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2210, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2214, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2218, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2222, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup2226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2226, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3203, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3207, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3211, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3215, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3219(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3219, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3223, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup3227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3227, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4204, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4208, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4212, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4216, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4220, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4224, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NpcGroup4228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4228, key='CustomerEnter', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 다음 손님
            return NextTurnCheck(self.ctx)


class NextTurnCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundCustomerRow') == 10103:
            return R01Customer02Row02Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 10202:
            return R01Customer03Row04Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 10304:
            return R01Customer04Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 10401: # 2Round
            return R01End(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20102:
            return R02Customer02Row03Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20203:
            return R02Customer03Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20301:
            return R02Customer04Row04Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20404:
            return R02Customer05Row02Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20502:
            return R02Customer06Row03Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20603:
            return R02Customer07Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20701:
            return R02Customer08Row04Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 20804: # 3Round
            return R02End(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30104:
            return R03Customer02Row02Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30202:
            return R03Customer03Row03Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30303:
            return R03Customer04Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30401:
            return R03Customer05Row02Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30502:
            return R03Customer06Row04Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30604:
            return R03Customer07Row03Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30703:
            return R03Customer08Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30801:
            return R03Customer09Row01Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 30901:
            return R03Customer10Row04Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 31004:
            return R03Customer11Row02Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 31102:
            return R03Customer12Row03Random(self.ctx)
        if self.user_value(key='RoundCustomerRow') == 31203:
            return R03End(self.ctx)


initial_state = Wait
