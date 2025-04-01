""" trigger/52010038_qd/mob_1_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveStart') == 1:
            return 생성(self.ctx)

    def on_exit(self) -> None:
        # 최초 3마리
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004], is_auto_targeting=True)
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004], is_auto_targeting=True)
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004], is_auto_targeting=True)
        self.spawn_monster(spawn_ids=[2011])


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011])
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004], is_auto_targeting=True, random_pick_count=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 생성(self.ctx)
        if self.user_value(key='WaveSlowDown') == 1:
            return 생성2(self.ctx)
        if self.user_value(key='WaveEnd') == 1:
            return 종료(self.ctx)


class 생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011])
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004], is_auto_targeting=True, random_pick_count=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 생성2(self.ctx)
        if self.user_value(key='WaveEnd') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
