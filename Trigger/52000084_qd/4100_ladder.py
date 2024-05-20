""" trigger/52000084_qd/4100_ladder.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[4100]) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4101]) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4102]) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4103]) # Ladder_Shortcut
        self.set_interact_object(trigger_ids=[10001128], state=0) # LeverForLadder

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9200, spawn_ids=[101]):
            # 설눈이 감지
            return PCComeDown(self.ctx)


class PCComeDown(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9400]):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[4100], visible=True, enable=True, fade=2) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4101], visible=True, enable=True, fade=2) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4102], visible=True, enable=True, fade=2) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4103], visible=True, enable=True, fade=2) # Ladder_Shortcut


initial_state = Wait
