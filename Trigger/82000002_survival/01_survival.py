""" trigger/82000002_survival/01_survival.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame, BannerType


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[4000,4100,4200,4300,4400,4500,4600,4700,4800]) # SafeZone Barrier Effect
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007], visible=True) # Barrier Center
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True) # Barrier North
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True) # Barrier South
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307], visible=True) # Barrier East
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407], visible=True) # Barrier West
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507], visible=True) # Barrier SouthEast
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607], visible=True) # Barrier SouthWest
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707], visible=True) # Barrier NorthEast
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807], visible=True) # Barrier NorthWest
        self.set_sound(trigger_id=20000) # BGM Intro
        self.set_sound(trigger_id=20001) # BGM Loop
        self.set_local_camera(camera_id=100)
        self.sight_range(enable=True, range=3, range_z=300, border=75)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            # 원본 state : Wait_Talk01
            # 비행선 생성하려면 : CheckPCLocation / 추가로 인원수 수정 필요
            # 비행선 없이 빠른 시작 : Countdown  / 인원수 수정 필요 없음
            return Wait_Talk01(self.ctx) # test용 수정 가능 지점

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect
        # test용 수정 가능 지점 / arg2="30" / arg2 시간 더 짧게 가능  arg2="10"
        self.set_timer(timer_id='1', seconds=59, auto_remove=True, display=True, v_offset=-80)
        self.write_log(log_name='Survival', event='Waiting_Start') # 서바이벌 대기 시작


class Wait_Talk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait_Talk02(self.ctx)
        if self.time_expired(timer_id='1'):
            return ChangeBGM(self.ctx)


class Wait_Talk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait_Talk03(self.ctx)
        if self.time_expired(timer_id='1'):
            return ChangeBGM(self.ctx)


class Wait_Talk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait_Talk01(self.ctx)
        if self.time_expired(timer_id='1'):
            return ChangeBGM(self.ctx)


class ChangeBGM(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(trigger_id=20000, enable=True) # BGM Intro

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return StartGameExplain(self.ctx)


class StartGameExplain(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GameExplain01(self.ctx)


class GameExplain01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=6000, script='$82000002_survival__01_SURVIVAL__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return GameExplain02(self.ctx)


class GameExplain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=3000, script='$82000002_survival__01_SURVIVAL__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GameExplain03(self.ctx)


class GameExplain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=3000, script='$82000002_survival__01_SURVIVAL__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GameExplain04(self.ctx)


class GameExplain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GameExplain05(self.ctx)


class GameExplain05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__14$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CheckPCLocation(self.ctx)


class CheckPCLocation(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return StartPoint01_North(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return StartPoint02_South(self.ctx)
        if self.user_detected(box_ids=[9003]):
            return StartPoint03_East(self.ctx)
        if self.user_detected(box_ids=[9004]):
            return StartPoint04_West(self.ctx)
        if self.user_detected(box_ids=[9005]):
            return StartPoint05_NorthWest(self.ctx)
        if self.user_detected(box_ids=[9006]):
            return StartPoint06_NorthEast(self.ctx)
        if self.user_detected(box_ids=[9007]):
            return StartPoint07_SouthWest(self.ctx)
        if self.user_detected(box_ids=[9008]):
            return StartPoint08_SouthEast(self.ctx)


class StartPoint01_North(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=1)


class StartPoint02_South(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=2)


class StartPoint03_East(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=3)


class StartPoint04_West(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=4)


class StartPoint05_NorthWest(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=5)


class StartPoint06_NorthEast(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=6)


class StartPoint07_SouthWest(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=7)


class StartPoint08_SouthEast(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=8)


class PVPReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__8$') # 누가 우승할지 보자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            # 원본 state : CheckTheNumberOfPlayers
            # 인원 체크 생략하려면  : MatchingSuccessDelay
            return CheckTheNumberOfPlayers(self.ctx) # test용 수정 가능 지점


class CheckTheNumberOfPlayers(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) >= 20:
            # 10명 이상이면 게임 시작
            return MatchingSuccessDelay(self.ctx)
        if self.count_users(box_id=9000) < 20:
            # 10명 미만이면 게임 취소
            return MatchingFailDelay(self.ctx)


class MatchingSuccessDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(trigger_id=7, key='HidePartyUI', value=1) # 팀 모드에서 사용하지 않음
        self.play_system_sound_in_box(sound='GuildBattle_Enter')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MatchingSuccess(self.ctx)


class MatchingSuccess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__9$') # 충분히 모였군!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return RideRiseUp(self.ctx)


class RideRiseUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='StartPatrol', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Countdown(self.ctx)


class Countdown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_field_game(type=FieldGame.MapleSurvivalTeam)
        self.show_count_ui(text='$82000002_survival__01_SURVIVAL__10$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return AreaOpen(self.ctx)


class AreaOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477], is_start=True) # 나태 버섯 Normal Mob
        self.set_user_value(trigger_id=5, key='RareBoxOnCount', value=1)
        self.set_user_value(trigger_id=8, key='RareMobOnCount', value=1)
        self.set_user_value(trigger_id=9, key='NormaBoxOnCount', value=1)
        self.set_user_value(trigger_id=16, key='ExtraEventCheck', value=1)
        # # test용 수정 가능 지점 : 이벤트 즉시 발동
        self.set_user_value(trigger_id=16, key='ExtraEventTestOn', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_user_value(trigger_id=4, key='InvincibleOff', value=1)
        self.add_buff(box_ids=[9000], skill_id=71000053, level=1, ignore_player=False, is_skill_set=False) # 31초 무적 버프
        # test용 수정 가능 지점 : 무적 버프 없이 게임하려면 주석 처리
        self.set_effect(trigger_ids=[4000,4100,4200,4300,4400,4500,4600,4700,4800]) # SafeZone Barrier Effect
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007], start_delay=1000, fade=1.0) # Barrier Center
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107], start_delay=1000, fade=1.0) # Barrier_North
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207], start_delay=1000, fade=1.0) # Barrier_South
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307], start_delay=1000, fade=1.0) # Barrier_East
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407], start_delay=1000, fade=1.0) # Barrier_West
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507], start_delay=1000, fade=1.0) # Barrier_SouthEast
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607], start_delay=1000, fade=1.0) # Barrier_SouthWest
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707], start_delay=1000, fade=1.0) # Barrier_NorthEast
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807], start_delay=1000, fade=1.0) # Barrier_NorthWest
        self.set_sound(trigger_id=20000) # BGM Intro
        self.set_sound(trigger_id=20001, enable=True) # BGM Loop
        self.write_log(log_name='Survival', event='Start') # 서바이벌 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            # test용 수정 가능 지점 : 게임 시작 후 스톰 생성 딜레이
            return GameStart(self.ctx)


class GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # test용 수정 가능 지점 : 스톰 생성 안하려면 주석 처리
        self.set_user_value(trigger_id=3, key='StormStart', value=1)
        self.write_log(log_name='Survival', event='StormStart') # 서바이벌 스톰 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return Quit(self.ctx)
        if not self.is_playing_maple_survival():
            return GameEnd(self.ctx)


# 인원 미만으로 인한 경기 취소
class MatchingFailDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='guildBattle_MatchingFail')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MatchingFail(self.ctx)


class MatchingFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__11$') # 인원 부족

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameCancel(self.ctx)


class GameCancel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__12$') # 경기 취소

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReadyToKickOut(self.ctx)


class ReadyToKickOut(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$82000002_survival__01_SURVIVAL__13$', duration=4000, box_ids=['0']) # 잠시 후 원래 있던 곳으로 돌아갑니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class GameEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9000], skill_id=70001101, level=1, ignore_player=False, is_skill_set=False) # 변신 탈 것 해제용 버프
        # 우승자 카메라 (LocalTargetCamera 호출) 연출 시, 워포그 해제
        self.sight_range(range=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=5, key='RareBoxOff', value=1)
        self.set_user_value(trigger_id=8, key='RareMobOff', value=1)
        self.set_user_value(trigger_id=9, key='NormaBoxOff', value=1)
        self.set_user_value(trigger_id=16, key='ExtraEventOff', value=1)
        self.destroy_monster(spawn_ids=[-1])
        self.move_user()
        self.start_combine_spawn(group_id=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477]) # 나태 버섯 Normal Mob


initial_state = Setting
