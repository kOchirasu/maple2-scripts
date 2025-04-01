""" trigger/51000003_dg/item_01.xml """
import trigger_api


# 포그 이펙트
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991119, key='item_710_spawn', value=0) # 모든 아이템 초기화
        self.set_user_value(trigger_id=991118, key='item_711_spawn', value=0)
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)
        self.set_user_value(trigger_id=991116, key='item_713_spawn', value=0)
        self.set_user_value(trigger_id=991115, key='item_714_spawn', value=0)
        self.set_user_value(trigger_id=991114, key='item_715_spawn', value=0)
        self.set_user_value(trigger_id=991113, key='item_716_spawn', value=0)
        self.set_user_value(trigger_id=991112, key='item_717_spawn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') == 1:
            return Round_01_Ready(self.ctx)


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 해당 시간 뒤 부터 아이템 생성 시작
            return Round_01_Start(self.ctx)


class Round_01_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return item_710(self.ctx)
        if self.random_condition(weight=1.0):
            return item_711(self.ctx)
        if self.random_condition(weight=1.0):
            return item_712(self.ctx)
        if self.random_condition(weight=1.0):
            return item_713(self.ctx)
        if self.random_condition(weight=1.0):
            return item_714(self.ctx)
        if self.random_condition(weight=1.0):
            return item_715(self.ctx)
        if self.random_condition(weight=1.0):
            return item_716(self.ctx)
        if self.random_condition(weight=1.0):
            return item_717(self.ctx)
        if self.user_value(key='Round_01') == 0:
            # 스위치가 꺼지면 스테이트 초기화
            return Round_check(self.ctx)


class NextSpawn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 5초 뒤에 랜덤스폰
            return Round_01_Start(self.ctx)
        if self.user_value(key='Round_01') == 0:
            # 스위치가 꺼지면 스테이트 초기화
            return Round_check(self.ctx)


class item_710(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[710]):
            # 플레이어가 없어야 아이템 생성
            return item_710_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_711(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[711]):
            # 플레이어가 없어야 아이템 생성
            return item_711_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_712(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[712]):
            # 플레이어가 없어야 아이템 생성
            return item_712_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_713(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[713]):
            # 플레이어가 없어야 아이템 생성
            return item_713_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_714(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[714]):
            # 플레이어가 없어야 아이템 생성
            return item_714_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_715(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[715]):
            # 플레이어가 없어야 아이템 생성
            return item_715_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_716(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[716]):
            # 플레이어가 없어야 아이템 생성
            return item_716_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_717(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[717]):
            # 플레이어가 없어야 아이템 생성
            return item_717_spawn(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 해당 조건을 만족하지 못했다면 다시 랜덤
            return Round_01_Start(self.ctx)


class item_710_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991119, key='item_710_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_711_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991118, key='item_711_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_712_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_713_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991116, key='item_713_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_714_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991115, key='item_714_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_715_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991114, key='item_715_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_716_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991113, key='item_716_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


class item_717_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991112, key='item_717_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> trigger_api.Trigger:
        return NextSpawn(self.ctx)


initial_state = Round_check
