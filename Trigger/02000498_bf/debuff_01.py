""" trigger/02000498_bf/debuff_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3600', seconds=3600)
        self.add_buff(box_ids=[102], skill_id=70000071, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3600'):
            return 대기(self.ctx)


initial_state = 대기
