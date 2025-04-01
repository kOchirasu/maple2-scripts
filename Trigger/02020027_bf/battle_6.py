""" trigger/02020027_bf/battle_6.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990009, key='summon_2', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1003]):
            return 스킬사용(self.ctx)


class 스킬사용(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon_2') == 1:
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False, delay=1000)

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 길막삭제


initial_state = 전투시작
