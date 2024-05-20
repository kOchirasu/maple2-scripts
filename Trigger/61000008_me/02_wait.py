""" trigger/61000008_me/02_wait.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=60, start_delay=1) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100001, text_id=26100001, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) >= 50:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100002, text_id=26100002, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) >= 50:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
