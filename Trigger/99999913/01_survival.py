""" trigger/99999913/01_survival.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame


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
        self.set_interact_object(trigger_ids=[11000037], state=1) # Normal Box
        self.set_interact_object(trigger_ids=[11000039], state=1) # Normal Box
        self.set_sound(trigger_id=20000) # BGM Intro
        self.set_sound(trigger_id=20001) # BGM Loop
        self.sight_range(enable=True, range=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Wait01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect


class Wait01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=60, start_delay=1, interval=1, v_offset=-80) # test용 수정 가능 지점
        self.set_event_ui(type=1, arg2='잠시 기다려주세요.\\n잠시 후 경기 시작점이 결정됩니다.', arg3='4000', arg4='0')
        self.write_log(log_name='Survival', event='Waiting_Start') # 서바이벌 대기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait02(self.ctx)
        if self.time_expired(timer_id='1'):
            # test용 수정 가능 지점 StartPositionRandomPick  / CheckTheNumberOfPlayers
            return CheckTheNumberOfPlayers(self.ctx)


class Wait02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait01(self.ctx)
        if self.time_expired(timer_id='1'):
            # test용 수정 가능 지점 StartPositionRandomPick  / CheckTheNumberOfPlayers
            return CheckTheNumberOfPlayers(self.ctx)


class CheckTheNumberOfPlayers(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9000) < 20:
            # 20명 미만이면 게임 취소
            return GameCancel01(self.ctx)
        if self.count_users(box_id=9000) >= 20:
            # 20명 이상이면 게임 시작
            return StartPositionRandomPick(self.ctx)


class StartPositionRandomPick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.set_event_ui(type=1, arg2='시작점으로 이동합니다.', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=12.5):
            return PCRemap01_North(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap02_South(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap03_East(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap04_West(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap05_NorthWest(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap06_NorthEast(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap07_SouthWest(self.ctx)
        if self.random_condition(weight=12.5):
            return PCRemap08_SouthEast(self.ctx)


class PCRemap01_North(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=101, box_id=9000)
        self.write_log(log_name='Survival', event='Waiting_PositionPick') # 위치 이동 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=1)


class PCRemap02_South(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=102, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=2)


class PCRemap03_East(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=103, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=3)


class PCRemap04_West(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=104, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=4)


class PCRemap05_NorthWest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=105, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=5)


class PCRemap06_NorthEast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=106, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=6)


class PCRemap07_SouthWest(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=107, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=7)


class PCRemap08_SouthEast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=82000001, portal_id=108, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PVPReady(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=2, key='SetRide', value=8)


class PVPReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='space 키를 누르면  수레에 탈 수 있습니다.\\nspace 키를 다시 누르면 수레에서 내립니다.', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PVPStart(self.ctx)


class PVPStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='경기를 곧 시작합니다!\\n경기 시작과 함께 수레가 출발합니다!', arg3='4000', arg4='0')
        self.create_field_game(type=FieldGame.MapleSurvival)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Countdown(self.ctx)


class Countdown(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='경기 시작!', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return AreaOpen(self.ctx)


class AreaOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=5, key='RareBoxOnCount', value=1)
        self.set_user_value(trigger_id=2, key='StartPatrol', value=1)
        self.set_sound(trigger_id=20000, enable=True) # BGM Intro
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_user_value(trigger_id=4, key='InvincibleOff', value=1)
        self.add_buff(box_ids=[9000], skill_id=71000053, level=1, is_player=False, is_skill_set=False) # 31초 무적
        self.set_effect(trigger_ids=[4000,4100,4200,4300,4400,4500,4600,4700,4800]) # SafeZone Barrier Effect
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007], start_delay=1000, fade=2.0) # Barrier Center
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107], start_delay=1000, fade=2.0) # Barrier_North
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207], start_delay=1000, fade=2.0) # Barrier_South
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307], start_delay=1000, fade=2.0) # Barrier_East
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407], start_delay=1000, fade=2.0) # Barrier_West
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507], start_delay=1000, fade=2.0) # Barrier_SouthEast
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607], start_delay=1000, fade=2.0) # Barrier_SouthWest
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707], start_delay=1000, fade=2.0) # Barrier_NorthEast
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807], start_delay=1000, fade=2.0) # Barrier_NorthWest
        self.write_log(log_name='Survival', event='Start') # 서바이벌 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return GameStart(self.ctx)


class GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # BGM Intro
        self.set_sound(trigger_id=20001, enable=True) # BGM Loop
        self.set_user_value(trigger_id=3, key='StormStart', value=1)
        self.write_log(log_name='Survival', event='StormStart') # 서바이벌 스톰 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000037], state=0) # Normal Box
        self.set_interact_object(trigger_ids=[11000039], state=0) # Normal Box
        self.set_user_value(trigger_id=5, key='RareBoxOff', value=1)
        self.write_log(log_name='Survival', event='Trigger_End') # 서바이벌 트리거 종료 로그 남김
        self.destroy_monster(spawn_ids=[-1])


# 인원 미만으로 인한 경기 취소
class GameCancel01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='참가자 부족으로 인해 경기를 취소합니다.', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameCancel02(self.ctx)


class GameCancel02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='잠시 후 원래 있던 곳으로 돌아갑니다.', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return GameCancel03(self.ctx)


class GameCancel03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000037], state=0) # Normal Box
        self.set_interact_object(trigger_ids=[11000039], state=0) # Normal Box
        self.destroy_monster(spawn_ids=[-1])
        self.move_user()


initial_state = Setting
