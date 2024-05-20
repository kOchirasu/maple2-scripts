""" trigger/02000066_bf/reward.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000011], state=2)
        self.set_interact_object(trigger_ids=[11000012], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return None # Missing State: 생성조건


initial_state = 시작
