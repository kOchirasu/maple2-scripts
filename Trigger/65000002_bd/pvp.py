""" trigger/65000002_bd/pvp.xml """
import trigger_api


class 시간표확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_timer(timer_id='60', seconds=60, interval=1)
        self.set_effect(trigger_ids=[601]) # 공지 효과음
        self.set_effect(trigger_ids=[602]) # 종료 효과음

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) >= 10:
            return 어나운스0(self.ctx)
        if self.time_expired(timer_id='60'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='60')


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) >= 2:
            return 어나운스0(self.ctx)
        if self.count_users(box_id=102) < 2:
            return 비김(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.play_system_sound_in_box(sound='BD_PVP_00')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__0$', arg3='6000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.play_system_sound_in_box(sound='BD_PVP_01')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__1$', arg3='6000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 어나운스2(self.ctx)


class 어나운스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.play_system_sound_in_box(sound='BD_PVP_02')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__2$', arg3='6000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 어나운스3(self.ctx)


class 어나운스3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.play_system_sound_in_box(sound='BD_PVP_03')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__3$', arg3='3000')
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return PvP(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(trigger_id=101, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(type=2)
        self.add_buff(box_ids=[101], skill_id=70000088, level=1, is_player=False, is_skill_set=False)
        self.add_buff(box_ids=[101], skill_id=70000089, level=1, is_player=False, is_skill_set=False)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.set_pvp_zone(box_id=101, prepare_time=5, match_time=300, additional_effect_id=90001002, type=2)
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(box_id=101):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.play_system_sound_in_box(sound='BD_PVP_04')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__4$', arg3='3000', arg4='101')
        self.set_effect(trigger_ids=[602], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 완료(self.ctx)


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


initial_state = 시간표확인
