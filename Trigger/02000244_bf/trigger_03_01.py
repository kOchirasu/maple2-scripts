""" trigger/02000244_bf/trigger_03_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[705,706])


initial_state = 대기
