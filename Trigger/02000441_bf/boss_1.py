""" trigger/02000441_bf/boss_1.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_buff') == 1:
            return 몬스터_사망(self.ctx)


class 몬스터_사망(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[401]) or self.monster_dead(spawn_ids=[402]):
            return 초강력버프(self.ctx)


class 초강력버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[401,402], skill_id=49200001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        pass


initial_state = idle
