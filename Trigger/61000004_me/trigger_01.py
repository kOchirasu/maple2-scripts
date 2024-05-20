""" trigger/61000004_me/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[301,302,303], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3201,3202,3301,3302,3401,3402,3403,3404])
        self.set_effect(trigger_ids=[71011])
        self.set_effect(trigger_ids=[71012])
        self.set_effect(trigger_ids=[71021])
        self.set_effect(trigger_ids=[71022])
        self.set_effect(trigger_ids=[72011])
        self.set_effect(trigger_ids=[72021])
        self.set_effect(trigger_ids=[73011])
        self.set_effect(trigger_ids=[73021])
        self.set_effect(trigger_ids=[73022])
        self.set_effect(trigger_ids=[73023])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 랜덤블록01(self.ctx)


class 랜덤블록01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3101], visible=True)
            self.set_effect(trigger_ids=[71011], visible=True)
            self.set_effect(trigger_ids=[71012], visible=True)
            return 랜덤블록02(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3102], visible=True)
            self.set_effect(trigger_ids=[71021], visible=True)
            self.set_effect(trigger_ids=[71022], visible=True)
            return 랜덤블록02(self.ctx)


class 랜덤블록02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3201], visible=True)
            self.set_effect(trigger_ids=[72011], visible=True)
            return 랜덤블록03(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3202], visible=True)
            self.set_effect(trigger_ids=[72021], visible=True)
            return 랜덤블록03(self.ctx)


class 랜덤블록03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3301], visible=True)
            self.set_effect(trigger_ids=[73011], visible=True)
            return 랜덤블록04(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3302], visible=True)
            self.set_effect(trigger_ids=[73021], visible=True)
            self.set_effect(trigger_ids=[73022], visible=True)
            self.set_effect(trigger_ids=[73023], visible=True)
            return 랜덤블록04(self.ctx)


class 랜덤블록04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3401,3402], visible=True)
            return 시작조건체크(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3403,3404], visible=True)
            return 시작조건체크(self.ctx)


class 시작조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return 어나운스0(self.ctx)
        if self.count_users(box_id=101) >= 20:
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='ME_Trigger_01_00')
        self.set_event_ui(type=1, arg2='$61000004_ME__TRIGGER_01__0$', arg3='7000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 어나운스1(self.ctx)


"""
전체 box : 105
대기 box : 101
승자 box : 102
"""
class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            self.set_mesh(trigger_ids=[301,302,303], start_delay=12)
            # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
            self.set_achievement(trigger_id=101, type='trigger', achieve='dailyquest_start')
            self.give_guild_exp(type=2)
            self.start_mini_game(box_id=105, round=1, game_name='escape')
            self.start_mini_game_round(box_id=105, round=1)
            self.move_user_to_box(box_id=101, portal_id=1)
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999111, key='gameStart', value=1)
        self.set_timer(timer_id='180', seconds=180, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='180'):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=102, type='trigger', achieve='escape_win')
        # self.mini_game_camera_direction(box_id=102, camera_id=901)
        self.set_event_ui(type=3, arg2='$61000004_ME__TRIGGER_01__2$', arg3='5000', arg4='102')
        self.set_event_ui(type=6, arg2='$61000004_ME__TRIGGER_01__3$', arg3='5000', arg4='!102')
        self.add_buff(box_ids=[102], skill_id=70000019, level=1)
        # self.set_event_ui(type=5, arg2='$61000004_ME__TRIGGER_01__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.end_mini_game_round(winner_box_id=102, exp_rate=0.25, is_gain_loser_bonus=True)
            self.mini_game_give_reward(winner_box_id=102, content_type='miniGame')
            self.end_mini_game(winner_box_id=102, game_name='escape')
            # self.set_local_camera(camera_id=901)
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
