""" trigger/52100053_qd/01_searchhiddenroute.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # PortalOn
        self.set_user_value(key='PortalOn', value=0)
        self.set_portal(portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PickRandomRoute(self.ctx)


class PickRandomRoute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 수 있는 길을 찾으세요.
        self.show_guide_summary(entity_id=20039701, text_id=20039701, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return BehindFireplace(self.ctx)
        if self.random_condition(weight=20.0):
            return BehindBookcase(self.ctx)
        if self.random_condition(weight=20.0):
            return FindKeyFromFabricbox(self.ctx)
        if self.random_condition(weight=20.0):
            return FindKeyFromCandle(self.ctx)
        if self.random_condition(weight=20.0):
            return FindKeyFromDocument(self.ctx)


class BehindBookcase(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3200, key='HiddenRouteOpen', value=1)
        self.set_user_value(trigger_id=3300, key='FindKey', value=2)
        self.set_user_value(trigger_id=3400, key='FindKey', value=2)
        self.set_user_value(trigger_id=3500, key='FindKey', value=2)


class BehindFireplace(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3100, key='HiddenRouteOpen', value=1)
        self.set_user_value(trigger_id=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3300, key='FindKey', value=2)
        self.set_user_value(trigger_id=3400, key='FindKey', value=2)
        self.set_user_value(trigger_id=3500, key='FindKey', value=2)


class FindKeyFromFabricbox(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3300, key='FindKey', value=1)
        self.set_user_value(trigger_id=3400, key='FindKey', value=2)
        self.set_user_value(trigger_id=3500, key='FindKey', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn') == 1:
            return PortalOn(self.ctx)


class FindKeyFromCandle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3300, key='FindKey', value=2)
        self.set_user_value(trigger_id=3400, key='FindKey', value=1)
        self.set_user_value(trigger_id=3500, key='FindKey', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn') == 1:
            return PortalOn(self.ctx)


class FindKeyFromDocument(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(trigger_id=3300, key='FindKey', value=2)
        self.set_user_value(trigger_id=3400, key='FindKey', value=2)
        self.set_user_value(trigger_id=3500, key='FindKey', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn') == 1:
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # PortalOn
        self.set_portal(portal_id=10, visible=True, enable=True)


initial_state = Wait
