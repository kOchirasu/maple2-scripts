""" trigger/52100110_qd/52100110_1.xml """
import trigger_api


class Ready521001101(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return 화이트박스생성521001101(self.ctx)
        if self.user_detected(box_ids=[2000]):
            return 화이트박스생성521001101(self.ctx)


class 화이트박스생성521001101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_mesh(trigger_ids=[10000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트체크521001101(self.ctx)


class 퀘스트체크521001101(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2000], quest_ids=[50101040], quest_states=[1]):
            return 화이트박스제거521001101(self.ctx)


class 화이트박스제거521001101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = Ready521001101
