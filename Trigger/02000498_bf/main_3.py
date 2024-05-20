""" trigger/02000498_bf/main_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344], visible=True)
        self.set_skill(trigger_ids=[704])
        self.set_effect(trigger_ids=[630])
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[6301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_3__0$', arg3='2000', arg4='0')
        self.dark_stream_start_round(round=11, ui_duration=3000, damage_penalty=30)
        self.set_event_ui(type=0, arg2='11,15,11')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드11(self.ctx)


class 라운드11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_3__1$', arg3='4000', arg4='0')
        self.dark_stream_spawn_monster(spawn_ids=[111001], score=295000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111001]):
            self.dark_stream_clear_round(round=11)
            self.set_achievement(trigger_id=103, type='trigger', achieve='11roundpass')
            return 라운드대기12(self.ctx)


class 라운드대기12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='12,15,11')
        self.dark_stream_start_round(round=12, ui_duration=3000, damage_penalty=30)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드12(self.ctx)


class 라운드12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[112001], score=78750)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[112001]):
            self.dark_stream_clear_round(round=12)
            self.set_achievement(trigger_id=103, type='trigger', achieve='12roundpass')
            return 라운드대기13(self.ctx)


class 라운드대기13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='13,15,11')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=13, ui_duration=3000, damage_penalty=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드13(self.ctx)


class 라운드13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[113001], score=43750)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[113001]):
            self.dark_stream_clear_round(round=13)
            self.set_achievement(trigger_id=103, type='trigger', achieve='13roundpass')
            return 라운드대기14(self.ctx)


class 라운드대기14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='14,15,11')
        self.dark_stream_start_round(round=14, ui_duration=3000, damage_penalty=30)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드14(self.ctx)


class 라운드14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[114001], score=48750)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[114001]):
            self.dark_stream_clear_round(round=14)
            self.set_achievement(trigger_id=103, type='trigger', achieve='14roundpass')
            return 라운드대기15(self.ctx)


class 라운드대기15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='15,15,11')
        self.set_effect(trigger_ids=[6301], visible=True)
        self.dark_stream_start_round(round=15, ui_duration=3000, damage_penalty=30)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드15(self.ctx)


class 라운드15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[115001], score=415000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[115001]):
            self.dark_stream_clear_round(round=15)
            self.set_achievement(trigger_id=103, type='trigger', achieve='15roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_effect(trigger_ids=[630], visible=True)
            self.set_skill(trigger_ids=[704], enable=True)
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
