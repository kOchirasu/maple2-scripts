""" trigger/02100002_bf/25_spawnholder_pink.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 메인 트리거에서 받는 신호
        self.set_user_value(key='ActivateHolder', value=0) # 메인 트리거에서 받는 신호
        self.set_user_value(key='DungeonQuit', value=0) # ON
        self.set_interact_object(trigger_ids=[10001256], state=2) # OFF
        self.set_interact_object(trigger_ids=[10001257], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ActivateHolder') == 1:
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SpawnStart(self.ctx)


class SpawnStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # OFF
        self.set_interact_object(trigger_ids=[10001257], state=1) # ON
        self.set_interact_object(trigger_ids=[10001256], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001257], state=0):
            return StopDelay(self.ctx)
        if self.user_value(key='DungeonQuit') == 1:
            return Quit(self.ctx)


class StopDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 홀드 값이 1이면 스폰 중지
        self.set_user_value(trigger_id=105, key='SpawnHold', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SpawnStop(self.ctx)
        if self.user_value(key='DungeonQuit') == 1:
            return Quit(self.ctx)


class SpawnStop(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # OFF
        self.set_interact_object(trigger_ids=[10001257], state=2) # ON
        self.set_interact_object(trigger_ids=[10001256], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001256], state=0):
            return StartDelay(self.ctx)
        if self.user_value(key='DungeonQuit') == 1:
            return Quit(self.ctx)


class StartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 홀드 값이 0이면 개시
        self.set_user_value(trigger_id=105, key='SpawnHold', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SpawnStart(self.ctx)
        if self.user_value(key='DungeonQuit') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ON
        self.set_interact_object(trigger_ids=[10001256], state=2) # OFF
        self.set_interact_object(trigger_ids=[10001257], state=0)


initial_state = Wait
