""" trigger/02000396_bf/10_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3410,3411,3412,3413], visible=True) # IronPlateHold
        self.set_effect(trigger_ids=[5100]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103]) # CubeSkillNotice
        self.destroy_monster(spawn_ids=[201,301])
        self.set_interact_object(trigger_ids=[10001129], state=0) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn') == 1:
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001129], state=1) # LeverForTrap
        self.set_effect(trigger_ids=[5100], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001129], state=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,301], auto_target=False)
        self.set_mesh(trigger_ids=[3410,3411,3412,3413], start_delay=500, fade=2.0) # IronPlateHold
        self.set_effect(trigger_ids=[5100]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102]) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103]) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,301])


initial_state = Setting
