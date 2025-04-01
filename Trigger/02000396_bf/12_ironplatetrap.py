""" trigger/02000396_bf/12_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3430,3431,3432,3433], visible=True) # IronPlateHold
        self.set_effect(trigger_ids=[5300]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5301]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5302]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5303]) # CubeSkillNotice
        self.destroy_monster(spawn_ids=[203,303])
        self.set_interact_object(trigger_ids=[10001131], state=0) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn') == 1:
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001131], state=1) # LeverForTrap
        self.set_effect(trigger_ids=[5300], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5301], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5302], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5303], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001131], state=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203,303], auto_target=False)
        self.set_mesh(trigger_ids=[3430,3431,3432,3433], start_delay=500, fade=2.0) # IronPlateHold
        self.set_effect(trigger_ids=[5300]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5301]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5302]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5303]) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203,303])


initial_state = Setting
