""" trigger/02000355_bf/actor09.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[609])
        self.set_actor(trigger_id=209, visible=True, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1901]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[609], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 더미해제(self.ctx)


class 더미해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=209, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2009]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
