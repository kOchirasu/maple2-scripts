""" trigger/52000052_qd/805_penalty_05round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyMob', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyMob') == 1:
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart01(self.ctx)


class FirstWaveStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90584,90586], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90583,90589], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90590,90592], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90595,90597], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90580,90581,90582,90583,90584,90585,90586,90587,90588,90589,90590,90591,90592,90593,90594,90595,90596,90597,90598,90599]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[90580,90581,90582,90583,90584,90585,90586,90587,90588,90589,90590,90591,90592,90593,90594,90595,90596,90597,90598,90599])
        self.set_user_value(trigger_id=905, key='PenaltyFinish', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
