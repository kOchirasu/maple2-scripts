""" trigger/61000021_me_003/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='OxQuizUGC') # OX 퀴즈 선언
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=100) >= 50:
            return 준비(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=105)
        self.set_timer(timer_id='2', seconds=1)
        self.move_user(map_id=61000021, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=105)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='IsQuizSubmit') == 1:
            return 문제표시(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='IsFinished') == 1:
            return 종료(self.ctx)


class 문제표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game(box_id=105, round=10, game_name='oxquiz_ugc')
        self.widget_action(type='OxQuizUGC', func='PeekQuiz')
        self.widget_action(type='OxQuizUGC', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 벽생성(self.ctx)


class 벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 정답체크(self.ctx)


class 정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuizUGC', func='PreJudge', widget_arg='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuizUGC', name='Correct') == 1:
            return 문제정답O(self.ctx)
        if self.widget_value(type='OxQuizUGC', name='Incorrect') == 1:
            return 문제정답X(self.ctx)


class 문제정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
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
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
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
        self.set_timer(timer_id='20', seconds=10)
        self.widget_action(type='OxQuizUGC', func='CleanUpQuiz')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 준비(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game(winner_box_id=105, game_name='oxquiz_ugc')
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000003_ME_003__MAIN__14$', arg3='3000', arg4='0')


class 종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__15$', arg3='3000', arg4='0')
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            self.move_user()
            return 대기(self.ctx)


initial_state = 입장
