""" trigger/02000066_bf/mob06.xml """
import trigger_api


# 파토스
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[906]): # 35레벨
            return 차타이머6(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[914]):
            return 차타이머12(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='5'):
            return 차생성3(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='5'):
            return 차생성6(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='40', seconds=40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='40'):
            return 차생성9(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='20'):
            return 차생성12(self.ctx)


class 차생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return 소멸(self.ctx)


class 차생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[906]):
            return 소멸(self.ctx)


class 차생성9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)


class 차생성12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1299])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 대기시간
