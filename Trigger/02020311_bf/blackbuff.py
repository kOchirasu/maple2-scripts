""" trigger/02020311_bf/blackbuff.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000406], state=0)
        self.set_interact_object(trigger_ids=[12000406], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.wait_tick(wait_tick=3000):
            self.set_interact_object(trigger_ids=[12000406], state=1)
            return 대기이(self.ctx)
        """
        if self.user_detected(box_ids=[801]):
            return 오브젝트체크(self.ctx)


class 대기이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)
        if self.user_detected(box_ids=[801]):
            return 오브젝트체크(self.ctx)


class 오브젝트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000406], state=0):
            return 오브젝트재생성(self.ctx)


class 오브젝트재생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_interact_object(trigger_ids=[12000406], state=1)
            return 오브젝트체크(self.ctx)


initial_state = 대기
