""" trigger/02000304_bf/mesh.xml """
import trigger_api


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
        self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
        self.set_mesh(trigger_ids=[4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116])
        self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212,4213,4214,4215,4216])
        self.set_mesh(trigger_ids=[4301,4302,4303,4304,4305,4306,4307,4308,4309,4310,4311,4312,4313,4314,4315,4316])
        self.set_mesh(trigger_ids=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414,4415,4416])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='10'):
            return 패턴01랜덤(self.ctx)


class 패턴01랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴01_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴01_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴01_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴01_D(self.ctx)


class 패턴01_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4204], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4313], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101], fade=2.0)
            self.set_mesh(trigger_ids=[3204], fade=2.0)
            self.set_mesh(trigger_ids=[3313], fade=2.0)
            self.set_mesh(trigger_ids=[3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101], fade=2.0)
            self.set_mesh(trigger_ids=[4204], fade=2.0)
            self.set_mesh(trigger_ids=[4313], fade=2.0)
            self.set_mesh(trigger_ids=[4416], fade=2.0)
            return 패턴01종료(self.ctx)


class 패턴01_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4115], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4214], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4303], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4402], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3115], fade=2.0)
            self.set_mesh(trigger_ids=[3214], fade=2.0)
            self.set_mesh(trigger_ids=[3303], fade=2.0)
            self.set_mesh(trigger_ids=[3402], fade=2.0)
            self.set_mesh(trigger_ids=[4115], fade=2.0)
            self.set_mesh(trigger_ids=[4214], fade=2.0)
            self.set_mesh(trigger_ids=[4303], fade=2.0)
            self.set_mesh(trigger_ids=[4402], fade=2.0)
            return 패턴01종료(self.ctx)


class 패턴01_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4110], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4211], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4307], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4406], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3110], fade=2.0)
            self.set_mesh(trigger_ids=[3211], fade=2.0)
            self.set_mesh(trigger_ids=[3307], fade=2.0)
            self.set_mesh(trigger_ids=[3406], fade=2.0)
            self.set_mesh(trigger_ids=[4110], fade=2.0)
            self.set_mesh(trigger_ids=[4211], fade=2.0)
            self.set_mesh(trigger_ids=[4307], fade=2.0)
            self.set_mesh(trigger_ids=[4406], fade=2.0)
            return 패턴01종료(self.ctx)


class 패턴01_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4213], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3116], fade=2.0)
            self.set_mesh(trigger_ids=[3213], fade=2.0)
            self.set_mesh(trigger_ids=[3304], fade=2.0)
            self.set_mesh(trigger_ids=[3401], fade=2.0)
            self.set_mesh(trigger_ids=[4116], fade=2.0)
            self.set_mesh(trigger_ids=[4213], fade=2.0)
            self.set_mesh(trigger_ids=[4304], fade=2.0)
            self.set_mesh(trigger_ids=[4401], fade=2.0)
            return 패턴01종료(self.ctx)


class 패턴01종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴02시작(self.ctx)


class 패턴02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='10'):
            return 패턴02랜덤(self.ctx)


class 패턴02랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴02_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴02_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴02_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴02_D(self.ctx)


class 패턴02_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4113], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4301], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4404], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3113], fade=2.0)
            self.set_mesh(trigger_ids=[3216], fade=2.0)
            self.set_mesh(trigger_ids=[3301], fade=2.0)
            self.set_mesh(trigger_ids=[3404], fade=2.0)
            self.set_mesh(trigger_ids=[4113], fade=2.0)
            self.set_mesh(trigger_ids=[4216], fade=2.0)
            self.set_mesh(trigger_ids=[4301], fade=2.0)
            self.set_mesh(trigger_ids=[4404], fade=2.0)
            return 패턴02종료(self.ctx)


class 패턴02_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4112], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4212], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4312], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4412], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3112], fade=2.0)
            self.set_mesh(trigger_ids=[3212], fade=2.0)
            self.set_mesh(trigger_ids=[3312], fade=2.0)
            self.set_mesh(trigger_ids=[3412], fade=2.0)
            self.set_mesh(trigger_ids=[4112], fade=2.0)
            self.set_mesh(trigger_ids=[4212], fade=2.0)
            self.set_mesh(trigger_ids=[4312], fade=2.0)
            self.set_mesh(trigger_ids=[4412], fade=2.0)
            return 패턴02종료(self.ctx)


class 패턴02_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104], fade=2.0)
            self.set_mesh(trigger_ids=[3216], fade=2.0)
            self.set_mesh(trigger_ids=[3304], fade=2.0)
            self.set_mesh(trigger_ids=[3416], fade=2.0)
            self.set_mesh(trigger_ids=[4104], fade=2.0)
            self.set_mesh(trigger_ids=[4216], fade=2.0)
            self.set_mesh(trigger_ids=[4304], fade=2.0)
            self.set_mesh(trigger_ids=[4416], fade=2.0)
            return 패턴02종료(self.ctx)


class 패턴02_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4107], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4206], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4307], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4406], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3107], fade=2.0)
            self.set_mesh(trigger_ids=[3206], fade=2.0)
            self.set_mesh(trigger_ids=[3307], fade=2.0)
            self.set_mesh(trigger_ids=[3406], fade=2.0)
            self.set_mesh(trigger_ids=[4107], fade=2.0)
            self.set_mesh(trigger_ids=[4206], fade=2.0)
            self.set_mesh(trigger_ids=[4307], fade=2.0)
            self.set_mesh(trigger_ids=[4406], fade=2.0)
            return 패턴02종료(self.ctx)


class 패턴02종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴03시작(self.ctx)


class 패턴03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='15'):
            return 패턴03랜덤(self.ctx)


class 패턴03랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴03_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴03_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴03_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴03_D(self.ctx)


class 패턴03_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4204,4213], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304,4313], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3204,3213], fade=2.0)
            self.set_mesh(trigger_ids=[3304,3313], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4204,4213], fade=2.0)
            self.set_mesh(trigger_ids=[4304,4313], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4416], fade=2.0)
            return 패턴03종료(self.ctx)


class 패턴03_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4106,4111], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4207,4210], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4307,4310], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4406,4411], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3106,3111], fade=2.0)
            self.set_mesh(trigger_ids=[3207,3210], fade=2.0)
            self.set_mesh(trigger_ids=[3307,3310], fade=2.0)
            self.set_mesh(trigger_ids=[3406,3411], fade=2.0)
            self.set_mesh(trigger_ids=[4106,4111], fade=2.0)
            self.set_mesh(trigger_ids=[4207,4210], fade=2.0)
            self.set_mesh(trigger_ids=[4307,4310], fade=2.0)
            self.set_mesh(trigger_ids=[4406,4411], fade=2.0)
            return 패턴03종료(self.ctx)


class 패턴03_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4103,4114], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4202,4215], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4302,4315], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4403,4414], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3103,3114], fade=2.0)
            self.set_mesh(trigger_ids=[3202,3215], fade=2.0)
            self.set_mesh(trigger_ids=[3302,3315], fade=2.0)
            self.set_mesh(trigger_ids=[3403,3414], fade=2.0)
            self.set_mesh(trigger_ids=[4103,4114], fade=2.0)
            self.set_mesh(trigger_ids=[4202,4215], fade=2.0)
            self.set_mesh(trigger_ids=[4302,4315], fade=2.0)
            self.set_mesh(trigger_ids=[4403,4414], fade=2.0)
            return 패턴03종료(self.ctx)


class 패턴03_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4108,4110], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4205,4211], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4306,4312], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4407,4409], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3108,3110], fade=2.0)
            self.set_mesh(trigger_ids=[3205,3211], fade=2.0)
            self.set_mesh(trigger_ids=[3306,3312], fade=2.0)
            self.set_mesh(trigger_ids=[3407,3409], fade=2.0)
            self.set_mesh(trigger_ids=[4108,4110], fade=2.0)
            self.set_mesh(trigger_ids=[4205,4211], fade=2.0)
            self.set_mesh(trigger_ids=[4306,4312], fade=2.0)
            self.set_mesh(trigger_ids=[4407,4409], fade=2.0)
            return 패턴03종료(self.ctx)


class 패턴03종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴04시작(self.ctx)


class 패턴04시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='15'):
            return 패턴04랜덤(self.ctx)


class 패턴04랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴04_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴04_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴04_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴04_D(self.ctx)


class 패턴04_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4112,4115], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4209,4214], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4303,4308], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4402,4415], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3112,3115], fade=2.0)
            self.set_mesh(trigger_ids=[3209,3214], fade=2.0)
            self.set_mesh(trigger_ids=[3303,3308], fade=2.0)
            self.set_mesh(trigger_ids=[3402,3415], fade=2.0)
            self.set_mesh(trigger_ids=[4112,4115], fade=2.0)
            self.set_mesh(trigger_ids=[4209,4214], fade=2.0)
            self.set_mesh(trigger_ids=[4303,4308], fade=2.0)
            self.set_mesh(trigger_ids=[4402,4415], fade=2.0)
            return 패턴04종료(self.ctx)


class 패턴04_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104,4113], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4301,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4404,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104,3113], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3216], fade=2.0)
            self.set_mesh(trigger_ids=[3301,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3404,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4104,4113], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4216], fade=2.0)
            self.set_mesh(trigger_ids=[4301,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4404,4413], fade=2.0)
            return 패턴04종료(self.ctx)


class 패턴04_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4102,4114], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4203,4215], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4302,4314], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4403,4415], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3102,3114], fade=2.0)
            self.set_mesh(trigger_ids=[3203,3215], fade=2.0)
            self.set_mesh(trigger_ids=[3302,3314], fade=2.0)
            self.set_mesh(trigger_ids=[3403,3415], fade=2.0)
            self.set_mesh(trigger_ids=[4102,4114], fade=2.0)
            self.set_mesh(trigger_ids=[4203,4215], fade=2.0)
            self.set_mesh(trigger_ids=[4302,4314], fade=2.0)
            self.set_mesh(trigger_ids=[4403,4415], fade=2.0)
            return 패턴04종료(self.ctx)


class 패턴04_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4112,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4209,4213], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304,4308], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4405], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3112,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3209,3213], fade=2.0)
            self.set_mesh(trigger_ids=[3304,3308], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3405], fade=2.0)
            self.set_mesh(trigger_ids=[4112,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4209,4213], fade=2.0)
            self.set_mesh(trigger_ids=[4304,4308], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4405], fade=2.0)
            return 패턴04종료(self.ctx)


class 패턴04종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴05시작(self.ctx)


class 패턴05시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='15'):
            return 패턴05랜덤(self.ctx)


class 패턴05랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴05_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴05_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴05_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴05_D(self.ctx)


class 패턴05_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4106,4111], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4204,4207,4210], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4307,4310,4313], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4406,4411,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3106,3111], fade=2.0)
            self.set_mesh(trigger_ids=[3204,3207,3210], fade=2.0)
            self.set_mesh(trigger_ids=[3307,3310,3313], fade=2.0)
            self.set_mesh(trigger_ids=[3406,3411,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4106,4111], fade=2.0)
            self.set_mesh(trigger_ids=[4204,4207,4210], fade=2.0)
            self.set_mesh(trigger_ids=[4307,4310,4313], fade=2.0)
            self.set_mesh(trigger_ids=[4406,4411,4416], fade=2.0)
            return 패턴05종료(self.ctx)


class 패턴05_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104,4107,4110], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4206,4211], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4306,4311,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4407,4410,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104,3107,3110], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3206,3211], fade=2.0)
            self.set_mesh(trigger_ids=[3306,3311,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3407,3410,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4104,4107,4110], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4206,4211], fade=2.0)
            self.set_mesh(trigger_ids=[4306,4311,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4407,4410,4413], fade=2.0)
            return 패턴05종료(self.ctx)


class 패턴05_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4104,4113], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4204,4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4301,4313,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4404,4413,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3104,3113], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3204,3216], fade=2.0)
            self.set_mesh(trigger_ids=[3301,3313,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3404,3413,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4104,4113], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4204,4216], fade=2.0)
            self.set_mesh(trigger_ids=[4301,4313,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4404,4413,4416], fade=2.0)
            return 패턴05종료(self.ctx)


class 패턴05_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4103,4106,4108], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4202,4205,4207], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4310,4312,4315], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4409,4411,4414], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3103,3106,3108], fade=2.0)
            self.set_mesh(trigger_ids=[3202,3205,3207], fade=2.0)
            self.set_mesh(trigger_ids=[3310,3312,3315], fade=2.0)
            self.set_mesh(trigger_ids=[3409,3411,3414], fade=2.0)
            self.set_mesh(trigger_ids=[4103,4106,4108], fade=2.0)
            self.set_mesh(trigger_ids=[4202,4205,4207], fade=2.0)
            self.set_mesh(trigger_ids=[4310,4312,4315], fade=2.0)
            self.set_mesh(trigger_ids=[4409,4411,4414], fade=2.0)
            return 패턴05종료(self.ctx)


class 패턴05종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴06시작(self.ctx)


class 패턴06시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='15'):
            return 패턴06랜덤(self.ctx)


class 패턴06랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴06_A(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴06_B(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴06_C(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴06_D(self.ctx)


class 패턴06_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104,4107,4112], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4206,4209], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4308,4311,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4405,4410,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104,3107,3112], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3206,3209], fade=2.0)
            self.set_mesh(trigger_ids=[3308,3311,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3405,3410,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4104,4107,4112], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4206,4209], fade=2.0)
            self.set_mesh(trigger_ids=[4308,4311,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4405,4410,4413], fade=2.0)
            return 패턴06종료(self.ctx)


class 패턴06_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4112,4115,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4209,4213,4214], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4303,4304,4308], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4402,4405], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3112,3115,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3209,3213,3214], fade=2.0)
            self.set_mesh(trigger_ids=[3303,3304,3308], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3402,3405], fade=2.0)
            self.set_mesh(trigger_ids=[4112,4115,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4209,4213,4214], fade=2.0)
            self.set_mesh(trigger_ids=[4303,4304,4308], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4402,4405], fade=2.0)
            return 패턴06종료(self.ctx)


class 패턴06_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4102,4105], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4203,4204,4208], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4309,4313,4314], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4412,4415,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3102,3105], fade=2.0)
            self.set_mesh(trigger_ids=[3203,3204,3208], fade=2.0)
            self.set_mesh(trigger_ids=[3309,3313,3314], fade=2.0)
            self.set_mesh(trigger_ids=[3412,3415,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4102,4105], fade=2.0)
            self.set_mesh(trigger_ids=[4203,4204,4208], fade=2.0)
            self.set_mesh(trigger_ids=[4309,4313,4314], fade=2.0)
            self.set_mesh(trigger_ids=[4412,4415,4416], fade=2.0)
            return 패턴06종료(self.ctx)


class 패턴06_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4107,4109,4115], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4206,4212,4214], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4308,4310,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4405,4411,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3107,3109,3115], fade=2.0)
            self.set_mesh(trigger_ids=[3206,3212,3214], fade=2.0)
            self.set_mesh(trigger_ids=[3308,3310,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3405,3411,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4107,4109,4115], fade=2.0)
            self.set_mesh(trigger_ids=[4206,4212,4214], fade=2.0)
            self.set_mesh(trigger_ids=[4308,4310,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4405,4411,4413], fade=2.0)
            return 패턴06종료(self.ctx)


class 패턴06종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴07시작(self.ctx)


class 패턴07시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='15'):
            return 패턴07랜덤(self.ctx)


class 패턴07랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_A(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_B(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_C(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_D(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_E(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_F(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_G(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_H(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_I(self.ctx)
        if self.random_condition(weight=10.0):
            return 패턴07_J(self.ctx)


class 패턴07_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4106,4111,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4204,4207,4210,4213], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304,4307,4310,4313], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4406,4411,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3106,3111,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3204,3207,3210,3213], fade=2.0)
            self.set_mesh(trigger_ids=[3304,3307,3310,3313], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3406,3411,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4106,4111,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4204,4207,4210,4213], fade=2.0)
            self.set_mesh(trigger_ids=[4304,4307,4310,4313], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4406,4411,4416], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104,4107,4110,4113], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4206,4211,4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4301,4306,4311,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4404,4407,4410,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104,3107,3110,3113], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3206,3211,3216], fade=2.0)
            self.set_mesh(trigger_ids=[3301,3306,3311,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3404,3407,3410,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4104,4107,4110,4113], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4206,4211,4216], fade=2.0)
            self.set_mesh(trigger_ids=[4301,4306,4311,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4404,4407,4410,4413], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4102,4105,4107,4110], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4203,4206,4208,4211], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4302,4305,4307,4310], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4403,4406,4408,4411], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3102,3105,3107,3110], fade=2.0)
            self.set_mesh(trigger_ids=[3203,3206,3208,3211], fade=2.0)
            self.set_mesh(trigger_ids=[3302,3305,3307,3310], fade=2.0)
            self.set_mesh(trigger_ids=[3403,3406,3408,3411], fade=2.0)
            self.set_mesh(trigger_ids=[4102,4105,4107,4110], fade=2.0)
            self.set_mesh(trigger_ids=[4203,4206,4208,4211], fade=2.0)
            self.set_mesh(trigger_ids=[4302,4305,4307,4310], fade=2.0)
            self.set_mesh(trigger_ids=[4403,4406,4408,4411], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4109,4111,4114,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4209,4211,4214,4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4309,4311,4314,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4409,4411,4414,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3109,3111,3114,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3209,3211,3214,3216], fade=2.0)
            self.set_mesh(trigger_ids=[3309,3311,3314,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3409,3411,3414,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4109,4111,4114,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4209,4211,4214,4216], fade=2.0)
            self.set_mesh(trigger_ids=[4309,4311,4314,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4409,4411,4414,4416], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4101,4104,4113,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4204,4213,4216], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4301,4304,4313,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4404,4413,4416], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3101,3104,3113,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3204,3213,3216], fade=2.0)
            self.set_mesh(trigger_ids=[3301,3304,3313,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3404,3413,3416], fade=2.0)
            self.set_mesh(trigger_ids=[4101,4104,4113,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4204,4213,4216], fade=2.0)
            self.set_mesh(trigger_ids=[4301,4304,4313,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4404,4413,4416], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4106,4107,4110,4111], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4206,4207,4210,4211], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4306,4307,4310,4311], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4406,4407,4410,4411], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3106,3107,3110,3111], fade=2.0)
            self.set_mesh(trigger_ids=[3206,3207,3210,3211], fade=2.0)
            self.set_mesh(trigger_ids=[3306,3307,3310,3311], fade=2.0)
            self.set_mesh(trigger_ids=[3406,3407,3410,3411], fade=2.0)
            self.set_mesh(trigger_ids=[4106,4107,4110,4111], fade=2.0)
            self.set_mesh(trigger_ids=[4206,4207,4210,4211], fade=2.0)
            self.set_mesh(trigger_ids=[4306,4307,4310,4311], fade=2.0)
            self.set_mesh(trigger_ids=[4406,4407,4410,4411], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4111,4112,4115,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4209,4210,4213,4214], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4303,4304,4307,4308], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4402,4405,4406], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3111,3112,3115,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3209,3210,3213,3214], fade=2.0)
            self.set_mesh(trigger_ids=[3303,3304,3307,3308], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3402,3405,3406], fade=2.0)
            self.set_mesh(trigger_ids=[4111,4112,4115,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4209,4210,4213,4214], fade=2.0)
            self.set_mesh(trigger_ids=[4303,4304,4307,4308], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4402,4405,4406], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4102,4103,4114,4115], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4202,4203,4214,4215], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4302,4303,4314,4315], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4402,4403,4414,4415], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3102,3103,3114,3115], fade=2.0)
            self.set_mesh(trigger_ids=[3202,3203,3214,3215], fade=2.0)
            self.set_mesh(trigger_ids=[3302,3303,3314,3315], fade=2.0)
            self.set_mesh(trigger_ids=[3402,3403,3414,3415], fade=2.0)
            self.set_mesh(trigger_ids=[4102,4103,4114,4115], fade=2.0)
            self.set_mesh(trigger_ids=[4202,4203,4214,4215], fade=2.0)
            self.set_mesh(trigger_ids=[4302,4303,4314,4315], fade=2.0)
            self.set_mesh(trigger_ids=[4402,4403,4414,4415], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4104,4108,4112,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4201,4205,4209,4213], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4304,4308,4312,4316], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4405,4409,4413], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3104,3108,3112,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3201,3205,3209,3213], fade=2.0)
            self.set_mesh(trigger_ids=[3304,3308,3312,3316], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3405,3409,3413], fade=2.0)
            self.set_mesh(trigger_ids=[4104,4108,4112,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4201,4205,4209,4213], fade=2.0)
            self.set_mesh(trigger_ids=[4304,4308,4312,4316], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4405,4409,4413], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4108,4111,4114,4116], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4205,4210,4213,4215], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4302,4304,4307,4312], visible=True, fade=2.0)
        self.set_mesh(trigger_ids=[4401,4403,4406,4409], visible=True, fade=2.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3108,3111,3114,3116], fade=2.0)
            self.set_mesh(trigger_ids=[3205,3210,3213,3215], fade=2.0)
            self.set_mesh(trigger_ids=[3302,3304,3307,3312], fade=2.0)
            self.set_mesh(trigger_ids=[3401,3403,3406,3409], fade=2.0)
            self.set_mesh(trigger_ids=[4108,4111,4114,4116], fade=2.0)
            self.set_mesh(trigger_ids=[4205,4210,4213,4215], fade=2.0)
            self.set_mesh(trigger_ids=[4302,4304,4307,4312], fade=2.0)
            self.set_mesh(trigger_ids=[4401,4403,4406,4409], fade=2.0)
            return 패턴07종료(self.ctx)


class 패턴07종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
            return 패턴07시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True)
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True)
        self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True)
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 시작대기
