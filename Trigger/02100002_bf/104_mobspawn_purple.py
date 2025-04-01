""" trigger/02100002_bf/104_mobspawn_purple.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탱크 리필 트리거에서 받는 신호
        self.set_user_value(key='Gauge', value=0) # 탱크 리필 트리거에서 받는 신호
        # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        self.set_user_value(key='StopSpawn', value=0)
        self.set_user_value(key='SpawnHold', value=0)
        self.destroy_monster(spawn_ids=[40100,40075,40050,40025,40001,41001,41002,41003])
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104])
        # Abnormal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Gauge') == 100:
            return Gauge100_Normal(self.ctx)


class Gauge100_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104], visible=True)
        self.spawn_monster(spawn_ids=[40100], auto_target=False) # 100%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold') == 1:
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge') == 75:
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


class Gauge75_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104], visible=True)
        self.spawn_monster(spawn_ids=[40075], auto_target=False) # 75%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold') == 1:
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge') == 100:
            return Gauge100_Normal(self.ctx)
        if self.user_value(key='Gauge') == 50:
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


class Gauge50_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104], visible=True)
        self.spawn_monster(spawn_ids=[40050], auto_target=False) # 50%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold') == 1:
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge') == 75:
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='Gauge') == 25:
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


class Gauge25_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104], visible=True)
        self.spawn_monster(spawn_ids=[40025], auto_target=False) # 25%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold') == 1:
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge') == 50:
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='Gauge') == 1:
            return Gauge1_Normal(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


class Gauge1_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5104], visible=True)
        self.spawn_monster(spawn_ids=[40001], auto_target=False) # 1%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold') == 1:
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge') == 25:
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


# 스폰 홀드
class SpawnHold(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnHold') == 0:
            return BackToGaugeState(self.ctx)
        if self.user_value(key='StopSpawn') == 1:
            return Quit(self.ctx)


# 돌연변이 슬라임 랜덤 낮은 확률
class Gauge_SpawnRamdom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=100.0, desc='Normal'):
            return Spawn_Normal(self.ctx)
        if self.random_condition(weight=5.0, desc='Eater'):
            return Spawn_Eater(self.ctx)
        """
        if self.random_condition(weight=1.0, desc='BigMom'):
            return Spawn_BigMom(self.ctx)
        """
        if self.random_condition(weight=10.0, desc='Runner'):
            return Spawn_Runner(self.ctx)


# 랜덤 스폰 공용
class Spawn_Normal(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return BackToGaugeState(self.ctx)


class Spawn_Eater(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Abnormal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5204], visible=True)
        self.spawn_monster(spawn_ids=[41001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return BackToGaugeState(self.ctx)


class Spawn_Runner(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Abnormal Slime Rebirth Sound
        self.set_effect(trigger_ids=[5204], visible=True)
        self.spawn_monster(spawn_ids=[41002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return BackToGaugeState(self.ctx)


"""
class Spawn_BigMom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[41003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return BackToGaugeState(self.ctx)
"""

# 게이지 상태 체크로 돌아가기 공용

class BackToGaugeState(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Gauge') == 100:
            return Gauge100_Normal(self.ctx)
        if self.user_value(key='Gauge') == 75:
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='Gauge') == 50:
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='Gauge') == 25:
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='Gauge') == 1:
            return Gauge1_Normal(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[40100,40075,40050,40025,40001,41001,41002,41003])


initial_state = Wait
