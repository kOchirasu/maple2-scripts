""" trigger/80000011_bonus/mainprocess_christmastree.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 이벤트대기중(self.ctx)


class 이벤트대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[201])
        self.set_ladder(trigger_ids=[202])
        self.set_ladder(trigger_ids=[203])
        self.set_ladder(trigger_ids=[204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 사다리나타남(self.ctx)


class 사다리나타남(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[201], visible=True, enable=True)
        self.set_ladder(trigger_ids=[202], visible=True, enable=True)
        self.set_ladder(trigger_ids=[203], visible=True, enable=True)
        self.set_ladder(trigger_ids=[204], visible=True, enable=True)
        self.set_timer(timer_id='2', seconds=30, start_delay=1, interval=1, v_offset=-90)
        self.show_guide_summary(entity_id=26300385, text_id=26300385)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            self.move_user()
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=26300385)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
