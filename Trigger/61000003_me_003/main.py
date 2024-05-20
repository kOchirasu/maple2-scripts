""" trigger/61000003_me_003/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='OxQuiz') # OX 퀴즈 선언
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        # self.set_portal(portal_id=99)
        # self.set_portal(portal_id=10002)
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
            return 시작준비(self.ctx)
        if self.wait_tick(wait_tick=60000):
            return 시작준비(self.ctx)


class 시작준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=105) # 해킹 보안용 시작 box 설정
        self.widget_action(type='OxQuiz', func='DevMode', widget_arg='0') # 개발자 모드 On (문제에 정답이 보인다)
        # self.widget_action(type='OxQuiz', func='ReserveQuiz', widget_arg='1916') # 특정 문제만 먼저 뽑을 때 사용

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 안내01(self.ctx)


class 안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 안내02(self.ctx)


class 안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__1$', arg3='4000', arg4='0')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 안내03(self.ctx)


class 안내03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__2$', arg3='4000', arg4='0')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제1(self.ctx)


class 문제1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game(box_id=105, round=10, game_name='oxquiz')
        self.start_mini_game_round(box_id=105, round=1)
        self.set_achievement(trigger_id=100, type='trigger', achieve='oxquiz_start')
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(trigger_id=100, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(type=2)
        # self.set_effect(trigger_ids=[612], visible=True)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        # OX 퀴즈 문제 뽑기, arg3=난이도(1~5)
        self.set_event_ui(type=0, arg2='1,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='1')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제1벽생성(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제1벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제1정답체크(self.ctx)


class 문제1정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제1정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제1정답X(self.ctx)


class 문제1정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제2준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='1')


class 문제1정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제2준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='1')


class 문제2준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__3$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제2(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=2)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='2,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='1')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제2벽생성(self.ctx)


class 문제2벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제2정답체크(self.ctx)


class 문제2정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제2정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제2정답X(self.ctx)


class 문제2정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제3준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='2')


class 문제2정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제3준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='2')


class 문제3준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__4$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제3(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=3)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='3,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='2')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제3벽생성(self.ctx)


class 문제3벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제3정답체크(self.ctx)


class 문제3정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제3정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제3정답X(self.ctx)


class 문제3정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제4준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='3')


class 문제3정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제4준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='3')


class 문제4준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__5$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제4(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=4)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='4,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='2')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제4벽생성(self.ctx)


class 문제4벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제4정답체크(self.ctx)


class 문제4정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='4')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제4정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제4정답X(self.ctx)


class 문제4정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제5준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='4')


class 문제4정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제5준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='4')


class 문제5준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__6$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제5(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=5)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='5,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='3')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제5벽생성(self.ctx)


class 문제5벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제5정답체크(self.ctx)


class 문제5정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제5정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제5정답X(self.ctx)


class 문제5정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제6준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='5')


class 문제5정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제6준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='5')


class 문제6준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__7$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제6(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=6)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='6,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='3')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제6벽생성(self.ctx)


class 문제6벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제6정답체크(self.ctx)


class 문제6정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='6')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제6정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제6정답X(self.ctx)


class 문제6정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제7준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='6')


class 문제6정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제7준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='6')


class 문제7준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__8$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제7(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=7)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='7,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='4')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제7벽생성(self.ctx)


class 문제7벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제7정답체크(self.ctx)


class 문제7정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='7')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제7정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제7정답X(self.ctx)


class 문제7정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제8준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='7')


class 문제7정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제8준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='7')


class 문제8준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__9$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제8(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=8)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='8,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='4')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제8벽생성(self.ctx)


class 문제8벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제8정답체크(self.ctx)


class 문제8정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='8')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제8정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제8정답X(self.ctx)


class 문제8정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제9준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='8')


class 문제8정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제9준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='8')


class 문제9준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__10$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제9(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=9)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='9,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='5')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제9벽생성(self.ctx)


class 문제9벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제9정답체크(self.ctx)


class 문제9정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='9')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제9정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제9정답X(self.ctx)


class 문제9정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제10준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='9')


class 문제9정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 문제10준비(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='9')


class 문제10준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605], visible=True)
        # self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Ready_01')
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__11$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제10(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 문제10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=105, round=10)
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Start_01')
        self.set_event_ui(type=0, arg2='10,10')
        self.widget_action(type='OxQuiz', func='PickQuiz', widget_arg='5')
        self.widget_action(type='OxQuiz', func='ShowQuiz', widget_arg='15')
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 문제10벽생성(self.ctx)


class 문제10벽생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문제10정답체크(self.ctx)


class 문제10정답체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='PreJudge', widget_arg='10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='OxQuiz', name='Correct') == 1:
            return 문제10정답O(self.ctx)
        if self.widget_value(type='OxQuiz', name='Incorrect') == 1:
            return 문제10정답X(self.ctx)


class 문제10정답O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=101, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=101, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 완료체크(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='10')


class 문제10정답X(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=102, exp_rate=0.1)
        self.play_system_sound_in_box(box_ids=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(box_ids=[101], sound='System_Quiz_Answer_Wrong_01')
        self.set_achievement(trigger_id=102, type='trigger', achieve='oxquiz_correct')
        self.widget_action(type='OxQuiz', func='ShowAnswer', widget_arg='5')
        self.set_random_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], start_delay=49, fade=10)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355])
        self.set_mesh(trigger_ids=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        # self.create_item(spawn_ids=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149])
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 완료체크(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='OxQuiz', func='Judge', widget_arg='10')


class 완료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.move_user(map_id=61000003, portal_id=99, box_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 성공(self.ctx)
        if not self.user_detected(box_ids=[105]):
            return 종료(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521])
        self.move_user(map_id=61000003, portal_id=99, box_id=104)
        # self.set_effect(trigger_ids=[606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 우승자카메라연출(self.ctx)


class 우승자카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=3, arg2='$61000003_ME_003__MAIN__12$', arg3='5000', arg4='105')
        self.set_event_ui(type=4, arg2='$61000003_ME_003__MAIN__13$', arg3='5000', arg4='!105')
        self.mini_game_camera_direction(box_id=105, camera_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_local_camera(camera_id=301)
            return 완료보상(self.ctx)


class 완료보상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='OxQuiz', func='Winner')
        self.add_buff(box_ids=[105], skill_id=70000019, level=1)
        self.mini_game_give_reward(winner_box_id=105, content_type='miniGame')
        self.end_mini_game(winner_box_id=105, game_name='oxquiz')
        self.set_achievement(trigger_id=105, type='trigger', achieve='oxquiz_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료2(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=105)
        self.end_mini_game(winner_box_id=105, game_name='oxquiz')
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000003_ME_003__MAIN__14$', arg3='3000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료2(self.ctx)


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
