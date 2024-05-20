""" trigger/52000082_qd/main.xml """
import trigger_api


class mapskill(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return mapskill_start(self.ctx)


class mapskill_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000114, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return mapskill(self.ctx)


initial_state = mapskill
