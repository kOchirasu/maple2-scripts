""" trigger/61000022_me/08_cheerupskill.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheerUpTimer') == 1:
            return CheerUpTimer_30(self.ctx)
        if self.user_value(key='CheerUpTimer') == 2:
            return CheerUpTimer_20(self.ctx)
        if self.user_value(key='CheerUpTimer') == 3:
            return CheerUpTimer_15(self.ctx)
        if self.user_value(key='CheerUpTimer') == 4:
            return CheerUpTimer_10(self.ctx)


class CheerUpTimer_30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, auto_remove=True) # Round1 / 30sec

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=26000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Round3 or Jackpot / 20sec
        self.set_timer(timer_id='1', seconds=20, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15, auto_remove=True) # Gamble / 15sec

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Round4 or Round 5 / 10sec
        self.set_timer(timer_id='1', seconds=10, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return GiveCheerUp(self.ctx)


class GiveCheerUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70000086, level=1, ignore_player=False, is_skill_set=False) # 할 수 있어 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheerUpTimer', value=0)
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
