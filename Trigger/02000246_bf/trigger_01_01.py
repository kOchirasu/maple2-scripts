""" trigger/02000246_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601,602,603,604,605,606,607,608,609])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601,602,603,604,605,606,607,608,609], auto_target=False)
        self.set_timer(timer_id='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605,606,607,608,609]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=180)


initial_state = 대기
