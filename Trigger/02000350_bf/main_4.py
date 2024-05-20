""" trigger/02000350_bf/main_4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528], visible=True)
        self.set_skill(trigger_ids=[705])
        self.set_effect(trigger_ids=[6401])
        self.set_effect(trigger_ids=[640])
        self.set_effect(trigger_ids=[630])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='16,20,16')
        self.dark_stream_start_round(round=16, ui_duration=3000, damage_penalty=50)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드16(self.ctx)


class 라운드16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_4__0$', arg3='4000', arg4='0')
        self.dark_stream_spawn_monster(spawn_ids=[116001], score=73000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[116001]):
            self.dark_stream_clear_round(round=16)
            self.set_achievement(trigger_id=104, type='trigger', achieve='16roundpass')
            return 라운드대기17(self.ctx)


class 라운드대기17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='17,20,16')
        self.dark_stream_start_round(round=17, ui_duration=3000, damage_penalty=50)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드17(self.ctx)


class 라운드17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[117001], score=56250)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[117001]):
            self.dark_stream_clear_round(round=17)
            self.set_achievement(trigger_id=104, type='trigger', achieve='17roundpass')
            return 라운드대기18(self.ctx)


class 라운드대기18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='18,20,16')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=18, ui_duration=3000, damage_penalty=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드18(self.ctx)


class 라운드18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[118001], score=90000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[118001]):
            self.dark_stream_clear_round(round=18)
            self.set_achievement(trigger_id=104, type='trigger', achieve='18roundpass')
            return 라운드대기19(self.ctx)


class 라운드대기19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='19,20,16')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=19, ui_duration=3000, damage_penalty=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드19(self.ctx)


class 라운드19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[119001,119002], score=80000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[119001,119002]):
            self.dark_stream_clear_round(round=19)
            self.set_achievement(trigger_id=104, type='trigger', achieve='19roundpass')
            return 라운드대기20(self.ctx)


class 라운드대기20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='20,20,16')
        self.set_effect(trigger_ids=[6401], visible=True)
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=20, ui_duration=3000, damage_penalty=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드20(self.ctx)


class 라운드20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[120001], score=600000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[120001]):
            self.dark_stream_clear_round(round=20)
            self.set_achievement(trigger_id=104, type='trigger', achieve='20roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_effect(trigger_ids=[640], visible=True)
            self.set_skill(trigger_ids=[705], enable=True)
            self.set_mesh(trigger_ids=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
