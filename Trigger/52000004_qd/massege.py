""" trigger/52000004_qd/massege.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 메세지01(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 메세지01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200404, text_id=25200404)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 메세지02(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200404)


class 메세지02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200405, text_id=25200405)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 메세지02대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200405)


class 메세지02대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 메세지03(self.ctx)


class 메세지03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200406, text_id=25200406)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 메세지03대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200406)


class 메세지03대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 메세지04(self.ctx)


class 메세지04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200407, text_id=25200407)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 메세지04대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200407)


class 메세지04대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 메세지05(self.ctx)


class 메세지05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200408, text_id=25200408)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 메세지05대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200408)


class 메세지05대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return 메세지06(self.ctx)


class 메세지06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200409, text_id=25200409)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200409)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
