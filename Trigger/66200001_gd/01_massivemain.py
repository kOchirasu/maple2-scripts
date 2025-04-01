""" trigger/66200001_gd/01_massivemain.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame, BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_field_game(type=FieldGame.GuildVsGame)
        self.user_tag_symbol(symbol1='guild_game_blue', symbol2='guild_game_red')
        self.set_sound(trigger_id=10000) # Intro
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000) # Puzzle
        self.set_effect(trigger_ids=[8000]) # Scratch
        self.set_effect(trigger_ids=[8002]) # BlueTeamBox
        self.set_effect(trigger_ids=[8003]) # BlueTeamArrow
        self.set_effect(trigger_ids=[8004]) # RedTeamBox
        self.set_effect(trigger_ids=[8005]) # RedTeamArrow
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True) # Dance
        self.set_mesh(trigger_ids=[511,512,513,514], visible=True) # Row1
        self.set_mesh(trigger_ids=[521,522,523,524], visible=True) # Row2
        self.set_mesh(trigger_ids=[531,532,533,534], visible=True) # Row3
        self.set_mesh(trigger_ids=[541,542,543,544], visible=True) # Row4
        self.set_mesh(trigger_ids=[110,111,112,113,114,115]) # 1,1 / 0 to 5
        self.set_mesh(trigger_ids=[120,121,122,123,124,125]) # 1,2 / 0 to 5
        self.set_mesh(trigger_ids=[130,131,132,133,134,135]) # 1,3 / 0 to 5
        self.set_mesh(trigger_ids=[140,141,142,143,144,145]) # 1,4 / 0 to 5
        self.set_mesh(trigger_ids=[210,211,212,213,214,215]) # 2,1 / 0 to 5
        self.set_mesh(trigger_ids=[220,221,222,223,224,225]) # 2,2 / 0 to 5
        self.set_mesh(trigger_ids=[230,231,232,233,234,235]) # 2,3 / 0 to 5
        self.set_mesh(trigger_ids=[240,241,242,243,244,245]) # 2,4 / 0 to 5
        self.set_mesh(trigger_ids=[310,311,312,313,314,315]) # 3,1 / 0 to 5
        self.set_mesh(trigger_ids=[320,321,322,323,324,325]) # 3,2 / 0 to 5
        self.set_mesh(trigger_ids=[330,331,332,333,334,335]) # 3,3 / 0 to 5
        self.set_mesh(trigger_ids=[340,341,342,343,344,345]) # 3,4 / 0 to 5
        self.set_mesh(trigger_ids=[410,411,412,413,414,415]) # 4,1 / 0 to 5
        self.set_mesh(trigger_ids=[420,421,422,423,424,425]) # 4,2 / 0 to 5
        self.set_mesh(trigger_ids=[430,431,432,433,434,435]) # 4,3 / 0 to 5
        self.set_mesh(trigger_ids=[440,441,442,443,444,445]) # 4,4 / 0 to 5
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914]) # Barrier
        self.set_interact_object(trigger_ids=[10001180], state=0) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_user_value(key='Round', value=0)
        self.set_user_value(key='DanceTime', value=0)
        self.set_user_value(key='WinnerTeam', value=0)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=7) # LeavePortal_EndGame
        self.set_portal(portal_id=8) # LeavePortal_EndGame
        self.set_portal(portal_id=9) # LeavePortal_EndGame
        self.set_portal(portal_id=10) # LeavePortal_EndGame

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return EntryDelay(self.ctx) # 테스트 수정 가능 지점


class EntryDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=9001) # 해킹 보안용 시작 box 설정
        self.set_user_value(trigger_id=9, key='MoveToTeamPortal', value=1) # 팀 대기 공간으로 이동 시작
        self.set_user_value(trigger_id=10, key='BannerCheckIn', value=1) # 대기 공간 인원 체크 시작
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        self.set_timer(timer_id='1', seconds=90) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            # MoveToTeamCamp
            return IsGameStartOrNot(self.ctx) # 테스트 수정 가능 지점


# 유효 게임 판정 (팀별 인원수 체크)
class IsGameStartOrNot(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000, user_tag_id=1) >= 10:
            # 1팀 10명 이상인지
            return IsGameStart_True01(self.ctx)
        if self.count_users(box_id=9000, user_tag_id=2) >= 10:
            # 2팀 10명 이상인지
            return IsGameStart_Ture02(self.ctx)
        if self.count_users(box_id=9000, user_tag_id=1) < 10:
            # 1팀 10명 미만이면
            return IsGameStart_False(self.ctx)


class IsGameStart_True01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000, user_tag_id=2) >= 10:
            # 2팀 10명 이상인지
            return MoveToTeamCamp(self.ctx)
        if self.count_users(box_id=9000, user_tag_id=2) < 10:
            # 2팀 10명 미만이면, 1팀 부전승
            return DefaultbyWin_BlueTeam(self.ctx) # 1팀=블루팀 부전승


class IsGameStart_Ture02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000, user_tag_id=1) >= 10:
            # 1팀 10명 이상인지
            return MoveToTeamCamp(self.ctx)
        if self.count_users(box_id=9000, user_tag_id=1) < 10:
            # 1팀 10명 미만이면, 2팀 부전승
            return DefaultbyWin_RedTeam(self.ctx) # 2팀=레드팀 부전승


class IsGameStart_False(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000, user_tag_id=2) < 10:
            # 2팀 10명 미만이면
            return GameCancel(self.ctx) # 게임 취소


# 팀 대기 공간으로 이동
class MoveToTeamCamp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9, key='MoveToTeamPortal', value=2) # 팀 대기 공간으로 이동 종료 = 입장 종료
        self.move_to_portal(user_tag_id=1, portal_id=21) # Tag1=Blue
        self.move_to_portal(user_tag_id=2, portal_id=22) # Tag2=Red
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GameGuide01(self.ctx)


# 길드 미니게임 대전 게임 진행 방식 안내
class GameGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.set_user_value(trigger_id=10, key='BannerCheckIn', value=0) # 대기 공간 인원 체크 종료
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=10000, enable=True) # Intro
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__0$', duration=5000, box_ids=['0'])
        self.set_achievement(trigger_id=9000, type='trigger', achieve='guildminigame_start') # 이벤트 퀘스트 관련

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameGuide02(self.ctx)


class GameGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__1$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameGuide03(self.ctx)


class GameGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__2$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameGuide04(self.ctx)


class GameGuide04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__3$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return R01Ready(self.ctx)


class R01Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=1) # 테스트 수정 가능 지점
        self.set_event_ui_round(rounds=[1,5]) # Round1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R01PlayerRandomPick01(self.ctx)


# 무작위 이동 안내 전 안내 / 1 라운드 전용
class R01PlayerRandomPick01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__67$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerRandomPick02(self.ctx)


class PlayerRandomPick02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='BattleField_Event')
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__5$', duration=5000, box_ids=['0'])
        self.set_effect(trigger_ids=[8002], visible=True) # BlueTeamBox
        self.set_effect(trigger_ids=[8003], visible=True) # BlueTeamArrow
        self.set_effect(trigger_ids=[8004], visible=True) # RedTeamBox
        self.set_effect(trigger_ids=[8005], visible=True) # RedTeamArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return PlayerRandomPickStartCount(self.ctx)


# 무작위 이동 안내 / 라운드 공용
class PlayerRandomPickStartCount(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$66200001_GD__01_MASSIVEMAIN__6$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PlayerRandomPickMove(self.ctx)


class PlayerRandomPickMove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8002]) # BlueTeamBox
        self.set_effect(trigger_ids=[8003]) # BlueTeamArrow
        self.set_effect(trigger_ids=[8004]) # RedTeamBox
        self.set_effect(trigger_ids=[8005]) # RedTeamArrow
        self.move_random_user(map_id=66200001, portal_id=1, box_id=9031, count=30) # 1번 포탈로 블루팀 최대 30명 이동
        self.move_random_user(map_id=66200001, portal_id=2, box_id=9032, count=30) # 2번 포탈로 블루팀 최대 30명 이동
        self.play_system_sound_in_box(box_ids=[9000], sound='GuildBattle_MemberPick')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CheckTheNumberOfPlayer(self.ctx)
        if not self.user_detected(box_ids=[9000]):
            return LeaveAll(self.ctx)


class CheckTheNumberOfPlayer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        self.play_system_sound_in_box(box_ids=[9000], sound='BattleField_Event')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round') == 1:
            return R01Start(self.ctx)
        if self.user_value(key='Round') == 2:
            return R02Start(self.ctx)
        if self.user_value(key='Round') == 3:
            return R03Start(self.ctx)
        if self.user_value(key='Round') == 4:
            return R04Start(self.ctx)
        if self.user_value(key='Round') == 5:
            return R05Start(self.ctx)


# R01 시작
class R01Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__7$', duration=3000, box_ids=['0']) # Voice 02000953
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_01')
        self.set_sound(trigger_id=10000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DanceTime(self.ctx)


"""
댄스 패턴 / 라운드 공용
R01 DanceTime 패턴 랜덤
"""
class R01DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.set_user_value(key='DanceTime', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0701(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms


# Dance 9000ms
class DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001181], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return CheckDanceRound(self.ctx)


# Dance 12000ms
class DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001182], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return CheckDanceRound(self.ctx)


# Dance 15000ms
class DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001183], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return CheckDanceRound(self.ctx)


# Dance 7000ms+ 9000ms
class DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001180], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return DancePattern0402(self.ctx)


class DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__8$', duration=1000) # Voice 02000958
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_01')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001180], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DancePattern0403(self.ctx)


class DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__9$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return DancePattern0404(self.ctx)


class DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001181], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return CheckDanceRound(self.ctx)


# Dance 9000ms+ 7000ms
class DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001181], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return DancePattern0502(self.ctx)


class DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__10$', duration=1000) # Voice 02000982
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_02')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001181], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DancePattern0503(self.ctx)


class DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__11$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001180], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return DancePattern0504(self.ctx)


class DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001180], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return CheckDanceRound(self.ctx)


# Dance 12000ms+ 7000ms
class DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001182], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return DancePattern0602(self.ctx)


class DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__12$', duration=1000) # Voice 02000983
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_03')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001182], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DancePattern0603(self.ctx)


class DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__13$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001180], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return DancePattern0604(self.ctx)


class DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001180], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return CheckDanceRound(self.ctx)


# Dance 7000ms+ 12000ms
class DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001180], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return DancePattern0702(self.ctx)


class DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__14$', duration=1000) # Voice 02000984
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_04')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001180], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DancePattern0703(self.ctx)


class DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__15$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001182], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return DancePattern0704(self.ctx)


class DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001182], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return CheckDanceRound(self.ctx)


class CheckDanceRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DanceTime') == 1:
            return R01_GameStartDelay(self.ctx)
        if self.user_value(key='DanceTime') == 2:
            return R02_GameStartDelay(self.ctx)
        if self.user_value(key='DanceTime') == 3:
            return R03_GameStartDelay(self.ctx)
        if self.user_value(key='DanceTime') == 4:
            return R04_GameStartDelay(self.ctx)
        if self.user_value(key='DanceTime') == 5:
            return R05_GameStartDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='DanceTime', value=0)


class R01_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01_GameStart(self.ctx)


class R01_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__16$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R01_GameTimerStart(self.ctx)


class R01_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round1 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R01G00Check(self.ctx)


"""
R01 인원 체크 시작
테스트 수정 가능 지점
"""
class R01G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 50:
            return G05P00_Random(self.ctx)
        if self.count_users(box_id=9001) > 40:
            return G05orG04(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G03orG04orG05(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G02orG03orG04(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G02orG03(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            return G01orG02(self.ctx)


"""
R01  인원 체크 끝
패턴 그룹 2개 랜덤 / 라운드 공용
"""
class G05orG04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=80.0):
            return G05P00_Random(self.ctx)
        if self.random_condition(weight=20.0):
            return G04P00_Random(self.ctx)


class G03orG04orG05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G03P00_Random(self.ctx)
        if self.random_condition(weight=60.0):
            return G04P00_Random(self.ctx)
        if self.random_condition(weight=30.0):
            return G05P00_Random(self.ctx)


class G02orG03orG04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G02P00_Random(self.ctx)
        if self.random_condition(weight=60.0):
            return G03P00_Random(self.ctx)
        if self.random_condition(weight=30.0):
            return G04P00_Random(self.ctx)


class G02orG03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=60.0):
            return G02P00_Random(self.ctx)
        if self.random_condition(weight=40.0):
            return G03P00_Random(self.ctx)


class G01orG02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=70.0):
            return G01P00_Random(self.ctx)
        if self.random_condition(weight=30.0):
            return G02P00_Random(self.ctx)


# G05 패턴 랜덤 / 라운드 공용
class G05P00_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return G05P01_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P02_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P03_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P04_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P05_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P06_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P07_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P08_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P09_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P10_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P11_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P12_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P13_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P14_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P15_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P16_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P17_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P18_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P19_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P20_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P21_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P22_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P23_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P24_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P25_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P26_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P27_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P28_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P29_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P30_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P31_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P32_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P33_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P34_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P35_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P36_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P37_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P38_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P39_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P40_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P41_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P42_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P43_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P44_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P45_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P46_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P47_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P48_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P49_RoundCheckIn(self.ctx)
        if self.random_condition(weight=2.0):
            return G05P50_RoundCheckIn(self.ctx)


# G04 패턴 랜덤
class G04P00_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G04P01_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P02_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P03_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P04_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P05_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P06_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P07_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P08_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P09_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P10_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P11_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P12_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P13_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P14_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P15_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P16_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P17_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P18_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P19_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P20_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P21_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P22_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P23_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P24_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P25_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P26_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P27_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P28_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P29_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P30_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P31_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P32_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P33_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P34_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P35_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P36_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P37_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P38_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P39_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G04P40_RoundCheckIn(self.ctx)


# G03 패턴 랜덤
class G03P00_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G03P01_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P02_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P03_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P04_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P05_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P06_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P07_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P08_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P09_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P10_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P11_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P12_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P13_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P14_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P15_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P16_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P17_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P18_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P19_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P20_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P21_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P22_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P23_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P24_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P25_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P26_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P27_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P28_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P29_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G03P30_RoundCheckIn(self.ctx)


# G02 패턴 랜덤
class G02P00_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G02P01_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P02_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P03_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P04_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P05_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P06_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P07_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P08_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P09_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P10_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P11_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P12_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P13_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P14_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P15_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P16_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P17_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P18_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P19_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P20_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P21_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P22_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P23_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P24_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P25_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P26_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P27_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P28_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P29_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G02P30_RoundCheckIn(self.ctx)


# G01 패턴 랜덤
class G01P00_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G01P01_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P02_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P03_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P04_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P05_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P06_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P07_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P08_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P09_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P10_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P11_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P12_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P13_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P14_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P15_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P16_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P17_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P18_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P19_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P20_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P21_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P22_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P23_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P24_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P25_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P26_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P27_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P28_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P29_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G01P30_RoundCheckIn(self.ctx)


# R01 종료
class R01EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7120, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7130, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7140, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7210, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7220, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7230, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7240, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7310, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7320, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7330, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7340, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7410, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7420, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7430, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7440, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=4, key='RoundScoreRecord', value=1) # 스코어 배너 기록
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01End(self.ctx)


class R01End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)
        self.set_user_value(trigger_id=8110, key='Barrier11', value=10)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=10)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=10)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=10)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=10)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=10)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=10)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=10)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=10)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=10)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=10)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=10)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=10)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=10)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=10)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=10)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RoundResultNotice01(self.ctx)


class RoundResultNotice01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            # BlueTeam_RoundWin
            return RoundResult_BlueTeamWin01(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            # BlueTeam_RoundWin
            return RoundResult_RedTeamWin01(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            # 무승부인 경우
            return RoundResult_Draw01(self.ctx)


class RoundResult_BlueTeamWin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__17$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__18$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R01RoundScoreRecord(self.ctx)


class RoundResult_RedTeamWin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__19$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__20$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R01RoundScoreRecord(self.ctx)


class RoundResult_Draw01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__21$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__22$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_Draw_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_Draw_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R01RoundScoreRecord(self.ctx)


# R01 라운드 승패 판정
class R01RoundScoreRecord(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WinnerTeam') == 0:
            return EveryPlayerVacuumGuide(self.ctx)
        if self.user_value(key='WinnerTeam') == 1:
            return BlueTeamWinAlreadyNotice(self.ctx)
        if self.user_value(key='WinnerTeam') == 2:
            return RedTeamWinAlreadyNotice(self.ctx)


# 라운드 종료 멤버 리셋 / 라운드 공용
class EveryPlayerVacuumGuide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__23$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveryPlayerVacuumExecute(self.ctx)


class EveryPlayerVacuumExecute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9001, user_tag_id=1, portal_id=21) # Tag1=Blue 통과자들 진영으로
        self.move_to_portal(box_id=9001, user_tag_id=2, portal_id=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round') == 1:
            return R02Ready(self.ctx)
        if self.user_value(key='Round') == 2:
            return R03Ready(self.ctx)
        if self.user_value(key='Round') == 3:
            return R04Ready(self.ctx)
        if self.user_value(key='Round') == 4:
            return R05Ready(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시


# R02 시작
class R02Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=2)
        self.set_event_ui_round(rounds=[2,5]) # Round2

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R02PlayerRandomPick01(self.ctx)


# 무작위 이동 안내 전 안내 / 2,3,4 라운드 전용
class R02PlayerRandomPick01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__4$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerRandomPick02(self.ctx)


# 무작위 이동 안내 / 라운드 공용
class R02Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__24$', duration=3000, box_ids=['0']) # Voice 02000954
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_02')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DanceTime(self.ctx)


# R02 DanceTime 패턴 랜덤
class R02DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.set_user_value(key='DanceTime', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0701(self.ctx)


# DancePattern & CheckDanceRound
class R02_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02_GameStart(self.ctx)


class R02_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__25$', duration=4000) # Voice 02000960
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R02_GameTimerStart(self.ctx)


class R02_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round2 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R02G00Check(self.ctx)


"""
R02 인원 체크 시작
테스트 수정 가능 지점
"""
class R02G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 50:
            return G05P00_Random(self.ctx)
        if self.count_users(box_id=9001) > 40:
            return G05orG04(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G03orG04orG05(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G02orG03orG04(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G02orG03(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            return G01orG02(self.ctx)


# R02 인원 체크 끝
class R02EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7120, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7130, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7140, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7210, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7220, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7230, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7240, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7310, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7320, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7330, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7340, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7410, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7420, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7430, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7440, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=4, key='RoundScoreRecord', value=2) # 스코어 배너 기록
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02End(self.ctx)


class R02End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)
        self.set_user_value(trigger_id=8110, key='Barrier11', value=10)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=10)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=10)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=10)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=10)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=10)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=10)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=10)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=10)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=10)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=10)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=10)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=10)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=10)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=10)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=10)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RoundResultNotice02(self.ctx)


class RoundResultNotice02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            # BlueTeam_RoundWin
            return RoundResult_BlueTeamWin02(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            # BlueTeam_RoundWin
            return RoundResult_RedTeamWin02(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            # 무승부인 경우
            return RoundResult_Draw02(self.ctx)


class RoundResult_BlueTeamWin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__26$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__27$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R02RoundScoreRecord(self.ctx)


class RoundResult_RedTeamWin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__28$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__29$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R02RoundScoreRecord(self.ctx)


class RoundResult_Draw02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__30$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__31$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_Draw_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_Draw_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R02RoundScoreRecord(self.ctx)


# R02 라운드 승패 판정
class R02RoundScoreRecord(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WinnerTeam') == 0:
            return EveryPlayerVacuumGuide(self.ctx)
        if self.user_value(key='WinnerTeam') == 1:
            return BlueTeamWinAlreadyNotice(self.ctx)
        if self.user_value(key='WinnerTeam') == 2:
            return RedTeamWinAlreadyNotice(self.ctx)


"""
라운드 종료 멤버 리셋 / 라운드 공용
R03 시작
"""
class R03Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=3)
        self.set_event_ui_round(rounds=[3,5]) # Round3

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R02PlayerRandomPick01(self.ctx)


class R03Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__32$', duration=3000, box_ids=['0']) # Voice 02000955
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_03')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        # self.start_mini_game_round(box_id=9001, round=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DanceTime(self.ctx)


# R03 DanceTime 패턴 랜덤
class R03DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.set_user_value(key='DanceTime', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return DancePattern0701(self.ctx)


# DancePattern & CheckDanceRound
class R03_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03_GameStart(self.ctx)


class R03_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__33$', duration=4000) # Voice 02000961
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R03_GameTimerStart(self.ctx)


class R03_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round3 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R03G00Check(self.ctx)


"""
R03 인원 체크 시작
테스트 수정 가능 지점
"""
class R03G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 50:
            return G05P00_Random(self.ctx)
        if self.count_users(box_id=9001) > 40:
            return G05orG04(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G03orG04orG05(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G02orG03orG04(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G02orG03(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            return G01orG02(self.ctx)


# R03 인원 체크 끝
class R03EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7120, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7130, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7140, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7210, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7220, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7230, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7240, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7310, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7320, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7330, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7340, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7410, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7420, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7430, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7440, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=4, key='RoundScoreRecord', value=3) # 스코어 배너 기록
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03End(self.ctx)


class R03End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)
        self.set_user_value(trigger_id=8110, key='Barrier11', value=10)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=10)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=10)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=10)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=10)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=10)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=10)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=10)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=10)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=10)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=10)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=10)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=10)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=10)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=10)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=10)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RoundResultNotice03(self.ctx)


class RoundResultNotice03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            # BlueTeam_RoundWin
            return RoundResult_BlueTeamWin03(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            # BlueTeam_RoundWin
            return RoundResult_RedTeamWin03(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            # 무승부인 경우
            return RoundResult_Draw03(self.ctx)


class RoundResult_BlueTeamWin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__34$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__35$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R03RoundScoreRecord(self.ctx)


class RoundResult_RedTeamWin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__36$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__37$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R03RoundScoreRecord(self.ctx)


class RoundResult_Draw03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__38$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__39$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_Draw_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_Draw_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R03RoundScoreRecord(self.ctx)


# R03 라운드 승패 판정
class R03RoundScoreRecord(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WinnerTeam') == 0:
            return EveryPlayerVacuumGuide(self.ctx)
        if self.user_value(key='WinnerTeam') == 1:
            return BlueTeamWinAlreadyNotice(self.ctx)
        if self.user_value(key='WinnerTeam') == 2:
            return RedTeamWinAlreadyNotice(self.ctx)


"""
라운드 종료 멤버 리셋 / 라운드 공용
R04 시작
"""
class R04Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=4)
        self.set_event_ui_round(rounds=[4,5]) # Round4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R02PlayerRandomPick01(self.ctx)


class R04Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__40$', duration=3000, box_ids=['0']) # Voice 02000956
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_04')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DanceTime(self.ctx)


# R04 DanceTime 패턴 랜덤
class R04DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.set_user_value(key='DanceTime', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return DancePattern01(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern02(self.ctx)
        if self.random_condition(weight=5.0):
            return DancePattern03(self.ctx)
        if self.random_condition(weight=25.0):
            return DancePattern0401(self.ctx)
        if self.random_condition(weight=25.0):
            return DancePattern0501(self.ctx)
        if self.random_condition(weight=20.0):
            return DancePattern0601(self.ctx)
        if self.random_condition(weight=20.0):
            return DancePattern0701(self.ctx)


# DancePattern & CheckDanceRound
class R04_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04_GameStart(self.ctx)


# R04 Normal Game
class R04_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__41$', duration=4000) # Voice 02000962
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R04_GameTimerStart(self.ctx)


class R04_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round4 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R04G00Check(self.ctx)


"""
R04 인원 체크 시작
테스트 수정 가능 지점
"""
class R04G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 50:
            return G05P00_Random(self.ctx)
        if self.count_users(box_id=9001) > 40:
            return G05orG04(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G03orG04orG05(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G02orG03orG04(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G02orG03(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            return G01orG02(self.ctx)


"""
R04 인원 체크 끝
R04 Normal End
"""
class R04EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7120, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7130, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7140, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7210, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7220, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7230, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7240, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7310, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7320, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7330, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7340, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7410, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7420, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7430, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7440, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=4, key='RoundScoreRecord', value=4) # 스코어 배너 기록
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04End(self.ctx)


class R04End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)
        self.set_user_value(trigger_id=8110, key='Barrier11', value=10)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=10)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=10)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=10)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=10)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=10)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=10)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=10)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=10)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=10)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=10)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=10)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=10)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=10)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=10)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=10)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return RoundResultNotice04(self.ctx)


class RoundResultNotice04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            # BlueTeam_RoundWin
            return RoundResult_BlueTeamWin04(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            # BlueTeam_RoundWin
            return RoundResult_RedTeamWin04(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            # 무승부인 경우
            return RoundResult_Draw04(self.ctx)


class RoundResult_BlueTeamWin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__42$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__43$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R04RoundScoreRecord(self.ctx)


class RoundResult_RedTeamWin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__44$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__45$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R04RoundScoreRecord(self.ctx)


class RoundResult_Draw04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__46$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__47$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_Draw_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_Draw_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return R04RoundScoreRecord(self.ctx)


# R04 라운드 승패 판정
class R04RoundScoreRecord(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WinnerTeam') == 0:
            return EveryPlayerVacuumGuide(self.ctx)
        if self.user_value(key='WinnerTeam') == 1:
            return BlueTeamWinAlreadyNotice(self.ctx)
        if self.user_value(key='WinnerTeam') == 2:
            return RedTeamWinAlreadyNotice(self.ctx)


"""
라운드 종료 멤버 리셋 / 라운드 공용
R05 시작
"""
class R05Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=5)
        self.set_event_ui_round(rounds=[5,5]) # Round5

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R05PlayerRandomPick01(self.ctx)


# 무작위 이동 안내 전 안내 / 5 라운드 전용
class R05PlayerRandomPick01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__68$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerRandomPick02(self.ctx)


class R05Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__48$', duration=3000, box_ids=['0']) # Voice 02000957
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_05')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DanceTime(self.ctx)


# R05 DanceTime 패턴 랜덤
class R05DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.set_user_value(key='DanceTime', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return DancePattern01(self.ctx)
        if self.random_condition(weight=3.0):
            return DancePattern02(self.ctx)
        if self.random_condition(weight=5.0):
            return DancePattern03(self.ctx)
        if self.random_condition(weight=20.0):
            return DancePattern0401(self.ctx)
        if self.random_condition(weight=20.0):
            return DancePattern0501(self.ctx)
        if self.random_condition(weight=25.0):
            return DancePattern0601(self.ctx)
        if self.random_condition(weight=25.0):
            return DancePattern0701(self.ctx)


# DancePattern & CheckDanceRound
class R05_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05_GameStart(self.ctx)


class R05_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001180], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001181], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001182], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001183], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$66200001_GD__01_MASSIVEMAIN__49$', duration=4000) # Voice 02000963
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R05_GameTimerStart(self.ctx)


class R05_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round5 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R05G05Check(self.ctx)


"""
R05 인원 체크 시작
테스트 수정 가능 지점
"""
class R05G05Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 50:
            return G05P00_Random(self.ctx)
        if self.count_users(box_id=9001) > 40:
            return G05orG04(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G03orG04orG05(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G02orG03orG04(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G02orG03(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            return G01orG02(self.ctx)


# R05 인원 체크 끝
class R05EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7120, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7130, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7140, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7210, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7220, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7230, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7240, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7310, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7320, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7330, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7340, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7410, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7420, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7430, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=7440, key='ColorEnd', value=1) # color reset
        self.set_user_value(trigger_id=4, key='RoundScoreRecord', value=5) # 스코어 배너 기록
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05End(self.ctx)


class R05End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)
        self.set_user_value(trigger_id=8110, key='Barrier11', value=10)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=10)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=10)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=10)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=10)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=10)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=10)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=10)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=10)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=10)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=10)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=10)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=10)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=10)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=10)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=10)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return RoundResultNotice05(self.ctx)


class RoundResultNotice05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_scored_team(team_id=1):
            # BlueTeam_RoundWin
            return RoundResult_BlueTeamWin05(self.ctx)
        if self.guild_vs_game_scored_team(team_id=2):
            # BlueTeam_RoundWin
            return RoundResult_RedTeamWin05(self.ctx)
        if self.guild_vs_game_scored_team(team_id=0):
            # 무승부인 경우
            return RoundResult_Draw05(self.ctx)


class RoundResult_BlueTeamWin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__50$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__51$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute(self.ctx)


class RoundResult_RedTeamWin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__52$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__53$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute(self.ctx)


class RoundResult_Draw05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__54$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__55$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_Draw_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_Draw_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute(self.ctx)


# 게임 종료 모든 팀원 각 진영으로
class GameWrapUp_EveryPlayerVacuumExecute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9001, user_tag_id=1, portal_id=21) # Tag1=Blue 통과자들 진영으로
        self.move_to_portal(box_id=9001, user_tag_id=2, portal_id=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return R05RoundScoreRecord(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시


# 최종 라운드 승패 판정
class R05RoundScoreRecord(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.guild_vs_game_winner_team(team_id=1):
            return BlueTeamWin_GiveReward(self.ctx)
        if self.guild_vs_game_winner_team(team_id=2):
            return RedTeamWin_GiveReward(self.ctx)
        if self.guild_vs_game_winner_team(team_id=0):
            return DrawGame_GiveReward(self.ctx)


# 5 라운드 이전 승패 판정
class BlueTeamWinAlreadyNotice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__56$', duration=3000, user_tag_id=1) # BlueTeam 승리
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__57$', duration=3000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return BlueTeamWinWinAlready_VacuumExecute(self.ctx)


class BlueTeamWinWinAlready_VacuumExecute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9001, user_tag_id=1, portal_id=21) # Tag1=Blue 통과자들 진영으로
        self.move_to_portal(box_id=9001, user_tag_id=2, portal_id=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BlueTeamWin_GiveReward(self.ctx)


class RedTeamWinAlreadyNotice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__58$', duration=3000, user_tag_id=2) # RedTeam 승리
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__59$', duration=3000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='System_YouWin_01')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='System_YouLose_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return RedTeamWinAlready_VacuumExecute(self.ctx)


class RedTeamWinAlready_VacuumExecute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9001, user_tag_id=1, portal_id=21) # Tag1=Blue 통과자들 진영으로
        self.move_to_portal(box_id=9001, user_tag_id=2, portal_id=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RedTeamWin_GiveReward(self.ctx)


# 정상 게임 1팀 블루팀 승리
class BlueTeamWin_GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_give_reward(type='fund', team_id=1, is_win=True) # BlueTeam 승리
        self.guild_vs_game_give_reward(type='exp', team_id=1, is_win=True) # BlueTeam 승리
        self.guild_vs_game_give_reward(type='guildCoin', team_id=1, is_win=True) # BlueTeam 승리
        self.guild_vs_game_give_contribution(team_id=1, is_win=True) # BlueTeam 승리
        self.guild_vs_game_give_reward(type='fund', team_id=2) # RedTeam 패배
        self.guild_vs_game_give_reward(type='exp', team_id=2) # RedTeam 패배
        self.guild_vs_game_give_reward(type='guildCoin', team_id=2) # RedTeam 패배
        self.guild_vs_game_give_contribution(team_id=2) # RedTeam 패배

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ResultPopUp_BlueTeamWin(self.ctx)


# 정상 게임 2팀 레드팀 승리
class RedTeamWin_GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_give_reward(type='fund', team_id=2, is_win=True) # RedTeam 승리
        self.guild_vs_game_give_reward(type='exp', team_id=2, is_win=True) # RedTeam 승리
        self.guild_vs_game_give_reward(type='guildCoin', team_id=2, is_win=True) # RedTeam 승리
        self.guild_vs_game_give_contribution(team_id=2, is_win=True) # RedTeam 승리
        self.guild_vs_game_give_reward(type='fund', team_id=1) # BlueTeam 패배
        self.guild_vs_game_give_reward(type='exp', team_id=1) # BlueTeam 패배
        self.guild_vs_game_give_reward(type='guildCoin', team_id=1) # BlueTeam 패배
        self.guild_vs_game_give_contribution(team_id=1) # BlueTeam 패배

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ResultPopUp_RedTeamWin(self.ctx)


# 정상 게임 무승부
class DrawGame_GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_give_reward(type='fund', team_id=1) # BlueTeam 무승부
        self.guild_vs_game_give_reward(type='exp', team_id=1) # BlueTeam 무승부
        self.guild_vs_game_give_reward(type='guildCoin', team_id=1) # BlueTeam 무승부
        self.guild_vs_game_give_contribution(team_id=1) # BlueTeam 무승부
        self.guild_vs_game_give_reward(type='fund', team_id=2) # RedTeam 무승부
        self.guild_vs_game_give_reward(type='exp', team_id=2) # RedTeam 무승부
        self.guild_vs_game_give_reward(type='guildCoin', team_id=2) # RedTeam 무승부
        self.guild_vs_game_give_contribution(team_id=2) # RedTeam 무승부

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ResultPopUp_Draw(self.ctx)


# 블루팀 승리 결과창 팝업
class ResultPopUp_BlueTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.guild_vs_game_result()
        self.guild_vs_game_log_result()
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='massive_success')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='massive_fail')
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return LeaveAll(self.ctx)


# 레드팀 승리 결과창 팝업
class ResultPopUp_RedTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.guild_vs_game_result()
        self.guild_vs_game_log_result()
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='massive_success')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='massive_fail')
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return LeaveAll(self.ctx)


# 무승부 결과창 팝업
class ResultPopUp_Draw(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.guild_vs_game_result()
        self.guild_vs_game_log_result()
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='massive_fail')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='massive_fail')
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return LeaveAll(self.ctx)


# 1팀=블루팀 부전승
class DefaultbyWin_BlueTeam(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__60$', duration=4000, user_tag_id=1)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__61$', duration=4000, user_tag_id=2)
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='massive_success')
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='massive_fail')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DefaultbyWin_BlueTeam_GiveReward(self.ctx)


class DefaultbyWin_BlueTeam_GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_give_reward(type='fund', team_id=1) # BlueTeam 부전승
        self.guild_vs_game_give_reward(type='exp', team_id=1) # BlueTeam 부전승
        self.guild_vs_game_give_reward(type='guildCoin', team_id=1) # BlueTeam 부전승
        self.guild_vs_game_give_contribution(team_id=1) # BlueTeam 부전승
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.guild_vs_game_log_won_by_default(team_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LeaveAll(self.ctx)


# 2팀=레드팀 부전승
class DefaultbyWin_RedTeam(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[0,0])
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__62$', duration=4000, user_tag_id=2)
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__63$', duration=4000, user_tag_id=1)
        self.play_system_sound_by_user_tag(user_tag_id=2, sound_key='massive_success')
        self.play_system_sound_by_user_tag(user_tag_id=1, sound_key='massive_fail')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DefaultbyWin_RedTeam_GiveReward(self.ctx)


class DefaultbyWin_RedTeam_GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_give_reward(type='fund', team_id=2) # RedTeam 부전승
        self.guild_vs_game_give_reward(type='exp', team_id=2) # RedTeam 부전승
        self.guild_vs_game_give_reward(type='guildCoin', team_id=2) # BlueTeam 부전승
        self.guild_vs_game_give_contribution(team_id=2) # RedTeam 부전승
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.guild_vs_game_log_won_by_default(team_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LeaveAll(self.ctx)


# 인원 미달 게임 취소
class GameCancel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True) # LeavePortal_EndGame
        self.set_event_ui_round(rounds=[0,0])
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__64$', duration=4000, trigger_box_id=9000)
        self.play_system_sound_in_box(box_ids=[9000], sound='massive_fail')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LeaveAll(self.ctx)


class LeaveAll(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guild_vs_game_end_game()
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_sound(trigger_id=40000) # Game
        self.show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__65$', duration=10000, trigger_box_id=9000)
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Ending_03')
        self.set_sound(trigger_id=10000) # Intro

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


"""
그룹별패턴 모음
G01 P01
"""
class G01P01_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P01Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P01_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P01_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P01_Check(self.ctx)


class G01P01_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P01TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P01_End(self.ctx)


class G01P01_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P01End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P02
class G01P02_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P02Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P02_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P02_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P02_Check(self.ctx)


class G01P02_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P02TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P02_End(self.ctx)


class G01P02_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P02End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P03
class G01P03_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P03Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P03_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P03_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P03_Check(self.ctx)


class G01P03_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P03TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P03_End(self.ctx)


class G01P03_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P03End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P04
class G01P04_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P04Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P04_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P04_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P04_Check(self.ctx)


class G01P04_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P04TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P04_End(self.ctx)


class G01P04_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P04End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P05
class G01P05_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P05Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P05_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P05_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P05_Check(self.ctx)


class G01P05_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P05TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P05_End(self.ctx)


class G01P05_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P05End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P06
class G01P06_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P06Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P06_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P06_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P06_Check(self.ctx)


class G01P06_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P06TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P06_End(self.ctx)


class G01P06_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P06End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P07
class G01P07_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P07Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P07_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P07_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P07_Check(self.ctx)


class G01P07_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P07TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P07_End(self.ctx)


class G01P07_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P07End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P08
class G01P08_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P08Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P08_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P08_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P08_Check(self.ctx)


class G01P08_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P08TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P08_End(self.ctx)


class G01P08_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P08End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P09
class G01P09_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P09Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P09_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P09_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P09_Check(self.ctx)


class G01P09_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P09TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P09_End(self.ctx)


class G01P09_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P09End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P10
class G01P10_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P10Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P10_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P10_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P10_Check(self.ctx)


class G01P10_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P10TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P10_End(self.ctx)


class G01P10_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P10End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P11
class G01P11_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P11Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P11_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P11_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P11_Check(self.ctx)


class G01P11_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P11TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P11_End(self.ctx)


class G01P11_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P11End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P12
class G01P12_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P12Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P12_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P12_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P12_Check(self.ctx)


class G01P12_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P12TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P12_End(self.ctx)


class G01P12_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P12End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P13
class G01P13_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P13Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P13_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P13_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P13_Check(self.ctx)


class G01P13_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P13TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P13_End(self.ctx)


class G01P13_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P13End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P14
class G01P14_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P14Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P14_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P14_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P14_Check(self.ctx)


class G01P14_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P14TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P14_End(self.ctx)


class G01P14_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P14End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P15
class G01P15_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P15Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P15_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P15_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P15_Check(self.ctx)


class G01P15_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P15TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P15_End(self.ctx)


class G01P15_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P15End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P16
class G01P16_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P16Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P16_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P16_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P16_Check(self.ctx)


class G01P16_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P16TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P16_End(self.ctx)


class G01P16_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P16End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P17
class G01P17_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P17Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P17_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P17_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P17_Check(self.ctx)


class G01P17_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P17TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P17_End(self.ctx)


class G01P17_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P17End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P18
class G01P18_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P18Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P18_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P18_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P18_Check(self.ctx)


class G01P18_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P18TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P18_End(self.ctx)


class G01P18_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P18End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P19
class G01P19_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P19Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P19_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P19_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P19_Check(self.ctx)


class G01P19_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P19TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P19_End(self.ctx)


class G01P19_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P19End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P20
class G01P20_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P20Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P20_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P20_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P20_Check(self.ctx)


class G01P20_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P20TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P20_End(self.ctx)


class G01P20_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P20End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P21
class G01P21_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P21Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P21_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P21_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P21_Check(self.ctx)


class G01P21_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P21TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P21_End(self.ctx)


class G01P21_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P21End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P22
class G01P22_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P22Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P22_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P22_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P22_Check(self.ctx)


class G01P22_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P22TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P22_End(self.ctx)


class G01P22_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P22End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P23
class G01P23_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P23Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P23_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P23_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P23_Check(self.ctx)


class G01P23_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P23TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P23_End(self.ctx)


class G01P23_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P23End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P24
class G01P24_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P24Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P24_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P24_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P24_Check(self.ctx)


class G01P24_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P24TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P24_End(self.ctx)


class G01P24_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P24End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P25
class G01P25_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P25Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P25_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P25_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P25_Check(self.ctx)


class G01P25_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P25TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P25_End(self.ctx)


class G01P25_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P25End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P26
class G01P26_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P26Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P26_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P26_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P26_Check(self.ctx)


class G01P26_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P26TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P26_End(self.ctx)


class G01P26_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P26End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P27
class G01P27_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P27Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P27_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P27_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P27_Check(self.ctx)


class G01P27_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P27TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P27_End(self.ctx)


class G01P27_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P27End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P28
class G01P28_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P28Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P28_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P28_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P28_Check(self.ctx)


class G01P28_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P28TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P28_End(self.ctx)


class G01P28_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P28End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P29
class G01P29_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P29Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P29_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P29_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P29_Check(self.ctx)


class G01P29_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P29TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P29_End(self.ctx)


class G01P29_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P29End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G01 P30
class G01P30_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P30Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G01P30_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G01P30_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G01P30_Check(self.ctx)


class G01P30_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='G01P30TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G01P30_End(self.ctx)


class G01P30_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G01P30End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P01
class G02P01_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P01Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P01_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P01_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P01_Check(self.ctx)


class G02P01_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P01TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P01_End(self.ctx)


class G02P01_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P01End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P02
class G02P02_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P02Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P02_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P02_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P02_Check(self.ctx)


class G02P02_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P02TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P02_End(self.ctx)


class G02P02_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P02End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P03
class G02P03_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P03Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P03_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P03_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P03_Check(self.ctx)


class G02P03_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P03TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P03_End(self.ctx)


class G02P03_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P03End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P04
class G02P04_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P04Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P04_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P04_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P04_Check(self.ctx)


class G02P04_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P04TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P04_End(self.ctx)


class G02P04_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P04End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P05
class G02P05_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P05Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P05_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P05_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P05_Check(self.ctx)


class G02P05_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P05TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P05_End(self.ctx)


class G02P05_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P05End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P06
class G02P06_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P06Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P06_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P06_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P06_Check(self.ctx)


class G02P06_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P06TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P06_End(self.ctx)


class G02P06_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P06End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P07
class G02P07_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P07Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P07_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P07_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P07_Check(self.ctx)


class G02P07_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P07TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P07_End(self.ctx)


class G02P07_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P07End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P08
class G02P08_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P08Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P08_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P08_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P08_Check(self.ctx)


class G02P08_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P08TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P08_End(self.ctx)


class G02P08_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P08End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P09
class G02P09_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P09Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P09_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P09_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P09_Check(self.ctx)


class G02P09_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P09TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P09_End(self.ctx)


class G02P09_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P09End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P10
class G02P10_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P10Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P10_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P10_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P10_Check(self.ctx)


class G02P10_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P10TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P10_End(self.ctx)


class G02P10_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P10End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P11
class G02P11_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P11Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P11_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P11_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P11_Check(self.ctx)


class G02P11_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P11TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P11_End(self.ctx)


class G02P11_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P11End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P12
class G02P12_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P12Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P12_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P12_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P12_Check(self.ctx)


class G02P12_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P12TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P12_End(self.ctx)


class G02P12_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P12End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P13
class G02P13_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P13Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P13_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P13_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P13_Check(self.ctx)


class G02P13_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P13TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P13_End(self.ctx)


class G02P13_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P13End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P14
class G02P14_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P14Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P14_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P14_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P14_Check(self.ctx)


class G02P14_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P14TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P14_End(self.ctx)


class G02P14_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P14End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P15
class G02P15_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P15Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P15_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P15_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P15_Check(self.ctx)


class G02P15_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P15TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P15_End(self.ctx)


class G02P15_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P15End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P16
class G02P16_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P16Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P16_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P16_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P16_Check(self.ctx)


class G02P16_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P16TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P16_End(self.ctx)


class G02P16_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P16End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P17
class G02P17_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P17Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P17_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P17_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P17_Check(self.ctx)


class G02P17_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P17TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P17_End(self.ctx)


class G02P17_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P17End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P18
class G02P18_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P18Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P18_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P18_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P18_Check(self.ctx)


class G02P18_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P18TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P18_End(self.ctx)


class G02P18_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P18End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P19
class G02P19_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P19Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P19_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P19_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P19_Check(self.ctx)


class G02P19_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P19TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P19_End(self.ctx)


class G02P19_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P19End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P20
class G02P20_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P20Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P20_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P20_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P20_Check(self.ctx)


class G02P20_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P20TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P20_End(self.ctx)


class G02P20_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P20End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P21
class G02P21_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P21Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P21_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P21_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P21_Check(self.ctx)


class G02P21_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P21TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P21_End(self.ctx)


class G02P21_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P21End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P22
class G02P22_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P22Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P22_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P22_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P22_Check(self.ctx)


class G02P22_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P22TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P22_End(self.ctx)


class G02P22_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P22End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P23
class G02P23_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P23Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P23_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P23_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P23_Check(self.ctx)


class G02P23_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P23TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P23_End(self.ctx)


class G02P23_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P23End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P24
class G02P24_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P24Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P24_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P24_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P24_Check(self.ctx)


class G02P24_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P24TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P24_End(self.ctx)


class G02P24_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P24End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P25
class G02P25_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P25Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P25_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P25_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P25_Check(self.ctx)


class G02P25_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P25TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P25_End(self.ctx)


class G02P25_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P25End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P26
class G02P26_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P26Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P26_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P26_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P26_Check(self.ctx)


class G02P26_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P26TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P26_End(self.ctx)


class G02P26_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P26End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P27
class G02P27_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P27Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P27_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P27_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P27_Check(self.ctx)


class G02P27_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P27TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P27_End(self.ctx)


class G02P27_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P27End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P28
class G02P28_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P28Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P28_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P28_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P28_Check(self.ctx)


class G02P28_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P28TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P28_End(self.ctx)


class G02P28_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P28End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P29
class G02P29_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P29Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P29_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P29_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P29_Check(self.ctx)


class G02P29_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P29TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P29_End(self.ctx)


class G02P29_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P29End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G02 P30
class G02P30_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P30Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G02P30_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G02P30_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G02P30_Check(self.ctx)


class G02P30_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=200, key='G02P30TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G02P30_End(self.ctx)


class G02P30_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G02P30End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P01
class G03P01_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P01Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P01_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P01_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P01_Check(self.ctx)


class G03P01_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P01TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P01_End(self.ctx)


class G03P01_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P01End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P02
class G03P02_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P02Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P02_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P02_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P02_Check(self.ctx)


class G03P02_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P02TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P02_End(self.ctx)


class G03P02_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P02End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P03
class G03P03_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P03Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P03_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P03_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P03_Check(self.ctx)


class G03P03_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P03TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P03_End(self.ctx)


class G03P03_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P03End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P04
class G03P04_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P04Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P04_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P04_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P04_Check(self.ctx)


class G03P04_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P04TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P04_End(self.ctx)


class G03P04_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P04End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P05
class G03P05_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P05Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P05_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P05_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P05_Check(self.ctx)


class G03P05_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P05TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P05_End(self.ctx)


class G03P05_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P05End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P06
class G03P06_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P06Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P06_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P06_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P06_Check(self.ctx)


class G03P06_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P06TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P06_End(self.ctx)


class G03P06_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P06End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P07
class G03P07_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P07Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P07_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P07_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P07_Check(self.ctx)


class G03P07_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P07TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P07_End(self.ctx)


class G03P07_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P07End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P08
class G03P08_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P08Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P08_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P08_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P08_Check(self.ctx)


class G03P08_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P08TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P08_End(self.ctx)


class G03P08_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P08End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P09
class G03P09_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P09Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P09_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P09_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P09_Check(self.ctx)


class G03P09_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P09TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P09_End(self.ctx)


class G03P09_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P09End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P10
class G03P10_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P10Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P10_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P10_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P10_Check(self.ctx)


class G03P10_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P10TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P10_End(self.ctx)


class G03P10_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P10End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P11
class G03P11_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P11Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P11_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P11_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P11_Check(self.ctx)


class G03P11_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P11TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P11_End(self.ctx)


class G03P11_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P11End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P12
class G03P12_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P12Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P12_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P12_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P12_Check(self.ctx)


class G03P12_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P12TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P12_End(self.ctx)


class G03P12_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P12End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P13
class G03P13_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P13Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P13_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P13_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P13_Check(self.ctx)


class G03P13_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P13TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P13_End(self.ctx)


class G03P13_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P13End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P14
class G03P14_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P14Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P14_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P14_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P14_Check(self.ctx)


class G03P14_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P14TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P14_End(self.ctx)


class G03P14_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P14End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P15
class G03P15_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P15Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P15_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P15_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P15_Check(self.ctx)


class G03P15_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P15TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P15_End(self.ctx)


class G03P15_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P15End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P16
class G03P16_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P16Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P16_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P16_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P16_Check(self.ctx)


class G03P16_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P16TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P16_End(self.ctx)


class G03P16_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P16End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P17
class G03P17_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P17Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P17_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P17_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P17_Check(self.ctx)


class G03P17_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P17TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P17_End(self.ctx)


class G03P17_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P17End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P18
class G03P18_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P18Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P18_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P18_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P18_Check(self.ctx)


class G03P18_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P18TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P18_End(self.ctx)


class G03P18_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P18End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P19
class G03P19_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P19Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P19_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P19_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P19_Check(self.ctx)


class G03P19_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P19TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P19_End(self.ctx)


class G03P19_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P19End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P20
class G03P20_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P20Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P20_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P20_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P20_Check(self.ctx)


class G03P20_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P20TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P20_End(self.ctx)


class G03P20_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P20End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P21
class G03P21_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P21Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P21_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P21_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P21_Check(self.ctx)


class G03P21_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P21TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P21_End(self.ctx)


class G03P21_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P21End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P22
class G03P22_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P22Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P22_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P22_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P22_Check(self.ctx)


class G03P22_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P22TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P22_End(self.ctx)


class G03P22_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P22End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P23
class G03P23_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P23Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P23_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P23_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P23_Check(self.ctx)


class G03P23_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P23TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P23_End(self.ctx)


class G03P23_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P23End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P24
class G03P24_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P24Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P24_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P24_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P24_Check(self.ctx)


class G03P24_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P24TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P24_End(self.ctx)


class G03P24_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P24End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P25
class G03P25_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P25Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P25_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P25_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P25_Check(self.ctx)


class G03P25_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P25TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P25_End(self.ctx)


class G03P25_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P25End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P26
class G03P26_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P26Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P26_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P26_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P26_Check(self.ctx)


class G03P26_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P26TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P26_End(self.ctx)


class G03P26_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P26End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P27
class G03P27_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P27Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P27_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P27_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P27_Check(self.ctx)


class G03P27_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P27TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P27_End(self.ctx)


class G03P27_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P27End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P28
class G03P28_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P28Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P28_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P28_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P28_Check(self.ctx)


class G03P28_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P28TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P28_End(self.ctx)


class G03P28_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P28End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P29
class G03P29_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P29Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P29_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P29_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P29_Check(self.ctx)


class G03P29_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P29TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P29_End(self.ctx)


class G03P29_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P29End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G03 P30
class G03P30_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P30Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G03P30_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G03P30_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G03P30_Check(self.ctx)


class G03P30_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300, key='G03P30TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G03P30_End(self.ctx)


class G03P30_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P30End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P01
class G04P01_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P01Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P01_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P01_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P01_Check(self.ctx)


class G04P01_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P01TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P01_End(self.ctx)


class G04P01_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P01End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P02
class G04P02_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P02Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P02_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P02_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P02_Check(self.ctx)


class G04P02_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P02TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P02_End(self.ctx)


class G04P02_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P02End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P03
class G04P03_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P03Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P03_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P03_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P03_Check(self.ctx)


class G04P03_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P03TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P03_End(self.ctx)


class G04P03_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P03End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P04
class G04P04_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P04Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P04_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P04_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P04_Check(self.ctx)


class G04P04_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P04TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P04_End(self.ctx)


class G04P04_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P04End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P05
class G04P05_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P05Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P05_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P05_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P05_Check(self.ctx)


class G04P05_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P05TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P05_End(self.ctx)


class G04P05_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P05End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P06
class G04P06_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P06Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P06_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P06_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P06_Check(self.ctx)


class G04P06_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P06TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P06_End(self.ctx)


class G04P06_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P06End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P07
class G04P07_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P07Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P07_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P07_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P07_Check(self.ctx)


class G04P07_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P07TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P07_End(self.ctx)


class G04P07_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P07End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P08
class G04P08_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P08Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P08_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P08_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P08_Check(self.ctx)


class G04P08_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P08TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P08_End(self.ctx)


class G04P08_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P08End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P09
class G04P09_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P09Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P09_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P09_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P09_Check(self.ctx)


class G04P09_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P09TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P09_End(self.ctx)


class G04P09_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P09End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P10
class G04P10_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P10Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P10_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P10_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P10_Check(self.ctx)


class G04P10_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P10TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P10_End(self.ctx)


class G04P10_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P10End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P11
class G04P11_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P11Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P11_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P11_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P11_Check(self.ctx)


class G04P11_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P11TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P11_End(self.ctx)


class G04P11_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P11End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P12
class G04P12_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P12Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P12_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P12_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P12_Check(self.ctx)


class G04P12_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P12TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P12_End(self.ctx)


class G04P12_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P12End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P13
class G04P13_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P13Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P13_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P13_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P13_Check(self.ctx)


class G04P13_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P13TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P13_End(self.ctx)


class G04P13_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P13End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P14
class G04P14_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P14Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P14_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P14_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P14_Check(self.ctx)


class G04P14_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P14TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P14_End(self.ctx)


class G04P14_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P14End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P15
class G04P15_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P15Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P15_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P15_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P15_Check(self.ctx)


class G04P15_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P15TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P15_End(self.ctx)


class G04P15_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P15End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P16
class G04P16_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P16Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P16_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P16_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P16_Check(self.ctx)


class G04P16_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P16TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P16_End(self.ctx)


class G04P16_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P16End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P17
class G04P17_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P17Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P17_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P17_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P17_Check(self.ctx)


class G04P17_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P17TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P17_End(self.ctx)


class G04P17_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P17End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P18
class G04P18_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P18Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P18_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P18_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P18_Check(self.ctx)


class G04P18_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P18TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P18_End(self.ctx)


class G04P18_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P18End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P19
class G04P19_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P19Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P19_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P19_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P19_Check(self.ctx)


class G04P19_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P19TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P19_End(self.ctx)


class G04P19_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P19End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P20
class G04P20_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P20Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P20_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P20_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P20_Check(self.ctx)


class G04P20_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P20TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P20_End(self.ctx)


class G04P20_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P20End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P21
class G04P21_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P21Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P21_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P21_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P21_Check(self.ctx)


class G04P21_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P21TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P21_End(self.ctx)


class G04P21_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P21End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P22
class G04P22_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P22Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P22_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P22_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P22_Check(self.ctx)


class G04P22_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P22TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P22_End(self.ctx)


class G04P22_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P22End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P23
class G04P23_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P23Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P23_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P23_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P23_Check(self.ctx)


class G04P23_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P23TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P23_End(self.ctx)


class G04P23_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P23End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P24
class G04P24_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P24Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P24_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P24_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P24_Check(self.ctx)


class G04P24_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P24TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P24_End(self.ctx)


class G04P24_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P24End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P25
class G04P25_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P25Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P25_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P25_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P25_Check(self.ctx)


class G04P25_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P25TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P25_End(self.ctx)


class G04P25_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P25End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P26
class G04P26_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P26Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P26_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P26_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P26_Check(self.ctx)


class G04P26_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P26TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P26_End(self.ctx)


class G04P26_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P26End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P27
class G04P27_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P27Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P27_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P27_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P27_Check(self.ctx)


class G04P27_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P27TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P27_End(self.ctx)


class G04P27_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P27End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P28
class G04P28_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P28Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P28_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P28_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P28_Check(self.ctx)


class G04P28_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P28TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P28_End(self.ctx)


class G04P28_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P28End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P29
class G04P29_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P29Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P29_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P29_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P29_Check(self.ctx)


class G04P29_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P29TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P29_End(self.ctx)


class G04P29_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P29End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P30
class G04P30_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P30Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P30_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P30_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P30_Check(self.ctx)


class G04P30_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P30TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P30_End(self.ctx)


class G04P30_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P30End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P31
class G04P31_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P31Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P31_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P31_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P31_Check(self.ctx)


class G04P31_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P31TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P31_End(self.ctx)


class G04P31_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P31End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P32
class G04P32_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P32Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P32_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P32_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P32_Check(self.ctx)


class G04P32_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P32TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P32_End(self.ctx)


class G04P32_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P32End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P33
class G04P33_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P33Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P33_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P33_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P33_Check(self.ctx)


class G04P33_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P33TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P33_End(self.ctx)


class G04P33_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P33End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P34
class G04P34_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P34Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P34_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P34_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P34_Check(self.ctx)


class G04P34_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P34TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P34_End(self.ctx)


class G04P34_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P34End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P35
class G04P35_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P35Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P35_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P35_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P35_Check(self.ctx)


class G04P35_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P35TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P35_End(self.ctx)


class G04P35_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P35End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P36
class G04P36_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P36Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P36_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P36_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P36_Check(self.ctx)


class G04P36_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P36TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P36_End(self.ctx)


class G04P36_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P36End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P37
class G04P37_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P37Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P37_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P37_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P37_Check(self.ctx)


class G04P37_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P37TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P37_End(self.ctx)


class G04P37_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P37End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P38
class G04P38_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P38Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P38_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P38_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P38_Check(self.ctx)


class G04P38_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P38TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P38_End(self.ctx)


class G04P38_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P38End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P39
class G04P39_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P39Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P39_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P39_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P39_Check(self.ctx)


class G04P39_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P39TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P39_End(self.ctx)


class G04P39_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P39End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G04 P40
class G04P40_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P40Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G04P40_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G04P40_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G04P40_Check(self.ctx)


class G04P40_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=400, key='G04P40TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G04P40_End(self.ctx)


class G04P40_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G04P40End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P01
class G05P01_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P01Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P01_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P01_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P01_Check(self.ctx)


class G05P01_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P01TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P01_End(self.ctx)


class G05P01_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P01End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P02
class G05P02_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P02Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P02_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P02_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P02_Check(self.ctx)


class G05P02_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P02TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P02_End(self.ctx)


class G05P02_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P02End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P03
class G05P03_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P03Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P03_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P03_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P03_Check(self.ctx)


class G05P03_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P03TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P03_End(self.ctx)


class G05P03_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P03End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P04
class G05P04_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P04Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P04_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P04_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P04_Check(self.ctx)


class G05P04_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P04TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P04_End(self.ctx)


class G05P04_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P04End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P05
class G05P05_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P05Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P05_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P05_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P05_Check(self.ctx)


class G05P05_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P05TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P05_End(self.ctx)


class G05P05_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P05End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P06
class G05P06_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P06Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P06_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P06_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P06_Check(self.ctx)


class G05P06_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P06TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P06_End(self.ctx)


class G05P06_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P06End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P07
class G05P07_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P07Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P07_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P07_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P07_Check(self.ctx)


class G05P07_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P07TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P07_End(self.ctx)


class G05P07_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P07End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P08
class G05P08_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P08Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P08_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P08_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P08_Check(self.ctx)


class G05P08_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P08TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P08_End(self.ctx)


class G05P08_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P08End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P09
class G05P09_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P09Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P09_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P09_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P09_Check(self.ctx)


class G05P09_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P09TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P09_End(self.ctx)


class G05P09_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P09End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P10
class G05P10_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P10Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P10_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P10_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P10_Check(self.ctx)


class G05P10_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P10TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P10_End(self.ctx)


class G05P10_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P10End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P11
class G05P11_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P11Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P11_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P11_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P11_Check(self.ctx)


class G05P11_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P11TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P11_End(self.ctx)


class G05P11_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P11End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P12
class G05P12_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P12Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P12_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P12_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P12_Check(self.ctx)


class G05P12_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P12TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P12_End(self.ctx)


class G05P12_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P12End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P13
class G05P13_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P13Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P13_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P13_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P13_Check(self.ctx)


class G05P13_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P13TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P13_End(self.ctx)


class G05P13_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P13End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P14
class G05P14_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P14Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P14_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P14_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P14_Check(self.ctx)


class G05P14_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P14TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P14_End(self.ctx)


class G05P14_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P14End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P15
class G05P15_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P15Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P15_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P15_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P15_Check(self.ctx)


class G05P15_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P15TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P15_End(self.ctx)


class G05P15_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P15End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P16
class G05P16_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P16Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P16_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P16_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P16_Check(self.ctx)


class G05P16_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P16TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P16_End(self.ctx)


class G05P16_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P16End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P17
class G05P17_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P17Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P17_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P17_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P17_Check(self.ctx)


class G05P17_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P17TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P17_End(self.ctx)


class G05P17_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P17End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P18
class G05P18_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P18Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P18_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P18_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P18_Check(self.ctx)


class G05P18_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P18TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P18_End(self.ctx)


class G05P18_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P18End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P19
class G05P19_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P19Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P19_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P19_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P19_Check(self.ctx)


class G05P19_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P19TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P19_End(self.ctx)


class G05P19_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P19End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P20
class G05P20_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P20Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P20_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P20_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P20_Check(self.ctx)


class G05P20_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P20TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P20_End(self.ctx)


class G05P20_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P20End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P21
class G05P21_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P21Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P21_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P21_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P21_Check(self.ctx)


class G05P21_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P21TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P21_End(self.ctx)


class G05P21_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P21End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P22
class G05P22_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P22Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P22_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P22_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P22_Check(self.ctx)


class G05P22_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P22TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P22_End(self.ctx)


class G05P22_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P22End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P23
class G05P23_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P23Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P23_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P23_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P23_Check(self.ctx)


class G05P23_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P23TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P23_End(self.ctx)


class G05P23_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P23End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P24
class G05P24_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P24Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P24_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P24_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P24_Check(self.ctx)


class G05P24_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P24TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P24_End(self.ctx)


class G05P24_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P24End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P25
class G05P25_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P25Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P25_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P25_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P25_Check(self.ctx)


class G05P25_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P25TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P25_End(self.ctx)


class G05P25_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P25End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P26
class G05P26_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P26Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P26_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P26_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P26_Check(self.ctx)


class G05P26_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P26TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P26_End(self.ctx)


class G05P26_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P26End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P27
class G05P27_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P27Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P27_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P27_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P27_Check(self.ctx)


class G05P27_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P27TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P27_End(self.ctx)


class G05P27_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P27End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P28
class G05P28_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P28Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P28_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P28_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P28_Check(self.ctx)


class G05P28_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P28TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P28_End(self.ctx)


class G05P28_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P28End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P29
class G05P29_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P29Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P29_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P29_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P29_Check(self.ctx)


class G05P29_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P29TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P29_End(self.ctx)


class G05P29_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P29End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P30
class G05P30_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P30Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P30_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P30_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P30_Check(self.ctx)


class G05P30_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P30TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P30_End(self.ctx)


class G05P30_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P30End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P31
class G05P31_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P31Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P31_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P31_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P31_Check(self.ctx)


class G05P31_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P31TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P31_End(self.ctx)


class G05P31_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P31End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P32
class G05P32_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P32Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P32_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P32_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P32_Check(self.ctx)


class G05P32_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P32TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P32_End(self.ctx)


class G05P32_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P32End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P33
class G05P33_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P33Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P33_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P33_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P33_Check(self.ctx)


class G05P33_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P33TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P33_End(self.ctx)


class G05P33_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P33End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P34
class G05P34_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P34Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P34_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P34_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P34_Check(self.ctx)


class G05P34_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P34TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P34_End(self.ctx)


class G05P34_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P34End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P35
class G05P35_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P35Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P35_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P35_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P35_Check(self.ctx)


class G05P35_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P35TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P35_End(self.ctx)


class G05P35_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P35End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P36
class G05P36_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P36Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P36_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P36_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P36_Check(self.ctx)


class G05P36_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P36TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P36_End(self.ctx)


class G05P36_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P36End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P37
class G05P37_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P37Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P37_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P37_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P37_Check(self.ctx)


class G05P37_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P37TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P37_End(self.ctx)


class G05P37_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P37End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P38
class G05P38_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P38Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P38_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P38_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P38_Check(self.ctx)


class G05P38_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P38TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P38_End(self.ctx)


class G05P38_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P38End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P39
class G05P39_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P39Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P39_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P39_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P39_Check(self.ctx)


class G05P39_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P39TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P39_End(self.ctx)


class G05P39_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P39End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P40
class G05P40_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P40Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P40_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P40_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P40_Check(self.ctx)


class G05P40_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P40TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P40_End(self.ctx)


class G05P40_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P40End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P41
class G05P41_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P41Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P41_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P41_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P41_Check(self.ctx)


class G05P41_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P41TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P41_End(self.ctx)


class G05P41_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P41End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P42
class G05P42_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P42Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P42_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P42_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P42_Check(self.ctx)


class G05P42_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P42TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P42_End(self.ctx)


class G05P42_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P42End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P43
class G05P43_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P43Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P43_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P43_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P43_Check(self.ctx)


class G05P43_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P43TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P43_End(self.ctx)


class G05P43_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P43End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P44
class G05P44_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P44Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P44_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P44_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P44_Check(self.ctx)


class G05P44_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P44TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P44_End(self.ctx)


class G05P44_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P44End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P45
class G05P45_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P45Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P45_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P45_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P45_Check(self.ctx)


class G05P45_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P45TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P45_End(self.ctx)


class G05P45_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P45End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P46
class G05P46_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P46Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P46_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P46_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P46_Check(self.ctx)


class G05P46_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P46TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P46_End(self.ctx)


class G05P46_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P46End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P47
class G05P47_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P47Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P47_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P47_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P47_Check(self.ctx)


class G05P47_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P47TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P47_End(self.ctx)


class G05P47_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P47End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P48
class G05P48_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P48Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P48_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P48_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P48_Check(self.ctx)


class G05P48_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P48TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P48_End(self.ctx)


class G05P48_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P48End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P49
class G05P49_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P49Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P49_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P49_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P49_Check(self.ctx)


class G05P49_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P49TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P49_End(self.ctx)


class G05P49_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P49End') == 1:
            return RoundCheckOutDelay(self.ctx)


# G05 P50
class G05P50_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P50Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G05P50_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G05P50_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G05P50_Check(self.ctx)


class G05P50_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=500, key='G05P50TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G05P50_End(self.ctx)


class G05P50_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P50End') == 1:
            return RoundCheckOutDelay(self.ctx)


class RoundCheckOutDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RoundCheckOut(self.ctx)


class RoundCheckOut(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        self.guild_vs_game_score_by_user(box_id=9001, score=1) # 이긴팀에게 라운드 스코어 1점 부여
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=True) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckNextRound(self.ctx)


class CheckNextRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round') == 1:
            return R01EndDelay(self.ctx)
        if self.user_value(key='Round') == 2:
            return R02EndDelay(self.ctx)
        if self.user_value(key='Round') == 3:
            return R03EndDelay(self.ctx)
        if self.user_value(key='Round') == 4:
            return R04EndDelay(self.ctx)
        if self.user_value(key='Round') == 5:
            return R05EndDelay(self.ctx)


initial_state = Wait
