""" trigger/02000293_bf/door02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1002, initial_sequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999998]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1002, initial_sequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000524,10000505], state=0):
            return 트리거02시작(self.ctx)


class 트리거02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[2029])
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 트리거03시작(self.ctx)


class 트리거03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[25000])
        self.destroy_monster(spawn_ids=[25001])
        self.destroy_monster(spawn_ids=[25002])
        self.destroy_monster(spawn_ids=[25003])
        self.destroy_monster(spawn_ids=[25004])
        self.destroy_monster(spawn_ids=[25005])
        self.destroy_monster(spawn_ids=[25006])
        self.destroy_monster(spawn_ids=[25007])
        self.destroy_monster(spawn_ids=[25008])
        self.set_actor(trigger_id=1002, initial_sequence='Closed')


initial_state = 대기
