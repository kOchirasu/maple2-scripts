""" trigger/02000191_bf/regentrigger0.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=100, spawn_ids=[900]):
            return 웜리젠91(self.ctx)


class 웜리젠91(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1,2])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1,2]):
            return 웜리젠91쿨타임(self.ctx)


class 웜리젠91쿨타임(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='9')
        self.set_timer(timer_id='9', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            self.reset_timer(timer_id='9')
            return 시작대기중(self.ctx)


initial_state = 시작대기중
