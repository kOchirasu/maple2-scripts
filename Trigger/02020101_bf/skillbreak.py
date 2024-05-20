""" trigger/02020101_bf/skillbreak.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900001, key='SkillBreakFail', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002181, level=1):
            return 스킬브레이크_실패(self.ctx)


class 스킬브레이크_실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1003], skill_id=70002151, level=1, is_skill_set=False)
        self.set_user_value(trigger_id=900001, key='SkillBreakFail', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
