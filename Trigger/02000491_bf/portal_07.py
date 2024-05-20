""" trigger/02000491_bf/portal_07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=807)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000989], state=0):
            return 포털활성화(self.ctx)


class 포털활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=807, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_interact_object(trigger_ids=[10000989], state=1)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
