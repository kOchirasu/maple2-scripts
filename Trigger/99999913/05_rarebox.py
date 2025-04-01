""" trigger/99999913/05_rarebox.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareBoxOnCount', value=0)
        self.set_user_value(key='RareBoxOff', value=0)
        self.set_interact_object(trigger_ids=[11000038], state=2) # Rare Box

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOnCount') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000038], state=2) # Rare Box

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=180000):
            # 3분 180000
            return BoxOn(self.ctx)


class BoxOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='머쉬룸 타워 근처에 황금 상자가 나타났습니다!\\n황금 상자를 차지해보세요!', duration=5000, box_ids=['0'])
        self.set_interact_object(trigger_ids=[11000038], state=1) # Rare Box

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000038], state=2) # Rare Box

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)


initial_state = Setting
