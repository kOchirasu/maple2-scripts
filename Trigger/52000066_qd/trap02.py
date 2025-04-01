""" trigger/52000066_qd/trap02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001071], state=0) # TrapLever
        self.set_mesh(trigger_ids=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, fade=3.0) # TrapMesh
        self.set_effect(trigger_ids=[5000]) # DownArrow
        self.set_user_value(key='TrapLeverOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapLeverOn') == 1:
            return TrapLeverOn01(self.ctx)


class TrapLeverOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001071], state=1) # TrapLever
        self.set_effect(trigger_ids=[5000], visible=True) # DownArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001071], state=0):
            return TrapFalse01(self.ctx)
        if self.user_value(key='TrapLeverOn') == 2:
            return Quit(self.ctx)


class TrapFalse01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # DownArrow
        self.set_interact_object(trigger_ids=[10001071], state=0) # TrapLever
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # TrapLever
        self.set_mesh(trigger_ids=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, start_delay=500, interval=50, fade=1.0) # TrapMesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            # 엘베 주변
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # DownArrow
        self.set_interact_object(trigger_ids=[10001071], state=0) # TrapLever


initial_state = Wait
