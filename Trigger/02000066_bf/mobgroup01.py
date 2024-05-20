""" trigger/02000066_bf/mobgroup01.xml """
import trigger_api


# 디펜스 모드 :  좀비모둠
class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[900]):
            return 차타이머1(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[904]):
            return 차타이머4(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[906]): # 35레벨
            return 차타이머6(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[908]):
            return 차타이머7(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[912]):
            return 차타이머10(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[914]):
            return 차타이머12(self.ctx)


class 차타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='51', seconds=51)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='51'):
            return 대기시간(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='42', seconds=42)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='42'):
            return 대기시간(self.ctx)


class 차타이머4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='37', seconds=37)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='37'):
            return 대기시간(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=33)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='33'):
            return 대기시간(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='30'):
            return 대기시간(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=27)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='27'):
            return 대기시간(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=25)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timer_id='25'):
            return 대기시간(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=20)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timer_id='20'):
            return 대기시간(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 시작
