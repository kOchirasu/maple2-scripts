""" trigger/02000328_bf/level_01_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5105])
        # self.spawn_monster(spawn_ids=[10005])
        self.set_mesh(trigger_ids=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521])
        self.set_mesh(trigger_ids=[41501,41502], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10002]):
            # self.set_cube(trigger_ids=[5105], is_visible=True)
            self.set_mesh(trigger_ids=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521], visible=True, interval=200, fade=2.0)
            self.set_mesh(trigger_ids=[41501,41502])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
