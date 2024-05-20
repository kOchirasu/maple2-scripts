""" trigger/02010054_bf/spawn_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000885], state=2)
        self.set_effect(trigger_ids=[611])
        self.set_mesh(trigger_ids=[3128], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611], visible=True)
        self.set_mesh(trigger_ids=[3128], fade=5.0)
        self.spawn_monster(spawn_ids=[2023], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2023]):
            self.set_interact_object(trigger_ids=[10000885], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
