""" trigger/83000002_colosseum/timer.xml """
import trigger_api


# <라운드 시작하면서 5분 시간 제한 타이머>
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer') == 1:
            return 스테이지1(self.ctx)
        if self.user_value(key='Timer') == 2:
            return 스테이지2(self.ctx)
        if self.user_value(key='Timer') == 3:
            return 스테이지3(self.ctx)
        if self.user_value(key='Timer') == 4:
            return 스테이지4(self.ctx)
        if self.user_value(key='Timer') == 5:
            return 스테이지5(self.ctx)
        if self.user_value(key='Timer') == 6:
            return 스테이지6(self.ctx)
        if self.user_value(key='Timer') == 7:
            return 스테이지7(self.ctx)
        if self.user_value(key='Timer') == 8:
            return 스테이지8(self.ctx)
        if self.user_value(key='Timer') == 9:
            return 스테이지9(self.ctx)
        if self.user_value(key='Timer') == 10:
            return 스테이지10(self.ctx)


class 스테이지1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=101, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크1(self.ctx)


class 타이머체크1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            self.set_user_value(trigger_id=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer2', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=102, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크2(self.ctx)


class 타이머체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            self.set_user_value(trigger_id=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[102]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer3', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=103, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크3(self.ctx)


class 타이머체크3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            self.set_user_value(trigger_id=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[103]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer4', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=104, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크4(self.ctx)


class 타이머체크4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[104]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer5', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=105, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크5(self.ctx)


class 타이머체크5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[105]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer6', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=106, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크6(self.ctx)


class 타이머체크6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer7', seconds=180, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=107, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크7(self.ctx)


class 타이머체크7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[107]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer8', seconds=300, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=108, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크8(self.ctx)


class 타이머체크8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[108]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer9', seconds=300, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=109, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크9(self.ctx)


class 타이머체크9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[109]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='LimitTimer10', seconds=300, auto_remove=True)
        # self.set_npc_duel_hp_bar(is_open=True, spawn_id=110, duration_tick=180000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        return 타이머체크10(self.ctx)


class 타이머체크10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[110]):
            self.set_user_value(trigger_id=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='LimitTimer')
        self.reset_timer(timer_id='LimitTimer2')
        self.reset_timer(timer_id='LimitTimer3')
        self.reset_timer(timer_id='LimitTimer4')
        self.reset_timer(timer_id='LimitTimer5')
        self.reset_timer(timer_id='LimitTimer6')
        self.reset_timer(timer_id='LimitTimer7')
        self.reset_timer(timer_id='LimitTimer8')
        self.reset_timer(timer_id='LimitTimer9')
        self.reset_timer(timer_id='LimitTimer10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


initial_state = 대기
