""" trigger/02000331_bf/safeportal05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=52)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99994]):
            return 포털작동(self.ctx)


class 포털작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=52, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 대기(self.ctx)


initial_state = 대기
