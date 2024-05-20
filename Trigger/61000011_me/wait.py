""" trigger/61000011_me/wait.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
