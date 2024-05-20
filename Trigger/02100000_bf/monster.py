""" trigger/02100000_bf/monster.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[80001], visible=True)
        self.set_mesh(trigger_ids=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010])
        self.set_mesh(trigger_ids=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014])

    def on_tick(self) -> trigger_api.Trigger:
        return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, minimap_visible=True)
        self.set_portal(portal_id=19, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[80001])
        self.spawn_monster(spawn_ids=[800011])
        self.spawn_monster(spawn_ids=[81001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # all_of:             <condition name="몬스터가죽어있으면" arg1="800011" />
        if self.monster_dead(spawn_ids=[80001]):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[80002])
        self.spawn_monster(spawn_ids=[800021])
        self.spawn_monster(spawn_ids=[810021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터사망_2(self.ctx)


class 몬스터사망_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[80002]) and self.monster_dead(spawn_ids=[800021]) and self.monster_dead(spawn_ids=[800011]):
            return 몬스터등장_3(self.ctx)


class 몬스터등장_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[81001])
        self.destroy_monster(spawn_ids=[81002])
        self.destroy_monster(spawn_ids=[810021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010], visible=True, interval=90, fade=1.0)
        self.set_mesh(trigger_ids=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014], visible=True, interval=90, fade=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 길생성(self.ctx)


class 길생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80001])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            pass


initial_state = 대기
