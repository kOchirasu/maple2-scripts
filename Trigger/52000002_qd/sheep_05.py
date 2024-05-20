""" trigger/52000002_qd/sheep_05.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[615])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000615], state=0):
            return NPC교체(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return NPC소멸(self.ctx)


class NPC교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.spawn_monster(spawn_ids=[1095])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.set_interact_object(trigger_ids=[10000615], state=2)
            return NPC이동(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return NPC소멸(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=6)
        self.set_effect(trigger_ids=[615], visible=True)
        self.move_npc(spawn_id=1095, patrol_name='MS2PatrolData_1095')
        self.set_dialogue(type=1, spawn_id=1095, script='$52000002_QD__SHEEP_05__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return NPC소멸(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1095])

    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중(self.ctx)


initial_state = 시작대기중
