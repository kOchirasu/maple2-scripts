""" trigger/52100041_qd/buff.xml """
import trigger_api


# 에디셔널 이펙트를 계속 걸어줌
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[720], skill_id=71000009, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return buff_01(self.ctx)


class buff_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[720], skill_id=71000009, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


initial_state = idle
