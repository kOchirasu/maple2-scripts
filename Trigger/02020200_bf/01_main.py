""" trigger/02020200_bf/01_main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3)
        self.set_effect(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027])
        self.set_effect(trigger_ids=[11001,11002,11003,11004,11005,11006,11007,11008])
        self.set_effect(trigger_ids=[12001,12002,12003,12004])
        self.set_visible_breakable_object(trigger_ids=[5010,5011,5012,5013,5014,5110,5111,5112,5113,5114,5210,5211,5212,5213,5214])
        self.set_breakable(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014])
        self.set_breakable(trigger_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110,5111,5112,5113,5114])
        self.set_breakable(trigger_ids=[5201,5202,5203,5204,5205,5206,5207,5208,5209,5210,5211,5212,5213,5214])
        self.set_interact_object(trigger_ids=[10002149], state=0)
        self.set_interact_object(trigger_ids=[10002150], state=0)
        self.set_interact_object(trigger_ids=[10002151], state=0)
        self.set_interact_object(trigger_ids=[10002152], state=0)
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096], visible=True)
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118], visible=True)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249,3250,3251,3252,3253,3254,3255,3256,3257,3258,3259,3260,3261,3262,3263,3264,3265,3266,3267,3268,3269,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3280,3281,3282,3283,3284,3285,3286,3287,3288,3289], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3365,3366,3367,3368,3369,3370,3371,3372,3373,3374,3375], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032])
        self.set_mesh(trigger_ids=[4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124,4125,4126,4127,4128,4129,4130,4131,4132,4133,4134,4135,4136,4137,4138,4139,4140,4141,4142,4143,4144,4145,4146,4147,4148,4149,4150,4151,4152,4153,4154,4155,4156,4157,4158,4159,4160,4161,4162,4163,4164,4165,4166,4167,4168,4169,4170,4171,4172,4173,4174,4175,4176,4177,4178,4179,4180,4181,4182,4183,4184,4185,4186,4187,4188])
        self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212,4213,4214,4215,4216,4217,4218,4219,4220,4221,4222,4223,4224,4225,4226,4227,4228,4229,4230,4231,4232,4233,4234,4235,4236,4237,4238,4239,4240,4241,4242,4243,4244,4245,4246,4247,4248,4249,4250,4251,4252,4253,4254,4255,4256,4257,4258,4259,4260,4261,4262,4263,4264,4265,4266,4267,4268,4269,4270,4271,4272,4273,4274,4275,4276,4277,4278,4279,4280,4281,4282,4283,4284,4285,4286,4287,4288,4289])
        self.set_mesh(trigger_ids=[4301,4302,4303,4304,4305,4306,4307,4308,4309,4310,4311,4312,4313,4314,4315,4316,4317,4318,4319,4320,4321,4322,4323,4324,4325,4326,4327,4328,4329,4330,4331,4332,4333,4334,4335,4336,4337,4338,4339,4340,4341,4342,4343,4344,4345,4346,4347,4348,4349,4350,4351,4352,4353,4354,4355,4356,4357,4358,4359,4360,4361,4362,4363,4364,4365,4366,4367,4368,4369,4370,4371,4372,4373,4374,4375])
        self.set_mesh_animation(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009], visible=True)
        self.set_user_value(trigger_id=99990002, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990003, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990004, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990005, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990006, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990007, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990008, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990009, key='BombOn', value=0)
        self.set_user_value(trigger_id=99990010, key='BombOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[908]):
            return 가이드메시지(self.ctx)


class 가이드메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12001], visible=True)
        self.show_guide_summary(entity_id=111, text_id=20110001) # 에네르 동력원을 전원부 위로 옮기세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[911], item_id=30001286):
            return 엘리베이터_1(self.ctx)


class 엘리베이터_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.set_effect(trigger_ids=[12001])
        self.hide_guide_summary(entity_id=111)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032], visible=True, interval=80, fade=3.0)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032], interval=80, fade=3.0)
        self.set_effect(trigger_ids=[11001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엘리베이터_1_활성화_대기(self.ctx)


class 엘리베이터_1_활성화_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009], visible=True)
        self.set_effect(trigger_ids=[11002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_1_활성화(self.ctx)


class 엘리베이터_1_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4013,4015,4017,4019,4021])
        self.set_visible_breakable_object(trigger_ids=[5010,5011,5012,5013,5014], visible=True)
        self.set_breakable(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 번방2(self.ctx)


class 번방2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009])
        self.spawn_monster(spawn_ids=[101,102,103,104], auto_target=False)
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109])
        self.set_user_value(trigger_id=99990002, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990003, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990004, key='BombOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104]):
            return 번방_클리어2(self.ctx)


class 번방_클리어2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12002], visible=True)
        self.set_user_value(trigger_id=99990002, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990003, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990004, key='BombOn', value=2)
        self.show_guide_summary(entity_id=111, text_id=20110001) # 에네르 동력원을 전원부 위로 옮기세요.
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_random_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], start_delay=32, fade=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[912], item_id=30001286):
            return 엘리베이터_2(self.ctx)


class 엘리베이터_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)
        self.set_effect(trigger_ids=[12002])
        self.hide_guide_summary(entity_id=111)
        self.set_mesh(trigger_ids=[4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124,4125,4126,4127,4128,4129,4130,4131,4132,4133,4134,4135,4136,4137,4138,4139,4140,4141,4142,4143,4144,4145,4146,4147,4148,4149,4150,4151,4152,4153,4154,4155,4156,4157,4158,4159,4160,4161,4162,4163,4164,4165,4166,4167,4168,4169,4170,4171,4172,4173,4174,4175,4176,4177,4178,4179,4180,4181,4182,4183,4184,4185,4186,4187,4188], visible=True, interval=50, fade=3.0)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188], interval=50, fade=3.0)
        self.set_effect(trigger_ids=[11003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_2_활성화_대기(self.ctx)


class 엘리베이터_2_활성화_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10010,10011,10012,10013,10014,10015,10016,10017,10018], visible=True)
        self.set_effect(trigger_ids=[11004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_2_활성화(self.ctx)


class 엘리베이터_2_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4133,4135,4137,4139,4141])
        self.set_visible_breakable_object(trigger_ids=[5110,5111,5112,5113,5114], visible=True)
        self.set_breakable(trigger_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110,5111,5112,5113,5114], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 번방3(self.ctx)


class 번방3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10010,10011,10012,10013,10014,10015,10016,10017,10018])
        self.spawn_monster(spawn_ids=[201,202,203,204,205], auto_target=False)
        self.set_mesh(trigger_ids=[1110,1111,1112,1113,1114,1115,1116,1117,1118])
        self.set_user_value(trigger_id=99990005, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990006, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990007, key='BombOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205]):
            return 번방_클리어3(self.ctx)


class 번방_클리어3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12003], visible=True)
        self.set_user_value(trigger_id=99990005, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990006, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990007, key='BombOn', value=2)
        self.show_guide_summary(entity_id=111, text_id=20110001) # 에네르 동력원을 전원부 위로 옮기세요.
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_random_mesh(trigger_ids=[1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064], start_delay=32, fade=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[913], item_id=30001286):
            return 엘리베이터_3(self.ctx)


class 엘리베이터_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3, is_enable=True)
        self.set_effect(trigger_ids=[12003])
        self.hide_guide_summary(entity_id=111)
        self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212,4213,4214,4215,4216,4217,4218,4219,4220,4221,4222,4223,4224,4225,4226,4227,4228,4229,4230,4231,4232,4233,4234,4235,4236,4237,4238,4239,4240,4241,4242,4243,4244,4245,4246,4247,4248,4249,4250,4251,4252,4253,4254,4255,4256,4257,4258,4259,4260,4261,4262,4263,4264,4265,4266,4267,4268,4269,4270,4271,4272,4273,4274,4275,4276,4277,4278,4279,4280,4281,4282,4283,4284,4285,4286,4287,4288,4289], visible=True, interval=50, fade=3.0)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249,3250,3251,3252,3253,3254,3255,3256,3257,3258,3259,3260,3261,3262,3263,3264,3265,3266,3267,3268,3269,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3280,3281,3282,3283,3284,3285,3286,3287,3288,3289], interval=50, fade=3.0)
        self.set_effect(trigger_ids=[11005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_3_활성화_대기(self.ctx)


class 엘리베이터_3_활성화_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10019,10020,10021,10022,10023,10024,10025,10026,10027], visible=True)
        self.set_effect(trigger_ids=[11006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_3_활성화(self.ctx)


class 엘리베이터_3_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4232,4234,4236,4238,4240])
        self.set_visible_breakable_object(trigger_ids=[5210,5211,5212,5213,5214], visible=True)
        self.set_breakable(trigger_ids=[5201,5202,5203,5204,5205,5206,5207,5208,5209,5210,5211,5212,5213,5214], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[904]):
            return 번방4(self.ctx)


class 번방4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10019,10020,10021,10022,10023,10024,10025,10026,10027])
        self.spawn_monster(spawn_ids=[301,302,303,304,305], auto_target=False)
        self.set_user_value(trigger_id=99990008, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990009, key='BombOn', value=1)
        self.set_user_value(trigger_id=99990010, key='BombOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303,304,305]):
            return 번방_클리어4(self.ctx)


class 번방_클리어4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12004], visible=True)
        self.set_user_value(trigger_id=99990008, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990009, key='BombOn', value=2)
        self.set_user_value(trigger_id=99990010, key='BombOn', value=2)
        self.show_guide_summary(entity_id=111, text_id=20110001) # 에네르 동력원을 전원부 위로 옮기세요.
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_random_mesh(trigger_ids=[1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096], start_delay=32, fade=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[914], item_id=30001286):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12004])
        self.hide_guide_summary(entity_id=111)
        self.set_mesh(trigger_ids=[4301,4302,4303,4304,4305,4306,4307,4308,4309,4310,4311,4312,4313,4314,4315,4316,4317,4318,4319,4320,4321,4322,4323,4324,4325,4326,4327,4328,4329,4330,4331,4332,4333,4334,4335,4336,4337,4338,4339,4340,4341,4342,4343,4344,4345,4346,4347,4348,4349,4350,4351,4352,4353,4354,4355,4356,4357,4358,4359,4360,4361,4362,4363,4364,4365,4366,4367,4368,4369,4370,4371,4372,4373,4374,4375], visible=True, interval=50, fade=3.0)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3365,3366,3367,3368,3369,3370,3371,3372,3373,3374,3375], interval=50, fade=3.0)
        self.set_effect(trigger_ids=[11007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11008], visible=True)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
