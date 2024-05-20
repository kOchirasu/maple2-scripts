""" trigger/03000110_bf/chest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000023], state=1)
        self.set_interact_object(trigger_ids=[11000008], state=2)
        self.set_interact_object(trigger_ids=[11000009], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            self.set_interact_object(trigger_ids=[11000023], state=2)
            return 차웨이브대기1(self.ctx)


class 차웨이브대기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=23000003, text_id=23000003, duration=5000)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차웨이브시작1(self.ctx)


class 차웨이브시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001,1002]):
            return 차웨이브대기2(self.ctx)


class 차웨이브대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차웨이브시작2(self.ctx)


class 차웨이브시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 차웨이브대기3(self.ctx)


class 차웨이브대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차웨이브시작3(self.ctx)


class 차웨이브시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[3001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3001]):
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
