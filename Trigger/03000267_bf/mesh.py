""" trigger/03000267_bf/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019], visible=True, interval=200, fade=2.0)
        self.set_interact_object(trigger_ids=[10000724], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000724], state=0):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019], interval=200, fade=2.0)
        self.set_timer(timer_id='25', seconds=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 대기(self.ctx)


initial_state = 대기
