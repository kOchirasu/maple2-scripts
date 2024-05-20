""" trigger/51000003_dg/wait.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000018], state=2)
        self.set_interact_object(trigger_ids=[11000019], state=2)
        self.set_interact_object(trigger_ids=[11000020], state=2)
        self.set_interact_object(trigger_ids=[11000021], state=2)


initial_state = idle
