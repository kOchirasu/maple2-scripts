""" trigger/52010022_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1003,1004], visible=True)


initial_state = idle
