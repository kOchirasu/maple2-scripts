""" trigger/65000001_bd/enter.xml """
import trigger_api


class 시간표확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_timer(timer_id='60', seconds=60, interval=1)
        self.set_effect(trigger_ids=[601]) # 공지 효과음

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 10:
            return 어나운스0(self.ctx)
        if self.time_expired(timer_id='60'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='60')


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 2:
            return 어나운스0(self.ctx)
        if self.count_users(box_id=101) < 2:
            return 비김(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.play_system_sound_in_box(sound='BD_Enter_00')
        self.set_event_ui(type=1, arg2='$65000001_BD__ENTER__0$', arg3='6000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.play_system_sound_in_box(sound='BD_Enter_01')
        self.set_event_ui(type=1, arg2='$65000001_BD__ENTER__1$', arg3='3000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return PvP(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
            self.set_achievement(trigger_id=105, type='trigger', achieve='dailyquest_start')
            self.give_guild_exp(type=2)
            self.set_pvp_zone(box_id=102, prepare_time=1, match_time=120, additional_effect_id=90001002, type=1)
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(box_id=102):
            return 게임종료(self.ctx)


class 비김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=5, arg2='$65000001_BD__ENTER__2$', arg3='3000', arg4='0')
            return 완료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=3, arg2='$65000001_BD__ENTER__3$', arg3='5000', arg4='102')
        self.add_buff(box_ids=[102], skill_id=70000063, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 보상(self.ctx)


class 보상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)
        self.play_system_sound_in_box(box_ids=[102], sound='BD_Enter_04')
        self.play_system_sound_in_box(box_ids=[103], sound='BD_Enter_05')
        self.set_event_ui(type=3, arg2='$65000001_BD__ENTER__4$', arg3='5000', arg4='102')
        self.set_event_ui(type=6, arg2='$65000001_BD__ENTER__5$', arg3='5000', arg4='!102')
        self.create_item(spawn_ids=[9001,9002,9003])
        self.create_item(spawn_ids=[9004], trigger_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시간표확인
