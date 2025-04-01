""" trigger/52000052_qd/808_penalty_08round.xml """
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
        self.spawn_monster(spawn_ids=[90886,90888], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90881,90883], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90890,90892], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90897,90899], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90880,90881,90882,90883,90884,90885,90886,90887,90888,90889,90890,90891,90892,90893,90894,90895,90896,90897,90898,90899]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[90880,90881,90882,90883,90884,90885,90886,90887,90888,90889,90890,90891,90892,90893,90894,90895,90896,90897,90898,90899])
        self.set_user_value(trigger_id=908, key='PenaltyFinish', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
