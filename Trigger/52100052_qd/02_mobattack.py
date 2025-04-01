""" trigger/52100052_qd/02_mobattack.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # DoorOpen
        self.set_effect(trigger_ids=[5002]) # DoorOpen
        self.set_effect(trigger_ids=[5003]) # DoorOpen
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Closed')
        self.set_agent(trigger_ids=[8000,8001], visible=True)
        self.set_agent(trigger_ids=[8002,8003], visible=True)
        self.set_agent(trigger_ids=[8004,8005], visible=True)
        self.destroy_monster(spawn_ids=[910,911,920,921,930,931]) # Mob
        self.set_user_value(key='MobSpawn', value=0)
        self.set_user_value(key='MobAttack', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawn') == 1:
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910,911], auto_target=False) # Mob01
        self.spawn_monster(spawn_ids=[920,921], auto_target=False) # Mob01
        self.spawn_monster(spawn_ids=[930,931], auto_target=False) # Mob01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobAttack') == 1:
            return MobAttackDelay(self.ctx)


class MobAttackDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return MobAttack01(self.ctx)


class MobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000,8001])
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened')
        self.set_effect(trigger_ids=[5001], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MobAttack02(self.ctx)


class MobAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8002,8003])
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.set_effect(trigger_ids=[5002], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MobAttack03(self.ctx)


class MobAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8004,8005])
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Opened')
        self.set_effect(trigger_ids=[5003], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910,911,920,921,930,931,901,902,903]):
            return MobClear(self.ctx)


class MobClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='MobClear', value=1)


initial_state = Setting
