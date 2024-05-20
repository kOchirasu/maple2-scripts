""" trigger/02000244_bf/trigger_02_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[703,704], visible=True)
        self.destroy_monster(spawn_ids=[622,623,624,625,626,627,628,629,630])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[622,623,624,625,626,627,628,629,630], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[622,623,624,625,626,627,628,629,630]):
            return 통과(self.ctx)
        if self.object_interacted(interact_ids=[10000302], state=0):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[703,704])
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
