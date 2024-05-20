""" trigger/02000213_bf/spawncheck.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1099]):
            return 잡몹소멸(self.ctx)


class 잡몹소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1009])
        self.destroy_monster(spawn_ids=[1010])
        self.destroy_monster(spawn_ids=[1011])
        self.destroy_monster(spawn_ids=[1012])
        self.destroy_monster(spawn_ids=[1013])
        self.destroy_monster(spawn_ids=[1014])
        self.destroy_monster(spawn_ids=[1015])
        self.destroy_monster(spawn_ids=[1016])
        self.destroy_monster(spawn_ids=[1017])
        self.destroy_monster(spawn_ids=[1018])
        self.destroy_monster(spawn_ids=[1019])
        self.destroy_monster(spawn_ids=[1020])
        self.destroy_monster(spawn_ids=[1021])
        self.destroy_monster(spawn_ids=[1022])
        self.destroy_monster(spawn_ids=[1023])
        self.destroy_monster(spawn_ids=[1024])
        self.destroy_monster(spawn_ids=[1025])
        self.destroy_monster(spawn_ids=[1026])
        self.destroy_monster(spawn_ids=[1027])
        self.destroy_monster(spawn_ids=[1028])
        self.destroy_monster(spawn_ids=[1029])
        self.destroy_monster(spawn_ids=[1030])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1099]):
            return 대기(self.ctx)


initial_state = 대기
