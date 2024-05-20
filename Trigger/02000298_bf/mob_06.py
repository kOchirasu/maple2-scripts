""" trigger/02000298_bf/mob_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            self.spawn_monster(spawn_ids=[1006], auto_target=False)
            return 종료(self.ctx)
        if self.user_detected(box_ids=[104]):
            self.spawn_monster(spawn_ids=[1006], auto_target=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
