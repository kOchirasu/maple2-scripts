""" trigger/02000350_bf/main_5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423,3424], visible=True)
        self.set_skill(trigger_ids=[706])
        self.set_effect(trigger_ids=[640])
        self.set_effect(trigger_ids=[650])
        self.set_effect(trigger_ids=[6501])
        self.set_effect(trigger_ids=[6502])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='21,25,21')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=21, ui_duration=3000, damage_penalty=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드21(self.ctx)


class 라운드21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_5__0$', arg3='4000', arg4='0')
        self.dark_stream_spawn_monster(spawn_ids=[121001], score=110000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121001]):
            self.dark_stream_clear_round(round=21)
            self.set_achievement(trigger_id=105, type='trigger', achieve='21roundpass')
            return 라운드대기22(self.ctx)


class 라운드대기22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='22,25,21')
        self.dark_stream_start_round(round=22, ui_duration=3000, damage_penalty=100)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드22(self.ctx)


class 라운드22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[122001,122002,122003], score=70000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[122001,122002,122003]):
            self.dark_stream_clear_round(round=22)
            self.set_achievement(trigger_id=105, type='trigger', achieve='22roundpass')
            return 라운드대기23(self.ctx)


class 라운드대기23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_event_ui(type=0, arg2='23,25,21')
        self.dark_stream_start_round(round=23, ui_duration=3000, damage_penalty=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드23(self.ctx)


class 라운드23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[123001], score=80000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[123001]):
            self.dark_stream_clear_round(round=23)
            self.set_achievement(trigger_id=105, type='trigger', achieve='23roundpass')
            return 라운드대기24(self.ctx)


class 라운드대기24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='24,25,21')
        self.dark_stream_start_round(round=24, ui_duration=3000, damage_penalty=100)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_5__1$', arg3='2000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드24(self.ctx)


class 라운드24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30, start_delay=1, interval=1, v_offset=80)
        self.spawn_monster(spawn_ids=[124099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.destroy_monster(spawn_ids=[124099])
            self.reset_timer(timer_id='30')
            self.dark_stream_clear_round(round=24)
            self.set_achievement(trigger_id=105, type='trigger', achieve='24roundpass')
            return 라운드대기25(self.ctx)


class 라운드대기25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='25,25,21')
        self.set_effect(trigger_ids=[6501], visible=True)
        self.set_effect(trigger_ids=[6502], visible=True)
        self.dark_stream_start_round(round=25, ui_duration=3000, damage_penalty=100)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드25(self.ctx)


class 라운드25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[125001,125002], score=750000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[125001,125002]):
            self.dark_stream_clear_round(round=25)
            self.set_achievement(trigger_id=105, type='trigger', achieve='25roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_effect(trigger_ids=[650], visible=True)
            self.set_skill(trigger_ids=[706], enable=True)
            self.set_mesh(trigger_ids=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423,3424])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
