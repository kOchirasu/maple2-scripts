""" trigger/02000351_bf/teleport_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=1):
            return start_sound(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[9000005], visible=True) # TeleportSound EFfect On


class start_sound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return idle(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[9000005]) # TeleportSound EFfect On


initial_state = idle
