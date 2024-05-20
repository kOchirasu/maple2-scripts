""" trigger/02000304_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 몬스터체크(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            return 카운트랜덤(self.ctx)


class 카운트랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 이동대기01(self.ctx)
        if self.random_condition(weight=25.0):
            return 이동대기02(self.ctx)
        if self.random_condition(weight=25.0):
            return 이동대기03(self.ctx)
        if self.random_condition(weight=25.0):
            return 이동대기04(self.ctx)


class 이동대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='90', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='90'):
            return 이동(self.ctx)


class 이동대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='100'):
            return 이동(self.ctx)


class 이동대기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='110', seconds=110)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='110'):
            return 이동(self.ctx)


class 이동대기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='120'):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MOVE__0$', time=2)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='2'):
            self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MOVE__1$', time=1)
            self.move_random_user(map_id=2000304, portal_id=11, box_id=101, count=1)
            return 이동2(self.ctx)


class 이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MOVE__2$', time=1)
            self.move_random_user(map_id=2000304, portal_id=12, box_id=101, count=1)
            return 이동3(self.ctx)


class 이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MOVE__3$', time=1)
            self.move_random_user(map_id=2000304, portal_id=13, box_id=101, count=1)
            return 이동4(self.ctx)


class 이동4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MOVE__4$', time=1)
            self.move_random_user(map_id=2000304, portal_id=14, box_id=101, count=1)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
