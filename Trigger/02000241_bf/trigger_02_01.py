""" trigger/02000241_bf/trigger_02_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[703,704])
        self.destroy_monster(spawn_ids=[613,614,615,616,617,618,619,620,621])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[613,614,615,616,617,618,619,620,621], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[613,614,615,616,617,618,619,620,621]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
