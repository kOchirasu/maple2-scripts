""" trigger/52100301_qd/3000053_phase_4_interect_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200025,200026])
        self.set_interact_object(trigger_ids=[10003113], state=2) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_4_Interect_03') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_03') == 0:
            return 대기(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200025,200026], visible=True)
        self.set_interact_object(trigger_ids=[10003113], state=1) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003113], state=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_4_Interect_03') == 0:
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200025,200026])
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_3', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_4_Interect_03') == 0:
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_3', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_03') == 0:
            return 대기(self.ctx)


initial_state = 대기
