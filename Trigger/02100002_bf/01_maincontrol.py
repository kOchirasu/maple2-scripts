""" trigger/02100002_bf/01_maincontrol.xml """
import trigger_api

#include dungeon_common/checkuser10_guildraid.py
from dungeon_common.checkuser10_guildraid import *


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # RainbowSlime_Sound
        self.set_effect(trigger_ids=[5002]) # PoopSlime_Sound
        self.limit_spawn_npc_count(limit_count=0, desc='몬스터 스폰 제한을 끕니다.') # 공장 가동하기 반응 오브젝트
        self.set_interact_object(trigger_ids=[10001239], state=0) # 결과 출력하기 반응 오브젝트
        self.set_interact_object(trigger_ids=[10001240], state=0) # 용광로 바닥 TOK always off
        self.set_mesh(trigger_ids=[3000])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123])
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223])
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323])
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423])
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523]) # 용광로 더미 몬스터 : 슬라임 죽이기
        self.destroy_monster(spawn_ids=[900]) # 결과 몬스터
        self.destroy_monster(spawn_ids=[1000,2000]) # 무지개 슬라임 공장 전용 위젯
        self.create_widget(type='RainbowMonster') # 입구 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 출구 포탈
        # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 컬러 게이지 샘플
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799], visible=True) # 빨강 게이지 샘플
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819], visible=True) # 용광로 더미 몬스터 : 슬라임 죽이기
        # 해당 필드에 몬스터의 수가  limitCount를 넘어가면 스폰을 중단한다.
        self.spawn_monster(spawn_ids=[900], auto_target=False)
        self.limit_spawn_npc_count(limit_count=200) # 정상 슬라임 몬스터 id 그룹 할당
        # Group 1 : yellowgreen
        # Group 2 : skyblue
        # Group 3 : orange
        # Group 4 : pink
        # Group 5 : purple
        self.widget_action(type='RainbowMonster', func='CreateGroup', widget_arg_num=1, widget_arg='34000122,34000123,34000124,34000142')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widget_arg_num=2, widget_arg='34000128,34000129,34000130,34000143')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widget_arg_num=3, widget_arg='34000125,34000126,34000127,34000144')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widget_arg_num=4, widget_arg='34000131,34000132,34000133,34000145')
        # 용광로 더미 몬스터에게 죽임을 당한 정상 슬라임만 점수로 체크
        self.widget_action(type='RainbowMonster', func='CreateGroup', widget_arg_num=5, widget_arg='34000134,34000135,34000136,34000146')
        # 일정 시간 동안 용광로에 유입된 정상 슬라임이 없으면 게이지 감소 패널티
        self.widget_action(type='RainbowMonster', func='SetKillerNpc', widget_arg='34000141', desc='34000141 npc가 죽인 몬스터만 스코어에 반영')
        # 용광로에 불량 슬라임이 들어가면 전체 게이지 랜덤 감소 패널티 / 34000138,34000139 두 종류 몬스터 미구현항목으로 제외 시킴(기획상 BigMom과 소환된 꼬마)
        self.widget_action(type='RainbowMonster', func='SetLoseScoreTick', widget_arg_num=60000, desc='60초마다 감점')
        self.widget_action(type='RainbowMonster', func='SetBadNpc', widget_arg='34000121,34000137', desc='해당 NPC가 킬러에게 죽으면 모든 게이지 감소')
        self.widget_action(type='RainbowMonster', func='SetBadNpcScore', widget_arg='2-5', desc='2~5칸 게이지가 떨어진다')
        self.widget_action(type='RainbowMonster', func='SetBadNpcSoundKey', widget_arg='GuildRaid_RainbowSlimeFactory_ScreenWarning_01', desc='게이지가 떨어질때 플레이할 사운드')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MaxGaugePattern_Random(self.ctx)


"""
MaxGaugePatter_RandomPick
5개의 그룹에서 100, 120, 140, 160, 180, 200 값 중 중복 없이 5개  Pick : 조합
"""
class MaxGaugePattern_Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # n번째 그룹에 100퍼센트를 X마리로 설정 : (N/20)값이 게이지 한 칸에 해당됨
        # self.widget_action(type='RainbowMonster', func='InitMaxScore', widget_arg_num=1, widget_arg='100')
        # self.widget_action(type='RainbowMonster', func='InitMaxScore', widget_arg_num=2, widget_arg='120')
        # self.widget_action(type='RainbowMonster', func='InitMaxScore', widget_arg_num=3, widget_arg='140')
        # self.widget_action(type='RainbowMonster', func='InitMaxScore', widget_arg_num=4, widget_arg='100')
        # self.widget_action(type='RainbowMonster', func='InitMaxScore', widget_arg_num=5, widget_arg='120')
        self.widget_action(type='RainbowMonster', func='InitRandomMaxScore', widget_arg='120,120,140,140,160,160')
        # # 점수를 게이지로 변환하여 매쉬 제어 : 1번 그룹에 3100부터 24번까지 메시를 스코어와 연결
        self.widget_action(type='RainbowMonster', func='ShowMaxScore')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widget_arg_num=1, widget_arg='3100')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widget_arg_num=2, widget_arg='3200')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widget_arg_num=3, widget_arg='3300')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widget_arg_num=4, widget_arg='3500')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widget_arg_num=5, widget_arg='3400')

    def on_tick(self) -> trigger_api.Trigger:
        # 임시 테스트용 데이터 세팅 가능 지점 CheckUser10_GuildRaid / DungeonStart / CloseCaptionSetting / BadEndingStart / HappyEndingStart
        return CheckUser10_GuildRaid(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption03(self.ctx)


class ShowCaption03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=900)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__2$')
        self.set_skip(state=ShowCaption03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption03Skip(self.ctx)


class ShowCaption03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShowCaption04(self.ctx)


class ShowCaption04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=901)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__3$')
        self.set_skip(state=ShowCaption04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption04Skip(self.ctx)


class ShowCaption04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption05(self.ctx)


class ShowCaption05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=902)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__4$')
        self.set_skip(state=ShowCaption05Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption05Skip(self.ctx)


class ShowCaption05Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.reset_camera(interpolation_time=1.0)
        self.set_user_value(trigger_id=2, key='GuideNpcSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.close_cinematic() # 컬러 게이지 샘플
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799]) # 빨강 게이지 샘플
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Guide01(self.ctx)


class Guide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99, key='PortalOn', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__5$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 5000 임시 테스트용 데이터 세팅 가능 지점 Guide02 / BadEndingStart / HappyEndingStart
            return Guide02(self.ctx)


class Guide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__6$', arg3='3000') # 공장 가동하기
        self.set_interact_object(trigger_ids=[10001239], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001239], state=0):
            return Guide03(self.ctx)


class Guide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_MachineOn_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__7$', arg3='2000')
        self.set_interact_object(trigger_ids=[10001239], state=0) # 슬라임 생성 신호
        self.set_user_value(trigger_id=11, key='ActivateTank', value=1)
        self.set_user_value(trigger_id=12, key='ActivateTank', value=1)
        self.set_user_value(trigger_id=13, key='ActivateTank', value=1)
        self.set_user_value(trigger_id=14, key='ActivateTank', value=1)
        self.set_user_value(trigger_id=15, key='ActivateTank', value=1) # 홀더 활성화 신호
        self.set_user_value(trigger_id=21, key='ActivateHolder', value=1)
        self.set_user_value(trigger_id=22, key='ActivateHolder', value=1)
        self.set_user_value(trigger_id=23, key='ActivateHolder', value=1)
        self.set_user_value(trigger_id=24, key='ActivateHolder', value=1)
        self.set_user_value(trigger_id=25, key='ActivateHolder', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TimmerStart(self.ctx)


class TimmerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99, key='MissionStart', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 10분
        # 임시 테스트용 데이터 세팅 가능 지점
        self.set_timer(timer_id='10000', seconds=600, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return EnableCheckOutput(self.ctx)


class EnableCheckOutput(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__8$', arg3='3000') # 결과 출력하기 반응 오브젝트
        self.set_interact_object(trigger_ids=[10001240], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001240], state=0):
            return CheckSuccess(self.ctx)
        if self.time_expired(timer_id='10000'):
            return MissionFail(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=11, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=12, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=13, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=14, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=15, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=21, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=22, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=23, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=24, key='DungeonQuit', value=1)
        self.set_user_value(trigger_id=25, key='DungeonQuit', value=1) # 용광로 소멸
        self.destroy_monster(spawn_ids=[900]) # 입구 포탈
        self.set_portal(portal_id=1)
        self.set_interact_object(trigger_ids=[10001234], state=0)


class CheckSuccess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='RainbowMonster', name='IsMissionSuccess') in [19,20,21]:
            return HappyEndingStart(self.ctx)
        if self.widget_value(type='RainbowMonster', name='IsMissionSuccess') not in [19,20,21]:
            return BadEndingStart(self.ctx)


# BadEnding 연출
class BadEndingStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=909)
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        self.move_user(map_id=2100002, portal_id=2, box_id=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BadEndingSpawn(self.ctx)


class BadEndingSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=908)
        self.set_effect(trigger_ids=[5002], visible=True) # PoopSlime_Sound
        # 돌연변이 킹슬라임
        self.spawn_monster(spawn_ids=[2000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return BadEndingEnd(self.ctx)


class BadEndingEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return MissionFail(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=9902, type='trigger', achieve='MakeMutantKingSlime')


# HappyEnding 연출
class HappyEndingStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=909)
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        self.move_user(map_id=2100002, portal_id=2, box_id=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return HappyEndingSpawn(self.ctx)


class HappyEndingSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=908)
        self.set_effect(trigger_ids=[5001], visible=True) # RainbowSlime_Sound
        # 무지개 킹슬라임
        self.spawn_monster(spawn_ids=[1000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return HappyEndingEnd(self.ctx)


class HappyEndingEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DungeonSuccess(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=9902, type='trigger', achieve='MakeRainbowKingSlime')


# 던전 클리어 선언
class DungeonSuccess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_achievement(trigger_id=9902, type='trigger', achieve='Find02100002')
        self.set_event_ui(type=7, arg2='$02100002_BF__01_MAINCONTROL__10$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ExitPortalOn(self.ctx)


class MissionFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='10000')
        self.set_event_ui(type=5, arg2='$02100002_BF__01_MAINCONTROL__9$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return DungeonFail(self.ctx)


# 던전 실패 선언
class DungeonFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        self.dungeon_fail()
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ExitPortalOn(self.ctx)


class ExitPortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 출구 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_user_value(trigger_id=99, key='DungeonClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
