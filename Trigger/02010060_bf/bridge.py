""" trigger/02010060_bf/bridge.xml """
import trigger_api


class NPC감지대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078])
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130])
        self.set_interact_object(trigger_ids=[10000918], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2099]):
            return 오브젝트반응대기(self.ctx)
        if self.user_value(key='FirstPhaseEnd') == 1:
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701], enable=True)
        self.set_interact_object(trigger_ids=[10000918], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000918], state=0):
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=100, type='trigger', achieve='TruthOfKargon')
        self.set_effect(trigger_ids=[610], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078], visible=True, interval=50, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이펙트생성(self.ctx)


class 이펙트생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130], visible=True, interval=100, fade=2.0)


initial_state = NPC감지대기
