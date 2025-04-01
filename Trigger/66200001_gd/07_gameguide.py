""" trigger/66200001_gd/07_gameguide.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameGuide') == 1:
            return GameGuide_20(self.ctx)


class GameGuide_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=19, auto_remove=True) # 20sec

    def on_tick(self) -> trigger_api.Trigger:
        return NormalGameGuide_01(self.ctx)


# Normal GameGuide
class NormalGameGuide_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26620104, text_id=26620104, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_02(self.ctx)


class NormalGameGuide_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26620105, text_id=26620105, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_03(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26620104, text_id=26620104, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NormalGameGuide_04(self.ctx)
        if self.time_expired(timer_id='1'):
            return Reset(self.ctx)


class NormalGameGuide_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26620105, text_id=26620105, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
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
