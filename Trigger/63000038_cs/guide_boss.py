""" trigger/63000038_cs/guide_boss.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossGuide') == 1:
            return 가이드분기(self.ctx)


class 가이드분기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            return 가이드출력(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002651], quest_states=[1]):
            return 가이드출력(self.ctx)


class 가이드출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26300384, text_id=26300384)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            self.hide_guide_summary(entity_id=26300384)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
