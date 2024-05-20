""" trigger/02000349_bf/wall_09.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], visible=True, interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[109]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[109]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
