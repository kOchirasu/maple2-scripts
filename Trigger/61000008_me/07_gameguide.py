""" trigger/61000008_me/07_gameguide.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameGuide') == 1:
            return GameGuideR1_30(self.ctx)
        if self.user_value(key='GameGuide') == 2:
            return GameGuideR2_20(self.ctx)
        if self.user_value(key='GameGuide') == 3:
            return GameGuideR3_15(self.ctx)
        if self.user_value(key='GameGuide') == 4:
            return GameGuideR4_10(self.ctx)
        if self.user_value(key='GameGuide') == 5:
            return GameGuideR5_10(self.ctx)
        if self.user_value(key='GameGuide') == 6:
            return GambleGuideR4_15(self.ctx)
        if self.user_value(key='GameGuide') == 7:
            return JackpotGuideR4_20(self.ctx)


class GameGuideR1_30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=29, auto_remove=True) # Round1 / 30sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


class GameGuideR2_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=19, auto_remove=True) # Round2 / 20sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


class GameGuideR3_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14, auto_remove=True) # Round3 / 15sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


class GameGuideR4_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=9, auto_remove=True) # Round4 / 10sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


class GameGuideR5_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=9, auto_remove=True) # Round5 / 10sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


# Normal GameGuide
class NormalGameGuide_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100804, text_id=26100804, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_02(self.ctx)


class NormalGameGuide_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100805, text_id=26100805, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_03(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100808, text_id=26100808, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_04(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100804, text_id=26100804, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_05(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100805, text_id=26100805, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_06(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100808, text_id=26100808, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Reset(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class GambleGuideR4_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14, auto_remove=True) # Round4 / 15sec Gamble

    def on_tick(self) -> trigger_api.Trigger:
        return GambleGameGuide_01(self.ctx)


class JackpotGuideR4_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=19, auto_remove=True) # Round4 / 20sec Jackpot

    def on_tick(self) -> trigger_api.Trigger:
        return GambleGameGuide_01(self.ctx)


# Gamble GameGuide
class GambleGameGuide_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100806, text_id=26100806, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GambleGameGuide_02(self.ctx)


class GambleGameGuide_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100807, text_id=26100807, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GambleGameGuide_03(self.ctx)


class GambleGameGuide_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100808, text_id=26100808, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GambleGameGuide_04(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class GambleGameGuide_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100806, text_id=26100806, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Reset(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GameGuide', value=0)
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
