""" trigger/99999883/testtrigger3.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001010], state=0) # FlyingCloud
        self.set_breakable(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001010], state=0):
            return TakeOffFlyingCloud01(self.ctx)


class TakeOffFlyingCloud01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_interact_object(trigger_ids=[10001010], state=2) # FlyingCloud
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True)
        self.set_breakable(trigger_ids=[4000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TakeOffFlyingCloud02(self.ctx)


class TakeOffFlyingCloud02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=99999883, portal_id=100, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TakeOffFlyingCloud03(self.ctx)


class TakeOffFlyingCloud03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return TakeOffFlyingCloud04(self.ctx)


class TakeOffFlyingCloud04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=99999883, portal_id=101, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4000])


initial_state = Wait
