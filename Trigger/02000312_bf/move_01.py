""" trigger/02000312_bf/move_01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001], visible=True) # Invisible_Barrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103], visible=True) # Move_OnWater
        self.set_mesh(trigger_ids=[3200,3201,3202,3203]) # Move_onTop
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_breakable(trigger_ids=[4000]) # Move_GoUp
        self.set_breakable(trigger_ids=[4001]) # Move_GoUp
        self.set_breakable(trigger_ids=[4002]) # Move_GoUp
        self.set_breakable(trigger_ids=[4003]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003]) # Move_GoUp
        self.set_effect(trigger_ids=[5003]) # LeverHear
        self.set_effect(trigger_ids=[5002]) # Wheel
        self.set_interact_object(trigger_ids=[10001034], state=2) # Lever
        self.set_user_value(key='BoardApp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BoardApp') == 1:
            return BoardApp01(self.ctx)


class BoardApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001]) # Invisible_Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BoardApp02(self.ctx)


class BoardApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # UI
        self.show_guide_summary(entity_id=20031204, text_id=20031204) # 레버를 당겨 이동 장치 작동시키기
        self.set_effect(trigger_ids=[5003], visible=True) # LeverHear
        self.set_interact_object(trigger_ids=[10001034], state=1) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001034], state=0):
            return BoardGoUp01(self.ctx)


class BoardGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20031204)
        self.set_effect(trigger_ids=[5002], visible=True) # Wheel
        self.set_mesh(trigger_ids=[3100,3101,3102,3103], start_delay=100, fade=2.0) # Move_OnWater
        self.set_interact_object(trigger_ids=[10001034], state=2) # Lever
        self.set_breakable(trigger_ids=[4000], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4001], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4002], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4003], enable=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003], visible=True) # Move_GoUp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BoardGoUp02(self.ctx)


class BoardGoUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BoardDisApp01(self.ctx)


class BoardDisApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200,3201,3202,3203], visible=True, start_delay=100, fade=2.0) # Move_onTop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return BoardDisApp02(self.ctx)


class BoardDisApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000]) # Move_GoUp
        self.set_breakable(trigger_ids=[4001]) # Move_GoUp
        self.set_breakable(trigger_ids=[4002]) # Move_GoUp
        self.set_breakable(trigger_ids=[4003]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002]) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003]) # Move_GoUp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BoardReset01(self.ctx)


class BoardReset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3101,3102,3103], visible=True) # Move_OnWater

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BoardReset02(self.ctx)


class BoardReset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001034], state=1) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001034], state=0):
            return BoardReset03(self.ctx)


class BoardReset03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200,3201,3202,3203], start_delay=100, fade=2.0) # Move_onTop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BoardGoUp01(self.ctx)


initial_state = Wait
