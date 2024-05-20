""" trigger/52100300_qd/archeon_interacobject_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002286], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002286], state=0):
            self.set_interact_object(trigger_ids=[10002286], state=2)
            return 재활성대기(self.ctx)


class 재활성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
