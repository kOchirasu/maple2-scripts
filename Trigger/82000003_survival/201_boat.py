""" trigger/82000003_survival/201_boat.xml """
import trigger_api


# 맵 외곽 동선
class BoatPatrol(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.npc_to_patrol_in_box(box_id=9501, npc_id=11400001, spawn_id='interactObject', patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return BoatPatrol(self.ctx)


initial_state = BoatPatrol
