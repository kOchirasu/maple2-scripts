""" trigger/02000328_bf/level_01_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5109])
        # self.spawn_monster(spawn_ids=[10009])
        self.set_mesh(trigger_ids=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922])
        self.set_mesh(trigger_ids=[41901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10006]):
            # self.set_cube(trigger_ids=[5109], is_visible=True)
            self.set_mesh(trigger_ids=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922], visible=True, interval=200, fade=2.0)
            self.set_mesh(trigger_ids=[41901])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
