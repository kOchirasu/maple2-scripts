""" trigger/52010023_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[7001])
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002500], quest_states=[2]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52010023_QD__MAIN__0$', time=5)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[101]):
            return Npc_out(self.ctx)


class Npc_out(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=True)
        self.destroy_monster(spawn_ids=[101])


initial_state = idle
