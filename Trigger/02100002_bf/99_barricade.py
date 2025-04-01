""" trigger/02100002_bf/99_barricade.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PortalOn', value=0)
        self.set_user_value(key='MissionStart', value=0)
        self.set_user_value(key='DungeonClear', value=0)
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=20)
        self.set_portal(portal_id=21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn') == 1:
            return PortalOnDelay(self.ctx)


class PortalOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=21, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MissionStart') == 1:
            return CountDown(self.ctx)


class CountDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02100002_BF__99_BARRICADE__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return ShutDown(self.ctx)


# 임시 테스트용 데이터 세팅 가능 지점 포탈 열어놓기
class ShutDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=20)
        self.set_portal(portal_id=21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear') == 1:
            return Release(self.ctx)


class Release(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
