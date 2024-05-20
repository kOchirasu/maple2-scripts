""" trigger/02000298_bf/mob_09.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[607])
        self.set_mesh(trigger_ids=[3016,3017,3018,3019,3020], visible=True)
        self.set_mesh(trigger_ids=[3216,3217,3218,3219,3220], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[110]):
            self.spawn_monster(spawn_ids=[1009], auto_target=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(box_ids=[111]):
            self.spawn_monster(spawn_ids=[1009], auto_target=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1009]):
            return 방호벽해제(self.ctx)


class 방호벽해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_mesh(trigger_ids=[3016,3017,3018,3019,3020], fade=5.0)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 번생성12(self.ctx)


class 번생성12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1012], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1012]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_mesh(trigger_ids=[3216,3217,3218,3219,3220], fade=5.0)
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
