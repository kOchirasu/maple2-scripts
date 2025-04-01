""" trigger/02020301_bf/3000062_phase_5_interect_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200033,200034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_5_Interect_02') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인터렉트_설정(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200033,200034], visible=True)
        self.set_interact_object(trigger_ids=[10003102], state=1) # 4페이즈 인터렉트 오브젝트 생성
        self.set_visible_breakable_object(trigger_ids=[5520])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003102], state=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_5_Interect_02') == 0:
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200033,200034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_5_Interect_02') == 0:
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_5_Interect_02') == 0:
            return 대기(self.ctx)


initial_state = 대기
