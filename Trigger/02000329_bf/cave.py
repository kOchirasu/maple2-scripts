""" trigger/02000329_bf/cave.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[711]):
            return 동굴전환시작(self.ctx)


class 동굴전환시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6701])


initial_state = 대기
