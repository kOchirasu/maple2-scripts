""" trigger/84000007_wd/01_massivemain.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000) # Intro
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000) # Puzzle
        self.set_effect(trigger_ids=[8000]) # Scratch
        self.set_effect(trigger_ids=[8002]) # Fireworks
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
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_user_value(key='Round', value=0)
        self.set_user_value(key='GambleSuccess', value=0)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return EntryDelay(self.ctx) # 테스트 수정 가능 지점


class EntryDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=40) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return MusicChange(self.ctx)
        if self.count_users(box_id=9000) >= 70:
            return MusicChange(self.ctx)


class MusicChange(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 종료 후 펀타임을 위해 전부 스테이지 밖으로 킥
        self.move_user(map_id=84000007, portal_id=1, box_id=9000)
        self.add_buff(box_ids=[9000], skill_id=99940042, level=1, ignore_player=False, is_skill_set=False) # 불꽃놀이 스킬셋 제공
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameGuide01(self.ctx)


class GameGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='BannerCheckIn', value=1)
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=10000, enable=True) # Intro
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__0$', duration=3000, box_ids=['0']) # Voice 02000952
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Notice_01')
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='dailyquest_start') # 결혼식 전용 매시브 이벤트로 off처리
        # # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_start')
        self.give_guild_exp(type=2)
        # self.set_mini_game_area_for_hack(box_id=9001) # 해킹 보안용 시작 box 설정
        self.start_mini_game(box_id=9001, round=5, is_show_result_ui=False, game_name='WDdancedancestop')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GameGuide02(self.ctx)


class GameGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__1$', duration=4000, box_ids=['0']) # Voice 02000981
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Notice_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return GameGuide03(self.ctx)


class GameGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__2$', duration=4000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return GameGuide04(self.ctx)


class GameGuide04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__3$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return R01Start(self.ctx) # 테스트 수정 가능 지점

    def on_exit(self) -> None:
        self.set_user_value(key='Round', value=1) # 테스트 수정 가능 지점


# R01 시작
class R01Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__4$', duration=3000, box_ids=['0']) # Voice 02000953
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_01')
        self.set_event_ui_round(rounds=[1,5]) # Round1
        self.set_sound(trigger_id=10000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.start_mini_game_round(box_id=9001, round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DanceTime(self.ctx)


# R01 DanceTime 패턴 랜덤
class R01DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return R01DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return R01DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return R01DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return R01DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return R01DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return R01DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return R01DancePattern0701(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms


# R01 Dance 9000ms
class R01DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 12000ms
class R01DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 15000ms
class R01DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001440], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 7000ms+ 9000ms
class R01DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R01DancePattern0402(self.ctx)


class R01DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__9$', duration=1000) # Voice 02000958
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_01')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01DancePattern0403(self.ctx)


class R01DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__10$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DancePattern0404(self.ctx)


class R01DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 9000ms+ 7000ms
class R01DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R01DancePattern0502(self.ctx)


class R01DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__11$', duration=1000) # Voice 02000982
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_02')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01DancePattern0503(self.ctx)


class R01DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__12$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DancePattern0504(self.ctx)


class R01DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 12000ms+ 7000ms
class R01DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R01DancePattern0602(self.ctx)


class R01DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__13$', duration=1000) # Voice 02000983
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_03')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01DancePattern0603(self.ctx)


class R01DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__14$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DancePattern0604(self.ctx)


class R01DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R01_GameStartDelay(self.ctx)


# R01 Dance 7000ms+ 12000ms
class R01DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R01DancePattern0702(self.ctx)


class R01DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__15$', duration=1000) # Voice 02000984
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_04')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01DancePattern0703(self.ctx)


class R01DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__16$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R01DancePattern0704(self.ctx)


class R01DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return R01_GameStartDelay(self.ctx)


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
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__17$', duration=4000) # Voice 02000959
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R01_GameTimerStart(self.ctx)


class R01_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=30, auto_remove=True, display=True, v_offset=-40) # Round1 / 30sec  / UI 표시
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
패턴 그룹 2개 랜덤
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


# G05 패턴 랜덤
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
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R01End(self.ctx)


class R01End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return R02Ready(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


"""
R01 종료 후 생존자 인원수에 따른 전체 보상 지급
R02 시작
"""
class R02Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=2)
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02)
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off처리
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02Start(self.ctx)


class R02Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__5$', duration=3000, box_ids=['0']) # Voice 02000954
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_02')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_event_ui_round(rounds=[2,5]) # Round2
        self.start_mini_game_round(box_id=9001, round=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DanceTime(self.ctx)


# R02 DanceTime 패턴 랜덤
class R02DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return R02DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return R02DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return R02DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return R02DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return R02DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return R02DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return R02DancePattern0701(self.ctx)


# R02 Dance 9000ms
class R02DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 12000ms
class R02DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 15000ms
class R02DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001440], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 7000ms+ 9000ms
class R02DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R02DancePattern0402(self.ctx)


class R02DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__9$', duration=1000) # Voice 02000958
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_01')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02DancePattern0403(self.ctx)


class R02DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__10$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DancePattern0404(self.ctx)


class R02DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 9000ms+ 7000ms
class R02DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R02DancePattern0502(self.ctx)


class R02DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__11$', duration=1000) # Voice 02000982
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_02')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02DancePattern0503(self.ctx)


class R02DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__12$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DancePattern0504(self.ctx)


class R02DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 12000ms+ 7000ms
class R02DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R02DancePattern0602(self.ctx)


class R02DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__13$', duration=1000) # Voice 02000983
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_03')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02DancePattern0603(self.ctx)


class R02DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__14$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DancePattern0604(self.ctx)


class R02DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R02_GameStartDelay(self.ctx)


# R02 Dance 7000ms+ 12000ms
class R02DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R02DancePattern0702(self.ctx)


class R02DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__15$', duration=1000) # Voice 02000984
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_04')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02DancePattern0703(self.ctx)


class R02DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__16$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R02DancePattern0704(self.ctx)


class R02DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return R02_GameStartDelay(self.ctx)


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
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__18$', duration=4000) # Voice 02000960
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R02_GameTimerStart(self.ctx)


class R02_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Round2 / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=2) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=2) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R02G00Check(self.ctx)


"""
R02 인원 체크 시작
테스트 수정 가능 지점
"""
class R02G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R02End(self.ctx)


class R02End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return R03Ready(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


"""
R02 종료 후 생존자 인원수에 따른 전체 보상 지급
R03 시작
"""
class R03Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=3)
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02)
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off처리
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03Start(self.ctx)


class R03Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__6$', duration=3000, box_ids=['0']) # Voice 02000955
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_03')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_event_ui_round(rounds=[3,5]) # Round3
        self.start_mini_game_round(box_id=9001, round=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DanceTime(self.ctx)


# R03 DanceTime 패턴 랜덤
class R03DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return R03DancePattern01(self.ctx)
        if self.random_condition(weight=30.0):
            return R03DancePattern02(self.ctx)
        if self.random_condition(weight=30.0):
            return R03DancePattern03(self.ctx)
        if self.random_condition(weight=3.0):
            return R03DancePattern0401(self.ctx)
        if self.random_condition(weight=3.0):
            return R03DancePattern0501(self.ctx)
        if self.random_condition(weight=2.0):
            return R03DancePattern0601(self.ctx)
        if self.random_condition(weight=2.0):
            return R03DancePattern0701(self.ctx)


# R03 Dance 9000ms
class R03DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 12000ms
class R03DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 15000ms
class R03DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001440], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 7000ms+ 9000ms
class R03DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R03DancePattern0402(self.ctx)


class R03DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__9$', duration=1000) # Voice 02000958
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_01')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03DancePattern0403(self.ctx)


class R03DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__10$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DancePattern0404(self.ctx)


class R03DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 9000ms+ 7000ms
class R03DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R03DancePattern0502(self.ctx)


class R03DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__11$', duration=1000) # Voice 02000982
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_02')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03DancePattern0503(self.ctx)


class R03DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__12$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DancePattern0504(self.ctx)


class R03DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 12000ms+ 7000ms
class R03DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R03DancePattern0602(self.ctx)


class R03DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__13$', duration=1000) # Voice 02000983
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_03')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03DancePattern0603(self.ctx)


class R03DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__14$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DancePattern0604(self.ctx)


class R03DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R03_GameStartDelay(self.ctx)


# R03 Dance 7000ms+ 12000ms
class R03DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R03DancePattern0702(self.ctx)


class R03DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__15$', duration=1000) # Voice 02000984
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_04')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03DancePattern0703(self.ctx)


class R03DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__16$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R03DancePattern0704(self.ctx)


class R03DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return R03_GameStartDelay(self.ctx)


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
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__19$', duration=4000) # Voice 02000961
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R03_GameTimerStart(self.ctx)


class R03_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=15, auto_remove=True, display=True, v_offset=-40) # Round3 / 15sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=3) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=3) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R03G00Check(self.ctx)


"""
R03 인원 체크 시작
테스트 수정 가능 지점
"""
class R03G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R03End(self.ctx)


class R03End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return R04Ready(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


"""
R03 종료 후 생존자 인원수에 따른 전체 보상 지급
R04 시작
"""
class R04Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=4)
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02)
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off처리
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04Start(self.ctx)


class R04Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__7$', duration=3000, box_ids=['0']) # Voice 02000956
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_04')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_event_ui_round(rounds=[4,5]) # Round4
        self.start_mini_game_round(box_id=9001, round=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DanceTime(self.ctx)


# R04 DanceTime 패턴 랜덤
class R04DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return R04DancePattern01(self.ctx)
        if self.random_condition(weight=3.0):
            return R04DancePattern02(self.ctx)
        if self.random_condition(weight=5.0):
            return R04DancePattern03(self.ctx)
        if self.random_condition(weight=25.0):
            return R04DancePattern0401(self.ctx)
        if self.random_condition(weight=25.0):
            return R04DancePattern0501(self.ctx)
        if self.random_condition(weight=20.0):
            return R04DancePattern0601(self.ctx)
        if self.random_condition(weight=20.0):
            return R04DancePattern0701(self.ctx)


# R04 Dance 9000ms
class R04DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 12000ms
class R04DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 15000ms
class R04DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001440], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 7000ms+ 9000ms
class R04DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R04DancePattern0402(self.ctx)


class R04DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__9$', duration=1000) # Voice 02000958
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_01')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04DancePattern0403(self.ctx)


class R04DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__10$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DancePattern0404(self.ctx)


class R04DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 9000ms+ 7000ms
class R04DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R04DancePattern0502(self.ctx)


class R04DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__11$', duration=1000) # Voice 02000982
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_02')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04DancePattern0503(self.ctx)


class R04DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__12$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DancePattern0504(self.ctx)


class R04DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 12000ms+ 7000ms
class R04DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R04DancePattern0602(self.ctx)


class R04DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__13$', duration=1000) # Voice 02000983
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_03')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04DancePattern0603(self.ctx)


class R04DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__14$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DancePattern0604(self.ctx)


class R04DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R04_GameStartDelay(self.ctx)


# R04 Dance 7000ms+ 12000ms
class R04DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R04DancePattern0702(self.ctx)


class R04DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__15$', duration=1000) # Voice 02000984
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_04')
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04DancePattern0703(self.ctx)


class R04DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__16$', duration=1500, box_ids=['0'])
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R04DancePattern0704(self.ctx)


class R04DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return R04_GameStartDelay(self.ctx)


class R04_GameStartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            # 결혼식전용 매시브이벤트로 잭팟기능 off
            # transition state="R04_GambleOrNormal00" /
            return R04_GameStart(self.ctx)


"""
R04 Gamble Or Normal 00
테스트 수정 가능 지점
"""
class R04_GambleOrNormal00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) >= 20:
            return R04_GambleOrJackpot(self.ctx)
        if self.count_users(box_id=9001) >= 10:
            return R04_GambleOrNormal(self.ctx)
        if self.count_users(box_id=9001) < 10:
            return R04_GameStart(self.ctx)


# R04 Gamble Or JackPot
class R04_GambleOrJackpot(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=75.0):
            return R04_GambleGuide01(self.ctx)
        if self.random_condition(weight=25.0):
            return R04_JackpotGuide01(self.ctx)


# R04 Gamble Or Normal
class R04_GambleOrNormal(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return R04_GambleGuide01(self.ctx)
        if self.random_condition(weight=50.0):
            return R04_GameStart(self.ctx)


# R04 Gamble Game
class R04_GambleGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=6) # Gamble Round
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__22$', duration=3000) # Voice 02000964
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_06')
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='system_event', level=4, sub_event='gamble')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R04_GambleGuide02(self.ctx)


class R04_GambleGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__23$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R04_GambleTimerStart(self.ctx)


class R04_GambleTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=15, auto_remove=True, display=True, v_offset=-40) # Gamble / 15sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=3) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=6) # 가이드 : 붉은색  발판

    def on_tick(self) -> trigger_api.Trigger:
        return R04GambleCheck(self.ctx)


"""
R04 Gamble 인원 체크 시작
테스트 수정 가능 지점
"""
class R04GambleCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 40:
            return G06P400_Random(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G06P300_Random(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G06P200_Random(self.ctx)
        if self.count_users(box_id=9001) > 10:
            return G06P100_Random(self.ctx)
        if self.count_users(box_id=9001) <= 10:
            # 인원이 갑자기 줄었을 때 트리거 멈춤 방지
            return G06P100_Random(self.ctx)


"""
R04 Gamble 인원 체크 끝
G06 Gamble Random Pattern 40
"""
class G06P400_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G06P401_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P402_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P403_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P404_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P405_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P406_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P407_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P408_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P409_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P410_RoundCheckIn(self.ctx)


# G06 Gamble Random Pattern 30
class G06P300_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G06P301_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P302_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P303_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P304_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P305_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P306_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P307_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P308_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P309_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P310_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P311_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P312_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P313_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P314_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P315_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P316_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P317_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P318_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P319_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P320_RoundCheckIn(self.ctx)


# G06 Gamble Random Pattern 20
class G06P200_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return G06P201_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P202_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P203_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P204_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P205_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P206_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P207_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P208_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P209_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P210_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P211_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P212_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P213_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P214_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P215_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P216_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P217_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P218_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P219_RoundCheckIn(self.ctx)
        if self.random_condition(weight=5.0):
            return G06P220_RoundCheckIn(self.ctx)


# G06 Gamble Random Pattern 10
class G06P100_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G06P101_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P102_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P103_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P104_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P105_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P106_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P107_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P108_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P109_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G06P110_RoundCheckIn(self.ctx)


# R04 Jackpot Game
class R04_JackpotGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=6) # Gamble Round
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__24$', duration=3000) # Voice 02000964
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_06')
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='system_event', level=4, sub_event='jackpot')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R04_JackpotGuide02(self.ctx)


class R04_JackpotGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__25$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return R04_JackpotTimerStart(self.ctx)


class R04_JackpotTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=20, auto_remove=True, display=True, v_offset=-40) # Jackpot / 20sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=2) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=7) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R04JackpotCheck(self.ctx)


"""
R04 Jackpot 인원 체크 시작
테스트 수정 가능 지점
"""
class R04JackpotCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) > 40:
            return G07P400_Random(self.ctx)
        if self.count_users(box_id=9001) > 30:
            return G07P300_Random(self.ctx)
        if self.count_users(box_id=9001) > 20:
            return G07P200_Random(self.ctx)
        if self.count_users(box_id=9001) <= 20:
            # 인원이 갑자기 줄어도 트리거 멈춤 방지
            return G07P200_Random(self.ctx)


"""
R04 Jackpot 인원 체크 끝
G07 Jackpot Random Pattern 400
"""
class G07P400_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G07P401_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P402_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P403_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P404_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P405_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P406_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P407_RoundCheckIn(self.ctx)


# G07 Jackpot Random Pattern 300
class G07P300_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G07P301_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P302_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P303_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P304_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P305_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P306_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P307_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P308_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P309_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P310_RoundCheckIn(self.ctx)


# G07 Jackpot Random Pattern 200
class G07P200_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return G07P201_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P202_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P203_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P204_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P205_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P206_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P207_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P208_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P209_RoundCheckIn(self.ctx)
        if self.random_condition(weight=10.0):
            return G07P210_RoundCheckIn(self.ctx)


# R04 Gamble End
class R04GambleEndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04GambleEnd(self.ctx)


class R04GambleEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return R05ReadyAfterGamble(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


# R05 After Gamble
class R05ReadyAfterGamble(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=5)
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02)
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05StartAfterGamble(self.ctx)


class R05StartAfterGamble(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GambleSuccess') == 1:
            return R05StartGamblePass(self.ctx)
        if self.user_value(key='GambleSuccess') == 0:
            return R05StartGambleFail(self.ctx)


class R05StartGamblePass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__26$', duration=5000, box_ids=['0']) # Voice 02000966
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_02')
        self.set_event_ui_round(rounds=[5,5]) # Round5
        self.start_mini_game_round(box_id=9001, round=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return R05DanceTimeDelay(self.ctx)


class R05StartGambleFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__27$', duration=4000, box_ids=['0']) # Voice 02000967
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_03')
        self.set_event_ui_round(rounds=[5,5]) # Round5
        self.start_mini_game_round(box_id=9001, round=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R05DanceTimeDelay(self.ctx)


# R04 Normal Game
class R04_GameStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=40000, enable=True) # Game
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__20$', duration=4000) # Voice 02000962
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R04_GameTimerStart(self.ctx)


class R04_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=10, auto_remove=True, display=True, v_offset=-40) # Round4 / 10sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=4) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=4) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R04G00Check(self.ctx)


"""
R04 인원 체크 시작
테스트 수정 가능 지점
"""
class R04G00Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


# R04 인원 체크 끝
class R05DanceTimeDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__33$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DanceTime(self.ctx)


# R04 Normal End
class R04EndDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R04End(self.ctx)


class R04End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return R05Ready(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


"""
R04 종료 후 생존자 인원수에 따른 전체 보상 지급
R05 시작
"""
class R05Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Round', value=5)
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02)
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off처리
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05Start(self.ctx)


class R05Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__8$', duration=3000, box_ids=['0']) # Voice 02000957
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancetime_05')
        self.set_sound(trigger_id=40000) # Intro
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_event_ui_round(rounds=[5,5]) # Round5
        self.start_mini_game_round(box_id=9001, round=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DanceTime(self.ctx)


# R05 DanceTime 패턴 랜덤
class R05DanceTime(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return R05DancePattern01(self.ctx)
        if self.random_condition(weight=3.0):
            return R05DancePattern02(self.ctx)
        if self.random_condition(weight=5.0):
            return R05DancePattern03(self.ctx)
        if self.random_condition(weight=20.0):
            return R05DancePattern0401(self.ctx)
        if self.random_condition(weight=20.0):
            return R05DancePattern0501(self.ctx)
        if self.random_condition(weight=25.0):
            return R05DancePattern0601(self.ctx)
        if self.random_condition(weight=25.0):
            return R05DancePattern0701(self.ctx)


# R05 Dance 9000ms
class R05DancePattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 12000ms
class R05DancePattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 15000ms
class R05DancePattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001440], state=1) # 15000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=19000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 7000ms+ 9000ms
class R05DancePattern0401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R05DancePattern0402(self.ctx)


class R05DancePattern0402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__34$', duration=1000)
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05DancePattern0403(self.ctx)


class R05DancePattern0403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__35$', duration=1500, box_ids=['0']) # Voice 02000985
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_05')
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DancePattern0404(self.ctx)


class R05DancePattern0404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 9000ms+ 7000ms
class R05DancePattern0501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001438], state=1) # 9000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return R05DancePattern0502(self.ctx)


class R05DancePattern0502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__36$', duration=1000)
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001438], state=0) # 9000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05DancePattern0503(self.ctx)


class R05DancePattern0503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__37$', duration=1500, box_ids=['0']) # Voice 02000985
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_05')
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DancePattern0504(self.ctx)


class R05DancePattern0504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 12000ms+ 7000ms
class R05DancePattern0601(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return R05DancePattern0602(self.ctx)


class R05DancePattern0602(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__38$', duration=1000)
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05DancePattern0603(self.ctx)


class R05DancePattern0603(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__39$', duration=1500, box_ids=['0']) # Voice 02000985
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_05')
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DancePattern0604(self.ctx)


class R05DancePattern0604(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return R05_GameStartDelay(self.ctx)


# R05 Dance 7000ms+ 12000ms
class R05DancePattern0701(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001437], state=1) # 7000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return R05DancePattern0702(self.ctx)


class R05DancePattern0702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__40$', duration=1000)
        self.set_sound(trigger_id=20000) # Dance
        self.set_sound(trigger_id=30000, enable=True) # Silence
        self.set_effect(trigger_ids=[8000], visible=True) # Scratch
        self.set_interact_object(trigger_ids=[10001437], state=0) # 7000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05DancePattern0703(self.ctx)


class R05DancePattern0703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__41$', duration=1500, box_ids=['0']) # Voice 02000985
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancerandom_05')
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001439], state=0) # 12000ms

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return R05DancePattern0704(self.ctx)


class R05DancePattern0704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=30000) # Silence
        self.set_sound(trigger_id=20000, enable=True) # Dance
        self.play_system_sound_in_box(box_ids=[9001], sound='DDStop_Stage_Ready_01')
        self.set_interact_object(trigger_ids=[10001439], state=1) # 12000ms
        self.set_user_value(trigger_id=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return R05_GameStartDelay(self.ctx)


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
        self.set_interact_object(trigger_ids=[10001437], state=2) # 7000ms
        self.set_interact_object(trigger_ids=[10001438], state=2) # 9000ms
        self.set_interact_object(trigger_ids=[10001439], state=2) # 12000ms
        self.set_interact_object(trigger_ids=[10001440], state=2) # 15000ms
        self.set_event_ui_script(type=BannerType.Text, script='$61000008_ME__01_MASSIVEMAIN__21$', duration=4000) # Voice 02000963
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Round_05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return R05_GameTimerStart(self.ctx)


class R05_GameTimerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11111', seconds=10, auto_remove=True, display=True, v_offset=-40) # Round5 / 10sec  / UI 표시
        self.set_user_value(trigger_id=8, key='CheerUpTimer', value=4) # 이속 증가 버프
        self.set_user_value(trigger_id=7, key='GameGuide', value=5) # 가이드 : 숫자 발판

    def on_tick(self) -> trigger_api.Trigger:
        return R05G05Check(self.ctx)


"""
R05 인원 체크 시작
테스트 수정 가능 지점
"""
class R05G05Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return R05End(self.ctx)


class R05End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.write_log(log_name='dancedancestop', trigger_id=9001, event='round_clear', level=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return GameWrapUp(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            return Fireworks_Lose(self.ctx)


# 불꽃놀이 : 전멸 시. 실제 불꽃놀이 효과는 동일하지만 생존자 유무에 따른 분기 설정
class Fireworks_Lose(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[902,903])
        # 센서: Fireworks.xml의 불꽃놀이 연출 시작
        self.set_user_value(trigger_id=9, key='Fireworks', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return FailAll(self.ctx)


# R05 종료 후 생존자 인원수에 따른 전체 보상 지급
class GameWrapUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.give_exp(box_id=9001, rate=5.7)
        self.end_mini_game_round(winner_box_id=9001, exp_rate=0.02) # win
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_pass') # 결혼식 전용 매시브 이벤트로 off처리
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Fireworks_Win(self.ctx)


"""
완료 카메라 연출 : 내부 규칙에 따라 가장 캐릭터 외모 점수가 높은 타겟을 비주는 카메라
state name="MiniGameCameraDirection"
onEnter
action name="MiniGameCameraDirection" boxId="9001" cameraId="910" /
LocalTargetCamera
/onEnter
condition name="WaitTick" waitTick="5000"
action name="카메라리셋" interpolationTime="1.0"/
불꽃놀이 위해 카메라 리셋
transition state="Fireworks_Win" /
/condition
onExit /
/state
불꽃놀이 : 승리 시. 실제 불꽃놀이 효과는 동일하지만 생존자 유무에 따른 분기 설정
"""

class Fireworks_Win(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[902,903])
        # 센서: Fireworks.xml의 불꽃놀이 연출 시작
        self.set_user_value(trigger_id=9, key='Fireworks', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return GameOver(self.ctx)


# 완료 보상
class GameOver(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=84000007, portal_id=3, box_id=9002)
        self.set_event_ui_script(type=BannerType.Winner, script='$61000008_ME__01_MASSIVEMAIN__29$', duration=3000, box_ids=['9001']) # Voice 02000968
        self.set_event_ui_script(type=BannerType.Lose, script='$61000008_ME__01_MASSIVEMAIN__30$', duration=3000, box_ids=['!9001']) # Voice 02000969
        self.play_system_sound_in_box(box_ids=[9001], sound='DJDD_Ending_01')
        self.play_system_sound_in_box(box_ids=[9010,9011,9012,9013], sound='DJDD_Ending_02')
        # self.set_achievement(trigger_id=9001, type='trigger', achieve='ddstop_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GiveReward(self.ctx)


class GiveReward(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.mini_game_give_reward(winner_box_id=9001, content_type='miniGame') # 결혼식 전용 매시브 이벤트로 off처리
        self.end_mini_game(winner_box_id=9001, game_name='WDdancedancestop')
        # self.create_item(spawn_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041,7042,7043,7044,7045,7046,7047,7048,7049,7050,7051,7052,7053,7054,7055,7056,7057,7058,7059,7060,7061,7062,7063,7064,7065,7066,7067,7068,7069,7070,7071,7072,7073,7074,7075,7076,7077,7078,7079,7080,7081,7082,7083,7084]) # Win
        # self.create_item(spawn_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016,6017,6018,6019,6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033,6034,6035,6036,6037,6038,6039,6040,6041,6042,6043,6044,6045,6046,6047,6048,6049,6050,6051,6052,6053,6054,6055,6056]) # Lose
        self.add_buff(box_ids=[9001], skill_id=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return LeaveAll(self.ctx)


class FailAll(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game(winner_box_id=9001, game_name='WDdancedancestop')
        self.set_event_ui_round(rounds=[0,0])
        self.set_event_ui_script(type=BannerType.GameOver, script='$61000008_ME__01_MASSIVEMAIN__28$', duration=5000) # Voice 02000969
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Ending_02')
        self.set_mesh(trigger_ids=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], start_delay=400) # Barrier
        self.set_user_value(trigger_id=4, key='BannerCheckIn', value=1)
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
        self.set_user_value(trigger_id=7110, key='Color11', value=5) # color reset
        self.set_user_value(trigger_id=7120, key='Color12', value=5) # color reset
        self.set_user_value(trigger_id=7130, key='Color13', value=5) # color reset
        self.set_user_value(trigger_id=7140, key='Color14', value=5) # color reset
        self.set_user_value(trigger_id=7210, key='Color21', value=5) # color reset
        self.set_user_value(trigger_id=7220, key='Color22', value=5) # color reset
        self.set_user_value(trigger_id=7230, key='Color23', value=5) # color reset
        self.set_user_value(trigger_id=7240, key='Color24', value=5) # color reset
        self.set_user_value(trigger_id=7310, key='Color31', value=5) # color reset
        self.set_user_value(trigger_id=7320, key='Color32', value=5) # color reset
        self.set_user_value(trigger_id=7330, key='Color33', value=5) # color reset
        self.set_user_value(trigger_id=7340, key='Color34', value=5) # color reset
        self.set_user_value(trigger_id=7410, key='Color41', value=5) # color reset
        self.set_user_value(trigger_id=7420, key='Color42', value=5) # color reset
        self.set_user_value(trigger_id=7430, key='Color43', value=5) # color reset
        self.set_user_value(trigger_id=7440, key='Color44', value=5) # color reset
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, start_delay=400, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LeaveAll(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='10004')


class LeaveAll(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 종료 후 펀타임을 위해 전부 스테이지 밖으로 킥
        self.move_user(map_id=84000007, portal_id=3, box_id=9001)
        self.add_buff(box_ids=[9000], skill_id=99940042, level=1, ignore_player=False, is_skill_set=False) # 도입부부터 폭죽 터트리고 놀 수 있게 변경
        self.set_local_camera(camera_id=910) # LocalTargetCamera
        # self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_sound(trigger_id=40000) # Game
        self.set_user_value(trigger_id=5, key='BannerNumber', value=0)
        self.set_event_ui_script(type=BannerType.Text, script='$84000007_WD__01_MASSIVEMAIN__0$', duration=10000) # Voice 02000970
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Ending_03')
        self.set_sound(trigger_id=10000) # Intro
        self.set_timer(timer_id='8888', seconds=150, display=True) # 60초 동안 자유시간
        self.set_photo_studio(is_enable=True) # 신규개발기능: 사진촬영

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8888'):
            # 타이머 끝나면 자동복귀 state로 이동
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.room_expire()


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


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
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut(self.ctx)


"""
GambleGame Pattern
G06 P101
"""
class G06P101_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P101Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P101_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P101_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P101_Check(self.ctx)


class G06P101_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P101TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P101_End(self.ctx)


class G06P101_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P101End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P102
class G06P102_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P102Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P102_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P102_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P102_Check(self.ctx)


class G06P102_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P102TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P102_End(self.ctx)


class G06P102_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P102End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P103
class G06P103_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P103Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P103_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P103_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P103_Check(self.ctx)


class G06P103_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P103TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P103_End(self.ctx)


class G06P103_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P103End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P104
class G06P104_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P104Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P104_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P104_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P104_Check(self.ctx)


class G06P104_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P104TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P104_End(self.ctx)


class G06P104_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P104End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P105
class G06P105_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P105Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P105_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P105_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P105_Check(self.ctx)


class G06P105_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P105TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P105_End(self.ctx)


class G06P105_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P105End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P106
class G06P106_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P106Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P106_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P106_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P106_Check(self.ctx)


class G06P106_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P106TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P106_End(self.ctx)


class G06P106_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P106End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P107
class G06P107_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P107Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P107_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P107_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P107_Check(self.ctx)


class G06P107_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P107TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P107_End(self.ctx)


class G06P107_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P107End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P108
class G06P108_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P108Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P108_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P108_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P108_Check(self.ctx)


class G06P108_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P108TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P108_End(self.ctx)


class G06P108_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P108End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P109
class G06P109_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P109Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P109_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P109_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P109_Check(self.ctx)


class G06P109_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P109TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P109_End(self.ctx)


class G06P109_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P109End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P110
class G06P110_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P110Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P110_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P110_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P110_Check(self.ctx)


class G06P110_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P110TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P110_End(self.ctx)


class G06P110_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P110End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P201
class G06P201_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P201Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P201_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P201_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P201_Check(self.ctx)


class G06P201_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P201TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P201_End(self.ctx)


class G06P201_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P201End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P202
class G06P202_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P202Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P202_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P202_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P202_Check(self.ctx)


class G06P202_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P202TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P202_End(self.ctx)


class G06P202_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P202End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P203
class G06P203_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P203Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P203_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P203_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P203_Check(self.ctx)


class G06P203_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P203TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P203_End(self.ctx)


class G06P203_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P203End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P204
class G06P204_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P204Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P204_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P204_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P204_Check(self.ctx)


class G06P204_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P204TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P204_End(self.ctx)


class G06P204_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P204End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P205
class G06P205_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P205Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P205_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P205_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P205_Check(self.ctx)


class G06P205_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P205TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P205_End(self.ctx)


class G06P205_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P205End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P206
class G06P206_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P206Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P206_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P206_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P206_Check(self.ctx)


class G06P206_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P206TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P206_End(self.ctx)


class G06P206_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P206End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P207
class G06P207_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P207Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P207_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P207_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P207_Check(self.ctx)


class G06P207_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P207TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P207_End(self.ctx)


class G06P207_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P207End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P208
class G06P208_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P208Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P208_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P208_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P208_Check(self.ctx)


class G06P208_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P208TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P208_End(self.ctx)


class G06P208_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P208End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P209
class G06P209_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P209Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P209_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P209_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P209_Check(self.ctx)


class G06P209_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P209TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P209_End(self.ctx)


class G06P209_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P209End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P210
class G06P210_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P210Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P210_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P210_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P210_Check(self.ctx)


class G06P210_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P210TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P210_End(self.ctx)


class G06P210_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P210End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P211
class G06P211_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P211Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P211_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P211_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P211_Check(self.ctx)


class G06P211_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P211TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P211_End(self.ctx)


class G06P211_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P211End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P212
class G06P212_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P212Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P212_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P212_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P212_Check(self.ctx)


class G06P212_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P212TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P212_End(self.ctx)


class G06P212_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P212End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P213
class G06P213_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P213Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P213_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P213_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P213_Check(self.ctx)


class G06P213_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P213TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P213_End(self.ctx)


class G06P213_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P213End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P214
class G06P214_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P214Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P214_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P214_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P214_Check(self.ctx)


class G06P214_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P214TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P214_End(self.ctx)


class G06P214_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P214End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P215
class G06P215_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P215Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P215_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P215_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P215_Check(self.ctx)


class G06P215_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P215TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P215_End(self.ctx)


class G06P215_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P215End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P216
class G06P216_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P216Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P216_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P216_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P216_Check(self.ctx)


class G06P216_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P216TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P216_End(self.ctx)


class G06P216_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P216End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P217
class G06P217_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P217Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P217_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P217_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P217_Check(self.ctx)


class G06P217_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P217TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P217_End(self.ctx)


class G06P217_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P217End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P218
class G06P218_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P218Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P218_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P218_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P218_Check(self.ctx)


class G06P218_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P218TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P218_End(self.ctx)


class G06P218_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P218End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P219
class G06P219_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P219Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P219_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P219_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P219_Check(self.ctx)


class G06P219_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P219TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P219_End(self.ctx)


class G06P219_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P219End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P220
class G06P220_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P220Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P220_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P220_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P220_Check(self.ctx)


class G06P220_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P220TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P220_End(self.ctx)


class G06P220_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P220End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P301
class G06P301_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P301Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P301_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P301_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P301_Check(self.ctx)


class G06P301_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P301TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P301_End(self.ctx)


class G06P301_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P301End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P302
class G06P302_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P302Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P302_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P302_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P302_Check(self.ctx)


class G06P302_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P302TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P302_End(self.ctx)


class G06P302_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P302End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P303
class G06P303_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P303Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P303_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P303_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P303_Check(self.ctx)


class G06P303_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P303TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P303_End(self.ctx)


class G06P303_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P303End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P304
class G06P304_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P304Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P304_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P304_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P304_Check(self.ctx)


class G06P304_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P304TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P304_End(self.ctx)


class G06P304_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P304End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P305
class G06P305_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P305Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P305_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P305_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P305_Check(self.ctx)


class G06P305_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P305TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P305_End(self.ctx)


class G06P305_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P305End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P306
class G06P306_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P306Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P306_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P306_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P306_Check(self.ctx)


class G06P306_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P306TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P306_End(self.ctx)


class G06P306_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P306End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P307
class G06P307_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P307Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P307_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P307_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P307_Check(self.ctx)


class G06P307_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P307TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P307_End(self.ctx)


class G06P307_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P307End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P308
class G06P308_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P308Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P308_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P308_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P308_Check(self.ctx)


class G06P308_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P308TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P308_End(self.ctx)


class G06P308_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P308End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P309
class G06P309_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P309Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P309_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P309_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P309_Check(self.ctx)


class G06P309_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P309TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P309_End(self.ctx)


class G06P309_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P309End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P310
class G06P310_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P310Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P310_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P310_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P310_Check(self.ctx)


class G06P310_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P310TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P310_End(self.ctx)


class G06P310_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P310End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P311
class G06P311_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P311Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P311_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P311_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P311_Check(self.ctx)


class G06P311_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P311TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P311_End(self.ctx)


class G06P311_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P311End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P312
class G06P312_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P312Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P312_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P312_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P312_Check(self.ctx)


class G06P312_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P312TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P312_End(self.ctx)


class G06P312_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P312End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P313
class G06P313_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P313Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P313_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P313_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P313_Check(self.ctx)


class G06P313_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P313TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P313_End(self.ctx)


class G06P313_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P313End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P314
class G06P314_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P314Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P314_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P314_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P314_Check(self.ctx)


class G06P314_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P314TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P314_End(self.ctx)


class G06P314_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P314End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P315
class G06P315_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P315Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P315_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P315_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P315_Check(self.ctx)


class G06P315_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P315TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P315_End(self.ctx)


class G06P315_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P315End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P316
class G06P316_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P316Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P316_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P316_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P316_Check(self.ctx)


class G06P316_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P316TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P316_End(self.ctx)


class G06P316_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P316End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P317
class G06P317_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P317Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P317_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P317_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P317_Check(self.ctx)


class G06P317_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P317TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P317_End(self.ctx)


class G06P317_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P317End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P318
class G06P318_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P318Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P318_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P318_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P318_Check(self.ctx)


class G06P318_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P318TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P318_End(self.ctx)


class G06P318_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P318End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P319
class G06P319_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P319Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P319_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P319_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P319_Check(self.ctx)


class G06P319_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P319TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P319_End(self.ctx)


class G06P319_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P319End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P320
class G06P320_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P320Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P320_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P320_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P320_Check(self.ctx)


class G06P320_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P320TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P320_End(self.ctx)


class G06P320_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P320End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P401
class G06P401_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P401Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P401_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P401_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P401_Check(self.ctx)


class G06P401_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P401TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P401_End(self.ctx)


class G06P401_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P401End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P402
class G06P402_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P402Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P402_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P402_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P402_Check(self.ctx)


class G06P402_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P402TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P402_End(self.ctx)


class G06P402_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P402End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P403
class G06P403_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P403Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P403_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P403_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P403_Check(self.ctx)


class G06P403_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P403TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P403_End(self.ctx)


class G06P403_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P403End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P404
class G06P404_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P404Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P404_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P404_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P404_Check(self.ctx)


class G06P404_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P404TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P404_End(self.ctx)


class G06P404_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P404End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P405
class G06P405_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P405Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P405_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P405_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P405_Check(self.ctx)


class G06P405_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P405TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P405_End(self.ctx)


class G06P405_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P405End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P406
class G06P406_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P406Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P406_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P406_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P406_Check(self.ctx)


class G06P406_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P406TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P406_End(self.ctx)


class G06P406_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P406End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P407
class G06P407_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P407Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P407_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P407_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P407_Check(self.ctx)


class G06P407_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P407TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P407_End(self.ctx)


class G06P407_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P407End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P408
class G06P408_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P408Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P408_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P408_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P408_Check(self.ctx)


class G06P408_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P408TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P408_End(self.ctx)


class G06P408_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P408End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P409
class G06P409_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P409Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P409_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P409_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P409_Check(self.ctx)


class G06P409_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P409TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P409_End(self.ctx)


class G06P409_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P409End') == 1:
            return RoundCheckOut(self.ctx)


# G06 P410
class G06P410_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P410Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G06P410_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G06P410_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G06P410_Check(self.ctx)


class G06P410_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=600, key='G06P410TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G06P410_End(self.ctx)


class G06P410_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P410End') == 1:
            return RoundCheckOut(self.ctx)


"""
JackpotGame Pattern
G07 P201
"""
class G07P201_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P201Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P201_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P201_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P201_Check(self.ctx)


class G07P201_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P201TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P201_End(self.ctx)


class G07P201_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P201End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P202
class G07P202_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P202Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P202_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P202_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P202_Check(self.ctx)


class G07P202_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P202TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P202_End(self.ctx)


class G07P202_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P202End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P203
class G07P203_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P203Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P203_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P203_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P203_Check(self.ctx)


class G07P203_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P203TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P203_End(self.ctx)


class G07P203_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P203End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P204
class G07P204_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P204Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P204_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P204_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P204_Check(self.ctx)


class G07P204_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P204TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P204_End(self.ctx)


class G07P204_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P204End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P205
class G07P205_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P205Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P205_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P205_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P205_Check(self.ctx)


class G07P205_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P205TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P205_End(self.ctx)


class G07P205_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P205End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P206
class G07P206_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P206Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P206_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P206_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P206_Check(self.ctx)


class G07P206_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P206TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P206_End(self.ctx)


class G07P206_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P206End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P207
class G07P207_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P207Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P207_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P207_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P207_Check(self.ctx)


class G07P207_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P207TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P207_End(self.ctx)


class G07P207_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P207End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P208
class G07P208_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P208Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P208_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P208_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P208_Check(self.ctx)


class G07P208_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P208TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P208_End(self.ctx)


class G07P208_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P208End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P209
class G07P209_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P209Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P209_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P209_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P209_Check(self.ctx)


class G07P209_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P209TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P209_End(self.ctx)


class G07P209_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P209End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P210
class G07P210_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P210Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P210_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P210_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P210_Check(self.ctx)


class G07P210_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P210TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P210_End(self.ctx)


class G07P210_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P210End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P301
class G07P301_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P301Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P301_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P301_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P301_Check(self.ctx)


class G07P301_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P301TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P301_End(self.ctx)


class G07P301_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P301End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P302
class G07P302_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P302Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P302_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P302_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P302_Check(self.ctx)


class G07P302_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P302TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P302_End(self.ctx)


class G07P302_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P302End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P303
class G07P303_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P303Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P303_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P303_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P303_Check(self.ctx)


class G07P303_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P303TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P303_End(self.ctx)


class G07P303_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P303End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P304
class G07P304_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P304Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P304_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P304_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P304_Check(self.ctx)


class G07P304_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P304TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P304_End(self.ctx)


class G07P304_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P304End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P305
class G07P305_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P305Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P305_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P305_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P305_Check(self.ctx)


class G07P305_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P305TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P305_End(self.ctx)


class G07P305_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P305End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P306
class G07P306_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P306Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P306_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P306_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P306_Check(self.ctx)


class G07P306_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P306TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P306_End(self.ctx)


class G07P306_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P306End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P307
class G07P307_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P307Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P307_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P307_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P307_Check(self.ctx)


class G07P307_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P307TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P307_End(self.ctx)


class G07P307_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P307End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P308
class G07P308_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P308Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P308_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P308_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P308_Check(self.ctx)


class G07P308_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P308TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P308_End(self.ctx)


class G07P308_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P308End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P309
class G07P309_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P309Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P309_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P309_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P309_Check(self.ctx)


class G07P309_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P309TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P309_End(self.ctx)


class G07P309_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P309End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P310
class G07P310_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P310Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P310_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P310_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P310_Check(self.ctx)


class G07P310_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P310TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P310_End(self.ctx)


class G07P310_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P310End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P401
class G07P401_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P401Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P401_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P401_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P401_Check(self.ctx)


class G07P401_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P401TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P401_End(self.ctx)


class G07P401_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P401End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P402
class G07P402_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P402Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P402_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P402_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P402_Check(self.ctx)


class G07P402_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P402TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P402_End(self.ctx)


class G07P402_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P402End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P403
class G07P403_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P403Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P403_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P403_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P403_Check(self.ctx)


class G07P403_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P403TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P403_End(self.ctx)


class G07P403_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P403End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P404
class G07P404_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P404Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P404_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P404_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P404_Check(self.ctx)


class G07P404_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P404TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P404_End(self.ctx)


class G07P404_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P404End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P405
class G07P405_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P405Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P405_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P405_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P405_Check(self.ctx)


class G07P405_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P405TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P405_End(self.ctx)


class G07P405_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P405End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P406
class G07P406_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P406Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P406_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P406_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P406_Check(self.ctx)


class G07P406_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P406TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P406_End(self.ctx)


class G07P406_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P406End') == 1:
            return RoundCheckOut(self.ctx)


# G07 P407
class G07P407_RoundCheckIn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P407Set', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11111'):
            return G07P407_CleanUp(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='11111')


class G07P407_CleanUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=901)
        self.set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        self.play_system_sound_in_box(box_ids=[9000], sound='DJDD_Dancing_01')
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], start_delay=2000, fade=2.0) # 스테이지 정리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return G07P407_Check(self.ctx)


class G07P407_Check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=700, key='G07P407TimeLimit', value=1)
        self.play_system_sound_in_box(box_ids=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return G07P407_End(self.ctx)


class G07P407_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P407End') == 1:
            return RoundCheckOut(self.ctx)


class RoundCheckOut(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='BannerCheckIn', value=1)
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
        if self.user_value(key='Round') == 6:
            return R04GambleEndDelay(self.ctx)
        if self.user_value(key='Round') == 5:
            return R05EndDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='Round', value=0)


initial_state = Wait
