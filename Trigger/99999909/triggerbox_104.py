""" trigger/99999909/triggerbox_104.xml """
import trigger_api


class 블록(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3038,3039,3040,3041,3042,3043,3044,3045,3046])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 블록생성(self.ctx)


class 블록생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[3038,3039,3040,3041,3042,3043,3044,3045,3046], visible=True, start_delay=4, fade=1)


initial_state = 블록
