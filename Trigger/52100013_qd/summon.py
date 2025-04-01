""" trigger/52100013_qd/summon.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') == 1:
            return Summon(self.ctx)


class Summon(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[501,502,503])
        self.set_user_value(trigger_id=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') == 1:
            return Summon_02(self.ctx)


class Summon_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52100013_QD__SUMMON__0$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52100013_QD__SUMMON__1$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[504,505,506])
        self.set_user_value(trigger_id=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') == 1:
            return Summon_03(self.ctx)


class Summon_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[507,508,509,510])
        self.set_user_value(trigger_id=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') == 1:
            return Summon(self.ctx)


initial_state = idle
