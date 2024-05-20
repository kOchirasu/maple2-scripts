""" trigger/99999912/01_movetest.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame


class Init(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_field_game(type=FieldGame.GuildVsGame)
        self.user_tag_symbol(symbol1='guild_game_red', symbol2='guild_game_blue')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000, user_tag_id=1) >= 1:
            return Wait(self.ctx)


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001129], state=1)
        self.set_interact_object(trigger_ids=[10001130], state=1)
        self.set_interact_object(trigger_ids=[10001131], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        # all_of:  <condition name="CheckSameUserTag" triggerBoxID="9000" />
        if self.object_interacted(interact_ids=[10001129], state=0):
            return Move01(self.ctx)


class Move01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='강제이동 트리거가 발동됩니다.')
        # self.move_to_portal(box_id=9000, user_tag_id=1, portal_id=1)
        # # desc 속성은 설명을 위해서 적어둔 것이니 사용할때는 지우고 사용해주시면 됩니다.
        self.move_to_portal(box_id=9000, user_tag_id=2, portal_id=2)
        self.move_to_portal(user_tag_id=1, portal_id=1)
        self.move_to_portal(user_tag_id=2, portal_id=2)
        self.show_event_result(type='notice', text='1팀 안녕?\\n줄바꿈확인', duration=3000, user_tag_id=1)
        self.show_event_result(type='notice', text='2팀 안녕?\\n줄바꿈확인', duration=3000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_ShowGuideSummary_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_PartTimeJob_Right_01')
        self.guild_vs_game_score_by_user(box_id=9000, score=1, desc='9000 트리거 박스 안의 유저수가 많은 팀에 1점을 추가한다.')
        self.guild_vs_game_give_reward(type='exp', team_id=1, is_win=True, desc='길드 경험치를 지급한다.')
        self.guild_vs_game_give_reward(type='fund', team_id=1, is_win=True, desc='길드 기금을 지급한다.')
        self.guild_vs_game_give_contribution(team_id=1, is_win=True, desc='길드 기여도를 지급한다.')
        self.guild_vs_game_give_reward(type='exp', team_id=2, desc='길드 경험치를 지급한다.')
        self.guild_vs_game_give_reward(type='fund', team_id=2, desc='길드 기금을 지급한다.')
        self.guild_vs_game_give_contribution(team_id=2, desc='길드 기여도를 지급한다.')
        self.guild_vs_game_result(desc='결과창을 출력')
        self.guild_vs_game_log_result(desc='로그를 남긴다')
        self.guild_vs_game_log_won_by_default(team_id=1, desc='1팀의 부전승 보상 로그를 남긴다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PrintWinnerTeam(self.ctx)


class PrintWinnerTeam(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            self.debug_string(value='1팀이 득점 했습니다')
            return Reset(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            self.debug_string(value='2팀이 득점 했습니다')
            return Reset(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            self.debug_string(value='아직 득점한 팀이 없습니다.')
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='트리거 초기화')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Init
