""" trigger/52100110_qd/52100110.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000])
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101040], quest_states=[1]):
            return 화이트박스제거(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[3]):
            return 로텔레포트52100105(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[2]):
            return 퀘스트용몬스터스폰(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[1]):
            return 퀘스트용몬스터스폰(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101020], quest_states=[3]):
            return 퀘스트용몬스터스폰(self.ctx)


class 퀘스트체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101040], quest_states=[1]):
            return 화이트박스제거(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[3]):
            return None # Missing State: State


class 로텔레포트52100105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000], visible=True)
        self.move_user(map_id=52100105, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


class 퀘스트용몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 화이트박스생성2(self.ctx)


class 화이트박스생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트체크2(self.ctx)


class 화이트박스제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = Ready
