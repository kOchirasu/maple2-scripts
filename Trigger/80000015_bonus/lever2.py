""" trigger/80000015_bonus/lever2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7102])
        self.set_interact_object(trigger_ids=[10001315], state=1)
        self.set_mesh(trigger_ids=[3006,3007,3008,3009,3010,3011], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 안내(self.ctx)
        if self.object_interacted(interact_ids=[10001315], state=0):
            return 문열림(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$80000015_bonus__lever2__0$', arg3='2000', arg4='102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001315], state=0):
            return 문열림(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 반응대기(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True)
        self.spawn_npc_range(range_ids=[2002], score=1500)
        self.set_mesh(trigger_ids=[3006,3007,3008,3009,3010,3011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999101, key='Dead_B', value=1)
        self.set_effect(trigger_ids=[6000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_skill(trigger_ids=[7102], enable=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
