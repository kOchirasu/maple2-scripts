""" trigger/02010070_bf/wind2.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='wind02', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999994]):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[50,51,52,53,54,55,56,57,58,59,60,61], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='wind02') == 1:
            return Change(self.ctx)


class Change(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[34,35,36])
        self.set_mesh(trigger_ids=[53])
        self.set_mesh(trigger_ids=[46])
        self.set_mesh(trigger_ids=[59])
        self.set_mesh(trigger_ids=[44])
        self.set_mesh(trigger_ids=[45])


initial_state = Wait
