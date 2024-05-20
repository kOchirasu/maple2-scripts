""" trigger/02000328_bf/level_01_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5102])
        # self.spawn_monster(spawn_ids=[10002])
        self.set_mesh(trigger_ids=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10002]):
            self.set_cube(trigger_ids=[5102], is_visible=True)
            self.set_mesh(trigger_ids=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218], visible=True, interval=200, fade=2.0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
