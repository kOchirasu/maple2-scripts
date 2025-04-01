""" trigger/02020051_bf/106_summon_mob_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster_2') == 1:
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[1001], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster_2') == 2:
            return 대기(self.ctx)


initial_state = 대기
