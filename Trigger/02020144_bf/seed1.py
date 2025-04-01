""" trigger/02020144_bf/seed1.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1003], skill_id=70002110, level=1, is_skill_set=False)
        # self.set_user_value(trigger_id=900005, key='TimerStart', value=0)
        # self.set_user_value(trigger_id=900005, key='TimerReset', value=0)
        self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(trigger_ids=[9001,9002,9003,9004])
        self.set_interact_object(trigger_ids=[10002124], state=0)
        self.set_interact_object(trigger_ids=[10002125], state=0)
        self.set_interact_object(trigger_ids=[10002126], state=0)
        self.set_interact_object(trigger_ids=[10002127], state=0)
        self.set_interact_object(trigger_ids=[10002128], state=0)
        self.set_interact_object(trigger_ids=[10002129], state=0)
        self.set_skill(trigger_ids=[901])
        self.set_skill(trigger_ids=[902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed') == 1:
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900009, key='Seed', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 활성화(self.ctx)


class 활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9001,9002,9003,9004], visible=True, fade=2.0)
        self.set_interact_object(trigger_ids=[10002124], state=1)
        self.set_interact_object(trigger_ids=[10002125], state=1)
        self.set_interact_object(trigger_ids=[10002126], state=1)
        self.set_interact_object(trigger_ids=[10002127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            self.set_mesh(trigger_ids=[9001,9002,9003,9004])
            self.set_interact_object(trigger_ids=[10002124], state=0)
            self.set_interact_object(trigger_ids=[10002125], state=0)
            self.set_interact_object(trigger_ids=[10002126], state=0)
            self.set_interact_object(trigger_ids=[10002127], state=0)
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002124], state=0):
            self.set_interact_object(trigger_ids=[10002125], state=0)
            self.set_interact_object(trigger_ids=[10002126], state=0)
            self.set_interact_object(trigger_ids=[10002127], state=0)
            self.set_mesh(trigger_ids=[9001,9002,9003,9004])
            return 씨앗심기1(self.ctx)
        if self.object_interacted(interact_ids=[10002125], state=0):
            self.set_interact_object(trigger_ids=[10002124], state=0)
            self.set_interact_object(trigger_ids=[10002126], state=0)
            self.set_interact_object(trigger_ids=[10002127], state=0)
            self.set_mesh(trigger_ids=[9001,9002,9003,9004])
            return 씨앗심기2(self.ctx)
        if self.object_interacted(interact_ids=[10002126], state=0):
            self.set_interact_object(trigger_ids=[10002124], state=0)
            self.set_interact_object(trigger_ids=[10002125], state=0)
            self.set_interact_object(trigger_ids=[10002127], state=0)
            self.set_mesh(trigger_ids=[9001,9002,9003,9004])
            return 씨앗심기3(self.ctx)
        if self.object_interacted(interact_ids=[10002127], state=0):
            self.set_interact_object(trigger_ids=[10002124], state=0)
            self.set_interact_object(trigger_ids=[10002125], state=0)
            self.set_interact_object(trigger_ids=[10002126], state=0)
            self.set_mesh(trigger_ids=[9001,9002,9003,9004])
            return 씨앗심기4(self.ctx)


class 씨앗심기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002128], state=1)
        self.set_interact_object(trigger_ids=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002128], state=0) or self.object_interacted(interact_ids=[10002129], state=0):
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(box_id=1004, additional_effect_id=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002128], state=1)
        self.set_interact_object(trigger_ids=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002128], state=0) or self.object_interacted(interact_ids=[10002129], state=0):
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(box_id=1004, additional_effect_id=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002128], state=1)
        self.set_interact_object(trigger_ids=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002128], state=0) or self.object_interacted(interact_ids=[10002129], state=0):
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(box_id=1004, additional_effect_id=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002128], state=1)
        self.set_interact_object(trigger_ids=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002128], state=0) or self.object_interacted(interact_ids=[10002129], state=0):
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(box_id=1004, additional_effect_id=70002109, level=1):
            return 종료(self.ctx)


class 나무생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[901], enable=True)
        self.set_skill(trigger_ids=[902], enable=True)
        self.set_interact_object(trigger_ids=[10002128], state=2)
        self.set_interact_object(trigger_ids=[10002129], state=2)
        self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_On')
        self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
            self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
            self.set_interact_object(trigger_ids=[10002128], state=0)
            self.set_interact_object(trigger_ids=[10002129], state=0)
            self.set_skill(trigger_ids=[901])
            self.set_skill(trigger_ids=[902])
            self.set_user_value(trigger_id=900009, key='Seed', value=0)
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900009, key='Seed', value=0)
        self.add_buff(box_ids=[1003], skill_id=70002110, level=1, is_skill_set=False)
        self.set_skill(trigger_ids=[901])
        self.set_skill(trigger_ids=[902])
        self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(trigger_ids=[9001,9002,9003,9004])
        self.set_interact_object(trigger_ids=[10002124], state=0)
        self.set_interact_object(trigger_ids=[10002125], state=0)
        self.set_interact_object(trigger_ids=[10002126], state=0)
        self.set_interact_object(trigger_ids=[10002127], state=0)
        self.set_interact_object(trigger_ids=[10002128], state=0)
        self.set_interact_object(trigger_ids=[10002129], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        return 시작(self.ctx)


initial_state = 시작
