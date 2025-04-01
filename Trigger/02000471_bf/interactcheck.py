""" trigger/02000471_bf/interactcheck.xml """
import trigger_api


class check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040314, key='InteractClear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='10002019clear') == 1 and self.user_value(key='10002020clear') == 1 and self.user_value(key='10002021clear') == 1 and self.user_value(key='10002022clear') == 1 and self.user_value(key='10002023clear') == 1 and self.user_value(key='10002024clear') == 1:
            return clear(self.ctx)


class clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040314, key='InteractClear', value=1)
        self.set_user_value(trigger_id=2040322, key='InteractClear', value=1)


initial_state = check
