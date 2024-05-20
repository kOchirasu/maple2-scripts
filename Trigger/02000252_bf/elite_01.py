""" trigger/02000252_bf/elite_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8901]) # 가이드 화살표
        self.set_effect(trigger_ids=[604]) # 벨라 음성
        self.set_mesh(trigger_ids=[2119,2120,2121,2122,2123,2124], visible=True)
        self.set_mesh(trigger_ids=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=903) >= 1:
            return 딜레이(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2119,2120,2121,2122,2123,2124], visible=True)
        self.set_mesh(trigger_ids=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=903) >= 1:
            return 딜레이2(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라(self.ctx)


class 딜레이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라2(self.ctx)


class 벨라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사(self.ctx)


class 벨라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_dialogue(type=1, spawn_id=1002, script='$02000252_BF__ELITE_01__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라스킬(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_dialogue(type=1, spawn_id=1002, script='$02000252_BF__ELITE_01__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라스킬2(self.ctx)


class 벨라스킬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이동(self.ctx)


class 벨라스킬2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이동2(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        # self.move_random_user(map_id=2000252, portal_id=9999, box_id=903, count=1)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[1093], auto_target=False)
        self.spawn_monster(spawn_ids=[1094], auto_target=False)
        self.spawn_monster(spawn_ids=[1095], auto_target=False)
        self.spawn_monster(spawn_ids=[1096], auto_target=False)
        self.spawn_monster(spawn_ids=[1097], auto_target=False)
        self.spawn_monster(spawn_ids=[1098], auto_target=False)
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.spawn_monster(spawn_ids=[1100], auto_target=False)
        self.spawn_monster(spawn_ids=[1101], auto_target=False)
        self.set_mesh(trigger_ids=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라삭제(self.ctx)


class 이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        # self.move_random_user(map_id=2000252, portal_id=9999, box_id=903, count=1)
        self.set_mesh(trigger_ids=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라삭제(self.ctx)


class 벨라삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return 개봉(self.ctx)


class 개봉(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8901], visible=True) # 가이드 화살표
        self.set_mesh(trigger_ids=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166])
        self.set_mesh(trigger_ids=[2119,2120,2121,2122,2123,2124])


initial_state = 대기
