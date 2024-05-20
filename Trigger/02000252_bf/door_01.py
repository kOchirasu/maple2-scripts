""" trigger/02000252_bf/door_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[169,170], visible=True)
        self.set_effect(trigger_ids=[8031], visible=True)
        self.set_effect(trigger_ids=[8032], visible=True)
        self.set_interact_object(trigger_ids=[10000401], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000401], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_effect(trigger_ids=[8031])
        self.set_effect(trigger_ids=[8032])
        self.set_mesh(trigger_ids=[169,170])
        self.spawn_monster(spawn_ids=[1012])
        self.set_dialogue(type=1, spawn_id=1012, script='$02000252_BF__DOOR_01__0$', time=2)
        self.move_npc(spawn_id=1012, patrol_name='MS2PatrolData_3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 삭제(self.ctx)


class 삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1012])


initial_state = 대기
