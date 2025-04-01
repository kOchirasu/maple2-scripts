""" trigger/66200001_gd/04_banner_roundscorerecord.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[999], visible=True) # mark
        self.set_mesh(trigger_ids=[1000], visible=True)
        self.set_mesh(trigger_ids=[1100], visible=True)
        self.set_mesh(trigger_ids=[1001,1002,1003])
        self.set_mesh(trigger_ids=[1100,1101,1102,1103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Enter(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[1000])
        self.set_mesh(trigger_ids=[1100])


class Enter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)
        self.set_user_value(key='BlueteamScore', value=0)
        self.set_user_value(key='RedteamScore', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord') == 1:
            return R01BannerUpdate(self.ctx)


class R01BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord') == 2:
            return R02BannerUpdate(self.ctx)


class R02BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord') == 3:
            return R03BannerUpdate(self.ctx)


class R03BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore') == 3:
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore') == 3:
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord') == 4:
            return R04BannerUpdate(self.ctx)


class R04BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore') == 3:
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore') == 3:
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord') == 5:
            return R05BannerUpdate(self.ctx)


class R05BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(team_id=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', start_mesh_id=1000, digit_count=1)
        self.set_user_value_from_guild_vs_game_score(team_id=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', start_mesh_id=1100, digit_count=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore') == 3:
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore') == 3:
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord') == 5:
            return EndGame(self.ctx)


class BlueTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='WinnerTeam', value=1)


class RedTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='WinnerTeam', value=2)


class EndGame(trigger_api.Trigger):
    pass


initial_state = Wait
