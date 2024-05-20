""" trigger/02000349_bf/wall_13.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316,31317,31318,31319,31320,31321,31322,31323,31324,31325,31326,31327,31328,31329,31330,31331,31332,31333], visible=True, interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[113]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316,31317,31318,31319,31320,31321,31322,31323,31324,31325,31326,31327,31328,31329,31330,31331,31332,31333], interval=10, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[113]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
