""" trigger/02020301_bf/300003_phase_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AI_Phase') == 2:
            return 패이즈_2_시작(self.ctx)


class 패이즈_2_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아르케온_탈것_생성(self.ctx)


class 아르케온_탈것_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000031, key='Phase_2_Interect_01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 쫄몹등장(self.ctx)


class 쫄몹등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000032, key='Phase_2_Interect_02', value=1)
        self.set_user_value(trigger_id=3000033, key='Phase_2_Interect_03', value=1)
        self.set_user_value(trigger_id=3000034, key='Phase_2_Interect_04', value=1)
        self.set_user_value(trigger_id=3000035, key='Phase_2_Interect_05', value=1)
        self.set_user_value(trigger_id=3000036, key='Phase_2_Interect_06', value=1)
        self.set_user_value(trigger_id=3000037, key='Phase_2_Interect_07', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 대기
