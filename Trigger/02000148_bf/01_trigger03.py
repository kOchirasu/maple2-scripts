""" trigger/02000148_bf/01_trigger03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000171], state=1)
        self.set_effect(trigger_ids=[209,210,211,212])
        self.set_mesh(trigger_ids=[317,318,319,320], visible=True)
        self.set_mesh(trigger_ids=[321,322,323,324])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000171], state=0):
            return 개봉박두(self.ctx)


class 개봉박두(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[317,318,319,320])
        self.spawn_monster(spawn_ids=[99,100,101,102])
        self.set_mesh(trigger_ids=[321,322,323,324], visible=True)
        self.set_effect(trigger_ids=[209,210,211,212], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99,100,101,102]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[403]):
            return 대기(self.ctx)


initial_state = 대기
