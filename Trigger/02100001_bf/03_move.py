""" trigger/02100001_bf/03_move.xml """
import trigger_api


# 아프렐라 오지 : 선인장 쪽에서 올라올 수 있는 발판
class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001242], state=1) # CrowMove
        self.set_breakable(trigger_ids=[4501]) # Move
        self.set_visible_breakable_object(trigger_ids=[4501], visible=True) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001242], state=0):
            return MoveStart(self.ctx)


class MoveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4501], enable=True) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return MoveStop(self.ctx)


class MoveStop(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4501]) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001242], state=1) # CrowMove

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001242], state=0):
            return MoveStart(self.ctx)


initial_state = Wait
