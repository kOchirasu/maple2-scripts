""" trigger/02100002_bf/02_guidenpcspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GuideNpcSpawn', value=0)
        self.destroy_monster(spawn_ids=[109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GuideNpcSpawn') == 1:
            return NpcSpawn(self.ctx)


class NpcSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_GuideNpc')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return CheckUser(self.ctx)


class CheckUser(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109])


initial_state = Wait
