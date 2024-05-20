""" trigger/99999905/seagull_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10503]):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData_2003')
            return None # Missing State: 종료


initial_state = 시작
