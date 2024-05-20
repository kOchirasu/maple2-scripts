""" trigger/61000006_me/trigger_03.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[402]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=999, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[501,502,503,504,505,506,507,508,509], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return 어나운스0(self.ctx)
        if self.count_users(box_id=402) >= 20:
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='ME_Trigger_03_00')
        self.set_event_ui(type=1, arg2='$61000006_ME__TRIGGER_03__0$', arg3='7000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000006_ME__TRIGGER_03__1$', count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999111, key='gameStart', value=1)
        self.set_timer(timer_id='160', seconds=160, interval=1)
        self.set_mesh(trigger_ids=[501,502,503,504,505,506,507,508,509])
        self.set_interact_object(trigger_ids=[10000224], state=1)
        self.set_interact_object(trigger_ids=[10000214], state=1)
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(trigger_id=402, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(type=2)
        self.start_mini_game(box_id=499, round=1, game_name='crazyrunner')
        self.start_mini_game_round(box_id=499, round=1)
        self.move_user_to_box(box_id=400, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='160'):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=401, type='trigger', achieve='crazyrunner_win')
        # self.mini_game_camera_direction(box_id=401, camera_id=301)
        self.set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        self.set_event_ui(type=6, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        self.add_buff(box_ids=[401], skill_id=70000019, level=1)
        # self.set_event_ui(type=5, arg2='$61000004_ME__TRIGGER_01__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.end_mini_game_round(winner_box_id=401, exp_rate=0.25, is_gain_loser_bonus=True) # 401 박스에만 트로피  부여
            self.mini_game_give_reward(winner_box_id=401, content_type='miniGame')
            self.end_mini_game(winner_box_id=401, game_name='crazyrunner')
            # self.set_local_camera(camera_id=301)
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 입장
