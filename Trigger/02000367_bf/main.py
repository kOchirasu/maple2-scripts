""" trigger/02000367_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106], visible=True)
        self.set_mesh(trigger_ids=[3113,3114], visible=True)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=22)
        self.set_portal(portal_id=33)
        self.set_portal(portal_id=44)
        self.set_interact_object(trigger_ids=[10000983], state=2)
        self.set_interact_object(trigger_ids=[10000984], state=2)
        self.set_interact_object(trigger_ids=[10000985], state=2)
        self.set_interact_object(trigger_ids=[10000986], state=2)
        self.set_interact_object(trigger_ids=[10000987], state=2)
        self.set_interact_object(trigger_ids=[10000988], state=2)
        self.set_interact_object(trigger_ids=[10000995], state=2)
        self.set_interact_object(trigger_ids=[10000996], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 전투01(self.ctx)


class 전투01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[11101,11102,11103,11104,11105,11106,11107,11201,11202,11203,11204,11205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[11101,11102,11103,11104,11105,11106,11107,11201,11202,11203,11204,11205]):
            return 전투02(self.ctx)


class 전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102])
        self.set_interact_object(trigger_ids=[10000983], state=1)
        self.set_interact_object(trigger_ids=[10000984], state=1)
        self.spawn_monster(spawn_ids=[12101,12102,12201,12202,12203,12204,12205,12206,12207], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[12101,12102,12201,12202,12203,12204,12205,12206,12207]):
            return 전투03(self.ctx)


class 전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3103,3104])
        self.set_interact_object(trigger_ids=[10000985], state=1)
        self.set_interact_object(trigger_ids=[10000986], state=1)
        self.spawn_monster(spawn_ids=[13101,13102,13103,13104,13105,13106,13107,13108,13109,13201,13202,13203,13204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[13101,13102,13103,13104,13105,13106,13107,13108,13109,13201,13202,13203,13204]):
            self.set_mesh(trigger_ids=[3105,3106])
            self.set_interact_object(trigger_ids=[10000987], state=1)
            self.set_interact_object(trigger_ids=[10000988], state=1)
            return 합류대기(self.ctx)


class 합류대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main') == 1:
            return 전투04(self.ctx)


class 전투04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[30001,30002,30003,30004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[30001,30002,30003,30004]):
            return 포털개방(self.ctx)


class 포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, visible=True, enable=True)
        self.set_portal(portal_id=22, visible=True, enable=True)
        self.set_portal(portal_id=33, visible=True, enable=True)
        self.set_portal(portal_id=44, visible=True, enable=True)
        self.spawn_monster(spawn_ids=[41101,41102,41103,41104,41105,41106,41201,41202,41203,41204], auto_target=False)
        self.set_user_value(trigger_id=9999900, key='main2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[41101,41102,41103,41104,41105,41106,41201,41202,41203,41204]):
            self.set_mesh(trigger_ids=[3113,3114])
            self.set_interact_object(trigger_ids=[10000995], state=1)
            self.set_interact_object(trigger_ids=[10000996], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
