""" trigger/99999927/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=99910120, level=1, is_player=False, is_skill_set=False)
        self.set_gravity(gravity=-25.0)
        self.spawn_monster(spawn_ids=[201])


initial_state = idle
