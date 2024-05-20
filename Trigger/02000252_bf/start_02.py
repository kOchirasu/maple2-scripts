""" trigger/02000252_bf/start_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(trigger_ids=[2113,2114,2115,2116,2117,2118])
        self.set_effect(trigger_ids=[8013])
        self.set_effect(trigger_ids=[8014])
        self.set_effect(trigger_ids=[8015])
        self.set_effect(trigger_ids=[8016])
        self.set_effect(trigger_ids=[8017])
        self.set_effect(trigger_ids=[8018])
        self.set_effect(trigger_ids=[8019])
        self.set_effect(trigger_ids=[8020])
        self.set_effect(trigger_ids=[8021])
        self.set_effect(trigger_ids=[8022])
        self.set_effect(trigger_ids=[8023])
        self.set_effect(trigger_ids=[8024])
        self.set_effect(trigger_ids=[8025])
        self.set_effect(trigger_ids=[8026])
        self.set_effect(trigger_ids=[8027])
        self.set_effect(trigger_ids=[8028])
        self.set_effect(trigger_ids=[8029])
        self.set_effect(trigger_ids=[8030])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=905) >= 1:
            return 예고이펙트(self.ctx)


"""
class 벨라소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.spawn_monster(spawn_ids=[1004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사(self.ctx)
"""

"""
class 벨라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_5')
            return 벨라스킬딜레이(self.ctx)
"""

"""
class 벨라스킬딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 예고이펙트(self.ctx)
"""

class 예고이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8013], visible=True)
        self.set_effect(trigger_ids=[8014], visible=True)
        self.set_effect(trigger_ids=[8015], visible=True)
        self.set_effect(trigger_ids=[8016], visible=True)
        self.set_effect(trigger_ids=[8017], visible=True)
        self.set_effect(trigger_ids=[8018], visible=True)
        self.set_effect(trigger_ids=[8019], visible=True)
        self.set_effect(trigger_ids=[8020], visible=True)
        self.set_effect(trigger_ids=[8021], visible=True)
        self.set_effect(trigger_ids=[8022], visible=True)
        self.set_effect(trigger_ids=[8023], visible=True)
        self.set_effect(trigger_ids=[8024], visible=True)
        self.set_effect(trigger_ids=[8025], visible=True)
        self.set_effect(trigger_ids=[8026], visible=True)
        self.set_effect(trigger_ids=[8027], visible=True)
        self.set_effect(trigger_ids=[8028], visible=True)
        self.set_effect(trigger_ids=[8029], visible=True)
        self.set_effect(trigger_ids=[8030], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 스킬시작대기(self.ctx)


class 스킬시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1063], auto_target=False)
        self.spawn_monster(spawn_ids=[1064], auto_target=False)
        self.spawn_monster(spawn_ids=[1065], auto_target=False)
        self.spawn_monster(spawn_ids=[1066], auto_target=False)
        self.spawn_monster(spawn_ids=[1067], auto_target=False)
        self.spawn_monster(spawn_ids=[1068], auto_target=False)
        self.spawn_monster(spawn_ids=[1069], auto_target=False)
        self.spawn_monster(spawn_ids=[1070], auto_target=False)
        self.spawn_monster(spawn_ids=[1071], auto_target=False)
        self.spawn_monster(spawn_ids=[1072], auto_target=False)
        self.spawn_monster(spawn_ids=[1073], auto_target=False)
        self.spawn_monster(spawn_ids=[1074], auto_target=False)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.set_effect(trigger_ids=[8013])
            self.set_effect(trigger_ids=[8014])
            self.set_effect(trigger_ids=[8015])
            self.set_effect(trigger_ids=[8016])
            self.set_effect(trigger_ids=[8017])
            self.set_effect(trigger_ids=[8018])
            self.set_effect(trigger_ids=[8019])
            self.set_effect(trigger_ids=[8020])
            self.set_effect(trigger_ids=[8021])
            self.set_effect(trigger_ids=[8022])
            self.set_effect(trigger_ids=[8023])
            self.set_effect(trigger_ids=[8024])
            self.set_effect(trigger_ids=[8025])
            self.set_effect(trigger_ids=[8026])
            self.set_effect(trigger_ids=[8027])
            self.set_effect(trigger_ids=[8028])
            self.set_effect(trigger_ids=[8029])
            self.set_effect(trigger_ids=[8030])
            return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(trigger_ids=[2113,2114,2115,2116,2117,2118])
        self.set_skill(trigger_ids=[2301], enable=True)
        self.set_skill(trigger_ids=[2302], enable=True)
        self.set_skill(trigger_ids=[2303], enable=True)
        self.set_skill(trigger_ids=[2304], enable=True)
        self.set_skill(trigger_ids=[2305], enable=True)
        self.set_skill(trigger_ids=[2306], enable=True)
        self.set_skill(trigger_ids=[2307], enable=True)
        self.set_skill(trigger_ids=[2308], enable=True)
        self.set_skill(trigger_ids=[2309], enable=True)
        self.set_skill(trigger_ids=[2310], enable=True)
        self.set_skill(trigger_ids=[2311], enable=True)
        self.set_skill(trigger_ids=[2312], enable=True)
        self.set_skill(trigger_ids=[2313], enable=True)
        self.set_skill(trigger_ids=[2314], enable=True)
        self.set_skill(trigger_ids=[2315], enable=True)
        self.set_skill(trigger_ids=[2316], enable=True)
        self.set_skill(trigger_ids=[2317], enable=True)
        self.set_skill(trigger_ids=[2318], enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1004])
        self.set_skill(trigger_ids=[2301])
        self.set_skill(trigger_ids=[2302])
        self.set_skill(trigger_ids=[2303])
        self.set_skill(trigger_ids=[2304])
        self.set_skill(trigger_ids=[2305])
        self.set_skill(trigger_ids=[2306])
        self.set_skill(trigger_ids=[2307])
        self.set_skill(trigger_ids=[2308])
        self.set_skill(trigger_ids=[2309])
        self.set_skill(trigger_ids=[2310])
        self.set_skill(trigger_ids=[2311])
        self.set_skill(trigger_ids=[2312])
        self.set_skill(trigger_ids=[2313])
        self.set_skill(trigger_ids=[2314])
        self.set_skill(trigger_ids=[2315])
        self.set_skill(trigger_ids=[2316])
        self.set_skill(trigger_ids=[2317])
        self.set_skill(trigger_ids=[2318])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2307], enable=True)
        self.set_skill(trigger_ids=[2308], enable=True)
        self.set_skill(trigger_ids=[2309], enable=True)
        self.set_skill(trigger_ids=[2310], enable=True)
        self.set_skill(trigger_ids=[2311], enable=True)
        self.set_skill(trigger_ids=[2312], enable=True)
        self.set_skill(trigger_ids=[2313], enable=True)
        self.set_skill(trigger_ids=[2314], enable=True)
        self.set_skill(trigger_ids=[2315], enable=True)
        self.set_skill(trigger_ids=[2316], enable=True)
        self.set_skill(trigger_ids=[2317], enable=True)
        self.set_skill(trigger_ids=[2318], enable=True)
        self.set_skill(trigger_ids=[2319], enable=True)
        self.set_skill(trigger_ids=[2320], enable=True)
        self.set_skill(trigger_ids=[2321], enable=True)
        self.set_skill(trigger_ids=[2322], enable=True)
        self.set_skill(trigger_ids=[2323], enable=True)
        self.set_skill(trigger_ids=[2324], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2307])
        self.set_skill(trigger_ids=[2308])
        self.set_skill(trigger_ids=[2309])
        self.set_skill(trigger_ids=[2310])
        self.set_skill(trigger_ids=[2311])
        self.set_skill(trigger_ids=[2312])
        self.set_skill(trigger_ids=[2313])
        self.set_skill(trigger_ids=[2314])
        self.set_skill(trigger_ids=[2315])
        self.set_skill(trigger_ids=[2316])
        self.set_skill(trigger_ids=[2317])
        self.set_skill(trigger_ids=[2318])
        self.set_skill(trigger_ids=[2319])
        self.set_skill(trigger_ids=[2320])
        self.set_skill(trigger_ids=[2321])
        self.set_skill(trigger_ids=[2322])
        self.set_skill(trigger_ids=[2323])
        self.set_skill(trigger_ids=[2324])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2313], enable=True)
        self.set_skill(trigger_ids=[2314], enable=True)
        self.set_skill(trigger_ids=[2315], enable=True)
        self.set_skill(trigger_ids=[2316], enable=True)
        self.set_skill(trigger_ids=[2317], enable=True)
        self.set_skill(trigger_ids=[2318], enable=True)
        self.set_skill(trigger_ids=[2319], enable=True)
        self.set_skill(trigger_ids=[2320], enable=True)
        self.set_skill(trigger_ids=[2321], enable=True)
        self.set_skill(trigger_ids=[2322], enable=True)
        self.set_skill(trigger_ids=[2323], enable=True)
        self.set_skill(trigger_ids=[2324], enable=True)
        self.set_skill(trigger_ids=[2325], enable=True)
        self.set_skill(trigger_ids=[2326], enable=True)
        self.set_skill(trigger_ids=[2327], enable=True)
        self.set_skill(trigger_ids=[2328], enable=True)
        self.set_skill(trigger_ids=[2329], enable=True)
        self.set_skill(trigger_ids=[2330], enable=True)
        self.set_skill(trigger_ids=[2331], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2313])
        self.set_skill(trigger_ids=[2314])
        self.set_skill(trigger_ids=[2315])
        self.set_skill(trigger_ids=[2316])
        self.set_skill(trigger_ids=[2317])
        self.set_skill(trigger_ids=[2318])
        self.set_skill(trigger_ids=[2319])
        self.set_skill(trigger_ids=[2320])
        self.set_skill(trigger_ids=[2321])
        self.set_skill(trigger_ids=[2322])
        self.set_skill(trigger_ids=[2323])
        self.set_skill(trigger_ids=[2324])
        self.set_skill(trigger_ids=[2325])
        self.set_skill(trigger_ids=[2326])
        self.set_skill(trigger_ids=[2327])
        self.set_skill(trigger_ids=[2328])
        self.set_skill(trigger_ids=[2329])
        self.set_skill(trigger_ids=[2330])
        self.set_skill(trigger_ids=[2331])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2319], enable=True)
        self.set_skill(trigger_ids=[2320], enable=True)
        self.set_skill(trigger_ids=[2321], enable=True)
        self.set_skill(trigger_ids=[2322], enable=True)
        self.set_skill(trigger_ids=[2323], enable=True)
        self.set_skill(trigger_ids=[2324], enable=True)
        self.set_skill(trigger_ids=[2325], enable=True)
        self.set_skill(trigger_ids=[2326], enable=True)
        self.set_skill(trigger_ids=[2327], enable=True)
        self.set_skill(trigger_ids=[2328], enable=True)
        self.set_skill(trigger_ids=[2329], enable=True)
        self.set_skill(trigger_ids=[2330], enable=True)
        self.set_skill(trigger_ids=[2331], enable=True)
        self.set_skill(trigger_ids=[2332], enable=True)
        self.set_skill(trigger_ids=[2333], enable=True)
        self.set_skill(trigger_ids=[2334], enable=True)
        self.set_skill(trigger_ids=[2335], enable=True)
        self.set_skill(trigger_ids=[2336], enable=True)
        self.set_skill(trigger_ids=[2337], enable=True)
        self.set_skill(trigger_ids=[2338], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2319])
        self.set_skill(trigger_ids=[2320])
        self.set_skill(trigger_ids=[2321])
        self.set_skill(trigger_ids=[2322])
        self.set_skill(trigger_ids=[2323])
        self.set_skill(trigger_ids=[2324])
        self.set_skill(trigger_ids=[2325])
        self.set_skill(trigger_ids=[2326])
        self.set_skill(trigger_ids=[2327])
        self.set_skill(trigger_ids=[2328])
        self.set_skill(trigger_ids=[2329])
        self.set_skill(trigger_ids=[2330])
        self.set_skill(trigger_ids=[2331])
        self.set_skill(trigger_ids=[2332])
        self.set_skill(trigger_ids=[2333])
        self.set_skill(trigger_ids=[2334])
        self.set_skill(trigger_ids=[2335])
        self.set_skill(trigger_ids=[2336])
        self.set_skill(trigger_ids=[2337])
        self.set_skill(trigger_ids=[2338])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2325], enable=True)
        self.set_skill(trigger_ids=[2326], enable=True)
        self.set_skill(trigger_ids=[2327], enable=True)
        self.set_skill(trigger_ids=[2328], enable=True)
        self.set_skill(trigger_ids=[2329], enable=True)
        self.set_skill(trigger_ids=[2330], enable=True)
        self.set_skill(trigger_ids=[2331], enable=True)
        self.set_skill(trigger_ids=[2332], enable=True)
        self.set_skill(trigger_ids=[2333], enable=True)
        self.set_skill(trigger_ids=[2334], enable=True)
        self.set_skill(trigger_ids=[2335], enable=True)
        self.set_skill(trigger_ids=[2336], enable=True)
        self.set_skill(trigger_ids=[2337], enable=True)
        self.set_skill(trigger_ids=[2338], enable=True)
        self.set_skill(trigger_ids=[2339], enable=True)
        self.set_skill(trigger_ids=[2340], enable=True)
        self.set_skill(trigger_ids=[2341], enable=True)
        self.set_skill(trigger_ids=[2342], enable=True)
        self.set_skill(trigger_ids=[2343], enable=True)
        self.set_skill(trigger_ids=[2344], enable=True)
        self.set_skill(trigger_ids=[2345], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2325])
        self.set_skill(trigger_ids=[2326])
        self.set_skill(trigger_ids=[2327])
        self.set_skill(trigger_ids=[2328])
        self.set_skill(trigger_ids=[2329])
        self.set_skill(trigger_ids=[2330])
        self.set_skill(trigger_ids=[2331])
        self.set_skill(trigger_ids=[2332])
        self.set_skill(trigger_ids=[2333])
        self.set_skill(trigger_ids=[2334])
        self.set_skill(trigger_ids=[2335])
        self.set_skill(trigger_ids=[2336])
        self.set_skill(trigger_ids=[2337])
        self.set_skill(trigger_ids=[2338])
        self.set_skill(trigger_ids=[2339])
        self.set_skill(trigger_ids=[2340])
        self.set_skill(trigger_ids=[2341])
        self.set_skill(trigger_ids=[2342])
        self.set_skill(trigger_ids=[2343])
        self.set_skill(trigger_ids=[2344])
        self.set_skill(trigger_ids=[2345])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬08(self.ctx)


class 스킬08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2332], enable=True)
        self.set_skill(trigger_ids=[2333], enable=True)
        self.set_skill(trigger_ids=[2334], enable=True)
        self.set_skill(trigger_ids=[2335], enable=True)
        self.set_skill(trigger_ids=[2336], enable=True)
        self.set_skill(trigger_ids=[2337], enable=True)
        self.set_skill(trigger_ids=[2338], enable=True)
        self.set_skill(trigger_ids=[2339], enable=True)
        self.set_skill(trigger_ids=[2340], enable=True)
        self.set_skill(trigger_ids=[2341], enable=True)
        self.set_skill(trigger_ids=[2342], enable=True)
        self.set_skill(trigger_ids=[2343], enable=True)
        self.set_skill(trigger_ids=[2344], enable=True)
        self.set_skill(trigger_ids=[2345], enable=True)
        self.set_skill(trigger_ids=[2346], enable=True)
        self.set_skill(trigger_ids=[2347], enable=True)
        self.set_skill(trigger_ids=[2348], enable=True)
        self.set_skill(trigger_ids=[2349], enable=True)
        self.set_skill(trigger_ids=[2350], enable=True)
        self.set_skill(trigger_ids=[2351], enable=True)
        self.set_skill(trigger_ids=[2352], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2332])
        self.set_skill(trigger_ids=[2333])
        self.set_skill(trigger_ids=[2334])
        self.set_skill(trigger_ids=[2335])
        self.set_skill(trigger_ids=[2336])
        self.set_skill(trigger_ids=[2337])
        self.set_skill(trigger_ids=[2338])
        self.set_skill(trigger_ids=[2339])
        self.set_skill(trigger_ids=[2340])
        self.set_skill(trigger_ids=[2341])
        self.set_skill(trigger_ids=[2342])
        self.set_skill(trigger_ids=[2343])
        self.set_skill(trigger_ids=[2344])
        self.set_skill(trigger_ids=[2345])
        self.set_skill(trigger_ids=[2346])
        self.set_skill(trigger_ids=[2347])
        self.set_skill(trigger_ids=[2348])
        self.set_skill(trigger_ids=[2349])
        self.set_skill(trigger_ids=[2350])
        self.set_skill(trigger_ids=[2351])
        self.set_skill(trigger_ids=[2352])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬09(self.ctx)


class 스킬09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2339], enable=True)
        self.set_skill(trigger_ids=[2340], enable=True)
        self.set_skill(trigger_ids=[2341], enable=True)
        self.set_skill(trigger_ids=[2342], enable=True)
        self.set_skill(trigger_ids=[2343], enable=True)
        self.set_skill(trigger_ids=[2344], enable=True)
        self.set_skill(trigger_ids=[2345], enable=True)
        self.set_skill(trigger_ids=[2346], enable=True)
        self.set_skill(trigger_ids=[2347], enable=True)
        self.set_skill(trigger_ids=[2348], enable=True)
        self.set_skill(trigger_ids=[2349], enable=True)
        self.set_skill(trigger_ids=[2350], enable=True)
        self.set_skill(trigger_ids=[2351], enable=True)
        self.set_skill(trigger_ids=[2352], enable=True)
        self.set_skill(trigger_ids=[2353], enable=True)
        self.set_skill(trigger_ids=[2354], enable=True)
        self.set_skill(trigger_ids=[2355], enable=True)
        self.set_skill(trigger_ids=[2356], enable=True)
        self.set_skill(trigger_ids=[2357], enable=True)
        self.set_skill(trigger_ids=[2358], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2339])
        self.set_skill(trigger_ids=[2340])
        self.set_skill(trigger_ids=[2341])
        self.set_skill(trigger_ids=[2342])
        self.set_skill(trigger_ids=[2343])
        self.set_skill(trigger_ids=[2344])
        self.set_skill(trigger_ids=[2345])
        self.set_skill(trigger_ids=[2346])
        self.set_skill(trigger_ids=[2347])
        self.set_skill(trigger_ids=[2348])
        self.set_skill(trigger_ids=[2349])
        self.set_skill(trigger_ids=[2350])
        self.set_skill(trigger_ids=[2351])
        self.set_skill(trigger_ids=[2352])
        self.set_skill(trigger_ids=[2353])
        self.set_skill(trigger_ids=[2354])
        self.set_skill(trigger_ids=[2355])
        self.set_skill(trigger_ids=[2356])
        self.set_skill(trigger_ids=[2357])
        self.set_skill(trigger_ids=[2358])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬10(self.ctx)


class 스킬10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2346], enable=True)
        self.set_skill(trigger_ids=[2347], enable=True)
        self.set_skill(trigger_ids=[2348], enable=True)
        self.set_skill(trigger_ids=[2349], enable=True)
        self.set_skill(trigger_ids=[2350], enable=True)
        self.set_skill(trigger_ids=[2351], enable=True)
        self.set_skill(trigger_ids=[2352], enable=True)
        self.set_skill(trigger_ids=[2353], enable=True)
        self.set_skill(trigger_ids=[2354], enable=True)
        self.set_skill(trigger_ids=[2355], enable=True)
        self.set_skill(trigger_ids=[2356], enable=True)
        self.set_skill(trigger_ids=[2357], enable=True)
        self.set_skill(trigger_ids=[2358], enable=True)
        self.set_skill(trigger_ids=[2359], enable=True)
        self.set_skill(trigger_ids=[2360], enable=True)
        self.set_skill(trigger_ids=[2361], enable=True)
        self.set_skill(trigger_ids=[2362], enable=True)
        self.set_skill(trigger_ids=[2363], enable=True)
        self.set_skill(trigger_ids=[2364], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2346])
        self.set_skill(trigger_ids=[2347])
        self.set_skill(trigger_ids=[2348])
        self.set_skill(trigger_ids=[2349])
        self.set_skill(trigger_ids=[2350])
        self.set_skill(trigger_ids=[2351])
        self.set_skill(trigger_ids=[2352])
        self.set_skill(trigger_ids=[2353])
        self.set_skill(trigger_ids=[2354])
        self.set_skill(trigger_ids=[2355])
        self.set_skill(trigger_ids=[2356])
        self.set_skill(trigger_ids=[2357])
        self.set_skill(trigger_ids=[2358])
        self.set_skill(trigger_ids=[2359])
        self.set_skill(trigger_ids=[2360])
        self.set_skill(trigger_ids=[2361])
        self.set_skill(trigger_ids=[2362])
        self.set_skill(trigger_ids=[2363])
        self.set_skill(trigger_ids=[2364])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬11(self.ctx)


class 스킬11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2353], enable=True)
        self.set_skill(trigger_ids=[2354], enable=True)
        self.set_skill(trigger_ids=[2355], enable=True)
        self.set_skill(trigger_ids=[2356], enable=True)
        self.set_skill(trigger_ids=[2357], enable=True)
        self.set_skill(trigger_ids=[2358], enable=True)
        self.set_skill(trigger_ids=[2359], enable=True)
        self.set_skill(trigger_ids=[2360], enable=True)
        self.set_skill(trigger_ids=[2361], enable=True)
        self.set_skill(trigger_ids=[2362], enable=True)
        self.set_skill(trigger_ids=[2363], enable=True)
        self.set_skill(trigger_ids=[2364], enable=True)
        self.set_skill(trigger_ids=[2365], enable=True)
        self.set_skill(trigger_ids=[2366], enable=True)
        self.set_skill(trigger_ids=[2367], enable=True)
        self.set_skill(trigger_ids=[2368], enable=True)
        self.set_skill(trigger_ids=[2369], enable=True)
        self.set_skill(trigger_ids=[2370], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬12대기(self.ctx)


class 스킬12대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2353])
        self.set_skill(trigger_ids=[2354])
        self.set_skill(trigger_ids=[2355])
        self.set_skill(trigger_ids=[2356])
        self.set_skill(trigger_ids=[2357])
        self.set_skill(trigger_ids=[2358])
        self.set_skill(trigger_ids=[2359])
        self.set_skill(trigger_ids=[2360])
        self.set_skill(trigger_ids=[2361])
        self.set_skill(trigger_ids=[2362])
        self.set_skill(trigger_ids=[2363])
        self.set_skill(trigger_ids=[2364])
        self.set_skill(trigger_ids=[2365])
        self.set_skill(trigger_ids=[2366])
        self.set_skill(trigger_ids=[2367])
        self.set_skill(trigger_ids=[2368])
        self.set_skill(trigger_ids=[2369])
        self.set_skill(trigger_ids=[2370])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬12(self.ctx)


class 스킬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2359], enable=True)
        self.set_skill(trigger_ids=[2360], enable=True)
        self.set_skill(trigger_ids=[2361], enable=True)
        self.set_skill(trigger_ids=[2362], enable=True)
        self.set_skill(trigger_ids=[2363], enable=True)
        self.set_skill(trigger_ids=[2364], enable=True)
        self.set_skill(trigger_ids=[2365], enable=True)
        self.set_skill(trigger_ids=[2366], enable=True)
        self.set_skill(trigger_ids=[2367], enable=True)
        self.set_skill(trigger_ids=[2368], enable=True)
        self.set_skill(trigger_ids=[2369], enable=True)
        self.set_skill(trigger_ids=[2370], enable=True)
        self.set_skill(trigger_ids=[2371], enable=True)
        self.set_skill(trigger_ids=[2372], enable=True)
        self.set_skill(trigger_ids=[2373], enable=True)
        self.set_skill(trigger_ids=[2374], enable=True)
        self.set_skill(trigger_ids=[2375], enable=True)
        self.set_skill(trigger_ids=[2376], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2359])
        self.set_skill(trigger_ids=[2360])
        self.set_skill(trigger_ids=[2361])
        self.set_skill(trigger_ids=[2362])
        self.set_skill(trigger_ids=[2363])
        self.set_skill(trigger_ids=[2364])
        self.set_skill(trigger_ids=[2365])
        self.set_skill(trigger_ids=[2366])
        self.set_skill(trigger_ids=[2367])
        self.set_skill(trigger_ids=[2368])
        self.set_skill(trigger_ids=[2369])
        self.set_skill(trigger_ids=[2370])
        self.set_skill(trigger_ids=[2371])
        self.set_skill(trigger_ids=[2372])
        self.set_skill(trigger_ids=[2373])
        self.set_skill(trigger_ids=[2374])
        self.set_skill(trigger_ids=[2375])
        self.set_skill(trigger_ids=[2376])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬13(self.ctx)


class 스킬13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2365], enable=True)
        self.set_skill(trigger_ids=[2366], enable=True)
        self.set_skill(trigger_ids=[2367], enable=True)
        self.set_skill(trigger_ids=[2368], enable=True)
        self.set_skill(trigger_ids=[2369], enable=True)
        self.set_skill(trigger_ids=[2370], enable=True)
        self.set_skill(trigger_ids=[2371], enable=True)
        self.set_skill(trigger_ids=[2372], enable=True)
        self.set_skill(trigger_ids=[2373], enable=True)
        self.set_skill(trigger_ids=[2374], enable=True)
        self.set_skill(trigger_ids=[2375], enable=True)
        self.set_skill(trigger_ids=[2376], enable=True)
        self.set_skill(trigger_ids=[2377], enable=True)
        self.set_skill(trigger_ids=[2378], enable=True)
        self.set_skill(trigger_ids=[2379], enable=True)
        self.set_skill(trigger_ids=[2380], enable=True)
        self.set_skill(trigger_ids=[2381], enable=True)
        self.set_skill(trigger_ids=[2382], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2365])
        self.set_skill(trigger_ids=[2366])
        self.set_skill(trigger_ids=[2367])
        self.set_skill(trigger_ids=[2368])
        self.set_skill(trigger_ids=[2369])
        self.set_skill(trigger_ids=[2370])
        self.set_skill(trigger_ids=[2371])
        self.set_skill(trigger_ids=[2372])
        self.set_skill(trigger_ids=[2373])
        self.set_skill(trigger_ids=[2374])
        self.set_skill(trigger_ids=[2375])
        self.set_skill(trigger_ids=[2376])
        self.set_skill(trigger_ids=[2377])
        self.set_skill(trigger_ids=[2378])
        self.set_skill(trigger_ids=[2379])
        self.set_skill(trigger_ids=[2380])
        self.set_skill(trigger_ids=[2381])
        self.set_skill(trigger_ids=[2382])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬14(self.ctx)


class 스킬14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2371], enable=True)
        self.set_skill(trigger_ids=[2372], enable=True)
        self.set_skill(trigger_ids=[2373], enable=True)
        self.set_skill(trigger_ids=[2374], enable=True)
        self.set_skill(trigger_ids=[2375], enable=True)
        self.set_skill(trigger_ids=[2376], enable=True)
        self.set_skill(trigger_ids=[2377], enable=True)
        self.set_skill(trigger_ids=[2378], enable=True)
        self.set_skill(trigger_ids=[2379], enable=True)
        self.set_skill(trigger_ids=[2380], enable=True)
        self.set_skill(trigger_ids=[2381], enable=True)
        self.set_skill(trigger_ids=[2382], enable=True)
        self.set_skill(trigger_ids=[2383], enable=True)
        self.set_skill(trigger_ids=[2384], enable=True)
        self.set_skill(trigger_ids=[2385], enable=True)
        self.set_skill(trigger_ids=[2386], enable=True)
        self.set_skill(trigger_ids=[2387], enable=True)
        self.set_skill(trigger_ids=[2388], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2371])
        self.set_skill(trigger_ids=[2372])
        self.set_skill(trigger_ids=[2373])
        self.set_skill(trigger_ids=[2374])
        self.set_skill(trigger_ids=[2375])
        self.set_skill(trigger_ids=[2376])
        self.set_skill(trigger_ids=[2377])
        self.set_skill(trigger_ids=[2378])
        self.set_skill(trigger_ids=[2379])
        self.set_skill(trigger_ids=[2380])
        self.set_skill(trigger_ids=[2381])
        self.set_skill(trigger_ids=[2382])
        self.set_skill(trigger_ids=[2383])
        self.set_skill(trigger_ids=[2384])
        self.set_skill(trigger_ids=[2385])
        self.set_skill(trigger_ids=[2386])
        self.set_skill(trigger_ids=[2387])
        self.set_skill(trigger_ids=[2388])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬15(self.ctx)


class 스킬15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2377], enable=True)
        self.set_skill(trigger_ids=[2378], enable=True)
        self.set_skill(trigger_ids=[2379], enable=True)
        self.set_skill(trigger_ids=[2380], enable=True)
        self.set_skill(trigger_ids=[2381], enable=True)
        self.set_skill(trigger_ids=[2382], enable=True)
        self.set_skill(trigger_ids=[2383], enable=True)
        self.set_skill(trigger_ids=[2384], enable=True)
        self.set_skill(trigger_ids=[2385], enable=True)
        self.set_skill(trigger_ids=[2386], enable=True)
        self.set_skill(trigger_ids=[2387], enable=True)
        self.set_skill(trigger_ids=[2388], enable=True)
        self.set_skill(trigger_ids=[2389], enable=True)
        self.set_skill(trigger_ids=[2390], enable=True)
        self.set_skill(trigger_ids=[2391], enable=True)
        self.set_skill(trigger_ids=[2392], enable=True)
        self.set_skill(trigger_ids=[2393], enable=True)
        self.set_skill(trigger_ids=[2394], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2377])
        self.set_skill(trigger_ids=[2378])
        self.set_skill(trigger_ids=[2379])
        self.set_skill(trigger_ids=[2380])
        self.set_skill(trigger_ids=[2381])
        self.set_skill(trigger_ids=[2382])
        self.set_skill(trigger_ids=[2383])
        self.set_skill(trigger_ids=[2384])
        self.set_skill(trigger_ids=[2385])
        self.set_skill(trigger_ids=[2386])
        self.set_skill(trigger_ids=[2387])
        self.set_skill(trigger_ids=[2388])
        self.set_skill(trigger_ids=[2389])
        self.set_skill(trigger_ids=[2390])
        self.set_skill(trigger_ids=[2391])
        self.set_skill(trigger_ids=[2392])
        self.set_skill(trigger_ids=[2393])
        self.set_skill(trigger_ids=[2394])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬16(self.ctx)


class 스킬16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2383], enable=True)
        self.set_skill(trigger_ids=[2384], enable=True)
        self.set_skill(trigger_ids=[2385], enable=True)
        self.set_skill(trigger_ids=[2386], enable=True)
        self.set_skill(trigger_ids=[2387], enable=True)
        self.set_skill(trigger_ids=[2388], enable=True)
        self.set_skill(trigger_ids=[2389], enable=True)
        self.set_skill(trigger_ids=[2390], enable=True)
        self.set_skill(trigger_ids=[2391], enable=True)
        self.set_skill(trigger_ids=[2392], enable=True)
        self.set_skill(trigger_ids=[2393], enable=True)
        self.set_skill(trigger_ids=[2394], enable=True)
        self.set_skill(trigger_ids=[2395], enable=True)
        self.set_skill(trigger_ids=[2396], enable=True)
        self.set_skill(trigger_ids=[2397], enable=True)
        self.set_skill(trigger_ids=[2398], enable=True)
        self.set_skill(trigger_ids=[2399], enable=True)
        self.set_skill(trigger_ids=[2400], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2383])
        self.set_skill(trigger_ids=[2384])
        self.set_skill(trigger_ids=[2385])
        self.set_skill(trigger_ids=[2386])
        self.set_skill(trigger_ids=[2387])
        self.set_skill(trigger_ids=[2388])
        self.set_skill(trigger_ids=[2389])
        self.set_skill(trigger_ids=[2390])
        self.set_skill(trigger_ids=[2391])
        self.set_skill(trigger_ids=[2392])
        self.set_skill(trigger_ids=[2393])
        self.set_skill(trigger_ids=[2394])
        self.set_skill(trigger_ids=[2395])
        self.set_skill(trigger_ids=[2396])
        self.set_skill(trigger_ids=[2397])
        self.set_skill(trigger_ids=[2398])
        self.set_skill(trigger_ids=[2399])
        self.set_skill(trigger_ids=[2400])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬17(self.ctx)


class 스킬17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2389], enable=True)
        self.set_skill(trigger_ids=[2390], enable=True)
        self.set_skill(trigger_ids=[2391], enable=True)
        self.set_skill(trigger_ids=[2392], enable=True)
        self.set_skill(trigger_ids=[2393], enable=True)
        self.set_skill(trigger_ids=[2394], enable=True)
        self.set_skill(trigger_ids=[2395], enable=True)
        self.set_skill(trigger_ids=[2396], enable=True)
        self.set_skill(trigger_ids=[2397], enable=True)
        self.set_skill(trigger_ids=[2398], enable=True)
        self.set_skill(trigger_ids=[2399], enable=True)
        self.set_skill(trigger_ids=[2400], enable=True)
        self.set_skill(trigger_ids=[2401], enable=True)
        self.set_skill(trigger_ids=[2402], enable=True)
        self.set_skill(trigger_ids=[2403], enable=True)
        self.set_skill(trigger_ids=[2404], enable=True)
        self.set_skill(trigger_ids=[2405], enable=True)
        self.set_skill(trigger_ids=[2406], enable=True)
        self.set_skill(trigger_ids=[2407], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2389])
        self.set_skill(trigger_ids=[2390])
        self.set_skill(trigger_ids=[2391])
        self.set_skill(trigger_ids=[2392])
        self.set_skill(trigger_ids=[2393])
        self.set_skill(trigger_ids=[2394])
        self.set_skill(trigger_ids=[2395])
        self.set_skill(trigger_ids=[2396])
        self.set_skill(trigger_ids=[2397])
        self.set_skill(trigger_ids=[2398])
        self.set_skill(trigger_ids=[2399])
        self.set_skill(trigger_ids=[2400])
        self.set_skill(trigger_ids=[2401])
        self.set_skill(trigger_ids=[2402])
        self.set_skill(trigger_ids=[2403])
        self.set_skill(trigger_ids=[2404])
        self.set_skill(trigger_ids=[2405])
        self.set_skill(trigger_ids=[2406])
        self.set_skill(trigger_ids=[2407])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬18(self.ctx)


class 스킬18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2401], enable=True)
        self.set_skill(trigger_ids=[2402], enable=True)
        self.set_skill(trigger_ids=[2403], enable=True)
        self.set_skill(trigger_ids=[2404], enable=True)
        self.set_skill(trigger_ids=[2405], enable=True)
        self.set_skill(trigger_ids=[2406], enable=True)
        self.set_skill(trigger_ids=[2407], enable=True)
        self.set_skill(trigger_ids=[2408], enable=True)
        self.set_skill(trigger_ids=[2409], enable=True)
        self.set_skill(trigger_ids=[2410], enable=True)
        self.set_skill(trigger_ids=[2411], enable=True)
        self.set_skill(trigger_ids=[2412], enable=True)
        self.set_skill(trigger_ids=[2413], enable=True)
        self.set_skill(trigger_ids=[2414], enable=True)
        self.set_skill(trigger_ids=[2415], enable=True)
        self.set_skill(trigger_ids=[2416], enable=True)
        self.set_skill(trigger_ids=[2417], enable=True)
        self.set_skill(trigger_ids=[2418], enable=True)
        self.set_skill(trigger_ids=[2419], enable=True)
        self.set_skill(trigger_ids=[2420], enable=True)
        self.set_skill(trigger_ids=[2421], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2401])
        self.set_skill(trigger_ids=[2402])
        self.set_skill(trigger_ids=[2403])
        self.set_skill(trigger_ids=[2404])
        self.set_skill(trigger_ids=[2405])
        self.set_skill(trigger_ids=[2406])
        self.set_skill(trigger_ids=[2407])
        self.set_skill(trigger_ids=[2408])
        self.set_skill(trigger_ids=[2409])
        self.set_skill(trigger_ids=[2410])
        self.set_skill(trigger_ids=[2411])
        self.set_skill(trigger_ids=[2412])
        self.set_skill(trigger_ids=[2413])
        self.set_skill(trigger_ids=[2414])
        self.set_skill(trigger_ids=[2415])
        self.set_skill(trigger_ids=[2416])
        self.set_skill(trigger_ids=[2417])
        self.set_skill(trigger_ids=[2418])
        self.set_skill(trigger_ids=[2419])
        self.set_skill(trigger_ids=[2420])
        self.set_skill(trigger_ids=[2421])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬19(self.ctx)


class 스킬19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2408], enable=True)
        self.set_skill(trigger_ids=[2409], enable=True)
        self.set_skill(trigger_ids=[2410], enable=True)
        self.set_skill(trigger_ids=[2411], enable=True)
        self.set_skill(trigger_ids=[2412], enable=True)
        self.set_skill(trigger_ids=[2413], enable=True)
        self.set_skill(trigger_ids=[2414], enable=True)
        self.set_skill(trigger_ids=[2415], enable=True)
        self.set_skill(trigger_ids=[2416], enable=True)
        self.set_skill(trigger_ids=[2417], enable=True)
        self.set_skill(trigger_ids=[2418], enable=True)
        self.set_skill(trigger_ids=[2419], enable=True)
        self.set_skill(trigger_ids=[2420], enable=True)
        self.set_skill(trigger_ids=[2421], enable=True)
        self.set_skill(trigger_ids=[2422], enable=True)
        self.set_skill(trigger_ids=[2423], enable=True)
        self.set_skill(trigger_ids=[2424], enable=True)
        self.set_skill(trigger_ids=[2425], enable=True)
        self.set_skill(trigger_ids=[2426], enable=True)
        self.set_skill(trigger_ids=[2427], enable=True)
        self.set_skill(trigger_ids=[2428], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2408])
        self.set_skill(trigger_ids=[2409])
        self.set_skill(trigger_ids=[2410])
        self.set_skill(trigger_ids=[2411])
        self.set_skill(trigger_ids=[2412])
        self.set_skill(trigger_ids=[2413])
        self.set_skill(trigger_ids=[2414])
        self.set_skill(trigger_ids=[2415])
        self.set_skill(trigger_ids=[2416])
        self.set_skill(trigger_ids=[2417])
        self.set_skill(trigger_ids=[2418])
        self.set_skill(trigger_ids=[2419])
        self.set_skill(trigger_ids=[2420])
        self.set_skill(trigger_ids=[2421])
        self.set_skill(trigger_ids=[2422])
        self.set_skill(trigger_ids=[2423])
        self.set_skill(trigger_ids=[2424])
        self.set_skill(trigger_ids=[2425])
        self.set_skill(trigger_ids=[2426])
        self.set_skill(trigger_ids=[2427])
        self.set_skill(trigger_ids=[2428])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬20(self.ctx)


class 스킬20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2415], enable=True)
        self.set_skill(trigger_ids=[2416], enable=True)
        self.set_skill(trigger_ids=[2417], enable=True)
        self.set_skill(trigger_ids=[2418], enable=True)
        self.set_skill(trigger_ids=[2419], enable=True)
        self.set_skill(trigger_ids=[2420], enable=True)
        self.set_skill(trigger_ids=[2421], enable=True)
        self.set_skill(trigger_ids=[2422], enable=True)
        self.set_skill(trigger_ids=[2423], enable=True)
        self.set_skill(trigger_ids=[2424], enable=True)
        self.set_skill(trigger_ids=[2425], enable=True)
        self.set_skill(trigger_ids=[2426], enable=True)
        self.set_skill(trigger_ids=[2427], enable=True)
        self.set_skill(trigger_ids=[2428], enable=True)
        self.set_skill(trigger_ids=[2429], enable=True)
        self.set_skill(trigger_ids=[2430], enable=True)
        self.set_skill(trigger_ids=[2431], enable=True)
        self.set_skill(trigger_ids=[2432], enable=True)
        self.set_skill(trigger_ids=[2433], enable=True)
        self.set_skill(trigger_ids=[2434], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2415])
        self.set_skill(trigger_ids=[2416])
        self.set_skill(trigger_ids=[2417])
        self.set_skill(trigger_ids=[2418])
        self.set_skill(trigger_ids=[2419])
        self.set_skill(trigger_ids=[2420])
        self.set_skill(trigger_ids=[2421])
        self.set_skill(trigger_ids=[2422])
        self.set_skill(trigger_ids=[2423])
        self.set_skill(trigger_ids=[2424])
        self.set_skill(trigger_ids=[2425])
        self.set_skill(trigger_ids=[2426])
        self.set_skill(trigger_ids=[2427])
        self.set_skill(trigger_ids=[2428])
        self.set_skill(trigger_ids=[2429])
        self.set_skill(trigger_ids=[2430])
        self.set_skill(trigger_ids=[2431])
        self.set_skill(trigger_ids=[2432])
        self.set_skill(trigger_ids=[2433])
        self.set_skill(trigger_ids=[2434])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬21(self.ctx)


class 스킬21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2422], enable=True)
        self.set_skill(trigger_ids=[2423], enable=True)
        self.set_skill(trigger_ids=[2424], enable=True)
        self.set_skill(trigger_ids=[2425], enable=True)
        self.set_skill(trigger_ids=[2426], enable=True)
        self.set_skill(trigger_ids=[2427], enable=True)
        self.set_skill(trigger_ids=[2428], enable=True)
        self.set_skill(trigger_ids=[2429], enable=True)
        self.set_skill(trigger_ids=[2430], enable=True)
        self.set_skill(trigger_ids=[2431], enable=True)
        self.set_skill(trigger_ids=[2432], enable=True)
        self.set_skill(trigger_ids=[2433], enable=True)
        self.set_skill(trigger_ids=[2434], enable=True)
        self.set_skill(trigger_ids=[2435], enable=True)
        self.set_skill(trigger_ids=[2436], enable=True)
        self.set_skill(trigger_ids=[2437], enable=True)
        self.set_skill(trigger_ids=[2438], enable=True)
        self.set_skill(trigger_ids=[2439], enable=True)
        self.set_skill(trigger_ids=[2440], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2422])
        self.set_skill(trigger_ids=[2423])
        self.set_skill(trigger_ids=[2424])
        self.set_skill(trigger_ids=[2425])
        self.set_skill(trigger_ids=[2426])
        self.set_skill(trigger_ids=[2427])
        self.set_skill(trigger_ids=[2428])
        self.set_skill(trigger_ids=[2429])
        self.set_skill(trigger_ids=[2430])
        self.set_skill(trigger_ids=[2431])
        self.set_skill(trigger_ids=[2432])
        self.set_skill(trigger_ids=[2433])
        self.set_skill(trigger_ids=[2434])
        self.set_skill(trigger_ids=[2435])
        self.set_skill(trigger_ids=[2436])
        self.set_skill(trigger_ids=[2437])
        self.set_skill(trigger_ids=[2438])
        self.set_skill(trigger_ids=[2439])
        self.set_skill(trigger_ids=[2440])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬22(self.ctx)


class 스킬22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2429], enable=True)
        self.set_skill(trigger_ids=[2430], enable=True)
        self.set_skill(trigger_ids=[2431], enable=True)
        self.set_skill(trigger_ids=[2432], enable=True)
        self.set_skill(trigger_ids=[2433], enable=True)
        self.set_skill(trigger_ids=[2434], enable=True)
        self.set_skill(trigger_ids=[2435], enable=True)
        self.set_skill(trigger_ids=[2436], enable=True)
        self.set_skill(trigger_ids=[2437], enable=True)
        self.set_skill(trigger_ids=[2438], enable=True)
        self.set_skill(trigger_ids=[2439], enable=True)
        self.set_skill(trigger_ids=[2440], enable=True)
        self.set_skill(trigger_ids=[2441], enable=True)
        self.set_skill(trigger_ids=[2442], enable=True)
        self.set_skill(trigger_ids=[2443], enable=True)
        self.set_skill(trigger_ids=[2444], enable=True)
        self.set_skill(trigger_ids=[2445], enable=True)
        self.set_skill(trigger_ids=[2446], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2429])
        self.set_skill(trigger_ids=[2430])
        self.set_skill(trigger_ids=[2431])
        self.set_skill(trigger_ids=[2432])
        self.set_skill(trigger_ids=[2433])
        self.set_skill(trigger_ids=[2434])
        self.set_skill(trigger_ids=[2435])
        self.set_skill(trigger_ids=[2436])
        self.set_skill(trigger_ids=[2437])
        self.set_skill(trigger_ids=[2438])
        self.set_skill(trigger_ids=[2439])
        self.set_skill(trigger_ids=[2440])
        self.set_skill(trigger_ids=[2441])
        self.set_skill(trigger_ids=[2442])
        self.set_skill(trigger_ids=[2443])
        self.set_skill(trigger_ids=[2444])
        self.set_skill(trigger_ids=[2445])
        self.set_skill(trigger_ids=[2446])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬23(self.ctx)


class 스킬23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2435], enable=True)
        self.set_skill(trigger_ids=[2436], enable=True)
        self.set_skill(trigger_ids=[2437], enable=True)
        self.set_skill(trigger_ids=[2438], enable=True)
        self.set_skill(trigger_ids=[2439], enable=True)
        self.set_skill(trigger_ids=[2440], enable=True)
        self.set_skill(trigger_ids=[2441], enable=True)
        self.set_skill(trigger_ids=[2442], enable=True)
        self.set_skill(trigger_ids=[2443], enable=True)
        self.set_skill(trigger_ids=[2444], enable=True)
        self.set_skill(trigger_ids=[2445], enable=True)
        self.set_skill(trigger_ids=[2446], enable=True)
        self.set_skill(trigger_ids=[2447], enable=True)
        self.set_skill(trigger_ids=[2448], enable=True)
        self.set_skill(trigger_ids=[2449], enable=True)
        self.set_skill(trigger_ids=[2450], enable=True)
        self.set_skill(trigger_ids=[2451], enable=True)
        self.set_skill(trigger_ids=[2452], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2435])
        self.set_skill(trigger_ids=[2436])
        self.set_skill(trigger_ids=[2437])
        self.set_skill(trigger_ids=[2438])
        self.set_skill(trigger_ids=[2439])
        self.set_skill(trigger_ids=[2440])
        self.set_skill(trigger_ids=[2441])
        self.set_skill(trigger_ids=[2442])
        self.set_skill(trigger_ids=[2443])
        self.set_skill(trigger_ids=[2444])
        self.set_skill(trigger_ids=[2445])
        self.set_skill(trigger_ids=[2446])
        self.set_skill(trigger_ids=[2447])
        self.set_skill(trigger_ids=[2448])
        self.set_skill(trigger_ids=[2449])
        self.set_skill(trigger_ids=[2450])
        self.set_skill(trigger_ids=[2451])
        self.set_skill(trigger_ids=[2452])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬24(self.ctx)


class 스킬24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2441], enable=True)
        self.set_skill(trigger_ids=[2442], enable=True)
        self.set_skill(trigger_ids=[2443], enable=True)
        self.set_skill(trigger_ids=[2444], enable=True)
        self.set_skill(trigger_ids=[2445], enable=True)
        self.set_skill(trigger_ids=[2446], enable=True)
        self.set_skill(trigger_ids=[2447], enable=True)
        self.set_skill(trigger_ids=[2448], enable=True)
        self.set_skill(trigger_ids=[2449], enable=True)
        self.set_skill(trigger_ids=[2450], enable=True)
        self.set_skill(trigger_ids=[2451], enable=True)
        self.set_skill(trigger_ids=[2452], enable=True)
        self.set_skill(trigger_ids=[2453], enable=True)
        self.set_skill(trigger_ids=[2454], enable=True)
        self.set_skill(trigger_ids=[2455], enable=True)
        self.set_skill(trigger_ids=[2456], enable=True)
        self.set_skill(trigger_ids=[2457], enable=True)
        self.set_skill(trigger_ids=[2458], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2441])
        self.set_skill(trigger_ids=[2442])
        self.set_skill(trigger_ids=[2443])
        self.set_skill(trigger_ids=[2444])
        self.set_skill(trigger_ids=[2445])
        self.set_skill(trigger_ids=[2446])
        self.set_skill(trigger_ids=[2447])
        self.set_skill(trigger_ids=[2448])
        self.set_skill(trigger_ids=[2449])
        self.set_skill(trigger_ids=[2450])
        self.set_skill(trigger_ids=[2451])
        self.set_skill(trigger_ids=[2452])
        self.set_skill(trigger_ids=[2453])
        self.set_skill(trigger_ids=[2454])
        self.set_skill(trigger_ids=[2455])
        self.set_skill(trigger_ids=[2456])
        self.set_skill(trigger_ids=[2457])
        self.set_skill(trigger_ids=[2458])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬25(self.ctx)


class 스킬25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2447], enable=True)
        self.set_skill(trigger_ids=[2448], enable=True)
        self.set_skill(trigger_ids=[2449], enable=True)
        self.set_skill(trigger_ids=[2450], enable=True)
        self.set_skill(trigger_ids=[2451], enable=True)
        self.set_skill(trigger_ids=[2452], enable=True)
        self.set_skill(trigger_ids=[2453], enable=True)
        self.set_skill(trigger_ids=[2454], enable=True)
        self.set_skill(trigger_ids=[2455], enable=True)
        self.set_skill(trigger_ids=[2456], enable=True)
        self.set_skill(trigger_ids=[2457], enable=True)
        self.set_skill(trigger_ids=[2458], enable=True)
        self.set_skill(trigger_ids=[2459], enable=True)
        self.set_skill(trigger_ids=[2460], enable=True)
        self.set_skill(trigger_ids=[2461], enable=True)
        self.set_skill(trigger_ids=[2462], enable=True)
        self.set_skill(trigger_ids=[2463], enable=True)
        self.set_skill(trigger_ids=[2464], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2447])
        self.set_skill(trigger_ids=[2448])
        self.set_skill(trigger_ids=[2449])
        self.set_skill(trigger_ids=[2450])
        self.set_skill(trigger_ids=[2451])
        self.set_skill(trigger_ids=[2452])
        self.set_skill(trigger_ids=[2453])
        self.set_skill(trigger_ids=[2454])
        self.set_skill(trigger_ids=[2455])
        self.set_skill(trigger_ids=[2456])
        self.set_skill(trigger_ids=[2457])
        self.set_skill(trigger_ids=[2458])
        self.set_skill(trigger_ids=[2459])
        self.set_skill(trigger_ids=[2460])
        self.set_skill(trigger_ids=[2461])
        self.set_skill(trigger_ids=[2462])
        self.set_skill(trigger_ids=[2463])
        self.set_skill(trigger_ids=[2464])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬26(self.ctx)


class 스킬26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2453], enable=True)
        self.set_skill(trigger_ids=[2454], enable=True)
        self.set_skill(trigger_ids=[2455], enable=True)
        self.set_skill(trigger_ids=[2456], enable=True)
        self.set_skill(trigger_ids=[2457], enable=True)
        self.set_skill(trigger_ids=[2458], enable=True)
        self.set_skill(trigger_ids=[2459], enable=True)
        self.set_skill(trigger_ids=[2460], enable=True)
        self.set_skill(trigger_ids=[2461], enable=True)
        self.set_skill(trigger_ids=[2462], enable=True)
        self.set_skill(trigger_ids=[2463], enable=True)
        self.set_skill(trigger_ids=[2464], enable=True)
        self.set_skill(trigger_ids=[2465], enable=True)
        self.set_skill(trigger_ids=[2466], enable=True)
        self.set_skill(trigger_ids=[2467], enable=True)
        self.set_skill(trigger_ids=[2468], enable=True)
        self.set_skill(trigger_ids=[2469], enable=True)
        self.set_skill(trigger_ids=[2470], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2453])
        self.set_skill(trigger_ids=[2454])
        self.set_skill(trigger_ids=[2455])
        self.set_skill(trigger_ids=[2456])
        self.set_skill(trigger_ids=[2457])
        self.set_skill(trigger_ids=[2458])
        self.set_skill(trigger_ids=[2459])
        self.set_skill(trigger_ids=[2460])
        self.set_skill(trigger_ids=[2461])
        self.set_skill(trigger_ids=[2462])
        self.set_skill(trigger_ids=[2463])
        self.set_skill(trigger_ids=[2464])
        self.set_skill(trigger_ids=[2465])
        self.set_skill(trigger_ids=[2466])
        self.set_skill(trigger_ids=[2467])
        self.set_skill(trigger_ids=[2468])
        self.set_skill(trigger_ids=[2469])
        self.set_skill(trigger_ids=[2470])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬27(self.ctx)


class 스킬27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2459], enable=True)
        self.set_skill(trigger_ids=[2460], enable=True)
        self.set_skill(trigger_ids=[2461], enable=True)
        self.set_skill(trigger_ids=[2462], enable=True)
        self.set_skill(trigger_ids=[2463], enable=True)
        self.set_skill(trigger_ids=[2464], enable=True)
        self.set_skill(trigger_ids=[2465], enable=True)
        self.set_skill(trigger_ids=[2466], enable=True)
        self.set_skill(trigger_ids=[2467], enable=True)
        self.set_skill(trigger_ids=[2468], enable=True)
        self.set_skill(trigger_ids=[2469], enable=True)
        self.set_skill(trigger_ids=[2470], enable=True)
        self.set_skill(trigger_ids=[2471], enable=True)
        self.set_skill(trigger_ids=[2472], enable=True)
        self.set_skill(trigger_ids=[2473], enable=True)
        self.set_skill(trigger_ids=[2474], enable=True)
        self.set_skill(trigger_ids=[2475], enable=True)
        self.set_skill(trigger_ids=[2476], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2459])
        self.set_skill(trigger_ids=[2460])
        self.set_skill(trigger_ids=[2461])
        self.set_skill(trigger_ids=[2462])
        self.set_skill(trigger_ids=[2463])
        self.set_skill(trigger_ids=[2464])
        self.set_skill(trigger_ids=[2465])
        self.set_skill(trigger_ids=[2466])
        self.set_skill(trigger_ids=[2467])
        self.set_skill(trigger_ids=[2468])
        self.set_skill(trigger_ids=[2469])
        self.set_skill(trigger_ids=[2470])
        self.set_skill(trigger_ids=[2471])
        self.set_skill(trigger_ids=[2472])
        self.set_skill(trigger_ids=[2473])
        self.set_skill(trigger_ids=[2474])
        self.set_skill(trigger_ids=[2475])
        self.set_skill(trigger_ids=[2476])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬28(self.ctx)


class 스킬28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2465], enable=True)
        self.set_skill(trigger_ids=[2466], enable=True)
        self.set_skill(trigger_ids=[2467], enable=True)
        self.set_skill(trigger_ids=[2468], enable=True)
        self.set_skill(trigger_ids=[2469], enable=True)
        self.set_skill(trigger_ids=[2470], enable=True)
        self.set_skill(trigger_ids=[2471], enable=True)
        self.set_skill(trigger_ids=[2472], enable=True)
        self.set_skill(trigger_ids=[2473], enable=True)
        self.set_skill(trigger_ids=[2474], enable=True)
        self.set_skill(trigger_ids=[2475], enable=True)
        self.set_skill(trigger_ids=[2476], enable=True)
        self.set_skill(trigger_ids=[2477], enable=True)
        self.set_skill(trigger_ids=[2478], enable=True)
        self.set_skill(trigger_ids=[2479], enable=True)
        self.set_skill(trigger_ids=[2480], enable=True)
        self.set_skill(trigger_ids=[2481], enable=True)
        self.set_skill(trigger_ids=[2482], enable=True)
        self.set_skill(trigger_ids=[2483], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2465])
        self.set_skill(trigger_ids=[2466])
        self.set_skill(trigger_ids=[2467])
        self.set_skill(trigger_ids=[2468])
        self.set_skill(trigger_ids=[2469])
        self.set_skill(trigger_ids=[2470])
        self.set_skill(trigger_ids=[2471])
        self.set_skill(trigger_ids=[2472])
        self.set_skill(trigger_ids=[2473])
        self.set_skill(trigger_ids=[2474])
        self.set_skill(trigger_ids=[2475])
        self.set_skill(trigger_ids=[2476])
        self.set_skill(trigger_ids=[2477])
        self.set_skill(trigger_ids=[2478])
        self.set_skill(trigger_ids=[2479])
        self.set_skill(trigger_ids=[2480])
        self.set_skill(trigger_ids=[2481])
        self.set_skill(trigger_ids=[2482])
        self.set_skill(trigger_ids=[2483])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬29(self.ctx)


class 스킬29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2471], enable=True)
        self.set_skill(trigger_ids=[2472], enable=True)
        self.set_skill(trigger_ids=[2473], enable=True)
        self.set_skill(trigger_ids=[2474], enable=True)
        self.set_skill(trigger_ids=[2475], enable=True)
        self.set_skill(trigger_ids=[2476], enable=True)
        self.set_skill(trigger_ids=[2477], enable=True)
        self.set_skill(trigger_ids=[2478], enable=True)
        self.set_skill(trigger_ids=[2479], enable=True)
        self.set_skill(trigger_ids=[2480], enable=True)
        self.set_skill(trigger_ids=[2481], enable=True)
        self.set_skill(trigger_ids=[2482], enable=True)
        self.set_skill(trigger_ids=[2483], enable=True)
        self.set_skill(trigger_ids=[2484], enable=True)
        self.set_skill(trigger_ids=[2485], enable=True)
        self.set_skill(trigger_ids=[2486], enable=True)
        self.set_skill(trigger_ids=[2487], enable=True)
        self.set_skill(trigger_ids=[2488], enable=True)
        self.set_skill(trigger_ids=[2489], enable=True)
        self.set_skill(trigger_ids=[2490], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2471])
        self.set_skill(trigger_ids=[2472])
        self.set_skill(trigger_ids=[2473])
        self.set_skill(trigger_ids=[2474])
        self.set_skill(trigger_ids=[2475])
        self.set_skill(trigger_ids=[2476])
        self.set_skill(trigger_ids=[2477])
        self.set_skill(trigger_ids=[2478])
        self.set_skill(trigger_ids=[2479])
        self.set_skill(trigger_ids=[2480])
        self.set_skill(trigger_ids=[2481])
        self.set_skill(trigger_ids=[2482])
        self.set_skill(trigger_ids=[2483])
        self.set_skill(trigger_ids=[2484])
        self.set_skill(trigger_ids=[2485])
        self.set_skill(trigger_ids=[2486])
        self.set_skill(trigger_ids=[2487])
        self.set_skill(trigger_ids=[2488])
        self.set_skill(trigger_ids=[2489])
        self.set_skill(trigger_ids=[2490])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬30(self.ctx)


class 스킬30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2477], enable=True)
        self.set_skill(trigger_ids=[2478], enable=True)
        self.set_skill(trigger_ids=[2479], enable=True)
        self.set_skill(trigger_ids=[2480], enable=True)
        self.set_skill(trigger_ids=[2481], enable=True)
        self.set_skill(trigger_ids=[2482], enable=True)
        self.set_skill(trigger_ids=[2483], enable=True)
        self.set_skill(trigger_ids=[2484], enable=True)
        self.set_skill(trigger_ids=[2485], enable=True)
        self.set_skill(trigger_ids=[2486], enable=True)
        self.set_skill(trigger_ids=[2487], enable=True)
        self.set_skill(trigger_ids=[2488], enable=True)
        self.set_skill(trigger_ids=[2489], enable=True)
        self.set_skill(trigger_ids=[2490], enable=True)
        self.set_skill(trigger_ids=[2491], enable=True)
        self.set_skill(trigger_ids=[2492], enable=True)
        self.set_skill(trigger_ids=[2493], enable=True)
        self.set_skill(trigger_ids=[2494], enable=True)
        self.set_skill(trigger_ids=[2495], enable=True)
        self.set_skill(trigger_ids=[2496], enable=True)
        self.set_skill(trigger_ids=[2497], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2477])
        self.set_skill(trigger_ids=[2478])
        self.set_skill(trigger_ids=[2479])
        self.set_skill(trigger_ids=[2480])
        self.set_skill(trigger_ids=[2481])
        self.set_skill(trigger_ids=[2482])
        self.set_skill(trigger_ids=[2483])
        self.set_skill(trigger_ids=[2484])
        self.set_skill(trigger_ids=[2485])
        self.set_skill(trigger_ids=[2486])
        self.set_skill(trigger_ids=[2487])
        self.set_skill(trigger_ids=[2488])
        self.set_skill(trigger_ids=[2489])
        self.set_skill(trigger_ids=[2490])
        self.set_skill(trigger_ids=[2491])
        self.set_skill(trigger_ids=[2492])
        self.set_skill(trigger_ids=[2493])
        self.set_skill(trigger_ids=[2494])
        self.set_skill(trigger_ids=[2495])
        self.set_skill(trigger_ids=[2496])
        self.set_skill(trigger_ids=[2497])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬31(self.ctx)


class 스킬31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2484], enable=True)
        self.set_skill(trigger_ids=[2485], enable=True)
        self.set_skill(trigger_ids=[2486], enable=True)
        self.set_skill(trigger_ids=[2487], enable=True)
        self.set_skill(trigger_ids=[2488], enable=True)
        self.set_skill(trigger_ids=[2489], enable=True)
        self.set_skill(trigger_ids=[2490], enable=True)
        self.set_skill(trigger_ids=[2491], enable=True)
        self.set_skill(trigger_ids=[2492], enable=True)
        self.set_skill(trigger_ids=[2493], enable=True)
        self.set_skill(trigger_ids=[2494], enable=True)
        self.set_skill(trigger_ids=[2495], enable=True)
        self.set_skill(trigger_ids=[2496], enable=True)
        self.set_skill(trigger_ids=[2497], enable=True)
        self.set_skill(trigger_ids=[2498], enable=True)
        self.set_skill(trigger_ids=[2499], enable=True)
        self.set_skill(trigger_ids=[2500], enable=True)
        self.set_skill(trigger_ids=[2501], enable=True)
        self.set_skill(trigger_ids=[2502], enable=True)
        self.set_skill(trigger_ids=[2503], enable=True)
        self.set_skill(trigger_ids=[2504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2484])
        self.set_skill(trigger_ids=[2485])
        self.set_skill(trigger_ids=[2486])
        self.set_skill(trigger_ids=[2487])
        self.set_skill(trigger_ids=[2488])
        self.set_skill(trigger_ids=[2489])
        self.set_skill(trigger_ids=[2490])
        self.set_skill(trigger_ids=[2491])
        self.set_skill(trigger_ids=[2492])
        self.set_skill(trigger_ids=[2493])
        self.set_skill(trigger_ids=[2494])
        self.set_skill(trigger_ids=[2495])
        self.set_skill(trigger_ids=[2496])
        self.set_skill(trigger_ids=[2497])
        self.set_skill(trigger_ids=[2498])
        self.set_skill(trigger_ids=[2499])
        self.set_skill(trigger_ids=[2500])
        self.set_skill(trigger_ids=[2501])
        self.set_skill(trigger_ids=[2502])
        self.set_skill(trigger_ids=[2503])
        self.set_skill(trigger_ids=[2504])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬32(self.ctx)


class 스킬32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2491], enable=True)
        self.set_skill(trigger_ids=[2492], enable=True)
        self.set_skill(trigger_ids=[2493], enable=True)
        self.set_skill(trigger_ids=[2494], enable=True)
        self.set_skill(trigger_ids=[2495], enable=True)
        self.set_skill(trigger_ids=[2496], enable=True)
        self.set_skill(trigger_ids=[2497], enable=True)
        self.set_skill(trigger_ids=[2498], enable=True)
        self.set_skill(trigger_ids=[2499], enable=True)
        self.set_skill(trigger_ids=[2500], enable=True)
        self.set_skill(trigger_ids=[2501], enable=True)
        self.set_skill(trigger_ids=[2502], enable=True)
        self.set_skill(trigger_ids=[2503], enable=True)
        self.set_skill(trigger_ids=[2504], enable=True)
        self.set_skill(trigger_ids=[2505], enable=True)
        self.set_skill(trigger_ids=[2506], enable=True)
        self.set_skill(trigger_ids=[2507], enable=True)
        self.set_skill(trigger_ids=[2508], enable=True)
        self.set_skill(trigger_ids=[2509], enable=True)
        self.set_skill(trigger_ids=[2510], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2491])
        self.set_skill(trigger_ids=[2492])
        self.set_skill(trigger_ids=[2493])
        self.set_skill(trigger_ids=[2494])
        self.set_skill(trigger_ids=[2495])
        self.set_skill(trigger_ids=[2496])
        self.set_skill(trigger_ids=[2497])
        self.set_skill(trigger_ids=[2498])
        self.set_skill(trigger_ids=[2499])
        self.set_skill(trigger_ids=[2500])
        self.set_skill(trigger_ids=[2501])
        self.set_skill(trigger_ids=[2502])
        self.set_skill(trigger_ids=[2503])
        self.set_skill(trigger_ids=[2504])
        self.set_skill(trigger_ids=[2505])
        self.set_skill(trigger_ids=[2506])
        self.set_skill(trigger_ids=[2507])
        self.set_skill(trigger_ids=[2508])
        self.set_skill(trigger_ids=[2509])
        self.set_skill(trigger_ids=[2510])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬33(self.ctx)


class 스킬33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2498], enable=True)
        self.set_skill(trigger_ids=[2499], enable=True)
        self.set_skill(trigger_ids=[2500], enable=True)
        self.set_skill(trigger_ids=[2501], enable=True)
        self.set_skill(trigger_ids=[2502], enable=True)
        self.set_skill(trigger_ids=[2503], enable=True)
        self.set_skill(trigger_ids=[2504], enable=True)
        self.set_skill(trigger_ids=[2505], enable=True)
        self.set_skill(trigger_ids=[2506], enable=True)
        self.set_skill(trigger_ids=[2507], enable=True)
        self.set_skill(trigger_ids=[2508], enable=True)
        self.set_skill(trigger_ids=[2509], enable=True)
        self.set_skill(trigger_ids=[2510], enable=True)
        self.set_skill(trigger_ids=[2511], enable=True)
        self.set_skill(trigger_ids=[2512], enable=True)
        self.set_skill(trigger_ids=[2513], enable=True)
        self.set_skill(trigger_ids=[2514], enable=True)
        self.set_skill(trigger_ids=[2515], enable=True)
        self.set_skill(trigger_ids=[2516], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬34대기(self.ctx)


class 스킬34대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2498])
        self.set_skill(trigger_ids=[2499])
        self.set_skill(trigger_ids=[2500])
        self.set_skill(trigger_ids=[2501])
        self.set_skill(trigger_ids=[2502])
        self.set_skill(trigger_ids=[2503])
        self.set_skill(trigger_ids=[2504])
        self.set_skill(trigger_ids=[2505])
        self.set_skill(trigger_ids=[2506])
        self.set_skill(trigger_ids=[2507])
        self.set_skill(trigger_ids=[2508])
        self.set_skill(trigger_ids=[2509])
        self.set_skill(trigger_ids=[2510])
        self.set_skill(trigger_ids=[2511])
        self.set_skill(trigger_ids=[2512])
        self.set_skill(trigger_ids=[2513])
        self.set_skill(trigger_ids=[2514])
        self.set_skill(trigger_ids=[2515])
        self.set_skill(trigger_ids=[2516])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬34(self.ctx)


class 스킬34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2505], enable=True)
        self.set_skill(trigger_ids=[2506], enable=True)
        self.set_skill(trigger_ids=[2507], enable=True)
        self.set_skill(trigger_ids=[2508], enable=True)
        self.set_skill(trigger_ids=[2509], enable=True)
        self.set_skill(trigger_ids=[2510], enable=True)
        self.set_skill(trigger_ids=[2511], enable=True)
        self.set_skill(trigger_ids=[2512], enable=True)
        self.set_skill(trigger_ids=[2513], enable=True)
        self.set_skill(trigger_ids=[2514], enable=True)
        self.set_skill(trigger_ids=[2515], enable=True)
        self.set_skill(trigger_ids=[2516], enable=True)
        self.set_skill(trigger_ids=[2517], enable=True)
        self.set_skill(trigger_ids=[2518], enable=True)
        self.set_skill(trigger_ids=[2519], enable=True)
        self.set_skill(trigger_ids=[2520], enable=True)
        self.set_skill(trigger_ids=[2521], enable=True)
        self.set_skill(trigger_ids=[2522], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬35대기(self.ctx)


class 스킬35대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2505])
        self.set_skill(trigger_ids=[2506])
        self.set_skill(trigger_ids=[2507])
        self.set_skill(trigger_ids=[2508])
        self.set_skill(trigger_ids=[2509])
        self.set_skill(trigger_ids=[2510])
        self.set_skill(trigger_ids=[2511])
        self.set_skill(trigger_ids=[2512])
        self.set_skill(trigger_ids=[2513])
        self.set_skill(trigger_ids=[2514])
        self.set_skill(trigger_ids=[2515])
        self.set_skill(trigger_ids=[2516])
        self.set_skill(trigger_ids=[2517])
        self.set_skill(trigger_ids=[2518])
        self.set_skill(trigger_ids=[2519])
        self.set_skill(trigger_ids=[2520])
        self.set_skill(trigger_ids=[2521])
        self.set_skill(trigger_ids=[2522])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬35(self.ctx)


class 스킬35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2511], enable=True)
        self.set_skill(trigger_ids=[2512], enable=True)
        self.set_skill(trigger_ids=[2513], enable=True)
        self.set_skill(trigger_ids=[2514], enable=True)
        self.set_skill(trigger_ids=[2515], enable=True)
        self.set_skill(trigger_ids=[2516], enable=True)
        self.set_skill(trigger_ids=[2517], enable=True)
        self.set_skill(trigger_ids=[2518], enable=True)
        self.set_skill(trigger_ids=[2519], enable=True)
        self.set_skill(trigger_ids=[2520], enable=True)
        self.set_skill(trigger_ids=[2521], enable=True)
        self.set_skill(trigger_ids=[2522], enable=True)
        self.set_skill(trigger_ids=[2523], enable=True)
        self.set_skill(trigger_ids=[2524], enable=True)
        self.set_skill(trigger_ids=[2525], enable=True)
        self.set_skill(trigger_ids=[2526], enable=True)
        self.set_skill(trigger_ids=[2527], enable=True)
        self.set_skill(trigger_ids=[2528], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬36대기(self.ctx)


class 스킬36대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[2511])
        self.set_skill(trigger_ids=[2512])
        self.set_skill(trigger_ids=[2513])
        self.set_skill(trigger_ids=[2514])
        self.set_skill(trigger_ids=[2515])
        self.set_skill(trigger_ids=[2516])
        self.set_skill(trigger_ids=[2517])
        self.set_skill(trigger_ids=[2518])
        self.set_skill(trigger_ids=[2519])
        self.set_skill(trigger_ids=[2520])
        self.set_skill(trigger_ids=[2521])
        self.set_skill(trigger_ids=[2522])
        self.set_skill(trigger_ids=[2523])
        self.set_skill(trigger_ids=[2524])
        self.set_skill(trigger_ids=[2525])
        self.set_skill(trigger_ids=[2526])
        self.set_skill(trigger_ids=[2527])
        self.set_skill(trigger_ids=[2528])


initial_state = 대기
