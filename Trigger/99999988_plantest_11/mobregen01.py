""" trigger/99999988_plantest_11/mobregen01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 웜리젠91(self.ctx)


class 웜리젠91(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1,2,3])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1,2,3]):
            return 웜리젠91쿨타임(self.ctx)


class 웜리젠91쿨타임(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='9')
        self.set_timer(timer_id='9', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            self.reset_timer(timer_id='9')
            return 시작대기중(self.ctx)


initial_state = 시작대기중
