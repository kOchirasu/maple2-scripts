""" trigger/02000375_bf/1123000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3400], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SecondPhaseEnd') == 1:
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3400])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
