""" trigger/80000015_bonus/spawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001326], state=2)
        self.set_interact_object(trigger_ids=[10001327], state=2)
        self.set_interact_object(trigger_ids=[10001328], state=2)
        self.set_interact_object(trigger_ids=[10001329], state=2)
        self.set_interact_object(trigger_ids=[10001330], state=2)
        self.set_interact_object(trigger_ids=[10001331], state=2)
        self.set_interact_object(trigger_ids=[10001332], state=2)
        self.set_interact_object(trigger_ids=[10001333], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 랜덤A(self.ctx)


class 랜덤A(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001326], state=1)
            return 랜덤B(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1501], auto_target=False)
            return 랜덤B(self.ctx)


class 랜덤B(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001327], state=1)
            return 랜덤C(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1502], auto_target=False)
            return 랜덤C(self.ctx)


class 랜덤C(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001328], state=1)
            return 랜덤D(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1503], auto_target=False)
            return 랜덤D(self.ctx)


class 랜덤D(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001329], state=1)
            return 랜덤E(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1504], auto_target=False)
            return 랜덤E(self.ctx)


class 랜덤E(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001330], state=1)
            return 랜덤F(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1505], auto_target=False)
            return 랜덤F(self.ctx)


class 랜덤F(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001331], state=1)
            return 랜덤G(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1506], auto_target=False)
            return 랜덤G(self.ctx)


class 랜덤G(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001332], state=1)
            return 랜덤H(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1507], auto_target=False)
            return 랜덤H(self.ctx)


class 랜덤H(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_interact_object(trigger_ids=[10001333], state=1)
            return 스폰1(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[1508], auto_target=False)
            return 스폰1(self.ctx)


class 스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021], score=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[112]):
            return 스폰2(self.ctx)


class 스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038], score=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[113]):
            return 스폰3(self.ctx)


class 스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061], score=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[114]):
            return 스폰4(self.ctx)


class 스폰4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083], score=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
