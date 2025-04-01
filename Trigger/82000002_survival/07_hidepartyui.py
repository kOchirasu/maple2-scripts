""" trigger/82000002_survival/07_hidepartyui.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='HidePartyUI', value=0)


class HidePartyUI(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_ui(ui_names=['PartyDialog'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return HidePartyUI(self.ctx)
        if self.user_value(key='HidePartyUI') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Setting
