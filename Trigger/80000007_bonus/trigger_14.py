""" trigger/80000007_bonus/trigger_14.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[303]):
            return 막힘(self.ctx)


class 막힘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[401,402,403,404,405,406,407,408,409])


initial_state = 대기
