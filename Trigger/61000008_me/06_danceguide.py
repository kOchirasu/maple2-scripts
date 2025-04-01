""" trigger/61000008_me/06_danceguide.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DanceGuide') == 1:
            return DanceGuideP1_Random(self.ctx)
        if self.user_value(key='DanceGuide') == 2:
            return DanceGuideP2_Random(self.ctx)
        if self.user_value(key='DanceGuide') == 3:
            return DanceGuideP3_01(self.ctx)
        if self.user_value(key='DanceGuide') == 41:
            return DanceGuideP41_01(self.ctx)
        if self.user_value(key='DanceGuide') == 42:
            return DanceGuideP42_01(self.ctx)
        if self.user_value(key='DanceGuide') == 51:
            return DanceGuideP51_01(self.ctx)
        if self.user_value(key='DanceGuide') == 52:
            return DanceGuideP52_01(self.ctx)
        if self.user_value(key='DanceGuide') == 61:
            return DanceGuideP61_01(self.ctx)
        if self.user_value(key='DanceGuide') == 62:
            return DanceGuideP62_01(self.ctx)
        if self.user_value(key='DanceGuide') == 71:
            return DanceGuideP71_01(self.ctx)
        if self.user_value(key='DanceGuide') == 72:
            return DanceGuideP72_01(self.ctx)


class DanceGuideP1_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return DanceGuideP11_01(self.ctx)
        if self.random_condition(weight=50.0):
            return DanceGuideP12_01(self.ctx)


class DanceGuideP2_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return DanceGuideP21_01(self.ctx)
        if self.random_condition(weight=50.0):
            return DanceGuideP22_01(self.ctx)


# 9000ms Type1
class DanceGuideP11_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DanceGuideP11_02(self.ctx)


class DanceGuideP11_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Reset(self.ctx)


# 9000ms Type2
class DanceGuideP12_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DanceGuideP12_02(self.ctx)


class DanceGuideP12_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Reset(self.ctx)


# 12000ms Type1
class DanceGuideP21_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DanceGuideP21_02(self.ctx)


class DanceGuideP21_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Reset(self.ctx)


# 12000ms Type2
class DanceGuideP22_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DanceGuideP22_02(self.ctx)


class DanceGuideP22_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Reset(self.ctx)


# 15000ms
class DanceGuideP3_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DanceGuideP3_02(self.ctx)


class DanceGuideP3_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DanceGuideP3_03(self.ctx)


class DanceGuideP3_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Reset(self.ctx)


# 7000ms+ 9000ms First
class DanceGuideP41_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Reset(self.ctx)


# 7000ms+ 9000ms Second
class DanceGuideP42_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DanceGuideP42_02(self.ctx)


class DanceGuideP42_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Reset(self.ctx)


# 9000ms+ 7000ms First
class DanceGuideP51_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DanceGuideP51_02(self.ctx)


class DanceGuideP51_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Reset(self.ctx)


# 9000ms+ 7000ms Second
class DanceGuideP52_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Reset(self.ctx)


# 12000ms+ 7000ms First
class DanceGuideP61_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DanceGuideP61_02(self.ctx)


class DanceGuideP61_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Reset(self.ctx)


# 12000ms+ 7000ms Second
class DanceGuideP62_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Reset(self.ctx)


# 7000ms+ 12000ms First
class DanceGuideP71_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100801, text_id=26100801, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Reset(self.ctx)


# 7000ms+ 12000ms Second
class DanceGuideP72_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100803, text_id=26100803, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return DanceGuideP72_02(self.ctx)


class DanceGuideP72_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26100802, text_id=26100802, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='DanceGuide', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
