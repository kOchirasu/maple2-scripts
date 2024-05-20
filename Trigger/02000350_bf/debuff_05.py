""" trigger/02000350_bf/debuff_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3600', seconds=3600)
        self.add_buff(box_ids=[106], skill_id=70000071, level=5, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3600'):
            return 대기(self.ctx)


initial_state = 대기
