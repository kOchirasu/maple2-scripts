""" trigger/02000483_bf/02_searchhiddenroute.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[920,921]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[920,921], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PickRandomRoute(self.ctx)


class PickRandomRoute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 또 다른 방으로 이동할 수 있는 길을 찾으세요.
        self.show_guide_summary(entity_id=20039702, text_id=20039702, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return BehindWoodbox(self.ctx)
        if self.random_condition(weight=50.0):
            return BehindWardrope(self.ctx)


class BehindWoodbox(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3600, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3700, key='HiddenRouteOpen', value=1)


class BehindWardrope(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3600, key='HiddenRouteOpen', value=1)
        self.set_user_value(trigger_id=3700, key='HiddenRouteOpen', value=2)


initial_state = Wait
