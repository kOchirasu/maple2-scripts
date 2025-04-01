""" trigger/52100201_qd/operate2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon') == 1:
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[206,207], auto_target=False)
        self.set_user_value(trigger_id=99990003, key='summon', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon') == 2:
            return 대기(self.ctx)


initial_state = 대기
