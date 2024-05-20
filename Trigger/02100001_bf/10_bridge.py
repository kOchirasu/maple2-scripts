""" trigger/02100001_bf/10_bridge.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3700,3701]) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9700]) and self.user_detected(box_ids=[9701]):
            return BridgeOn(self.ctx)


class BridgeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3700,3701], visible=True, start_delay=300, fade=2.0) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BridgeOff(self.ctx)


class BridgeOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3700,3701], fade=2.0) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
