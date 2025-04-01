""" trigger/02000367_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3107,3108,3109,3110,3111,3112], visible=True)
        self.set_mesh(trigger_ids=[3115,3116], visible=True)
        self.set_interact_object(trigger_ids=[10000989], state=2)
        self.set_interact_object(trigger_ids=[10000990], state=2)
        self.set_interact_object(trigger_ids=[10000991], state=2)
        self.set_interact_object(trigger_ids=[10000992], state=2)
        self.set_interact_object(trigger_ids=[10000993], state=2)
        self.set_interact_object(trigger_ids=[10000994], state=2)
        self.set_interact_object(trigger_ids=[10000997], state=2)
        self.set_interact_object(trigger_ids=[10000998], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return 전투01(self.ctx)


class 전투01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[21101,21102,21103,21104,21105,21106,21107,21201,21202,21203,21204,21205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[21101,21102,21103,21104,21105,21106,21107,21201,21202,21203,21204,21205]):
            return 전투02(self.ctx)


class 전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3107,3108])
        self.set_interact_object(trigger_ids=[10000989], state=1)
        self.set_interact_object(trigger_ids=[10000990], state=1)
        self.spawn_monster(spawn_ids=[22101,22102,22103,22104,22105,22106,22107,22201,22202,22203,22204,22205,22206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[22101,22102,22103,22104,22105,22106,22107,22201,22202,22203,22204,22205,22206]):
            return 전투03(self.ctx)


class 전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3109,3110])
        self.set_interact_object(trigger_ids=[10000991], state=1)
        self.set_interact_object(trigger_ids=[10000992], state=1)
        self.spawn_monster(spawn_ids=[23101,23102,23103,23104,23105,23106,23107,23108,23201,23202,23203,23204,23205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[23101,23102,23103,23104,23105,23106,23107,23108,23201,23202,23203,23204,23205]):
            self.set_mesh(trigger_ids=[3111,3112])
            self.set_interact_object(trigger_ids=[10000993], state=1)
            self.set_interact_object(trigger_ids=[10000994], state=1)
            self.set_user_value(trigger_id=9999901, key='main', value=1)
            return 합류대기(self.ctx)


class 합류대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main2') == 1:
            return 전투04(self.ctx)


class 전투04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[51101,51102,51103,51104,51105,51106,51107,51108,51201,51202,51203,51204,51205,51206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[51101,51102,51103,51104,51105,51106,51107,51108,51201,51202,51203,51204,51205,51206]):
            self.set_mesh(trigger_ids=[3115,3116])
            self.set_interact_object(trigger_ids=[10000997], state=1)
            self.set_interact_object(trigger_ids=[10000998], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
