""" trigger/02000298_bf/mob_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[605])
        self.set_mesh(trigger_ids=[3006,3007,3008,3009,3010], visible=True)
        self.set_mesh(trigger_ids=[3206,3207,3208,3209,3210], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            self.spawn_monster(spawn_ids=[1005], auto_target=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(box_ids=[103]):
            self.spawn_monster(spawn_ids=[1005], auto_target=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1005]):
            return 방호벽해제(self.ctx)


class 방호벽해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_mesh(trigger_ids=[3006,3007,3008,3009,3010], fade=5.0)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 번생성10(self.ctx)


class 번생성10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1010]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_mesh(trigger_ids=[3206,3207,3208,3209,3210], fade=5.0)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
