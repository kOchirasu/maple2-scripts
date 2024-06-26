""" trigger/80000011_bonus/wait_christmastree.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, auto_remove=True, display=True, v_offset=-90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='ME_001_Wait_00')
        self.show_guide_summary(entity_id=26100001, text_id=26100001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=26100001)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='ME_001_Wait_00')
        self.show_guide_summary(entity_id=26100002, text_id=26100002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=26100002)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
