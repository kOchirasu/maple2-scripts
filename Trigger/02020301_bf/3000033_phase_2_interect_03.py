""" trigger/02020301_bf/3000033_phase_2_interect_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_2_Interect_03') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[702])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[702]):
            return 재생성(self.ctx)
        if self.user_value(key='Phase_2_Interect_03') == 0:
            return 대기(self.ctx)


class 재생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 시작(self.ctx)
        if self.user_value(key='Phase_2_Interect_03') == 0:
            return 대기(self.ctx)


initial_state = 대기
