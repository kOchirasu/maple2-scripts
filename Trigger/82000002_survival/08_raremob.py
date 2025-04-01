""" trigger/82000002_survival/08_raremob.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareMobOnCount', value=0)
        self.set_user_value(key='RareMobOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareMobOnCount') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            # 30초 30000
            return MobSpawn(self.ctx)
        if self.user_value(key='RareMobOff') == 1:
            return Quit(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareMobOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354])


initial_state = Setting
