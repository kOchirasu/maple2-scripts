""" trigger/61000011_me/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='OxQuizUGC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # OX 퀴즈 선언
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True) # O
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True) # X
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True) # 주변
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521]) # 벽
        self.widget_action(type='OxQuizUGC', func='ShowHostUI')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='IsStarted') == 1:
            return 게임시작(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsCanceled') == 1:
            return 게임취소(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game(box_id=105, round=10, game_name='oxquiz_ugc')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=105)
        self.set_timer(timer_id='2', seconds=1)
        self.move_user(map_id=61000021, portal_id=99, box_id=104)
        # StartMiniGameRound 는 OxQuizUGC 위젯의 StartRound 에서 불러줌
        self.widget_action(type='OxQuizUGC', func='StartRound')
        self.widget_action(type='OxQuizUGC', func='HostUIChange', widget_arg='InputQuiz')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=105)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsCanceled') == 1:
            return 게임취소(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsFinished') == 1:
            return 게임끝(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsQuizSubmit') == 1:
            return 문제표시(self.ctx)


class 문제표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='ShowQuiz', widget_arg='15')
        self.widget_action(type='OxQuizUGC', func='HostUIChange', widget_arg='Move')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='15', seconds=15)
        self.set_achievement(trigger_id=100, type='trigger', achieve='bjoxquiz_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 벽생성(self.ctx)


class 벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='CreateWall')
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 정답대기(self.ctx)


class 정답대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='HostUIChange', widget_arg='SelectAnswer')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='IsRemoveWall') == 1:
            return 문제표시(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsAnswerSubmit') == 1:
            return 정답체크(self.ctx)


class 정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='PreJudge', widget_arg='1')
        self.widget_action(type='OxQuizUGC', func='HostUIChange', widget_arg='Judge')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='Correct') == 1:
            return 문제정답O(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='Incorrect') == 1:
            return 문제정답X(self.ctx)


class 문제정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.widget_action(type='OxQuizUGC', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제정리(self.ctx)


class 문제정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.widget_action(type='OxQuizUGC', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제정리(self.ctx)


class 문제정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='20', seconds=2)
        self.widget_action(type='OxQuizUGC', func='EndRound')
        self.move_user(map_id=61000011, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='IsFinished') == 1:
            return 게임끝(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsCanceled') == 1:
            return 게임취소(self.ctx)
        if self.time_expired(timer_id='20'):
            return 준비(self.ctx)


class 게임끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 성공(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 게임취소(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.GameOver, script='$61000011_ME__GAME_END_BY_CANCEL$', duration=3000, box_ids='0')
        self.set_timer(timer_id='2', seconds=10)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 마무리(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuizUGC', func='EndGame')
        self.end_mini_game(winner_box_id=105, game_name='oxquiz_ugc', is_only_winner=True)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 우승자카메라연출(self.ctx)


class 우승자카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Bonus, script='$61000011_ME__WINNER_IS$', duration=5000, box_ids='105')
        self.set_event_ui_script(type=BannerType.Bonus, script='$61000011_ME__ENVY_IS$', duration=5000, box_ids='!105')
        self.mini_game_camera_direction(box_id=105, camera_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_local_camera(camera_id=301)
            return 완료보상(self.ctx)


class 완료보상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='EndGame')
        self.end_mini_game(winner_box_id=105, game_name='oxquiz_ugc', is_only_winner=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 성공알림(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='EndGame')
        self.end_mini_game(winner_box_id=105, game_name='oxquiz_ugc', is_only_winner=True)
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_event_ui_round(rounds=[0,0])
        self.set_event_ui_script(type=BannerType.Success, script='$61000011_ME__GAME_END_BY_ALL_RETIRED$', duration=3000, box_ids='0')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 마무리(self.ctx)


class 성공알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Fail, script='$61000011_ME__MAIN__SUCCESS_IS$', duration=3000, box_ids='0')
        self.set_timer(timer_id='40', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='40'):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_event_ui_script(type=BannerType.GameOver, script='$61000011_ME__MAIN__GOODBYE$', duration=3000, box_ids='0')
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            self.widget_action(type='OxQuizUGC', func='MoveAllUser')
            return 대기(self.ctx)


initial_state = 입장
