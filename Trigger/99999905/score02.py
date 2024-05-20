""" trigger/99999905/score02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000414], state=0):
            return 점수(self.ctx)


class 점수(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[604], visible=True)
        # self.allocate_battlefield_points(box_id=105, points=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
