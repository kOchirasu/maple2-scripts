""" trigger/02000349_bf/wall_07.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[37001,37002,37003,37004,37005,37006,37007,37008,37009,37010,37011,37012,37013,37014,37015,37016,37017,37018,37019], visible=True, interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[37001,37002,37003,37004,37005,37006,37007,37008,37009,37010,37011,37012,37013,37014,37015,37016,37017,37018,37019], interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[107]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
