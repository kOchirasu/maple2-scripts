""" trigger/02010039_bf/checkbridge06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[5002], quest_ids=[40002110], quest_states=[1]):
            return 업적발생(self.ctx)


class 업적발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=5002, type='trigger', achieve='checkBridge')

    def on_tick(self) -> trigger_api.Trigger:
        return 초기화준비(self.ctx)


class 초기화준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
