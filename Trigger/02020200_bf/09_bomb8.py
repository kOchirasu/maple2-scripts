""" trigger/02020200_bf/09_bomb8.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[312], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[312]):
            return 폭탄_터짐(self.ctx)


class 폭탄_터짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2008], start_delay=1500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn') == 2:
            return 종료(self.ctx)
        return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn') == 2:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=40000):
            self.set_mesh(trigger_ids=[2008], visible=True, fade=3.0)
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[312])
        self.set_mesh(trigger_ids=[2008], start_delay=1500, fade=3.0)


initial_state = 대기
