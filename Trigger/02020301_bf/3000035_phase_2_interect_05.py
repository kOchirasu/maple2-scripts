""" trigger/02020301_bf/3000035_phase_2_interect_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_2_Interect_05') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[704])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[704]):
            return 재생성(self.ctx)
        if self.user_value(key='Phase_2_Interect_05') == 0:
            return 대기(self.ctx)


class 재생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 시작(self.ctx)
        if self.user_value(key='Phase_2_Interect_05') == 0:
            return 대기(self.ctx)


initial_state = 대기
