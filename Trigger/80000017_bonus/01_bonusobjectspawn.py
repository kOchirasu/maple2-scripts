""" trigger/80000017_bonus/01_bonusobjectspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            # 맵에 유저가 있으면
            return SpawnOn(self.ctx)


class SpawnOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_user():
            # 맵에 유저가 없으면
            return SpawnOff(self.ctx)


class SpawnOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533])


initial_state = Setting
