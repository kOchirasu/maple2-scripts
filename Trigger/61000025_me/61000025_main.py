""" trigger/61000025_me/61000025_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame, Locale, BannerType


# None
class StateNone(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_field_game(type=FieldGame.HideAndSeek, reset=True) # TriggerID 시작
        self.field_game_constant(key='BeginTriggerID', value='1') # TriggerID 끝
        self.field_game_constant(key='EndTriggerID', value='36') # 숨바꼭질 플레이를 위한 최소 유저수
        self.field_game_constant(key='RequireUserCount', value='2') # 숨바꼭질 플레이어 입장 대기 시간
        self.field_game_constant(key='EnterableSeconds', value='60') # 숨바꼭질 게임룰 설명 시간
        self.field_game_constant(key='GameRuleNoticeTick', value='10000') # 방폭 진행 소요 시간
        self.field_game_constant(key='ShortOfUserTick', value='10000') # 편 나누기 소요 시간
        # 유저가 게임포탈로 이동할 동안 카메라 무빙 소요 시간
        self.field_game_constant(key='DivideTeamsSeconds', value='5')
        self.field_game_constant(key='MoveGameAreaTick', value='2000') # 사물팀 숨는 소요 시간
        self.field_game_constant(key='BeInHidingTeamsSeconds', value='30') # 술래팀 사물찾는데 소요 시간
        self.field_game_constant(key='LookingForATeamsSeconds', value='150') # 승패 알림 소요 시간
        self.field_game_constant(key='TeamMatchResultTick', value='15000') # 숨바꼭질 게임종료 설명 시간
        self.field_game_constant(key='GameExitNoticeTick', value='10000') # 사물팀 경험치 할당 주기
        # 술래팀 무적 시간 (전체 시간에서 아래 시간 만큼 남았을때 발동.)
        self.field_game_constant(key='HideTeamExpDurationTick', value='30000')
        self.field_game_constant(key='SeekTeamInvincibleTick', value='20000') # 술래팀 무적 안내 시간
        self.field_game_constant(key='InvincibleNoticeTick', value='7000') # 술래팀 무적 안내 메세지
        self.field_game_constant(key='InvincibleMessage', value='$61000025_ME__61000025_MAIN__6$') # 대기지역 포탈 아이디
        self.field_game_constant(key='PortalWaitAreaID', value='1') # 게임지역 포탈 아이디
        self.field_game_constant(key='PortalGameAreaID', value='10') # 탈락지역 포탈 아이디
        self.field_game_constant(key='PortalFailAreaID', value='20') # 술래팀이 사용하는 SkillSet
        self.field_game_constant(key='SeekTeamSkillSetID', value='99930041') # 사물팀 경험치
        self.field_game_constant(key='HideTeamExp', value='0') # 술래팀 경험치
        # KR 승리팀 보상 id, rank, count
        self.field_game_constant(key='SeekTeamExp', value='0')
        self.field_game_constant(key='WinnerRewardItemID', value='30001442', feature='MassiveHideAndSeek', locale=Locale.KR)
        self.field_game_constant(key='WinnerRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.KR)
        # KR 패배팀 보상 id, rank, count
        self.field_game_constant(key='WinnerRewardItemCount', value='3', feature='MassiveHideAndSeek', locale=Locale.KR)
        self.field_game_constant(key='LoserRewardItemID', value='30001442', feature='MassiveHideAndSeek', locale=Locale.KR)
        self.field_game_constant(key='LoserRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.KR)
        # CN 승리팀 보상 id, rank, count
        self.field_game_constant(key='LoserRewardItemCount', value='1', feature='MassiveHideAndSeek', locale=Locale.KR)
        self.field_game_constant(key='WinnerRewardItemID', value='30001446', feature='MassiveHideAndSeek', locale=Locale.CN)
        self.field_game_constant(key='WinnerRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.CN)
        # CN 패배팀 보상 id, rank, count
        self.field_game_constant(key='WinnerRewardItemCount', value='3', feature='MassiveHideAndSeek', locale=Locale.CN)
        self.field_game_constant(key='LoserRewardItemID', value='30001446', feature='MassiveHideAndSeek', locale=Locale.CN)
        self.field_game_constant(key='LoserRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.CN)
        # NA 승리팀 보상 id, rank, count
        self.field_game_constant(key='LoserRewardItemCount', value='1', feature='MassiveHideAndSeek', locale=Locale.CN)
        self.field_game_constant(key='WinnerRewardItemID', value='30000610', feature='MassiveHideAndSeek', locale=Locale.NA)
        self.field_game_constant(key='WinnerRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.NA)
        # NA 패배팀 보상 id, rank, count
        self.field_game_constant(key='WinnerRewardItemCount', value='2', feature='MassiveHideAndSeek', locale=Locale.NA)
        self.field_game_constant(key='LoserRewardItemID', value='30000610', feature='MassiveHideAndSeek', locale=Locale.NA)
        self.field_game_constant(key='LoserRewardItemRank', value='1', feature='MassiveHideAndSeek', locale=Locale.NA)
        self.field_game_constant(key='LoserRewardItemCount', value='1', feature='MassiveHideAndSeek', locale=Locale.NA) # 관전 CameraID
        self.field_game_constant(key='WatchCameraID', value='101') # 데일리 이벤트
        self.field_game_constant(key='EventDailyQuestStart', value='dailyquest_start') # 숨바꼭질 참여 이벤트
        self.field_game_constant(key='EventHideAndSeekStart', value='hideandseek_start') # 숨바꼭질 승리 이벤트
        self.field_game_constant(key='EventHideAndSeekWin', value='hideandseek_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaitForEnterUser') == 1:
            return WaitForEnterUser(self.ctx)


# 유저를 대기 한다.
class WaitForEnterUser(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 숨바꼭질 플레이어 입장 대기 시간
        self.set_timer(timer_id='1', seconds=60, auto_remove=True, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameRuleNotice') == 1:
            return GameRuleNotice(self.ctx)
        if self.user_value(key='ShortOfUser') == 1:
            return ShortOfUser(self.ctx)
        if self.wait_and_reset_tick(wait_tick=5000):
            self.show_guide_summary(entity_id=26500301, text_id=26500301, duration=4500)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')
        self.hide_guide_summary(entity_id=26500301)


# 게임룰을 설명한다.
class GameRuleNotice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 숨바꼭질 게임룰 설명 시간
        self.set_event_ui_script(type=BannerType.Text, script='$61000023_ME__61000023_MAIN__1$', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DivideIntoTeams') == 1:
            return DivideIntoTeams(self.ctx)


# 팀 나누기
class DivideIntoTeams(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 편 나누기 시간
        self.show_count_ui(text='$61000023_ME__61000023_MAIN__0$', count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MoveGameArea') == 1:
            return MoveGameArea(self.ctx)
        if self.user_value(key='ShortOfUser') == 1:
            return ShortOfUser(self.ctx)


# 유저가 게임포탈로 이동할 동안 카메라 무빙
class MoveGameArea(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BeInHidingTeams') == 1:
            return BeInHidingTeams(self.ctx)
        if self.user_value(key='ShortOfUser') == 1:
            return ShortOfUser(self.ctx)


# 사물로 숨기
class BeInHidingTeams(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 사물팀 숨는 소요 시간
        self.set_timer(timer_id='1', seconds=30, auto_remove=True, display=True)
        self.field_game_message(custom=1, type='SetEventUI', arg1=True, script='$61000023_ME__61000023_MAIN__2$', duration=30000)
        self.field_game_message(custom=2, type='SetEventUI', arg1=True, script='$61000023_ME__61000023_MAIN__3$', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LookingForATeams') == 1:
            return LookingForATeams(self.ctx)
        if self.user_value(key='TeamMatchResult') == 1:
            return TeamMatchResult(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


# 술래잡기 시작
class LookingForATeams(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 술래팀 사물찾는데 소요 시간
        self.set_timer(timer_id='1', seconds=150, auto_remove=True, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TeamMatchResult') == 1:
            return TeamMatchResult(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


# 숨바꼭질 승패 결정
class TeamMatchResult(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameExitNotice') == 1:
            return GameExitNotice(self.ctx)


# 게임종료를 설명한다.
class GameExitNotice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 숨바꼭질 게임종료 설명 시간
        self.set_event_ui_script(type=BannerType.Text, script='$61000023_ME__61000023_MAIN__4$', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return End(self.ctx)


# 플레이어 부족으로 방폭 메세지
class ShortOfUser(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 방폭 진행 시간 단위
        self.set_event_ui_script(type=BannerType.Text, script='$61000023_ME__61000023_MAIN__5$', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return End(self.ctx)


# 게임종료
class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


initial_state = StateNone
