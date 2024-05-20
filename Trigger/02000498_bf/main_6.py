""" trigger/02000498_bf/main_6.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3601])
        self.set_effect(trigger_ids=[6601])
        self.set_effect(trigger_ids=[6602])
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6601], visible=True)
        self.dark_stream_start_round(round=26, ui_duration=3000, damage_penalty=200)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='26,30,26')
            return 라운드26(self.ctx)


class 라운드26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__0$', arg3='4000', arg4='0')
        self.dark_stream_spawn_monster(spawn_ids=[126001], score=2200000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[126001]):
            self.dark_stream_clear_round(round=26)
            self.set_achievement(trigger_id=106, type='trigger', achieve='26roundpass')
            return 라운드대기27(self.ctx)


class 라운드대기27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6601], visible=True)
        self.dark_stream_start_round(round=27, ui_duration=3000, damage_penalty=200)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='27,30,26')
            return 라운드27(self.ctx)


class 라운드27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[127001], score=2500000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[127001]):
            self.dark_stream_clear_round(round=27)
            self.set_achievement(trigger_id=106, type='trigger', achieve='27roundpass')
            return 라운드대기28(self.ctx)


class 라운드대기28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6601], visible=True)
        self.dark_stream_start_round(round=28, ui_duration=3000, damage_penalty=200)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='28,30,26')
            return 라운드28(self.ctx)


class 라운드28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[128001], score=3000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[128001]):
            self.dark_stream_clear_round(round=28)
            self.set_achievement(trigger_id=106, type='trigger', achieve='28roundpass')
            return 라운드대기29(self.ctx)


class 라운드대기29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6601], visible=True)
        self.dark_stream_start_round(round=29, ui_duration=3000, damage_penalty=200)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='29,30,26')
            return 라운드29(self.ctx)


class 라운드29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[129001], score=5000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[129001]):
            self.dark_stream_clear_round(round=29)
            self.set_achievement(trigger_id=106, type='trigger', achieve='29roundpass')
            return 라운드대기30(self.ctx)


class 라운드대기30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6602], visible=True)
        self.dark_stream_start_round(round=30, ui_duration=3000, damage_penalty=200)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='30,30,26')
            return 라운드30(self.ctx)


class 라운드30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3601], visible=True)
        self.spawn_monster(spawn_ids=[130001])
        self.dark_stream_spawn_monster(spawn_ids=[130002], score=8000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[130002]):
            self.set_mesh(trigger_ids=[3601])
            self.destroy_monster(spawn_ids=[130001])
            self.dark_stream_clear_round(round=30)
            self.set_achievement(trigger_id=106, type='trigger', achieve='30roundpass')
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=7, arg2='$02000350_BF__MAIN_6__1$', arg3='3000', arg4='0')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__2$', arg3='2500', arg4='0')
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
