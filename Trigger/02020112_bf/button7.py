""" trigger/02020112_bf/button7.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[931], job_code=0):
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=9907, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ButtonSuccess') == 1:
            return 종료(self.ctx)
        if self.user_detected(box_ids=[923], job_code=0):
            return 감지(self.ctx)


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=9907, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ButtonSuccess') == 1:
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[923], job_code=0):
            return 작동(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=9907, initial_sequence='Interaction_Lapentafoothold_A01_On')


initial_state = 대기
