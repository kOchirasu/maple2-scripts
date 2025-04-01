""" trigger/02000490_bf/statue12.xml """
import trigger_api


class 세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[12], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 수신대기(self.ctx)


class 수신대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StatueAnimal01Death') == 1:
            self.set_mesh(trigger_ids=[12])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[12])


initial_state = 세팅
