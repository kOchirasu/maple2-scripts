""" trigger/02020101_bf/gimmick1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon') == 1:
            return 몬스터소환(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,202,203,204], auto_target=False)
        self.set_user_value(trigger_id=900003, key='summon', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,202,203,204], arg2=False)
        self.set_user_value(trigger_id=900003, key='summon', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
