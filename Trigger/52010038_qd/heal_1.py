""" trigger/52010038_qd/heal_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001258], state=2)
        self.set_interact_object(trigger_ids=[10001259], state=2)
        self.set_interact_object(trigger_ids=[10001260], state=2)
        self.set_interact_object(trigger_ids=[10001261], state=2)
        self.set_interact_object(trigger_ids=[10001262], state=2)
        self.set_interact_object(trigger_ids=[10001263], state=2)
        self.set_interact_object(trigger_ids=[10001264], state=2)
        self.set_interact_object(trigger_ids=[10001265], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WoundStart') == 1:
            return 랜덤조건(self.ctx)


class 랜덤조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=13.0):
            return 체크10001258(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001259(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001260(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001261(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001262(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001263(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001264(self.ctx)
        if self.random_condition(weight=13.0):
            return 체크10001265(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001258(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001258], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001258(self.ctx)


class 생성10001258(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001258], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001259(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001259], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001259(self.ctx)


class 생성10001259(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001259], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001260(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001260], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001260(self.ctx)


class 생성10001260(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001260], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001261(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001261], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001261(self.ctx)


class 생성10001261(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001261], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001262(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001262], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001262(self.ctx)


class 생성10001262(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001262], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001263(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001263], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001263(self.ctx)


class 생성10001263(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001263], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001264(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001264], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001264(self.ctx)


class 생성10001264(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001264], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001265(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001265], state=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 생성10001265(self.ctx)


class 생성10001265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001265], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd') == 1:
            self.set_user_value(trigger_id=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


initial_state = 대기
