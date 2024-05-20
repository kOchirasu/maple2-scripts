""" trigger/02000290_bf/wind.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701])
        self.set_effect(trigger_ids=[601]) # 스킬 준비 효과음
        self.set_effect(trigger_ids=[602]) # 스킬 발동 효과음
        self.set_effect(trigger_ids=[603]) # 스킬 발동 이펙트
        self.set_effect(trigger_ids=[604]) # 스킬 발동 이펙트
        self.set_effect(trigger_ids=[605]) # 스킬 발동 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 종료(self.ctx)
        if self.random_condition(weight=33.0):
            return A스킬작동(self.ctx)
        if self.random_condition(weight=33.0):
            return B스킬작동(self.ctx)
        if self.random_condition(weight=34.0):
            return C스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=4000):
            self.set_effect(trigger_ids=[601], visible=True)
            self.show_guide_summary(entity_id=20002906, text_id=20002906)
            return 스킬발동(self.ctx)


class B스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            self.set_effect(trigger_ids=[601], visible=True)
            self.show_guide_summary(entity_id=20002906, text_id=20002906)
            return 스킬발동(self.ctx)


class C스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=8000):
            self.set_effect(trigger_ids=[601], visible=True)
            self.show_guide_summary(entity_id=20002906, text_id=20002906)
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=4000):
            self.hide_guide_summary(entity_id=20002906)
            self.set_effect(trigger_ids=[602], visible=True)
            self.set_effect(trigger_ids=[603], visible=True)
            self.set_effect(trigger_ids=[604], visible=True)
            self.set_effect(trigger_ids=[605], visible=True)
            self.set_skill(trigger_ids=[701], enable=True)
            return 스킬랜덤(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002906)


initial_state = 시작대기중
