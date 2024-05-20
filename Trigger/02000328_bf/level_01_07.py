""" trigger/02000328_bf/level_01_07.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5107])
        # self.spawn_monster(spawn_ids=[10007])
        self.set_mesh(trigger_ids=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719])
        self.set_mesh(trigger_ids=[41701], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10006]):
            # self.set_cube(trigger_ids=[5107], is_visible=True)
            self.set_mesh(trigger_ids=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719], visible=True, interval=200, fade=2.0)
            self.set_mesh(trigger_ids=[41701])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
