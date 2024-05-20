""" trigger/02000350_bf/main_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[6110])
        self.set_effect(trigger_ids=[6111])
        self.set_effect(trigger_ids=[6112])
        self.set_effect(trigger_ids=[6113])
        self.set_effect(trigger_ids=[6201])
        self.set_skill(trigger_ids=[703])
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='6,10,6')
        self.dark_stream_start_round(round=6, ui_duration=3000, damage_penalty=10)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드6(self.ctx)


class 라운드6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__0$', arg3='4000', arg4='0')
        self.dark_stream_spawn_monster(spawn_ids=[106001,106002,106003,106004,106005], score=18000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106001,106002,106003,106004,106005]):
            self.dark_stream_clear_round(round=6)
            self.set_achievement(trigger_id=102, type='trigger', achieve='6roundpass')
            return 라운드대기7(self.ctx)


class 라운드대기7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='7,10,6')
        self.dark_stream_start_round(round=7, ui_duration=3000, damage_penalty=10)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드7(self.ctx)


class 라운드7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[107001,107002,107003,107004,107005], score=22000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[107001,107002,107003,107004,107005]):
            self.dark_stream_clear_round(round=7)
            self.set_achievement(trigger_id=102, type='trigger', achieve='7roundpass')
            return 라운드대기8(self.ctx)


class 라운드대기8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='8,10,6')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=8, ui_duration=3000, damage_penalty=10)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__1$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드8(self.ctx)


class 라운드8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30, start_delay=1, interval=1, v_offset=80)
        self.spawn_monster(spawn_ids=[108099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.destroy_monster(spawn_ids=[108099])
            self.reset_timer(timer_id='30')
            self.dark_stream_clear_round(round=8)
            self.set_achievement(trigger_id=102, type='trigger', achieve='8roundpass')
            return 라운드대기9(self.ctx)


class 라운드대기9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='9,10,6')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=9, ui_duration=3000, damage_penalty=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드9(self.ctx)


class 라운드9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[109001,109002,109003,109004], score=65000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109001,109002,109003,109004]):
            self.dark_stream_clear_round(round=9)
            self.set_achievement(trigger_id=102, type='trigger', achieve='9roundpass')
            return 라운드대기10(self.ctx)


class 라운드대기10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='10,10,6')
        self.set_effect(trigger_ids=[6201], visible=True)
        self.dark_stream_start_round(round=10, ui_duration=3000, damage_penalty=10)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드10(self.ctx)


class 라운드10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[110001], score=270000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[110001]):
            self.dark_stream_clear_round(round=10)
            self.set_achievement(trigger_id=102, type='trigger', achieve='10roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_effect(trigger_ids=[620], visible=True)
            self.set_skill(trigger_ids=[703], enable=True)
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235])
            self.set_event_ui(type=0, arg2='0,0')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
