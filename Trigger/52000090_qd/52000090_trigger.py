""" trigger/52000090_qd/52000090_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[50100470], quest_states=[1]):
            return 진행중일때20002272(self.ctx)
        if self.quest_user_detected(box_ids=[9100], quest_ids=[20002272], quest_states=[1]):
            return 진행중일때20002272(self.ctx)


class 진행중일때20002272(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_npc_range(range_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진행중일때02_20002272(self.ctx)


class 진행중일때02_20002272(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_npc_range(range_ids=[1011,1012,1013,1014,1015])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진행중일때03_20002272(self.ctx)


class 진행중일때03_20002272(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_npc_range(range_ids=[1016,1017,1018,1019,1020])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진행중일때04_20002272(self.ctx)


class 진행중일때04_20002272(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_npc_range(range_ids=[1021,1022,1023,1024,1025,1026,1027,1028,1029])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
