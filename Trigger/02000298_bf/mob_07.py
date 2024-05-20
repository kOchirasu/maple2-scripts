""" trigger/02000298_bf/mob_07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[606])
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205], visible=True)
        self.set_mesh(trigger_ids=[3211,3212,3213,3214,3215], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            self.spawn_monster(spawn_ids=[1007], auto_target=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(box_ids=[107]):
            self.spawn_monster(spawn_ids=[1007], auto_target=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1007]):
            return 방호벽해제(self.ctx)


class 방호벽해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205], fade=5.0)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 번생성11(self.ctx)


class 번생성11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1011]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_mesh(trigger_ids=[3211,3212,3213,3214,3215], fade=5.0)
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
