""" trigger/80000020_bonus/01_bonusobjectspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            # 맵에 유저가 있으면
            return SpawnOn(self.ctx)


class SpawnOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_user():
            # 맵에 유저가 없으면
            return SpawnOff(self.ctx)


class SpawnOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578])


initial_state = Setting
