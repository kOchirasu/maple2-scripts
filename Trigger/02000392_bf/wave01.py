""" trigger/02000392_bf/wave01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='wave01') == 1:
            return 소환(self.ctx)
        if self.user_value(key='EndDungeon') == 1:
            return 종료(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[1901,1902,1903,1904,1905,1906,1907,1908,1909], is_auto_targeting=True, random_pick_count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 대기(self.ctx)
        if self.user_value(key='EndDungeon') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
