""" trigger/03000054_bf/elite.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000008], state=2)
        self.set_interact_object(trigger_ids=[11000009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            self.spawn_monster(spawn_ids=[1001,1002,1003], auto_target=False)
            return 엘리트등장(self.ctx)


class 엘리트등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=23000002, text_id=23000002, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 엘리트등장(self.ctx)
        if self.monster_dead(spawn_ids=[1001,1002,1003]):
            self.hide_guide_summary(entity_id=23000002)
            self.set_event_ui(type=7, arg3='2000', arg4='0')
            return 상자확률(self.ctx)


class 상자확률(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=90.0):
            self.set_interact_object(trigger_ids=[11000008], state=1)
            return 종료(self.ctx)
        if self.random_condition(weight=10.0):
            self.set_interact_object(trigger_ids=[11000009], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
