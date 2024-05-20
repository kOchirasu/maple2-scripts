""" trigger/02000304_bf/minion_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[114]):
            self.spawn_monster(spawn_ids=[1007,1008], auto_target=False)
            return 종료체크(self.ctx)
        if self.monster_dead(spawn_ids=[2001]):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1007,1008]):
            return 대기시간(self.ctx)
        if self.monster_dead(spawn_ids=[2001]):
            self.destroy_monster(spawn_ids=[1007,1008])
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_user(map_id=2000304, portal_id=10, box_id=114)
            return 대기(self.ctx)


initial_state = 대기
