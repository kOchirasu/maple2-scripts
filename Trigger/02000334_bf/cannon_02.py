""" trigger/02000334_bf/cannon_02.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[98011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon_02') == 1:
            return 마킹비표시(self.ctx)


class 마킹비표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[98011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90012, spawn_ids=[190]):
            # 돼지왕 타보를 감지
            return 마킹표시(self.ctx)


class 마킹표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[98011], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=90012, spawn_ids=[190]):
            return 마킹비표시(self.ctx)


initial_state = Idle
