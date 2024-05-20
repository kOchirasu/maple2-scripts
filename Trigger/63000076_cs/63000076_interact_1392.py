""" trigger/63000076_cs/63000076_interact_1392.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[115], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001392], state=0):
            return 화난요정_01_1392(self.ctx)


class 화난요정_01_1392(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108])
        self.destroy_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[208])
        self.spawn_monster(spawn_ids=[215])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[208,215]):
            return 화난요정_02_1392(self.ctx)


class 화난요정_02_1392(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 화난요정_03_1392(self.ctx)


class 화난요정_03_1392(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[115], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
