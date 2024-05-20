""" trigger/65000001_bd/wait.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='60', seconds=60, start_delay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 어나운스01(self.ctx)


class 어나운스01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26500201, text_id=26500201, duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어나운스01(self.ctx)
        if self.count_users(box_id=101) >= 2:
            return 종료(self.ctx)
        if self.time_expired(timer_id='60'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=26500201)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
