""" trigger/02000471_bf/warp.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 1:
            return warp_1st(self.ctx)


class warp_1st(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return warp_1(self.ctx)
        if self.random_condition(weight=17.0):
            return warp_2(self.ctx)
        if self.random_condition(weight=16.0):
            return warp_3(self.ctx)
        if self.random_condition(weight=17.0):
            return warp_4(self.ctx)
        if self.random_condition(weight=16.0):
            return warp_5(self.ctx)
        if self.random_condition(weight=17.0):
            return warp_6(self.ctx)


class warp_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=11, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=12, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=13, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=14, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=15, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=16, box_id=720, count=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp') == 2:
            return warp_2nd(self.ctx)


class warp_2nd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17.0):
            return warp2_1(self.ctx)
        if self.random_condition(weight=17.0):
            return warp2_2(self.ctx)
        if self.random_condition(weight=16.0):
            return warp2_3(self.ctx)
        if self.random_condition(weight=17.0):
            return warp2_4(self.ctx)
        if self.random_condition(weight=16.0):
            return warp2_5(self.ctx)
        if self.random_condition(weight=17.0):
            return warp2_6(self.ctx)


class warp2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=11, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


class warp2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=12, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


class warp2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=13, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


class warp2_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=14, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


class warp2_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=15, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


class warp2_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2000471, portal_id=16, box_id=720, count=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARP__0$', duration=3000, box_ids=['0'])


initial_state = idle
