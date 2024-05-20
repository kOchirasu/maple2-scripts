""" trigger/66000004_gd/pvp.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='60', seconds=30, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=104) >= 20:
            return PvP(self.ctx)
        if self.time_expired(timer_id='60'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='60')


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=104) >= 2:
            return PvP(self.ctx)
        if self.count_users(box_id=104) < 2:
            return 비김(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        # self.set_achievement(trigger_id=106, type='trigger', achieve='dailyquest_start')
        self.set_pvp_zone(box_id=104, prepare_time=3, match_time=600, additional_effect_id=90001002, type=3, box_ids=[1,2,101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
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
            return 종료(self.ctx)


class 비김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=5, arg2='$65000002_BD__PVP__5$', arg3='3000', arg4='0')
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
