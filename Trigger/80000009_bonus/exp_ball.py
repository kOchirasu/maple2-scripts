""" trigger/80000009_bonus/exp_ball.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[402]):
            self.create_item(spawn_ids=[9001,9002,9003,9004,9005])
            return 초5(self.ctx)


class 초5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.create_item(spawn_ids=[9001])
            return 초10(self.ctx)


class 초10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.create_item(spawn_ids=[9001])
            return 초15(self.ctx)


class 초15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.create_item(spawn_ids=[9001])
            return 초20(self.ctx)


class 초20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.create_item(spawn_ids=[9001])
            return 초25(self.ctx)


class 초25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.create_item(spawn_ids=[9001])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
