""" trigger/02000346_bf/triggerwater.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, fade=5.0)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 발판랜덤(self.ctx)


class 발판랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)
        self.set_random_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], start_delay=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 유저체크(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return None # Missing State: 종료


class 유저체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[60002]):
            self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True)
            return 대기시간(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return None # Missing State: 종료


initial_state = 시작
