""" trigger/80000008_bonus/trigger_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000211], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000211], state=0):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=401, spawn_ids=[104]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.set_timer(timer_id='4', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 아이템(self.ctx)


class 아이템(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[502])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
