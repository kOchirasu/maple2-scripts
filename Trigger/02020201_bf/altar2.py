""" trigger/02020201_bf/altar2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 전투시작체크(self.ctx)


class 전투시작체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[101]):
            return 생성대기(self.ctx)


class 생성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gogo') == 1:
            return 생성대기2(self.ctx)


class 생성대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 전투체크(self.ctx)


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[101]):
            return 제단생성(self.ctx)


class 제단생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 제단파괴체크(self.ctx)


class 제단파괴체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[202]):
            return 제단재생성시간(self.ctx)


class 제단재생성시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='Sidephase', value=1, is_modify=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=40000):
            self.set_ai_extra_data(key='Sidephase', value=-1, is_modify=True)
            return 전투체크(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
