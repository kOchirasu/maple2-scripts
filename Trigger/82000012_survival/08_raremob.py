""" trigger/82000012_survival/08_raremob.xml """
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
        self.start_combine_spawn(group_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareMobOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])


initial_state = Setting
