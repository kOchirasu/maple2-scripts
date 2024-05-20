""" trigger/99999908/main.xml """
import trigger_api
from System.Numerics import Vector3


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117])
        self.set_ambient_light(primary=Vector3(1,1,1))
        self.set_directional_light(diffuse_color=Vector3(1,1,1))
        self.set_timer(timer_id='240', seconds=240, start_delay=1, interval=1)


class switch(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 시작(self.ctx)


initial_state = 시작
