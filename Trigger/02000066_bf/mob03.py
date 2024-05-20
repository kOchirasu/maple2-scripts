""" trigger/02000066_bf/mob03.xml """
import trigger_api


# 디펜스 모드 :  엘리트
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class 차타이머2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='80', seconds=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='80'):
            return 생성랜덤(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='75', seconds=75)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='75'):
            return 생성랜덤(self.ctx)


class 차타이머4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='68', seconds=68)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='68'):
            return 생성랜덤(self.ctx)


class 차타이머5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='63', seconds=63)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='63'):
            return 생성랜덤(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='58', seconds=58)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='58'):
            return 생성랜덤(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='68', seconds=68)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='68'):
            return 생성랜덤(self.ctx)


class 차타이머8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='62', seconds=62)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='62'):
            return 생성랜덤(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='60'):
            return 생성랜덤(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='55', seconds=55)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='55'):
            return 생성랜덤(self.ctx)


class 차타이머11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='52', seconds=52)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='52'):
            return 생성랜덤(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='49', seconds=49)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='49'):
            return 생성랜덤(self.ctx)


class 생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=12.0):
            return 번생성1(self.ctx)
        if self.random_condition(weight=13.0):
            return 번생성2(self.ctx)
        if self.random_condition(weight=12.0):
            return 번생성3(self.ctx)
        if self.random_condition(weight=13.0):
            return 번생성4(self.ctx)
        if self.random_condition(weight=12.0):
            return 번생성5(self.ctx)
        if self.random_condition(weight=13.0):
            return 번생성6(self.ctx)
        if self.random_condition(weight=12.0):
            return 번생성7(self.ctx)
        if self.random_condition(weight=13.0):
            return 번생성8(self.ctx)


class 번생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1207], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1208], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1201])
        self.destroy_monster(spawn_ids=[1202])
        self.destroy_monster(spawn_ids=[1203])
        self.destroy_monster(spawn_ids=[1204])
        self.destroy_monster(spawn_ids=[1205])
        self.destroy_monster(spawn_ids=[1206])
        self.destroy_monster(spawn_ids=[1207])
        self.destroy_monster(spawn_ids=[1208])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 대기시간
