""" trigger/99999905/pvp.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)
        self.set_mesh(trigger_ids=[3001,3002,3003,4001,4002,4003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=104) >= 1:
            return PvP(self.ctx)
        if self.time_expired(timer_id='30'):
            return PvP(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_pvp_zone(box_id=104, prepare_time=3, match_time=600, additional_effect_id=90001002, type=3, box_ids=[1,2,101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_event_ui(type=1, arg2='$99999905__PVP__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_event_ui(type=1, arg2='$99999905__PVP__1$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 어나운스2(self.ctx)


class 어나운스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_event_ui(type=1, arg2='$99999905__PVP__2$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 어나운스3(self.ctx)


class 어나운스3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_count_ui(text='$99999905__PVP__3$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            self.set_mesh(trigger_ids=[3001,3002,3003,4001,4002,4003])
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(box_id=104):
            return 게임종료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return None # Missing State: 보상


initial_state = 시작
