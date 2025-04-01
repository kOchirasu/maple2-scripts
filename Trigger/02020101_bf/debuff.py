""" trigger/02020101_bf/debuff.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Debuff') == 1:
            return 디버프시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 디버프시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='Debuff', value=0)
        self.add_buff(box_ids=[1004], skill_id=70002122, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Debuff') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900002, key='Debuff', value=0)
        self.remove_buff(box_id=1004, skill_id=70002122, is_player=True)
        self.add_buff(box_ids=[1004], skill_id=70002123, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Debuff') == 0:
            return 대기(self.ctx)


initial_state = 대기
