""" trigger/02000386_bf/main_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[901]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=901, script='$02000386_BF__MAIN_02__0$', time=2)
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[901])


initial_state = idle
