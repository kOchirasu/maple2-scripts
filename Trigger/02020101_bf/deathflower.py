""" trigger/02020101_bf/deathflower.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='flower') == 1:
            return 랜덤대상선정(self.ctx)


class 랜덤대상선정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.random_additional_effect(target='pc', box_id=1003, target_count=1, tick=3, wait_tick=2, target_effect='Additional/Etc/Eff_Target_Select_Keep.xml', additional_effect_id=62100021)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            self.set_user_value(trigger_id=900007, key='flower', value=0)
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=2000):
            self.set_user_value(trigger_id=900007, key='flower', value=0)
            return 변수초기화(self.ctx)


class 변수초기화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='flower') == 0:
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=1004, skill_id=62100021, is_player=True)
        self.remove_buff(box_id=1004, skill_id=62100022, is_player=True)
        self.remove_buff(box_id=1004, skill_id=62100023, is_player=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
