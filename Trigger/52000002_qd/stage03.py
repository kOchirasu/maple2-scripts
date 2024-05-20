""" trigger/52000002_qd/stage03.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000612,10000613,10000614,10000615,10000616], state=2):
            return 박스체크(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 시작대기중(self.ctx)


class 박스체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 안내시작(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 시작대기중(self.ctx)


class 안내시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200206, text_id=25200206)
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200206)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[101]):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
