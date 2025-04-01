""" trigger/52100052_qd/11_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3420,3421,3422,3423], visible=True) # IronPlateHold
        self.set_effect(trigger_ids=[5200]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203]) # CubeSkillNotice
        self.destroy_monster(spawn_ids=[202,302])
        self.set_interact_object(trigger_ids=[10002081], state=0) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn') == 1:
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002081], state=1) # LeverForTrap
        self.set_effect(trigger_ids=[5200], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002081], state=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)
        self.set_mesh(trigger_ids=[3420,3421,3422,3423], start_delay=500, fade=2.0) # IronPlateHold
        self.set_effect(trigger_ids=[5200]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203]) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202,302])


initial_state = Setting
