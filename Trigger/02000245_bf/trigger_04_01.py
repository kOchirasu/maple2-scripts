""" trigger/02000245_bf/trigger_04_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[707,708])
        self.destroy_monster(spawn_ids=[616,617,618,619,620,621,622,623,624])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[204]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[616,617,618,619,620,621,622,623,624], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[616,617,618,619,620,621,622,623,624]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[707,708])
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
