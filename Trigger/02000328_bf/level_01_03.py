""" trigger/02000328_bf/level_01_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5103])
        # self.spawn_monster(spawn_ids=[10003])
        self.set_mesh(trigger_ids=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316])
        self.set_mesh(trigger_ids=[41301,41302,41303], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10002]):
            # self.set_cube(trigger_ids=[5103], is_visible=True)
            self.set_mesh(trigger_ids=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316], visible=True, interval=200, fade=2.0)
            self.set_mesh(trigger_ids=[41301,41302,41303])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
