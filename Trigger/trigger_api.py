import clr
clr.AddReference("System.Numerics")
clr.AddReference("Maple2.Server.Game")

from typing import List
from System import Array, Int32, String
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align, FieldGame, Locale, Weather, BannerType


class Trigger:
    def __init__(self, ctx: ...):
        self.ctx = ctx

    def on_enter(self) -> 'Trigger':
        """Invoked after transitioning to this state."""
        pass

    def on_tick(self) -> 'Trigger':
        """Periodically invoked while in this state."""
        pass

    def on_exit(self) -> None:
        """Invoked before transitioning to another state."""
        pass

    """ Actions """
    def add_balloon_talk(self, spawn_id: int=0, msg: str='', duration: int=0, delay_tick: int=0, npc_id: int=0) -> None:
        """AddBalloonTalk

        Args:
            spawn_id (int): _description_. Defaults to 0.
            msg (str): _description_. Defaults to ''.
            duration (int): _description_. Defaults to 0.
            delay_tick (int): _description_. Defaults to 0.
            npc_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.AddBalloonTalk(spawn_id, msg, duration, delay_tick, npc_id)

    def add_buff(self, box_ids: List[int], skill_id: int, level: int, is_player: bool=True, is_skill_set: bool=True, feature: str='') -> None:
        """버프를걸어준다

        Args:
            box_ids (List[int]): _description_.
            skill_id (int): _description_.
            level (int): _description_.
            is_player (bool): _description_. Defaults to True.
            is_skill_set (bool): _description_. Defaults to True.
            feature (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.AddBuff(Array[Int32](box_ids), skill_id, level, is_player, is_skill_set, feature)

    def add_cinematic_talk(self, npc_id: int, illust_id: str='', msg: str='', duration: int=0, align: Align=Align.Top, delay_tick: int=0) -> None:
        """AddCinematicTalk

        Args:
            npc_id (int): _description_.
            illust_id (str): _description_. Defaults to ''.
            msg (str): _description_. Defaults to ''.
            duration (int): _description_. Defaults to 0.
            align (Align): _description_. Defaults to Align.Top.
            delay_tick (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.AddCinematicTalk(npc_id, illust_id, msg, duration, align, delay_tick)

    def add_effect_nif(self, spawn_id: int, nif_path: str='', is_outline: bool=False, scale: float=0.0, rotate_z: int=0) -> None:
        """AddEffectNif

        Args:
            spawn_id (int): _description_.
            nif_path (str): _description_. Defaults to ''.
            is_outline (bool): _description_. Defaults to False.
            scale (float): _description_. Defaults to 0.0.
            rotate_z (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.AddEffectNif(spawn_id, nif_path, is_outline, scale, rotate_z)

    def add_user_value(self, value: int, key: str='') -> None:
        """AddUserValue

        Args:
            value (int): _description_.
            key (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.AddUserValue(key, value)

    def allocate_battlefield_points(self, box_id: int, points: int) -> None:
        """전장점수를준다

        Args:
            box_id (int): _description_.
            points (int): _description_.

        Returns: None
        """
        self.ctx.AllocateBattlefieldPoints(box_id, points)

    def announce(self, content: str, type: int=0, arg3: bool=False) -> None:
        """공지를한다

        Args:
            content (str): _description_.
            type (int): _description_. Defaults to 0.
            arg3 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.Announce(type, content, arg3)

    def arcade_boom_boom_ocean_clear_round(self, round: int) -> None:
        """ArcadeBoomBoomOcean: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeBoomBoomOceanClearRound(round)

    def arcade_boom_boom_ocean_end_game(self) -> None:
        """ArcadeBoomBoomOcean: type=EndGame

        Returns: None
        """
        self.ctx.ArcadeBoomBoomOceanEndGame()

    def arcade_boom_boom_ocean_set_skill_score(self, id: int, score: int) -> None:
        """ArcadeBoomBoomOcean: type=SetSkillScore

        Args:
            id (int): _description_.
            score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeBoomBoomOceanSetSkillScore(id, score)

    def arcade_boom_boom_ocean_start_game(self, life_count: int) -> None:
        """ArcadeBoomBoomOcean: type=StartGame

        Args:
            life_count (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeBoomBoomOceanStartGame(life_count)

    def arcade_boom_boom_ocean_start_round(self, round: int, round_duration: int, time_score_rate: int) -> None:
        """ArcadeBoomBoomOcean: type=StartRound

        Args:
            round (int): _description_.
            round_duration (int): _description_.
            time_score_rate (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeBoomBoomOceanStartRound(round, round_duration, time_score_rate)

    def arcade_spring_farm_clear_round(self, round: int) -> None:
        """ArcadeSpringFarm: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeSpringFarmClearRound(round)

    def arcade_spring_farm_end_game(self) -> None:
        """ArcadeSpringFarm: type=EndGame

        Returns: None
        """
        self.ctx.ArcadeSpringFarmEndGame()

    def arcade_spring_farm_set_interact_score(self, id: int, score: int) -> None:
        """ArcadeSpringFarm: type=SetInteractScore

        Args:
            id (int): _description_.
            score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeSpringFarmSetInteractScore(id, score)

    def arcade_spring_farm_spawn_monster(self, spawn_ids: List[int], score: int) -> None:
        """ArcadeSpringFarm: type=SpawnMonster

        Args:
            spawn_ids (List[int]): _description_.
            score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeSpringFarmSpawnMonster(Array[Int32](spawn_ids), score)

    def arcade_spring_farm_start_game(self, life_count: int) -> None:
        """ArcadeSpringFarm: type=StartGame

        Args:
            life_count (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeSpringFarmStartGame(life_count)

    def arcade_spring_farm_start_round(self, ui_duration: int, round: int, time_score_type: str, time_score_rate: int, round_duration: int) -> None:
        """ArcadeSpringFarm: type=StartRound

        Args:
            ui_duration (int): _description_.
            round (int): _description_.
            time_score_type (str): _description_.
            time_score_rate (int): _description_.
            round_duration (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeSpringFarmStartRound(ui_duration, round, time_score_type, time_score_rate, round_duration)

    def arcade_three_two_one_clear_round(self, round: int) -> None:
        """ArcadeThreeTwoOne: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneClearRound(round)

    def arcade_three_two_one_end_game(self) -> None:
        """ArcadeThreeTwoOne: type=EndGame

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneEndGame()

    def arcade_three_two_one_result_round(self, result_direction: int) -> None:
        """ArcadeThreeTwoOne: type=ResultRound

        Args:
            result_direction (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneResultRound(result_direction)

    def arcade_three_two_one_result_round2(self, round: int) -> None:
        """ArcadeThreeTwoOne: type=ResultRound2

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneResultRound2(round)

    def arcade_three_two_one_start_game(self, life_count: int, init_score: int) -> None:
        """ArcadeThreeTwoOne: type=StartGame

        Args:
            life_count (int): _description_.
            init_score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneStartGame(life_count, init_score)

    def arcade_three_two_one_start_round(self, ui_duration: int, round: int) -> None:
        """ArcadeThreeTwoOne: type=StartRound

        Args:
            ui_duration (int): _description_.
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOneStartRound(ui_duration, round)

    def arcade_three_two_one2_clear_round(self, round: int) -> None:
        """ArcadeThreeTwoOne2: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2ClearRound(round)

    def arcade_three_two_one2_end_game(self) -> None:
        """ArcadeThreeTwoOne2: type=EndGame

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2EndGame()

    def arcade_three_two_one2_result_round(self, result_direction: int) -> None:
        """ArcadeThreeTwoOne2: type=ResultRound

        Args:
            result_direction (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2ResultRound(result_direction)

    def arcade_three_two_one2_result_round2(self, round: int) -> None:
        """ArcadeThreeTwoOne2: type=ResultRound2

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2ResultRound2(round)

    def arcade_three_two_one2_start_game(self, life_count: int, init_score: int) -> None:
        """ArcadeThreeTwoOne2: type=StartGame

        Args:
            life_count (int): _description_.
            init_score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2StartGame(life_count, init_score)

    def arcade_three_two_one2_start_round(self, ui_duration: int, round: int) -> None:
        """ArcadeThreeTwoOne2: type=StartRound

        Args:
            ui_duration (int): _description_.
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne2StartRound(ui_duration, round)

    def arcade_three_two_one3_clear_round(self, round: int) -> None:
        """ArcadeThreeTwoOne3: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3ClearRound(round)

    def arcade_three_two_one3_end_game(self) -> None:
        """ArcadeThreeTwoOne3: type=EndGame

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3EndGame()

    def arcade_three_two_one3_result_round(self, result_direction: int) -> None:
        """ArcadeThreeTwoOne3: type=ResultRound

        Args:
            result_direction (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3ResultRound(result_direction)

    def arcade_three_two_one3_result_round2(self, round: int) -> None:
        """ArcadeThreeTwoOne3: type=ResultRound2

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3ResultRound2(round)

    def arcade_three_two_one3_start_game(self, life_count: int, init_score: int) -> None:
        """ArcadeThreeTwoOne3: type=StartGame

        Args:
            life_count (int): _description_.
            init_score (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3StartGame(life_count, init_score)

    def arcade_three_two_one3_start_round(self, ui_duration: int, round: int) -> None:
        """ArcadeThreeTwoOne3: type=StartRound

        Args:
            ui_duration (int): _description_.
            round (int): _description_.

        Returns: None
        """
        self.ctx.ArcadeThreeTwoOne3StartRound(ui_duration, round)

    def change_background(self, dds: str) -> None:
        """ChangeBackground

        Args:
            dds (str): _description_.

        Returns: None
        """
        self.ctx.ChangeBackground(dds)

    def change_monster(self, from_spawn_id: int, to_spawn_id: int) -> None:
        """몬스터를변경한다

        Args:
            from_spawn_id (int): _description_.
            to_spawn_id (int): _description_.

        Returns: None
        """
        self.ctx.ChangeMonster(from_spawn_id, to_spawn_id)

    def close_cinematic(self) -> None:
        """CloseCinematic

        Returns: None
        """
        self.ctx.CloseCinematic()

    def create_field_game(self, type: FieldGame, reset: bool=False) -> None:
        """CreateFieldGame

        Args:
            type (FieldGame): _description_.
            reset (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.CreateFieldGame(type, reset)

    def create_item(self, spawn_ids: List[int], trigger_id: int=0, item_id: int=0, arg5: int=0) -> None:
        """아이템을생성한다

        Args:
            spawn_ids (List[int]): _description_.
            trigger_id (int): _description_. Defaults to 0.
            item_id (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.CreateItem(Array[Int32](spawn_ids), trigger_id, item_id, arg5)

    def create_widget(self, type: str) -> None:
        """CreateWidget

        Args:
            type (str): _description_.

        Returns: None
        """
        self.ctx.CreateWidget(type)

    def dark_stream_clear_round(self, round: int) -> None:
        """DarkStream: type=ClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.DarkStreamClearRound(round)

    def dark_stream_spawn_monster(self, spawn_ids: List[int], score: int) -> None:
        """DarkStream: type=SpawnMonster

        Args:
            spawn_ids (List[int]): _description_.
            score (int): _description_.

        Returns: None
        """
        self.ctx.DarkStreamSpawnMonster(Array[Int32](spawn_ids), score)

    def dark_stream_start_game(self, round: int) -> None:
        """DarkStream: type=StartGame

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.DarkStreamStartGame(round)

    def dark_stream_start_round(self, round: int, ui_duration: int, damage_penalty: int) -> None:
        """DarkStream: type=StartRound

        Args:
            round (int): _description_.
            ui_duration (int): _description_.
            damage_penalty (int): _description_.

        Returns: None
        """
        self.ctx.DarkStreamStartRound(round, ui_duration, damage_penalty)

    def debug_string(self, value: str, feature: str='') -> None:
        """DebugString

        Args:
            value (str): _description_.
            feature (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.DebugString(value, feature)

    def destroy_monster(self, spawn_ids: List[int], arg2: bool=True) -> None:
        """몬스터소멸시킨다

        Args:
            spawn_ids (List[int]): _description_.
            arg2 (bool): _description_. Defaults to True.

        Returns: None
        """
        self.ctx.DestroyMonster(Array[Int32](spawn_ids), arg2)

    def dungeon_clear(self, ui_type: str='None') -> None:
        """DungeonClear

        Args:
            ui_type (str): _description_. Defaults to 'None'.

        Returns: None
        """
        self.ctx.DungeonClear(ui_type)

    def dungeon_clear_round(self, round: int) -> None:
        """DungeonClearRound

        Args:
            round (int): _description_.

        Returns: None
        """
        self.ctx.DungeonClearRound(round)

    def dungeon_close_timer(self) -> None:
        """DungeonCloseTimer

        Returns: None
        """
        self.ctx.DungeonCloseTimer()

    def dungeon_disable_ranking(self) -> None:
        """DungeonDisableRanking

        Returns: None
        """
        self.ctx.DungeonDisableRanking()

    def dungeon_enable_give_up(self, is_enable: bool=False) -> None:
        """DungeonEnableGiveUp

        Args:
            is_enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.DungeonEnableGiveUp(is_enable)

    def dungeon_fail(self) -> None:
        """DungeonFail

        Returns: None
        """
        self.ctx.DungeonFail()

    def dungeon_mission_complete(self, mission_id: int, feature: str='') -> None:
        """DungeonMissionComplete

        Args:
            mission_id (int): _description_.
            feature (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.DungeonMissionComplete(feature, mission_id)

    def dungeon_move_lap_time_to_now(self, id: int) -> None:
        """DungeonMoveLapTimeToNow

        Args:
            id (int): _description_.

        Returns: None
        """
        self.ctx.DungeonMoveLapTimeToNow(id)

    def dungeon_reset_time(self, seconds: int) -> None:
        """DungeonResetTime

        Args:
            seconds (int): _description_.

        Returns: None
        """
        self.ctx.DungeonResetTime(seconds)

    def dungeon_set_end_time(self) -> None:
        """DungeonSetEndTime

        Returns: None
        """
        self.ctx.DungeonSetEndTime()

    def dungeon_set_lap_time(self, id: int, lap_time: int=0) -> None:
        """DungeonSetLapTime

        Args:
            id (int): _description_.
            lap_time (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.DungeonSetLapTime(id, lap_time)

    def dungeon_stop_timer(self) -> None:
        """DungeonStopTimer

        Returns: None
        """
        self.ctx.DungeonStopTimer()

    def set_dungeon_variable(self, var_id: int, value: int) -> None:
        """DungeonVariable

        Args:
            var_id (int): _description_.
            value (int): _description_.

        Returns: None
        """
        self.ctx.SetDungeonVariable(var_id, value)

    def enable_local_camera(self, is_enable: bool=False) -> None:
        """EnableLocalCamera

        Args:
            is_enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.EnableLocalCamera(is_enable)

    def enable_spawn_point_pc(self, spawn_id: int, is_enable: bool=False) -> None:
        """EnableSpawnPointPC

        Args:
            spawn_id (int): _description_.
            is_enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.EnableSpawnPointPc(spawn_id, is_enable)

    def end_mini_game(self, winner_box_id: int=0, game_name: str='', is_only_winner: bool=False) -> None:
        """EndMiniGame

        Args:
            winner_box_id (int): _description_. Defaults to 0.
            game_name (str): _description_. Defaults to ''.
            is_only_winner (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.EndMiniGame(winner_box_id, game_name, is_only_winner)

    def end_mini_game_round(self, winner_box_id: int, exp_rate: float=0.0, meso: float=0.0, is_only_winner: bool=False, is_gain_loser_bonus: bool=False, game_name: str='') -> None:
        """EndMiniGameRound

        Args:
            winner_box_id (int): _description_.
            exp_rate (float): _description_. Defaults to 0.0.
            meso (float): _description_. Defaults to 0.0.
            is_only_winner (bool): _description_. Defaults to False.
            is_gain_loser_bonus (bool): _description_. Defaults to False.
            game_name (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.EndMiniGameRound(winner_box_id, exp_rate, meso, is_only_winner, is_gain_loser_bonus, game_name)

    def face_emotion(self, spawn_id: int=0, emotion_name: str='') -> None:
        """FaceEmotion

        Args:
            spawn_id (int): _description_. Defaults to 0.
            emotion_name (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.FaceEmotion(spawn_id, emotion_name)

    def field_game_constant(self, key: str, value: str, feature: str='', locale: Locale=Locale.ALL) -> None:
        """FieldGameConstant

        Args:
            key (str): _description_.
            value (str): _description_.
            feature (str): _description_. Defaults to ''.
            locale (Locale): _description_. Defaults to Locale.ALL.

        Returns: None
        """
        self.ctx.FieldGameConstant(key, value, feature, locale)

    def field_game_message(self, type: str, script: str, custom: int=0, arg1: bool=False, duration: int=0) -> None:
        """FieldGameMessage

        Args:
            type (str): _description_.
            script (str): _description_.
            custom (int): _description_. Defaults to 0.
            arg1 (bool): _description_. Defaults to False.
            duration (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.FieldGameMessage(custom, type, arg1, script, duration)

    def field_war_end(self, is_clear: bool=False) -> None:
        """FieldWarEnd

        Args:
            is_clear (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.FieldWarEnd(is_clear)

    def give_exp(self, box_id: int, rate: float=1.0, arg3: bool=False) -> None:
        """GiveExp

        Args:
            box_id (int): _description_.
            rate (float): _description_. Defaults to 1.0.
            arg3 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.GiveExp(box_id, rate, arg3)

    def give_guild_exp(self, type: int, box_id: int=0) -> None:
        """GiveGuildExp

        Args:
            type (int): _description_.
            box_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.GiveGuildExp(box_id, type)

    def give_reward_content(self, reward_id: int) -> None:
        """GiveRewardContent

        Args:
            reward_id (int): _description_.

        Returns: None
        """
        self.ctx.GiveRewardContent(reward_id)

    def guide_event(self, event_id: int) -> None:
        """GuideEvent

        Args:
            event_id (int): _description_.

        Returns: None
        """
        self.ctx.GuideEvent(event_id)

    def guild_vs_game_end_game(self) -> None:
        """GuildVsGameEndGame

        Returns: None
        """
        self.ctx.GuildVsGameEndGame()

    def guild_vs_game_give_contribution(self, team_id: int, is_win: bool=False, desc: str='') -> None:
        """GuildVsGameGiveContribution

        Args:
            team_id (int): _description_.
            is_win (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameGiveContribution(team_id, is_win, desc)

    def guild_vs_game_give_reward(self, team_id: int, type: str='', is_win: bool=False, desc: str='') -> None:
        """GuildVsGameGiveReward

        Args:
            team_id (int): _description_.
            type (str): _description_. Defaults to ''.
            is_win (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameGiveReward(type, team_id, is_win, desc)

    def guild_vs_game_log_result(self, desc: str='') -> None:
        """GuildVsGameLogResult

        Args:
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameLogResult(desc)

    def guild_vs_game_log_won_by_default(self, team_id: int, desc: str='') -> None:
        """GuildVsGameLogWonByDefault

        Args:
            team_id (int): _description_.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameLogWonByDefault(team_id, desc)

    def guild_vs_game_result(self, desc: str='') -> None:
        """GuildVsGameResult

        Args:
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameResult(desc)

    def guild_vs_game_score_by_user(self, box_id: int, score: int, desc: str='') -> None:
        """GuildVsGameScoreByUser

        Args:
            box_id (int): _description_.
            score (int): _description_.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.GuildVsGameScoreByUser(box_id, score, desc)

    def hide_guide_summary(self, entity_id: int, text_id: int=0) -> None:
        """HideGuideSummary

        Args:
            entity_id (int): _description_.
            text_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.HideGuideSummary(entity_id, text_id)

    def init_npc_rotation(self, spawn_ids: List[int]) -> None:
        """InitNpcRotation

        Args:
            spawn_ids (List[int]): _description_.

        Returns: None
        """
        self.ctx.InitNpcRotation(Array[Int32](spawn_ids))

    def kick_music_audience(self, box_id: int, portal_id: int) -> None:
        """KickMusicAudience

        Args:
            box_id (int): _description_.
            portal_id (int): _description_.

        Returns: None
        """
        self.ctx.KickMusicAudience(box_id, portal_id)

    def limit_spawn_npc_count(self, limit_count: int, desc: str='') -> None:
        """LimitSpawnNpcCount

        Args:
            limit_count (int): _description_.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.LimitSpawnNpcCount(limit_count, desc)

    def lock_my_pc(self, is_lock: bool=False) -> None:
        """LockMyPC

        Args:
            is_lock (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.LockMyPc(is_lock)

    def mini_game_camera_direction(self, box_id: int, camera_id: int) -> None:
        """MiniGameCameraDirection

        Args:
            box_id (int): _description_.
            camera_id (int): _description_.

        Returns: None
        """
        self.ctx.MiniGameCameraDirection(box_id, camera_id)

    def mini_game_give_exp(self, box_id: int, exp_rate: float=1.0, is_outside: bool=False) -> None:
        """MiniGameGiveExp

        Args:
            box_id (int): _description_.
            exp_rate (float): _description_. Defaults to 1.0.
            is_outside (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.MiniGameGiveExp(box_id, exp_rate, is_outside)

    def mini_game_give_reward(self, winner_box_id: int, content_type: str, game_name: str='') -> None:
        """MiniGameGiveReward

        Args:
            winner_box_id (int): _description_.
            content_type (str): _description_.
            game_name (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.MiniGameGiveReward(winner_box_id, content_type, game_name)

    def move_npc(self, spawn_id: int, patrol_name: str) -> None:
        """NPC를이동시킨다

        Args:
            spawn_id (int): _description_.
            patrol_name (str): _description_.

        Returns: None
        """
        self.ctx.MoveNpc(spawn_id, patrol_name)

    def move_npc_to_pos(self, spawn_id: int, pos: Vector3, rot: Vector3) -> None:
        """MoveNpcToPos

        Args:
            spawn_id (int): _description_.
            pos (Vector3): _description_.
            rot (Vector3): _description_.

        Returns: None
        """
        self.ctx.MoveNpcToPos(spawn_id, pos, rot)

    def move_random_user(self, map_id: int, portal_id: int, box_id: int, count: int) -> None:
        """무작위유저를이동시킨다

        Args:
            map_id (int): _description_.
            portal_id (int): _description_.
            box_id (int): _description_.
            count (int): _description_.

        Returns: None
        """
        self.ctx.MoveRandomUser(map_id, portal_id, box_id, count)

    def move_to_portal(self, user_tag_id: int=0, portal_id: int=0, box_id: int=0) -> None:
        """MoveToPortal

        Args:
            user_tag_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
            box_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.MoveToPortal(user_tag_id, portal_id, box_id)

    def move_user(self, map_id: int=0, portal_id: int=0, box_id: int=0) -> None:
        """유저를이동시킨다

        Args:
            map_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
            box_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.MoveUser(map_id, portal_id, box_id)

    def move_user_path(self, patrol_name: str) -> None:
        """유저를경로이동시킨다

        Args:
            patrol_name (str): _description_.

        Returns: None
        """
        self.ctx.MoveUserPath(patrol_name)

    def move_user_to_box(self, box_id: int, portal_id: int) -> None:
        """MoveUserToBox

        Args:
            box_id (int): _description_.
            portal_id (int): _description_.

        Returns: None
        """
        self.ctx.MoveUserToBox(box_id, portal_id)

    def move_user_to_pos(self, pos: Vector3, rot: Vector3=Vector3()) -> None:
        """MoveUserToPos

        Args:
            pos (Vector3): _description_.
            rot (Vector3): _description_. Defaults to Vector3().

        Returns: None
        """
        self.ctx.MoveUserToPos(pos, rot)

    def notice(self, script: str, type: int=0, arg3: bool=False) -> None:
        """Notice

        Args:
            script (str): _description_.
            type (int): _description_. Defaults to 0.
            arg3 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.Notice(type, script, arg3)

    def npc_remove_additional_effect(self, spawn_id: int, additional_effect_id: int) -> None:
        """NpcRemoveAdditionalEffect

        Args:
            spawn_id (int): _description_.
            additional_effect_id (int): _description_.

        Returns: None
        """
        self.ctx.NpcRemoveAdditionalEffect(spawn_id, additional_effect_id)

    def npc_to_patrol_in_box(self, box_id: int, npc_id: int, spawn_id: str='', patrol_name: str='') -> None:
        """NpcToPatrolInBox

        Args:
            box_id (int): _description_.
            npc_id (int): _description_.
            spawn_id (str): _description_. Defaults to ''.
            patrol_name (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.NpcToPatrolInBox(box_id, npc_id, spawn_id, patrol_name)

    def patrol_condition_user(self, patrol_index: int, additional_effect_id: int, patrol_name: str='') -> None:
        """PatrolConditionUser

        Args:
            patrol_index (int): _description_.
            additional_effect_id (int): _description_.
            patrol_name (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.PatrolConditionUser(patrol_name, patrol_index, additional_effect_id)

    def play_scene_movie(self, file_name: str='', movie_id: int=0, skip_type: str='') -> None:
        """PlaySceneMovie

        Args:
            file_name (str): _description_. Defaults to ''.
            movie_id (int): _description_. Defaults to 0.
            skip_type (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.PlaySceneMovie(file_name, movie_id, skip_type)

    def play_system_sound_by_user_tag(self, user_tag_id: int, sound_key: str) -> None:
        """PlaySystemSoundByUserTag

        Args:
            user_tag_id (int): _description_.
            sound_key (str): _description_.

        Returns: None
        """
        self.ctx.PlaySystemSoundByUserTag(user_tag_id, sound_key)

    def play_system_sound_in_box(self, sound: str, box_ids: List[int]=[]) -> None:
        """PlaySystemSoundInBox

        Args:
            sound (str): _description_.
            box_ids (List[int]): _description_. Defaults to [].

        Returns: None
        """
        self.ctx.PlaySystemSoundInBox(sound, Array[Int32](box_ids))

    def random_additional_effect(self, target: str='', box_id: int=0, spawn_id: int=0, target_count: int=0, tick: int=0, wait_tick: int=0, target_effect: str='', additional_effect_id: int=0) -> None:
        """RandomAdditionalEffect

        Args:
            target (str): _description_. Defaults to ''.
            box_id (int): _description_. Defaults to 0.
            spawn_id (int): _description_. Defaults to 0.
            target_count (int): _description_. Defaults to 0.
            tick (int): _description_. Defaults to 0.
            wait_tick (int): _description_. Defaults to 0.
            target_effect (str): _description_. Defaults to ''.
            additional_effect_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.RandomAdditionalEffect(target, box_id, spawn_id, target_count, tick, wait_tick, target_effect, additional_effect_id)

    def remove_balloon_talk(self, spawn_id: int=0) -> None:
        """RemoveBalloonTalk

        Args:
            spawn_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.RemoveBalloonTalk(spawn_id)

    def remove_buff(self, box_id: int, skill_id: int, is_player: bool=False) -> None:
        """버프를삭제한다

        Args:
            box_id (int): _description_.
            skill_id (int): _description_.
            is_player (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.RemoveBuff(box_id, skill_id, is_player)

    def remove_cinematic_talk(self) -> None:
        """RemoveCinematicTalk

        Returns: None
        """
        self.ctx.RemoveCinematicTalk()

    def remove_effect_nif(self, spawn_id: int) -> None:
        """RemoveEffectNif

        Args:
            spawn_id (int): _description_.

        Returns: None
        """
        self.ctx.RemoveEffectNif(spawn_id)

    def reset_camera(self, interpolation_time: float=0.0) -> None:
        """카메라리셋

        Args:
            interpolation_time (float): _description_. Defaults to 0.0.

        Returns: None
        """
        self.ctx.ResetCamera(interpolation_time)

    def reset_timer(self, timer_id: str='') -> None:
        """타이머를초기화한다

        Args:
            timer_id (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.ResetTimer(timer_id)

    def room_expire(self) -> None:
        """RoomExpire

        Returns: None
        """
        self.ctx.RoomExpire()

    def score_board_create(self, type: str, title: str, max_score: int=0) -> None:
        """ScoreBoardCreate

        Args:
            type (str): _description_.
            title (str): _description_.
            max_score (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.ScoreBoardCreate(type, title, max_score)

    def score_board_remove(self) -> None:
        """ScoreBoardRemove

        Returns: None
        """
        self.ctx.ScoreBoardRemove()

    def score_board_set_score(self, score: int) -> None:
        """ScoreBoardSetScore

        Args:
            score (int): _description_.

        Returns: None
        """
        self.ctx.ScoreBoardSetScore(score)

    def select_camera(self, trigger_id: int, enable: bool=True) -> None:
        """카메라를선택한다

        Args:
            trigger_id (int): _description_.
            enable (bool): _description_. Defaults to True.

        Returns: None
        """
        self.ctx.SelectCamera(trigger_id, enable)

    def select_camera_path(self, path_ids: List[int], return_view: bool=True) -> None:
        """카메라경로를선택한다

        Args:
            path_ids (List[int]): _description_.
            return_view (bool): _description_. Defaults to True.

        Returns: None
        """
        self.ctx.SelectCameraPath(Array[Int32](path_ids), return_view)

    def set_achievement(self, trigger_id: int=0, type: str='', achieve: str='') -> None:
        """업적이벤트를발생시킨다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to ''.
            achieve (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetAchievement(trigger_id, type, achieve)

    def set_actor(self, trigger_id: int, visible: bool=False, initial_sequence: str='', arg4: bool=False, arg5: bool=False) -> None:
        """액터를설정한다

        Args:
            trigger_id (int): _description_.
            visible (bool): _description_. Defaults to False.
            initial_sequence (str): _description_. Defaults to ''.
            arg4 (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetActor(trigger_id, visible, initial_sequence, arg4, arg5)

    def set_agent(self, trigger_ids: List[int], visible: bool=False) -> None:
        """AGENT를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetAgent(Array[Int32](trigger_ids), visible)

    def set_ai_extra_data(self, key: str, value: int, is_modify: bool=False, box_id: int=0) -> None:
        """SetAiExtraData

        Args:
            key (str): _description_.
            value (int): _description_.
            is_modify (bool): _description_. Defaults to False.
            box_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetAiExtraData(key, value, is_modify, box_id)

    def set_ambient_light(self, primary: Vector3, secondary: Vector3=Vector3(), tertiary: Vector3=Vector3()) -> None:
        """SetAmbientLight

        Args:
            primary (Vector3): _description_.
            secondary (Vector3): _description_. Defaults to Vector3().
            tertiary (Vector3): _description_. Defaults to Vector3().

        Returns: None
        """
        self.ctx.SetAmbientLight(primary, secondary, tertiary)

    def set_breakable(self, trigger_ids: List[int], enable: bool=False) -> None:
        """움직이는발판을설정한다

        Args:
            trigger_ids (List[int]): _description_.
            enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetBreakable(Array[Int32](trigger_ids), enable)

    def set_cinematic_intro(self, text: str='') -> None:
        """SetCinematicIntro

        Args:
            text (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetCinematicIntro(text)

    def set_cinematic_ui(self, type: int, script: str='', arg3: bool=False) -> None:
        """연출UI를설정한다

        Args:
            type (int): _description_.
            script (str): _description_. Defaults to ''.
            arg3 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetCinematicUi(type, script, arg3)

    def set_cube(self, trigger_ids: List[int], is_visible: bool=False, random_count: int=0) -> None:
        """SetCube

        Args:
            trigger_ids (List[int]): _description_.
            is_visible (bool): _description_. Defaults to False.
            random_count (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetCube(Array[Int32](trigger_ids), is_visible, random_count)

    def set_dialogue(self, type: int, script: str, spawn_id: int=0, time: int=0, arg5: int=0, align: Align=Align.Top) -> None:
        """대화를설정한다

        Args:
            type (int): _description_.
            script (str): _description_.
            spawn_id (int): _description_. Defaults to 0.
            time (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
            align (Align): _description_. Defaults to Align.Top.

        Returns: None
        """
        self.ctx.SetDialogue(type, spawn_id, script, time, arg5, align)

    def set_directional_light(self, diffuse_color: Vector3, specular_color: Vector3=Vector3()) -> None:
        """SetDirectionalLight

        Args:
            diffuse_color (Vector3): _description_.
            specular_color (Vector3): _description_. Defaults to Vector3().

        Returns: None
        """
        self.ctx.SetDirectionalLight(diffuse_color, specular_color)

    def set_effect(self, trigger_ids: List[int], visible: bool=False, start_delay: int=0, interval: int=0) -> None:
        """이펙트를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetEffect(Array[Int32](trigger_ids), visible, start_delay, interval)

    def set_event_ui_countdown(self, round_countdown: List[int], script: str='', box_ids: List[str]=[]) -> None:
        """이벤트UI를설정한다: arg1=2

        Args:
            round_countdown (List[int]): _description_.
            script (str): _description_. Defaults to ''.
            box_ids (List[str]): _description_. Defaults to [].

        Returns: None
        """
        self.ctx.SetEventUiCountdown(script, Array[Int32](round_countdown), Array[String](box_ids))

    def set_event_ui_round(self, rounds: List[int], v_offset: int=0, arg3: int=0) -> None:
        """이벤트UI를설정한다: arg1=0

        Args:
            rounds (List[int]): _description_.
            v_offset (int): _description_. Defaults to 0.
            arg3 (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetEventUiRound(Array[Int32](rounds), v_offset, arg3)

    def set_event_ui_script(self, type: BannerType, duration: int, script: str='', box_ids: List[str]=[]) -> None:
        """이벤트UI를설정한다: arg1=1

        Args:
            type (BannerType): _description_.
            duration (int): _description_.
            script (str): _description_. Defaults to ''.
            box_ids (List[str]): _description_. Defaults to [].

        Returns: None
        """
        self.ctx.SetEventUiScript(type, script, duration, Array[String](box_ids))

    def set_gravity(self, gravity: float) -> None:
        """SetGravity

        Args:
            gravity (float): _description_.

        Returns: None
        """
        self.ctx.SetGravity(gravity)

    def set_interact_object(self, trigger_ids: List[int], state: int, arg4: bool=False, arg3: bool=False) -> None:
        """오브젝트반응설정한다

        Args:
            trigger_ids (List[int]): _description_.
            state (int): _description_.
            arg4 (bool): _description_. Defaults to False.
            arg3 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetInteractObject(Array[Int32](trigger_ids), state, arg4, arg3)

    def set_ladder(self, trigger_ids: List[int], visible: bool=False, enable: bool=False, fade: int=0) -> None:
        """사다리를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            fade (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetLadder(Array[Int32](trigger_ids), visible, enable, fade)

    def set_local_camera(self, camera_id: int, enable: bool=False) -> None:
        """SetLocalCamera

        Args:
            camera_id (int): _description_.
            enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetLocalCamera(camera_id, enable)

    def set_mesh(self, trigger_ids: List[int], visible: bool=False, start_delay: int=0, interval: int=0, fade: float=0.0, desc: str='') -> None:
        """메쉬를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            fade (float): _description_. Defaults to 0.0.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetMesh(Array[Int32](trigger_ids), visible, start_delay, interval, fade, desc)

    def set_mesh_animation(self, trigger_ids: List[int], visible: bool=False, start_delay: int=0, interval: int=0) -> None:
        """메쉬애니를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetMeshAnimation(Array[Int32](trigger_ids), visible, start_delay, interval)

    def set_mini_game_area_for_hack(self, box_id: int) -> None:
        """SetMiniGameAreaForHack

        Args:
            box_id (int): _description_.

        Returns: None
        """
        self.ctx.SetMiniGameAreaForHack(box_id)

    def set_npc_duel_hp_bar(self, spawn_id: int, is_open: bool=False, duration_tick: int=0, npc_hp_step: int=0) -> None:
        """SetNpcDuelHpBar

        Args:
            spawn_id (int): _description_.
            is_open (bool): _description_. Defaults to False.
            duration_tick (int): _description_. Defaults to 0.
            npc_hp_step (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetNpcDuelHpBar(is_open, spawn_id, duration_tick, npc_hp_step)

    def set_npc_emotion_loop(self, spawn_id: int, sequence_name: str='', duration: float=0.0) -> None:
        """SetNpcEmotionLoop

        Args:
            spawn_id (int): _description_.
            sequence_name (str): _description_. Defaults to ''.
            duration (float): _description_. Defaults to 0.0.

        Returns: None
        """
        self.ctx.SetNpcEmotionLoop(spawn_id, sequence_name, duration)

    def set_npc_emotion_sequence(self, spawn_id: int, sequence_name: str, duration_tick: int=0) -> None:
        """SetNpcEmotionSequence

        Args:
            spawn_id (int): _description_.
            sequence_name (str): _description_.
            duration_tick (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetNpcEmotionSequence(spawn_id, sequence_name, duration_tick)

    def set_npc_rotation(self, spawn_id: int, rotation: float) -> None:
        """SetNpcRotation

        Args:
            spawn_id (int): _description_.
            rotation (float): _description_.

        Returns: None
        """
        self.ctx.SetNpcRotation(spawn_id, rotation)

    def set_onetime_effect(self, id: int=0, enable: bool=False, path: str='') -> None:
        """SetOnetimeEffect

        Args:
            id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
            path (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetOnetimeEffect(id, enable, path)

    def set_pc_emotion_loop(self, sequence_name: str, duration: float=0.0, loop: bool=False) -> None:
        """SetPcEmotionLoop

        Args:
            sequence_name (str): _description_.
            duration (float): _description_. Defaults to 0.0.
            loop (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetPcEmotionLoop(sequence_name, duration, loop)

    def set_pc_emotion_sequence(self, sequence_names: List[str]) -> None:
        """SetPcEmotionSequence

        Args:
            sequence_names (List[str]): _description_.

        Returns: None
        """
        self.ctx.SetPcEmotionSequence(Array[String](sequence_names))

    def set_pc_rotation(self, rotation: Vector3) -> None:
        """SetPcRotation

        Args:
            rotation (Vector3): _description_.

        Returns: None
        """
        self.ctx.SetPcRotation(rotation)

    def set_photo_studio(self, is_enable: bool=False) -> None:
        """SetPhotoStudio

        Args:
            is_enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetPhotoStudio(is_enable)

    def set_portal(self, portal_id: int, visible: bool=False, enable: bool=False, minimap_visible: bool=False, arg5: bool=False) -> None:
        """포탈을설정한다

        Args:
            portal_id (int): _description_.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            minimap_visible (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetPortal(portal_id, visible, enable, minimap_visible, arg5)

    def set_pvp_zone(self, box_id: int, prepare_time: int, match_time: int, additional_effect_id: int=0, type: int=0, box_ids: List[int]=[]) -> None:
        """PVP존을설정한다

        Args:
            box_id (int): _description_.
            prepare_time (int): _description_.
            match_time (int): _description_.
            additional_effect_id (int): _description_. Defaults to 0.
            type (int): _description_. Defaults to 0.
            box_ids (List[int]): _description_. Defaults to [].

        Returns: None
        """
        self.ctx.SetPvpZone(box_id, prepare_time, match_time, additional_effect_id, type, Array[Int32](box_ids))

    def set_quest_accept(self, quest_id: int) -> None:
        """SetQuestAccept

        Args:
            quest_id (int): _description_.

        Returns: None
        """
        self.ctx.SetQuestAccept(quest_id)

    def set_quest_complete(self, quest_id: int) -> None:
        """SetQuestComplete

        Args:
            quest_id (int): _description_.

        Returns: None
        """
        self.ctx.SetQuestComplete(quest_id)

    def set_random_mesh(self, trigger_ids: List[int], visible: bool=False, start_delay: int=0, interval: int=0, fade: int=0) -> None:
        """랜덤메쉬를설정한다

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            fade (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetRandomMesh(Array[Int32](trigger_ids), visible, start_delay, interval, fade)

    def set_rope(self, trigger_id: int, visible: bool=False, enable: bool=False, fade: int=0) -> None:
        """로프를설정한다

        Args:
            trigger_id (int): _description_.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            fade (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetRope(trigger_id, visible, enable, fade)

    def set_scene_skip(self, state: 'Trigger'=None, action: str='') -> None:
        """SetSceneSkip

        Args:
            state ('Trigger'): _description_. Defaults to None.
            action (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetSceneSkip(state, action)

    def set_skill(self, trigger_ids: List[int], enable: bool=False) -> None:
        """스킬을설정한다

        Args:
            trigger_ids (List[int]): _description_.
            enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetSkill(Array[Int32](trigger_ids), enable)

    def set_skip(self, state: 'Trigger'=None) -> None:
        """스킵을설정한다

        Args:
            state ('Trigger'): _description_. Defaults to None.

        Returns: None
        """
        self.ctx.SetSkip(state)

    def set_sound(self, trigger_id: int, enable: bool=False) -> None:
        """사운드를설정한다

        Args:
            trigger_id (int): _description_.
            enable (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetSound(trigger_id, enable)

    def set_state(self, id: int, states: List[str], randomize: bool=False) -> None:
        """상태를설정한다

        Args:
            id (int): _description_.
            states (List[str]): _description_.
            randomize (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetState(id, Array[String](states), randomize)

    def set_time_scale(self, enable: bool=False, start_scale: float=0.0, end_scale: float=0.0, duration: float=0.0, interpolator: int=0) -> None:
        """SetTimeScale

        Args:
            enable (bool): _description_. Defaults to False.
            start_scale (float): _description_. Defaults to 0.0.
            end_scale (float): _description_. Defaults to 0.0.
            duration (float): _description_. Defaults to 0.0.
            interpolator (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetTimeScale(enable, start_scale, end_scale, duration, interpolator)

    def set_timer(self, timer_id: str='', seconds: int=0, auto_remove: bool=False, display: bool=False, v_offset: int=0, type: str='', desc: str='') -> None:
        """타이머를설정한다

        Args:
            timer_id (str): _description_. Defaults to ''.
            seconds (int): _description_. Defaults to 0.
            auto_remove (bool): _description_. Defaults to False.
            display (bool): _description_. Defaults to False.
            v_offset (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to ''.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetTimer(timer_id, seconds, auto_remove, display, v_offset, type, desc)

    def set_user_value(self, key: str, value: int, trigger_id: int=0) -> None:
        """SetUserValue

        Args:
            key (str): _description_.
            value (int): _description_.
            trigger_id (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SetUserValue(trigger_id, key, value)

    def set_user_value_from_dungeon_reward_count(self, dungeon_reward_id: int, key: str='') -> None:
        """SetUserValueFromDungeonRewardCount

        Args:
            dungeon_reward_id (int): _description_.
            key (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetUserValueFromDungeonRewardCount(key, dungeon_reward_id)

    def set_user_value_from_guild_vs_game_score(self, team_id: int, key: str='') -> None:
        """SetUserValueFromGuildVsGameScore

        Args:
            team_id (int): _description_.
            key (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SetUserValueFromGuildVsGameScore(team_id, key)

    def set_user_value_from_user_count(self, trigger_box_id: int, key: str, user_tag_id: int) -> None:
        """SetUserValueFromUserCount

        Args:
            trigger_box_id (int): _description_.
            key (str): _description_.
            user_tag_id (int): _description_.

        Returns: None
        """
        self.ctx.SetUserValueFromUserCount(trigger_box_id, key, user_tag_id)

    def set_visible_breakable_object(self, trigger_ids: List[int], visible: bool=False) -> None:
        """SetVisibleBreakableObject

        Args:
            trigger_ids (List[int]): _description_.
            visible (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetVisibleBreakableObject(Array[Int32](trigger_ids), visible)

    def set_visible_ui(self, ui_names: List[str], visible: bool=False) -> None:
        """SetVisibleUI

        Args:
            ui_names (List[str]): _description_.
            visible (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.SetVisibleUi(Array[String](ui_names), visible)

    def shadow_expedition_close_boss_gauge(self) -> None:
        """ShadowExpedition: type=CloseBossGauge

        Returns: None
        """
        self.ctx.ShadowExpeditionCloseBossGauge()

    def shadow_expedition_open_boss_gauge(self, max_gauge_point: int, title: str='') -> None:
        """ShadowExpedition: type=OpenBossGauge

        Args:
            max_gauge_point (int): _description_.
            title (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.ShadowExpeditionOpenBossGauge(max_gauge_point, title)

    def show_caption(self, type: str, title: str, desc: str='', align: Align=Align.Top, offset_rate_x: float=0.0, offset_rate_y: float=0.0, duration: int=0, scale: float=0.0) -> None:
        """ShowCaption

        Args:
            type (str): _description_.
            title (str): _description_.
            desc (str): _description_. Defaults to ''.
            align (Align): _description_. Defaults to Align.Top.
            offset_rate_x (float): _description_. Defaults to 0.0.
            offset_rate_y (float): _description_. Defaults to 0.0.
            duration (int): _description_. Defaults to 0.
            scale (float): _description_. Defaults to 0.0.

        Returns: None
        """
        self.ctx.ShowCaption(type, title, desc, align, offset_rate_x, offset_rate_y, duration, scale)

    def show_count_ui(self, text: str, count: int, stage: int=0, sound_type: int=1) -> None:
        """ShowCountUI

        Args:
            text (str): _description_.
            count (int): _description_.
            stage (int): _description_. Defaults to 0.
            sound_type (int): _description_. Defaults to 1.

        Returns: None
        """
        self.ctx.ShowCountUi(text, stage, count, sound_type)

    def show_event_result(self, type: str, text: str, duration: int=0, user_tag_id: int=0, trigger_box_id: int=0, is_outside: bool=False) -> None:
        """ShowEventResult

        Args:
            type (str): _description_.
            text (str): _description_.
            duration (int): _description_. Defaults to 0.
            user_tag_id (int): _description_. Defaults to 0.
            trigger_box_id (int): _description_. Defaults to 0.
            is_outside (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.ShowEventResult(type, text, duration, user_tag_id, trigger_box_id, is_outside)

    def show_guide_summary(self, entity_id: int, text_id: int=0, duration: int=0) -> None:
        """ShowGuideSummary

        Args:
            entity_id (int): _description_.
            text_id (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.ShowGuideSummary(entity_id, text_id, duration)

    def show_round_ui(self, round: int, duration: int=0, is_final_round: bool=False) -> None:
        """ShowRoundUI

        Args:
            round (int): _description_.
            duration (int): _description_. Defaults to 0.
            is_final_round (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.ShowRoundUi(round, duration, is_final_round)

    def side_npc_cutin(self, illust: str, duration: int) -> None:
        """SideNpcTalk: type=cutin

        Args:
            illust (str): _description_.
            duration (int): _description_.

        Returns: None
        """
        self.ctx.SideNpcCutin(illust, duration)

    def side_npc_movie(self, usm: str, duration: int) -> None:
        """SideNpcTalk: type=movie

        Args:
            usm (str): _description_.
            duration (int): _description_.

        Returns: None
        """
        self.ctx.SideNpcMovie(usm, duration)

    def side_npc_talk(self, npc_id: int, illust: str, duration: int, script: str, voice: str='') -> None:
        """SideNpcTalk: type=talk

        Args:
            npc_id (int): _description_.
            illust (str): _description_.
            duration (int): _description_.
            script (str): _description_.
            voice (str): _description_. Defaults to ''.

        Returns: None
        """
        self.ctx.SideNpcTalk(npc_id, illust, duration, script, voice)

    def side_npc_talk_bottom(self, npc_id: int, illust: str, duration: int, script: str) -> None:
        """SideNpcTalk: type=talkbottom

        Args:
            npc_id (int): _description_.
            illust (str): _description_.
            duration (int): _description_.
            script (str): _description_.

        Returns: None
        """
        self.ctx.SideNpcTalkBottom(npc_id, illust, duration, script)

    def sight_range(self, range: int, enable: bool=False, range_z: int=0, border: int=0) -> None:
        """SightRange

        Args:
            range (int): _description_.
            enable (bool): _description_. Defaults to False.
            range_z (int): _description_. Defaults to 0.
            border (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SightRange(enable, range, range_z, border)

    def spawn_item_range(self, range_ids: List[int], random_pick_count: int) -> None:
        """SpawnItemRange

        Args:
            range_ids (List[int]): _description_.
            random_pick_count (int): _description_.

        Returns: None
        """
        self.ctx.SpawnItemRange(Array[Int32](range_ids), random_pick_count)

    def spawn_monster(self, spawn_ids: List[int], auto_target: bool=True, delay: int=0) -> None:
        """몬스터를생성한다

        Args:
            spawn_ids (List[int]): _description_.
            auto_target (bool): _description_. Defaults to True.
            delay (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SpawnMonster(Array[Int32](spawn_ids), auto_target, delay)

    def spawn_npc_range(self, range_ids: List[int], is_auto_targeting: bool=False, random_pick_count: int=0, score: int=0) -> None:
        """SpawnNpcRange

        Args:
            range_ids (List[int]): _description_.
            is_auto_targeting (bool): _description_. Defaults to False.
            random_pick_count (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.SpawnNpcRange(Array[Int32](range_ids), is_auto_targeting, random_pick_count, score)

    def start_combine_spawn(self, group_id: List[int], is_start: bool=False) -> None:
        """StartCombineSpawn

        Args:
            group_id (List[int]): _description_.
            is_start (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.StartCombineSpawn(Array[Int32](group_id), is_start)

    def start_mini_game(self, box_id: int, round: int, game_name: str, is_show_result_ui: bool=True) -> None:
        """StartMiniGame

        Args:
            box_id (int): _description_.
            round (int): _description_.
            game_name (str): _description_.
            is_show_result_ui (bool): _description_. Defaults to True.

        Returns: None
        """
        self.ctx.StartMiniGame(box_id, round, game_name, is_show_result_ui)

    def start_mini_game_round(self, box_id: int, round: int) -> None:
        """StartMiniGameRound

        Args:
            box_id (int): _description_.
            round (int): _description_.

        Returns: None
        """
        self.ctx.StartMiniGameRound(box_id, round)

    def start_tutorial(self) -> None:
        """startTutorial

        Returns: None
        """
        self.ctx.StartTutorial()

    def talk_npc(self, spawn_id: int) -> None:
        """TalkNpc

        Args:
            spawn_id (int): _description_.

        Returns: None
        """
        self.ctx.TalkNpc(spawn_id)

    def unset_mini_game_area_for_hack(self) -> None:
        """UnSetMiniGameAreaForHack

        Returns: None
        """
        self.ctx.UnsetMiniGameAreaForHack()

    def use_state(self, id: int=0, randomize: bool=False) -> None:
        """상태를사용한다

        Args:
            id (int): _description_. Defaults to 0.
            randomize (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.UseState(id, randomize)

    def user_tag_symbol(self, symbol1: str, symbol2: str) -> None:
        """UserTagSymbol

        Args:
            symbol1 (str): _description_.
            symbol2 (str): _description_.

        Returns: None
        """
        self.ctx.UserTagSymbol(symbol1, symbol2)

    def user_value_to_number_mesh(self, key: str, start_mesh_id: int, digit_count: int) -> None:
        """UserValueToNumberMesh

        Args:
            key (str): _description_.
            start_mesh_id (int): _description_.
            digit_count (int): _description_.

        Returns: None
        """
        self.ctx.UserValueToNumberMesh(key, start_mesh_id, digit_count)

    def visible_my_pc(self, is_visible: bool) -> None:
        """VisibleMyPC

        Args:
            is_visible (bool): _description_.

        Returns: None
        """
        self.ctx.VisibleMyPc(is_visible)

    def weather(self, weather_type: Weather) -> None:
        """Weather

        Args:
            weather_type (Weather): _description_.

        Returns: None
        """
        self.ctx.Weather(weather_type)

    def wedding_broken(self) -> None:
        """WeddingBroken

        Returns: None
        """
        self.ctx.WeddingBroken()

    def wedding_move_user(self, entry_type: str, map_id: int, portal_ids: List[int], box_id: int) -> None:
        """WeddingMoveUser

        Args:
            entry_type (str): _description_.
            map_id (int): _description_.
            portal_ids (List[int]): _description_.
            box_id (int): _description_.

        Returns: None
        """
        self.ctx.WeddingMoveUser(entry_type, map_id, Array[Int32](portal_ids), box_id)

    def wedding_mutual_agree(self, agree_type: str) -> None:
        """WeddingMutualAgree

        Args:
            agree_type (str): _description_.

        Returns: None
        """
        self.ctx.WeddingMutualAgree(agree_type)

    def wedding_mutual_cancel(self, agree_type: str) -> None:
        """WeddingMutualCancel

        Args:
            agree_type (str): _description_.

        Returns: None
        """
        self.ctx.WeddingMutualCancel(agree_type)

    def wedding_set_user_emotion(self, entry_type: str, id: int) -> None:
        """WeddingSetUserEmotion

        Args:
            entry_type (str): _description_.
            id (int): _description_.

        Returns: None
        """
        self.ctx.WeddingSetUserEmotion(entry_type, id)

    def wedding_set_user_look_at(self, entry_type: str, look_at_entry_type: str, immediate: bool=False) -> None:
        """WeddingSetUserLookAt

        Args:
            entry_type (str): _description_.
            look_at_entry_type (str): _description_.
            immediate (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.WeddingSetUserLookAt(entry_type, look_at_entry_type, immediate)

    def wedding_set_user_rotation(self, entry_type: str, rotation: Vector3, immediate: bool=False) -> None:
        """WeddingSetUserRotation

        Args:
            entry_type (str): _description_.
            rotation (Vector3): _description_.
            immediate (bool): _description_. Defaults to False.

        Returns: None
        """
        self.ctx.WeddingSetUserRotation(entry_type, rotation, immediate)

    def wedding_user_to_patrol(self, entry_type: str, patrol_name: str='', patrol_index: int=0) -> None:
        """WeddingUserToPatrol

        Args:
            entry_type (str): _description_.
            patrol_name (str): _description_. Defaults to ''.
            patrol_index (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.WeddingUserToPatrol(patrol_name, entry_type, patrol_index)

    def wedding_vow_complete(self) -> None:
        """WeddingVowComplete

        Returns: None
        """
        self.ctx.WeddingVowComplete()

    def widget_action(self, type: str, func: str, widget_arg: str='', desc: str='', widget_arg_num: int=0) -> None:
        """WidgetAction

        Args:
            type (str): _description_.
            func (str): _description_.
            widget_arg (str): _description_. Defaults to ''.
            desc (str): _description_. Defaults to ''.
            widget_arg_num (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.WidgetAction(type, func, widget_arg, desc, widget_arg_num)

    def write_log(self, log_name: str, event: str='', trigger_id: int=0, sub_event: str='', level: int=0) -> None:
        """로그를남긴다

        Args:
            log_name (str): _description_.
            event (str): _description_. Defaults to ''.
            trigger_id (int): _description_. Defaults to 0.
            sub_event (str): _description_. Defaults to ''.
            level (int): _description_. Defaults to 0.

        Returns: None
        """
        self.ctx.WriteLog(log_name, event, trigger_id, sub_event, level)


    """ Conditions """
    def bonus_game_reward(self, box_id: int) -> int:
        """보너스게임보상받은유저를감지했으면

        Args:
            box_id (int): _description_.

        Returns:
            int: type
        """
        return self.ctx.BonusGameReward(box_id)

    def check_any_user_additional_effect(self, box_id: int, additional_effect_id: int, level: int) -> bool:
        """CheckAnyUserAdditionalEffect

        Args:
            box_id (int): _description_.
            additional_effect_id (int): _description_.
            level (int): _description_.

        Returns: None
        """
        return self.ctx.CheckAnyUserAdditionalEffect(box_id, additional_effect_id, level)

    def check_dungeon_lobby_user_count(self) -> bool:
        """CheckDungeonLobbyUserCount

        Returns: None
        """
        return self.ctx.CheckDungeonLobbyUserCount()

    def check_npc_additional_effect(self, spawn_id: int, additional_effect_id: int, level: int) -> bool:
        """CheckNpcAdditionalEffect

        Args:
            spawn_id (int): _description_.
            additional_effect_id (int): _description_.
            level (int): _description_.

        Returns: None
        """
        return self.ctx.CheckNpcAdditionalEffect(spawn_id, additional_effect_id, level)

    def npc_damage(self, spawn_id: int) -> float:
        """CheckNpcDamage

        Args:
            spawn_id (int): _description_.

        Returns:
            float: damage_rate
        """
        return self.ctx.NpcDamage(spawn_id)

    def npc_extra_data(self, spawn_point_id: int, extra_data_key: str) -> int:
        """CheckNpcExtraData

        Args:
            spawn_point_id (int): _description_.
            extra_data_key (str): _description_.

        Returns:
            int: extra_data_value
        """
        return self.ctx.NpcExtraData(spawn_point_id, extra_data_key)

    def npc_hp(self, spawn_id: int, is_relative: bool) -> int:
        """CheckNpcHp

        Args:
            spawn_id (int): _description_.
            is_relative (bool): _description_.

        Returns:
            int: value
        """
        return self.ctx.NpcHp(spawn_id, is_relative)

    def check_same_user_tag(self, box_id: int) -> bool:
        """CheckSameUserTag

        Args:
            box_id (int): _description_.

        Returns: None
        """
        return self.ctx.CheckSameUserTag(box_id)

    def check_user(self) -> bool:
        """CheckUser

        Returns: None
        """
        return self.ctx.CheckUser()

    def user_count(self) -> int:
        """CheckUserCount

        Returns:
            int: check_count
        """
        return self.ctx.UserCount()

    def count_users(self, box_id: int, user_tag_id: int=0) -> int:
        """여러명의유저를감지했으면

        Args:
            box_id (int): _description_.
            user_tag_id (int): _description_. Defaults to 0.

        Returns:
            int: min_users
        """
        return self.ctx.CountUsers(box_id, user_tag_id)

    def day_of_week(self, desc: str='') -> int:
        """DayOfWeek

        Args:
            desc (str): _description_. Defaults to ''.

        Returns:
            int: day_of_weeks
        """
        return self.ctx.DayOfWeek(desc)

    def detect_liftable_object(self, box_ids: List[int], item_id: int) -> bool:
        """DetectLiftableObject

        Args:
            box_ids (List[int]): _description_.
            item_id (int): _description_.

        Returns: None
        """
        return self.ctx.DetectLiftableObject(Array[Int32](box_ids), item_id)

    def dungeon_play_time(self) -> int:
        """DungeonCheckPlayTime

        Returns:
            int: play_seconds
        """
        return self.ctx.DungeonPlayTime()

    def dungeon_state(self) -> str:
        """DungeonCheckState

        Returns:
            str: check_state
        """
        return self.ctx.DungeonState()

    def dungeon_first_user_mission_score(self) -> int:
        """DungeonFirstUserMissionScore

        Returns:
            int: score
        """
        return self.ctx.DungeonFirstUserMissionScore()

    def dungeon_id(self) -> int:
        """DungeonID

        Returns:
            int: dungeon_id
        """
        return self.ctx.DungeonId()

    def dungeon_level(self) -> int:
        """DungeonLevel

        Returns:
            int: level
        """
        return self.ctx.DungeonLevel()

    def dungeon_max_user_count(self) -> int:
        """DungeonMaxUserCount

        Returns:
            int: value
        """
        return self.ctx.DungeonMaxUserCount()

    def dungeon_round(self) -> int:
        """DungeonRoundRequire

        Returns:
            int: round
        """
        return self.ctx.DungeonRound()

    def dungeon_timeout(self) -> bool:
        """DungeonTimeOut

        Returns: None
        """
        return self.ctx.DungeonTimeout()

    def dungeon_variable(self, var_id: int) -> int:
        """DungeonVariable

        Args:
            var_id (int): _description_.

        Returns:
            int: value
        """
        return self.ctx.DungeonVariable(var_id)

    def guild_vs_game_scored_team(self, team_id: int) -> bool:
        """GuildVsGameScoredTeam

        Args:
            team_id (int): _description_.

        Returns: None
        """
        return self.ctx.GuildVsGameScoredTeam(team_id)

    def guild_vs_game_winner_team(self, team_id: int) -> bool:
        """GuildVsGameWinnerTeam

        Args:
            team_id (int): _description_.

        Returns: None
        """
        return self.ctx.GuildVsGameWinnerTeam(team_id)

    def is_dungeon_room(self) -> bool:
        """IsDungeonRoom

        Returns: None
        """
        return self.ctx.IsDungeonRoom()

    def is_playing_maple_survival(self) -> bool:
        """IsPlayingMapleSurvival

        Returns: None
        """
        return self.ctx.IsPlayingMapleSurvival()

    def monster_dead(self, spawn_ids: List[int], auto_target: bool=True) -> bool:
        """몬스터가죽어있으면

        Args:
            spawn_ids (List[int]): _description_.
            auto_target (bool): _description_. Defaults to True.

        Returns: None
        """
        return self.ctx.MonsterDead(Array[Int32](spawn_ids), auto_target)

    def monster_in_combat(self, spawn_ids: List[int]) -> bool:
        """몬스터가전투상태면

        Args:
            spawn_ids (List[int]): _description_.

        Returns: None
        """
        return self.ctx.MonsterInCombat(Array[Int32](spawn_ids))

    def npc_detected(self, box_id: int, spawn_ids: List[int]) -> bool:
        """NPC를감지했으면

        Args:
            box_id (int): _description_.
            spawn_ids (List[int]): _description_.

        Returns: None
        """
        return self.ctx.NpcDetected(box_id, Array[Int32](spawn_ids))

    def npc_is_dead_by_string_id(self, string_id: str) -> bool:
        """NpcIsDeadByStringID

        Args:
            string_id (str): _description_.

        Returns: None
        """
        return self.ctx.NpcIsDeadByStringId(string_id)

    def object_interacted(self, interact_ids: List[int], state: int=0) -> bool:
        """오브젝트가반응했으면

        Args:
            interact_ids (List[int]): _description_.
            state (int): _description_. Defaults to 0.

        Returns: None
        """
        return self.ctx.ObjectInteracted(Array[Int32](interact_ids), state)

    def pvp_zone_ended(self, box_id: int) -> bool:
        """PVP존이종료했으면

        Args:
            box_id (int): _description_.

        Returns: None
        """
        return self.ctx.PvpZoneEnded(box_id)

    def quest_user_detected(self, box_ids: List[int], quest_ids: List[int], quest_states: List[int], job_code: int=0) -> bool:
        """퀘스트유저를감지하면

        Args:
            box_ids (List[int]): _description_.
            quest_ids (List[int]): _description_.
            quest_states (List[int]): _description_.
            job_code (int): _description_. Defaults to 0.

        Returns: None
        """
        return self.ctx.QuestUserDetected(Array[Int32](box_ids), Array[Int32](quest_ids), Array[Int32](quest_states), job_code)

    def random_condition(self, weight: float, desc: str='') -> bool:
        """랜덤조건

        Args:
            weight (float): _description_.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        return self.ctx.RandomCondition(weight, desc)

    def score_board_score(self) -> int:
        """ScoreBoardCompare

        Returns:
            int: score
        """
        return self.ctx.ScoreBoardScore()

    def shadow_expedition_points(self) -> int:
        """ShadowExpeditionReachPoint

        Returns:
            int: point
        """
        return self.ctx.ShadowExpeditionPoints()

    def time_expired(self, timer_id: str) -> bool:
        """시간이경과했으면

        Args:
            timer_id (str): _description_.

        Returns: None
        """
        return self.ctx.TimeExpired(timer_id)

    def user_detected(self, box_ids: List[int], job_code: int=0) -> bool:
        """유저를감지했으면

        Args:
            box_ids (List[int]): _description_.
            job_code (int): _description_. Defaults to 0.

        Returns: None
        """
        return self.ctx.UserDetected(Array[Int32](box_ids), job_code)

    def user_value(self, key: str) -> int:
        """UserValue

        Args:
            key (str): _description_.

        Returns:
            int: value
        """
        return self.ctx.UserValue(key)

    def wait_and_reset_tick(self, wait_tick: int) -> bool:
        """WaitAndResetTick

        Args:
            wait_tick (int): _description_.

        Returns: None
        """
        return self.ctx.WaitAndResetTick(wait_tick)

    def wait_seconds_user_value(self, key: str, desc: str='') -> bool:
        """WaitSecondsUserValue

        Args:
            key (str): _description_.
            desc (str): _description_. Defaults to ''.

        Returns: None
        """
        return self.ctx.WaitSecondsUserValue(key, desc)

    def wait_tick(self, wait_tick: int) -> bool:
        """WaitTick

        Args:
            wait_tick (int): _description_.

        Returns: None
        """
        return self.ctx.WaitTick(wait_tick)

    def wedding_entry_in_field(self, entry_type: str, is_in_field: bool) -> bool:
        """WeddingEntryInField

        Args:
            entry_type (str): _description_.
            is_in_field (bool): _description_.

        Returns: None
        """
        return self.ctx.WeddingEntryInField(entry_type, is_in_field)

    def wedding_hall_state(self, success: bool=False) -> str:
        """WeddingHallState

        Args:
            success (bool): _description_. Defaults to False.

        Returns:
            str: hall_state
        """
        return self.ctx.WeddingHallState(success)

    def wedding_mutual_agree_result(self, agree_type: str) -> bool:
        """WeddingMutualAgreeResult

        Args:
            agree_type (str): _description_.

        Returns:
            bool: success
        """
        return self.ctx.WeddingMutualAgreeResult(agree_type)

    def widget_value(self, type: str, name: str, desc: str='') -> int:
        """WidgetCondition

        Args:
            type (str): _description_.
            name (str): _description_.
            desc (str): _description_. Defaults to ''.

        Returns:
            int: condition
        """
        return self.ctx.WidgetValue(type, name, desc)

