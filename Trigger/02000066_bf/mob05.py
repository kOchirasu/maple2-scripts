""" trigger/02000066_bf/mob05.xml """
import trigger_api


# 디펜스 모드 :  해골B
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[901]): # 33레벨
            return 차타이머2(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[905]): # 35레벨
            return 차타이머5(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[908]):
            return 차타이머7(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[909]):
            return 차타이머8(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[912]):
            return 차타이머10(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[913]):
            return 차타이머11(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[914]):
            return 차타이머12(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='13'):
            return 생성랜덤(self.ctx)


class 차타이머5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[905]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='11'):
            return 생성랜덤(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='10'):
            return 생성랜덤(self.ctx)


class 차타이머8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='9'):
            return 생성랜덤(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='8', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='8'):
            return 생성랜덤(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='7'):
            return 생성랜덤(self.ctx)


class 차타이머11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='6'):
            return 생성랜덤(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='5'):
            return 생성랜덤(self.ctx)


class 생성랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1401], auto_target=False)
        self.spawn_monster(spawn_ids=[1402], auto_target=False)
        self.spawn_monster(spawn_ids=[1403], auto_target=False)
        self.spawn_monster(spawn_ids=[1404], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1401])
        self.destroy_monster(spawn_ids=[1402])
        self.destroy_monster(spawn_ids=[1403])
        self.destroy_monster(spawn_ids=[1404])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 대기시간
