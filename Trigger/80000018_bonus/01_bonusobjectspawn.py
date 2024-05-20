""" trigger/80000018_bonus/01_bonusobjectspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            # 맵에 유저가 있으면
            return SpawnOn(self.ctx)


class SpawnOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_user():
            # 맵에 유저가 없으면
            return SpawnOff(self.ctx)


class SpawnOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548])


initial_state = Setting
