""" trigger/80000019_bonus/01_bonusobjectspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            # 맵에 유저가 있으면
            return SpawnOn(self.ctx)


class SpawnOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_user():
            # 맵에 유저가 없으면
            return SpawnOff(self.ctx)


class SpawnOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563])


initial_state = Setting
