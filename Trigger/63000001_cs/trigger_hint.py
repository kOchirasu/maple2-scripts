""" trigger/63000001_cs/trigger_hint.xml """
import trigger_api


class 힌트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818], visible=True, start_delay=2, fade=1000)
        self.set_timer(timer_id='99', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818])
        self.set_timer(timer_id='41', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='41'):
            return 힌트(self.ctx)


initial_state = 힌트
