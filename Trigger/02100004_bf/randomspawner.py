""" trigger/02100004_bf/randomspawner.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundStart') == 1:
            return 랜덤스폰(self.ctx)


class 랜덤스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999992, key='RoundStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return 중복체크01(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크02(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크03(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크04(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크05(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크06(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크08(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크09(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크10(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크11(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크12(self.ctx)
        if self.random_condition(weight=10.0):
            return 중복체크13(self.ctx)


class 중복체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned01') == 0:
            self.set_user_value(trigger_id=999101, key='NpcSpawn01', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned01') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned02') == 0:
            self.set_user_value(trigger_id=999102, key='NpcSpawn02', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned02') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned03') == 0:
            self.set_user_value(trigger_id=999103, key='NpcSpawn03', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned03') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned04') == 0:
            self.set_user_value(trigger_id=999104, key='NpcSpawn04', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned04') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned05') == 0:
            self.set_user_value(trigger_id=999105, key='NpcSpawn05', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned05') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned06') == 0:
            self.set_user_value(trigger_id=999106, key='NpcSpawn06', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned06') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned08') == 0:
            self.set_user_value(trigger_id=999108, key='NpcSpawn08', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned08') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned09') == 0:
            self.set_user_value(trigger_id=999109, key='NpcSpawn09', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned09') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned10') == 0:
            self.set_user_value(trigger_id=999110, key='NpcSpawn10', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned10') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned11') == 0:
            self.set_user_value(trigger_id=999111, key='NpcSpawn11', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned11') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned12') == 0:
            self.set_user_value(trigger_id=999112, key='NpcSpawn12', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned12') == 1:
            return 랜덤스폰(self.ctx)


class 중복체크13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned13') == 0:
            self.set_user_value(trigger_id=999113, key='NpcSpawn13', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned13') == 1:
            return 랜덤스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
