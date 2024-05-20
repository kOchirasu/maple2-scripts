""" trigger/63000050_cs/tria_seige_ready.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[20002263], quest_states=[3]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아침공전시작(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[20002263], quest_states=[2]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아방공호로(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[20002263], quest_states=[1]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아침공전시작(self.ctx)


class 트라이아침공전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000068, portal_id=1)


class 트라이아방공호로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000069, portal_id=1)


initial_state = start
