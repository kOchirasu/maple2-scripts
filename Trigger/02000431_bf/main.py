""" trigger/02000431_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10001108], state=2)
        self.set_mesh(trigger_ids=[3000])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=True)
        self.set_mesh(trigger_ids=[3901,3902,3903,3904], visible=True)
        self.spawn_monster(spawn_ids=[1099,2094,2095,2096,2097,2098,2099], auto_target=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='start') == 1:
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=300)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 부선장대사01(self.ctx)


class 부선장대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=24003011, script='$02000431_BF__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 해적이동01(self.ctx)


class 해적이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2099, script='$02000431_BF__MAIN__1$', time=3)
        self.set_npc_emotion_sequence(spawn_id=1099, sequence_name='Attack_01_C')
        self.select_camera(trigger_id=301)
        self.move_npc(spawn_id=2094, patrol_name='MS2PatrolData_2094A')
        self.move_npc(spawn_id=2095, patrol_name='MS2PatrolData_2095A')
        self.move_npc(spawn_id=2096, patrol_name='MS2PatrolData_2096A')
        self.move_npc(spawn_id=2097, patrol_name='MS2PatrolData_2097A')
        self.move_npc(spawn_id=2098, patrol_name='MS2PatrolData_2098A')
        self.move_npc(spawn_id=2099, patrol_name='MS2PatrolData_2099A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라302(self.ctx)


class 카메라302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부선장대사03(self.ctx)


class 부선장대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.set_dialogue(type=2, spawn_id=24003011, script='$02000431_BF__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4858):
            return 세이렌대사01(self.ctx)


class 세이렌대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=309)
        self.set_dialogue(type=2, spawn_id=24003010, script='$02000431_BF__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4179):
            return 카메라310(self.ctx)


class 카메라310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
        self.set_npc_emotion_sequence(spawn_id=1098, sequence_name='Attack_01_D')
        self.set_dialogue(type=1, spawn_id=1099, script='$02000431_BF__MAIN__4$', time=3)
        self.set_npc_emotion_sequence(spawn_id=1099, sequence_name='Attack_01_D')
        self.select_camera(trigger_id=310)
        self.set_effect(trigger_ids=[603], visible=True)
        self.add_buff(box_ids=[2094], skill_id=70000055, level=1)
        self.add_buff(box_ids=[2095], skill_id=70000055, level=1)
        self.add_buff(box_ids=[2096], skill_id=70000055, level=1)
        self.add_buff(box_ids=[2097], skill_id=70000055, level=1)
        self.add_buff(box_ids=[2098], skill_id=70000055, level=1)
        self.add_buff(box_ids=[2099], skill_id=70000055, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라304(self.ctx)


class 카메라304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2099, script='$02000431_BF__MAIN__5$', time=3)
        self.set_npc_emotion_sequence(spawn_id=1099, sequence_name='Attack_01_I')
        self.select_camera(trigger_id=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1300):
            self.destroy_monster(spawn_ids=[1099])
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라305(self.ctx)


class 카메라305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603])
        self.destroy_monster(spawn_ids=[2094,2095,2096,2097,2098,2099])
        self.spawn_monster(spawn_ids=[2100], auto_target=False)
        self.spawn_monster(spawn_ids=[1098], auto_target=False)
        self.select_camera(trigger_id=305)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 세이렌연주02(self.ctx)


class 세이렌연주02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1098, script='$02000431_BF__MAIN__6$', time=3)
        self.play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
        self.set_npc_emotion_sequence(spawn_id=1098, sequence_name='Attack_01_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 물큐브제거(self.ctx)


class 물큐브제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 세이렌이동(self.ctx)


class 세이렌이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1098, script='$02000431_BF__MAIN__7$', time=3)
        self.select_camera(trigger_id=306)
        self.move_npc(spawn_id=1098, patrol_name='MS2PatrolData_1098A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 카메라307(self.ctx)


class 카메라307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1098])
        self.select_camera(trigger_id=307)
        self.set_dialogue(type=2, spawn_id=24003011, script='$02000431_BF__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라308(self.ctx)


class 카메라308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
        self.select_camera(trigger_id=308)
        self.set_npc_emotion_sequence(spawn_id=2100, sequence_name='Attack_01_A')
        self.set_dialogue(type=1, spawn_id=2100, script='$02000431_BF__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=True)
        self.set_mesh(trigger_ids=[3901,3902,3903,3904])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.select_camera(trigger_id=306, enable=False)
        self.reset_camera()
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.destroy_monster(spawn_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
            self.destroy_monster(spawn_ids=[1098,1099,2094,2095,2096,2097,2098,2099,2100])
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2199], auto_target=False)
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
        self.spawn_npc_range(range_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039101, text_id=20039101, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2199]):
            return 사망딜레이(self.ctx)


class 퀘스트던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2299], auto_target=False)
        self.spawn_npc_range(range_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
        self.spawn_npc_range(range_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.show_guide_summary(entity_id=20039101, text_id=20039101, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2299]):
            return 사망딜레이(self.ctx)


class 사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
            return 오브젝트카메라(self.ctx)


class 오브젝트카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=하프반응대기)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.select_camera(trigger_id=307)
        self.set_interact_object(trigger_ids=[10001108], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 하프반응대기(self.ctx)


class 하프반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State
        self.reset_camera()
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039102, text_id=20039102, duration=3000)
        # self.select_camera(trigger_id=307, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001108], state=0):
            self.play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
            self.set_effect(trigger_ids=[601])
            return 연주딜레이(self.ctx)


class 연주딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 물큐브제거2(self.ctx)


class 물큐브제거2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[602], visible=True)
        self.select_camera(trigger_id=305)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201])
        self.set_portal(portal_id=2, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # self.select_camera(trigger_id=305, enable=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039103, text_id=20039103)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()


initial_state = 대기
