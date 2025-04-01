""" trigger/61000010_me/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            # self.set_local_camera(camera_id=302, enable=True)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return 어나운스0(self.ctx)
        if self.user_value(key='GameStart') == 1:
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000010_ME__main__0$', duration=3000, box_ids=['0'])
        self.set_achievement(trigger_id=101, type='trigger', achieve='ShanghaiRunnersStart')
        # self.set_local_camera(camera_id=302)
        # self.reset_camera(interpolation_time=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000006_ME__TRIGGER_03__1$', count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=190, display=True)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003])
        self.set_user_value(trigger_id=999111, key='gameStart', value=1)
        self.start_mini_game(box_id=199, round=1, game_name='shanghairunner')
        self.start_mini_game_round(box_id=199, round=1)
        self.move_user_to_box(box_id=101, portal_id=1)
        self.set_achievement(trigger_id=101, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Winner, script='$61000006_ME__TRIGGER_03__2$', duration=5000, box_ids=['401'])
        self.set_event_ui_script(type=BannerType.Bonus, script='$61000006_ME__TRIGGER_03__3$', duration=5000, box_ids=['!401'])
        # self.add_buff(box_ids=[199], skill_id=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.end_mini_game_round(winner_box_id=102, exp_rate=0.25, is_gain_loser_bonus=True)
            self.mini_game_give_reward(winner_box_id=102, content_type='MiniGameType2')
            self.end_mini_game(winner_box_id=102, game_name='shanghairunner')
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 입장
