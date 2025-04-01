""" trigger/02000066_bf/q10003067.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[103], quest_ids=[50001642], quest_states=[2]):
            return 포털활성화(self.ctx)


class 포털활성화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='woodsoflife') == 1:
            return None # Missing State: 포털비활성화


class 가이드활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=10003067)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
