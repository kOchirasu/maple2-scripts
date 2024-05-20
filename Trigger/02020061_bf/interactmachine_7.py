""" trigger/02020061_bf/interactmachine_7.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002139], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002139], state=0):
            return 재활성대기(self.ctx)


class 재활성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_any_user_additional_effect(box_id=9107, additional_effect_id=99910370, level=1):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
