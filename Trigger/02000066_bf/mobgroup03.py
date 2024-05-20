""" trigger/02000066_bf/mobgroup03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1501])
        self.destroy_monster(spawn_ids=[1502])
        self.destroy_monster(spawn_ids=[1503])
        self.destroy_monster(spawn_ids=[1504])
        self.destroy_monster(spawn_ids=[1505])
        self.destroy_monster(spawn_ids=[1506])
        self.destroy_monster(spawn_ids=[1507])
        self.destroy_monster(spawn_ids=[1508])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 대기시간(self.ctx)


# 디펜스 모드 :  해골 자코 모둠
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[900]):
            return 차타이머1(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[901]):
            return 차타이머2(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[904]):
            return 차타이머4(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[905]):
            return 차타이머5(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[906]): # 35레벨
            return 차타이머6(self.ctx)
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


class 차타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=14)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='14'):
            return 대기시간(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='6'):
            return 대기시간(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=11)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='11'):
            return 대기시간(self.ctx)


class 차타이머4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=11)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='11'):
            return 대기시간(self.ctx)


class 차타이머5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='5'):
            return 대기시간(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='10'):
            return 대기시간(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=11)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='11'):
            return 대기시간(self.ctx)


class 차타이머8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='5'):
            return 대기시간(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='10'):
            return 대기시간(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=14)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='14'):
            return 대기시간(self.ctx)


class 차타이머11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='7', seconds=7)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='7'):
            return 대기시간(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=13)
        self.spawn_monster(spawn_ids=[1501], auto_target=False)
        self.spawn_monster(spawn_ids=[1502], auto_target=False)
        self.spawn_monster(spawn_ids=[1503], auto_target=False)
        self.spawn_monster(spawn_ids=[1504], auto_target=False)
        self.spawn_monster(spawn_ids=[1505], auto_target=False)
        self.spawn_monster(spawn_ids=[1506], auto_target=False)
        self.spawn_monster(spawn_ids=[1507], auto_target=False)
        self.spawn_monster(spawn_ids=[1508], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='13'):
            return 대기시간(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1501])
        self.destroy_monster(spawn_ids=[1502])
        self.destroy_monster(spawn_ids=[1503])
        self.destroy_monster(spawn_ids=[1504])
        self.destroy_monster(spawn_ids=[1505])
        self.destroy_monster(spawn_ids=[1506])
        self.destroy_monster(spawn_ids=[1507])
        self.destroy_monster(spawn_ids=[1508])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 시작
