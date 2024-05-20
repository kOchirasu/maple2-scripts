""" trigger/99999922/event1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999910]):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='300', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1000]):
            return 진행2(self.ctx)


class 진행2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[999910], skill_id=49179111, level=1)
        self.set_timer(timer_id='300', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='300'):
            return 시작10(self.ctx)


class 시작10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='400', seconds=60)


initial_state = 대기
