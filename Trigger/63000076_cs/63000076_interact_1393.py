""" trigger/63000076_cs/63000076_interact_1393.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[112])
        self.spawn_monster(spawn_ids=[113])
        self.spawn_monster(spawn_ids=[114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001393], state=0):
            return 화난요정_01_1393(self.ctx)


class 화난요정_01_1393(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109])
        self.destroy_monster(spawn_ids=[110])
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.spawn_monster(spawn_ids=[209])
        self.spawn_monster(spawn_ids=[210])
        self.spawn_monster(spawn_ids=[211])
        self.spawn_monster(spawn_ids=[212])
        self.spawn_monster(spawn_ids=[213])
        self.spawn_monster(spawn_ids=[214])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[209,210,211,212,213,214]):
            return 화난요정_02_1393(self.ctx)


class 화난요정_02_1393(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 화난요정_03_1393(self.ctx)


class 화난요정_03_1393(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.spawn_monster(spawn_ids=[114], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
