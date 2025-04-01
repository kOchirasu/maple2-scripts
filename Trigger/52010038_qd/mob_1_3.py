""" trigger/52010038_qd/mob_1_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='bombStart') == 1:
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2097], auto_target=False)
        self.spawn_npc_range(range_ids=[2008,2009,2010], is_auto_targeting=True)
        self.spawn_npc_range(range_ids=[2101,2102,2103,2104,2105,2106,2107], is_auto_targeting=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2097]):
            self.set_user_value(trigger_id=999001, key='CoreIsDead', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
