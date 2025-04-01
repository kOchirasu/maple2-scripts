""" trigger/02100001_bf/99_barricade.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CageDoorOpen', value=0)
        self.set_user_value(key='MissionStart', value=0)
        self.set_user_value(key='MissionComplete', value=0)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # Cage
        self.set_mesh(trigger_ids=[3100], visible=True) # Cage Door
        self.set_mesh(trigger_ids=[3101,3102,3103], visible=True) # Cage Mesh
        self.set_effect(trigger_ids=[5001]) # MetalDoorOpen 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # MetalDoorClose 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CageDoorOpen') == 1:
            return CageDoorOpenDelay(self.ctx)


class CageDoorOpenDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CageDoorOpen(self.ctx)


class CageDoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Open') # Cage
        self.set_mesh(trigger_ids=[3100], start_delay=300) # Cage Door

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MissionStart') == 1:
            return CountDown(self.ctx)


class CountDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui_script(type=BannerType.Text, script='$02100001_BF__99_BARRICADE__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return ShutDown(self.ctx)


class ShutDown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # MetalDoorClose 사운드 이펙트
        self.set_user_value(trigger_id=5, key='GiveBuffSlowly', value=1)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # Cage
        self.set_mesh(trigger_ids=[3100], visible=True) # Cage Door

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MissionComplete') == 1:
            return Release(self.ctx)


class Release(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Open') # Cage
        self.set_mesh(trigger_ids=[3100], start_delay=300) # Cage Door

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
