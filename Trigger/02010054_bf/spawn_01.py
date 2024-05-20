""" trigger/02010054_bf/spawn_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000884], state=2)
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3127], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[610], visible=True)
        self.spawn_monster(spawn_ids=[2022], auto_target=False)
        self.set_mesh(trigger_ids=[3127], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2022]):
            self.set_interact_object(trigger_ids=[10000884], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
