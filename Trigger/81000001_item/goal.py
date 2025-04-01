""" trigger/81000001_item/goal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gameStart') == 1:
            return 결승점(self.ctx)


class 결승점(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, is_only_winner=True, exp_rate=1.0)
        self.mini_game_give_reward(winner_box_id=102, content_type='UserOpenMiniGameExtraReward', game_name='UserMassive_Escape') # 1일 5회 추가 보너스
        self.end_mini_game(winner_box_id=102, is_only_winner=True, game_name='UserMassive_Escape')
        self.add_buff(box_ids=[102], skill_id=70000132, level=1)
        self.add_buff(box_ids=[102], skill_id=70000019, level=1) # 에레브의 축복 버프 걸어줌

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 결승점(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
