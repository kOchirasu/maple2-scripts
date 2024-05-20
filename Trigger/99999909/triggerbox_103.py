""" trigger/99999909/triggerbox_103.xml """
import trigger_api


class 블록(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3031,3032,3033,3034,3035,3036,3037])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 블록생성(self.ctx)


class 블록생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[3031,3032,3033,3034,3035,3036,3037], visible=True, start_delay=4, fade=1)


initial_state = 블록
