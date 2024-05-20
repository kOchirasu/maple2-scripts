""" trigger/02000252_bf/elite_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8902]) # 가이드 화살표
        self.set_effect(trigger_ids=[605]) # 벨라 음성
        self.set_mesh(trigger_ids=[2113,2114,2115,2116,2117,2118], visible=True)
        self.set_mesh(trigger_ids=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=904) >= 1:
            return 딜레이(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2113,2114,2115,2116,2117,2118], visible=True)
        self.set_mesh(trigger_ids=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=904) >= 1:
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
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사(self.ctx)


class 벨라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_dialogue(type=1, spawn_id=1003, script='$02000252_BF__ELITE_02__0$', time=2)
        self.set_scene_skip(state=이동, action='nextState')
        # self.set_skip(state=이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라스킬(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_dialogue(type=1, spawn_id=1003, script='$02000252_BF__ELITE_02__1$', time=2)
        self.set_scene_skip(state=이동, action='nextState')
        # self.set_skip(state=이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라스킬2(self.ctx)


class 벨라스킬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_4')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이동(self.ctx)


class 벨라스킬2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_scene_skip() # Missing State: State
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_4')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이동2(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        # self.move_random_user(map_id=2000252, portal_id=9998, box_id=904, count=1)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[1102], auto_target=False)
        self.spawn_monster(spawn_ids=[1103], auto_target=False)
        self.spawn_monster(spawn_ids=[1104], auto_target=False)
        self.spawn_monster(spawn_ids=[1105], auto_target=False)
        self.spawn_monster(spawn_ids=[1106], auto_target=False)
        self.spawn_monster(spawn_ids=[1107], auto_target=False)
        self.spawn_monster(spawn_ids=[1108], auto_target=False)
        self.spawn_monster(spawn_ids=[1109], auto_target=False)
        self.spawn_monster(spawn_ids=[1110], auto_target=False)
        self.set_mesh(trigger_ids=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라삭제(self.ctx)


class 이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        # self.move_random_user(map_id=2000252, portal_id=9998, box_id=904, count=1)
        self.set_mesh(trigger_ids=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라삭제(self.ctx)


class 벨라삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[202]):
            return 개봉(self.ctx)


class 개봉(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8902], visible=True) # 가이드 화살표
        self.set_mesh(trigger_ids=[2113,2114,2115,2116,2117,2118])
        self.set_mesh(trigger_ids=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145])


initial_state = 대기
